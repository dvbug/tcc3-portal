/**
 * Created by devnode on 15-11-24.
 */

function getSchedules(date,lineNo,type){
    $.jsonp({
        url:"http://192.168.1.125:8080/api/v1.0/schedules/"+date+"/"+lineNo+"/"+type,
        success: function(data){
            $('#train_graph').html(data)
        },
        error: function() {
            alert("on_train_graph_click error "+"http://192.168.1.125:8080/api/v1.0/schedules/"+date+"/"+lineNo+"/"+type);
        }
    });
};