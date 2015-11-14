#!/bin/sh

# pybabel init -i messages.pot -d translations -l zh_cn

type pybabel >/dev/null 2>&1 || { echo >&2 "I require pybabel but it's not installed.  Aborting.";return; }



for DIR in ./*
    do
        if  [ -d ./${DIR} ] &&[ ! `expr match ${DIR} ./__` -eq 4 ]; then
            cd ${DIR}
            pybabel init -i messages.pot -d translations -l zh_Hans_CN
            cd ..
        fi
    done
