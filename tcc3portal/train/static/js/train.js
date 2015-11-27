/**
 * Created by devnode on 15-11-24.
 */

function getSchedules(parent, date,lineNo,type){
    $.jsonp({
        url:"http://192.168.1.125:8080/api/v1.0/schedules/"+date+"/"+lineNo+"/"+type+"?callback=?",
        //url:"http://192.168.1.125:8080/api/v1.0/schedules/"+date+"/"+lineNo+"/"+type+"/1023&1024?callback=?",
        success: function(json_data){
            draw(parent, date, json_data)
        },
        error: function() {
            alert("on_train_graph_click error "+"http://192.168.1.125:8080/api/v1.0/schedules/"+date+"/"+lineNo+"/"+type);
        }
    });
}

function draw(parent, date, json_data){

    d3.select(parent.get(0)).select("svg").remove();
    d3.select(parent.get(0)).select(".no_data_tip").remove();
    d3.select("body").select(".svg_tooltip").remove();


    var xAxisTicksCount = 480; //有多少个横轴点, 80:30min, 160:15min, 480:5min
    var initStepWidth = 30; // 刻度步长
    //var initWidth = 20000;//影响横轴的显示范围
    var initWidth = initStepWidth * xAxisTicksCount ;
    var initHeight = 600;

    var formatDateTime = d3.time.format("%Y%m%d%H%M%S");
    var formatDate = d3.time.format("%Y%m%d");
    var formatTime = d3.time.format("%H:%M");

    var stations = []; // lazy load.
    var trains = [];
    var schedules = json_data.data.schedules;

    if (isEmptyObject(schedules)){
        d3.select(parent.get(0)).append('div')
            .attr("class", "text-center no_data_tip")
            .text("No Data.");
        return;
    }

    //trains.
    for(var trip in schedules){
        trains.push(parse_schedule(trip, schedules[trip]))
    }
    //var tmp_trains = trains;
    //var tmp_max_times = [];
    //var tmp_min_times = [];
    //tmp_trains.map(function (t) {
    //    t.stops.sort(function (s1, s2) {
    //            return s1.time - s2.time;
    //        });
    //    tmp_max_times.push(t.stops[t.stops.length-1].time);
    //    tmp_min_times.push(t.stops[0].time);
    //});
    //var beginTime = tmp_min_times.sort(function (t1, t2) {
    //            return t1 - t2;
    //        })[0];
    //var endTime = tmp_max_times.sort(function (t1, t2) {
    //            return t2 - t1;
    //        })[0];
    //beginTime.setMinutes(beginTime.getMinutes() - 5);
    //endTime.setMinutes(endTime.getMinutes() + 5);

    var beginTime = formatDate.parse(date);
    var endTime = formatDate.parse(date);
    beginTime.setHours(beginTime.getHours() + 4);
    endTime.setDate(endTime.getDate() + 1);
    endTime.setHours(endTime.getHours() + 1);
    var margin = {top: 20, right: 30, bottom: 20, left: 150},
        width = initWidth - margin.left - margin.right,
        height = initHeight - margin.top - margin.bottom;          // 700影响运行图高度

    // 鼠标移动到列车线产生的tooltip
    var tooltip = d3.select("body")
        .append("div")
        .attr("class", "svg_tooltip")
        .style("visibility", "hidden")
        .text("a simple tooltip");

    var x = d3.time.scale()
        .domain([beginTime, endTime])
        //.range([0, width]);
        .range([0, initWidth]);//影响横轴的单位时间的宽度

    var y = d3.scale.linear()
        .range([0, height]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .ticks(xAxisTicksCount)
        .tickFormat(formatTime);

    var line = d3.svg.line()
        .x(function(d) { return x(d.time); })
        .y(function(d) { return y(d.station.distance); });


    var svg = d3.select(parent.get(0)).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    svg.append("defs").append("clipPath")
        .attr("id", "clip")
        .append("rect")
        .attr("y", -margin.top)
        .attr("width", width)
        .attr("height", height + margin.top + margin.bottom);

    svg.append("rect")
        .attr("id", "timelinerange")
        .attr("y", -margin.top)
        .attr("width", width)
        .attr("height", height + margin.top + margin.bottom)
        .style("fill", "transparent")
        .on("mousemove", function(e){
            return d3.select('.svg_time_line').select("line").attr("transform", "translate(" + d3.mouse(this)[0] + ",0)");
        });



    y.domain(d3.extent(stations,function(d){
            return d.distance;
        }));

    var station_g = svg.append("g").attr("class", "station");

    station_g.append("line")
        .attr("x1", "0")
        .attr("x2", "0")
        .attr("y1", "0")
        .attr("y2", height);
    var station = station_g.selectAll("g")
        .data(stations)
        .enter().append("g")
        .attr("transform", function(d) {
            return "translate(0," + y(d.distance) + ")"; });

    // 绘制左侧纵轴, y轴
    station.append("text")
        .attr("x", -6)
        .attr("dy", ".35em")
        .text(function(d) {
            return d.name; });

    // 绘制横向背景线
    station.append("line")
        .attr("x2", width);


    // 绘制顶部横轴, x轴
    svg.append("g")
        .attr("class", "x top axis")
        .call(xAxis.orient("top"));

    // 绘制底部横轴, y轴
    svg.append("g")
        .attr("class", "x bottom axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis.orient("bottom"));


    // draw time line
    var time_line = svg.append("g")
        .attr("class", "svg_time_line");
    time_line.append("line")
        .attr("x1", "0")
        .attr("x2", "0")
        .attr("y1", "0")
        .attr("y2", height);

    var train = svg.append("g")
        .attr("class", "train")
        .attr("clip-path", "url(#clip)")
        .selectAll("g")
        .data(trains.filter(function(d) { return /[NLB]/.test(d.type); }))
        .enter().append("g")
        .attr("class", function(d) { return d.type; });

    // 绘制列车线
    train.append("path")
        .attr("d", function(d) { return line(d.stops); })
        .on("mouseover", function(d){
             //d3.select(this).classed("hover", true);

            tooltip.text("Train No: " + d.trip);
            return tooltip.style("visibility", "visible");})
        .on("mousemove", function(){ return tooltip.style("top",
            (d3.event.pageY-13)+"px").style("left",(d3.event.pageX+13)+"px");})
        .on("mouseout", function(){
            //d3.select(this).classed("hover", false);
            return tooltip.style("visibility", "hidden");
        })
        .on("mousedown", function(d){
            //console.log('path mousedown.')
            d3.select("body").on("mousedown", function(){
                svg.selectAll('.train').selectAll("g").classed({"unselected": false, "selected": false});
                d3.select("body").on("mousedown", null);
                //console.log('body mousedown.')
            });

            svg.selectAll('.train').selectAll("g").classed({"unselected": true, "selected": false});

            var selected_paths = svg.selectAll('.train').selectAll("g")
                .filter(function(td){ return td.trip === d.trip ? this:null;});
            selected_paths.classed({"unselected": false, "selected": true});

            d3.event.stopPropagation();
        });


    // 绘制小圆点
    //train.selectAll("circle")
    //    .data(function(d) { return d.stops; })
    //    .enter().append("circle")
    //    .attr("transform", function(d) {  return "translate(" + x(d.time) + "," + y(d.station.distance) + ")"; })
    //    //.attr("value", function (d) { return d.station.name+ d.time;}) // for test
    //    .attr("r", 1.5)              // 点直径
    //    .on("mouseover", function(d){
    //        var format = d3.time.format("%H:%M:%S");
    //        tooltip.text(d.station.name+"\n"+format(d.time));
    //        d3.select(this).attr("r", "3");                                                       //<circle cx="168" cy="179" r="59"
    //        return tooltip.style("visibility", "visible");
    //    })
    //    .on("mousemove", function(){ return tooltip.style("top",
    //        (d3.event.pageY-13)+"px").style("left",(d3.event.pageX+13)+"px");})
    //    .on("mouseout", function(){
    //        d3.select(this).attr("r", "1.5");
    //        return tooltip.style("visibility", "hidden");});

    function parse_schedule(trip, schedule){
        var train_data = {};
        train_data.trip = trip;
        train_data.direction = schedule.direction;
        train_data.type = schedule.type;
        train_data.stops = get_stops(schedule);
        return train_data;
    }

    function get_stops(schedule){
        var tmp_stations = [];

        for(var k in schedule){
            if (/^stop\|/.test(k)){
                var p = k.split("|");
                tmp_stations.push({
                    key: k,
                    name:p[1],
                    id: p[2],
                    distance: +p[3],
                    zone: +p[4],
                    a_or_d: p[5],
                    order: +p[6]
                    })
            }
        }
        if (stations.length == 0){
            stations = tmp_stations
        }

        return tmp_stations
            .map(function(s){
                return {
                    station: s,
                    time: parseTimeForData(schedule[s.key])
                };})
            .filter(function(s){return s.time != null;})
            .sort(function (s1, s2) {
                return s1.time - s2.time;
            });
    }

    function parseTimeForAxis(s) {
        var t = formatDateTime.parse(s);
        if (t != null && t.getHours() < 3) t.setDate(t.getDate() + 1);
        return t;
    }

    function parseTimeForData(s) {
        return formatDateTime.parse(s);
    }

    function isEmptyObject(obj) {
         for (var i in obj) {
          return false;
         }
         return true;
    }
}