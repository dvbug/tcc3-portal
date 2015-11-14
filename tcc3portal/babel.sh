#!/bin/sh

# pybabel extract -F babel.cfg -o messages.pot .

type pybabel >/dev/null 2>&1 || { echo >&2 "I require pybabel but it's not installed.  Aborting.";return; }



for DIR in ./*
    do
        if  [ -d ./${DIR} ] &&[ ! `expr match ${DIR} ./__` -eq 4 ]; then
            cd ${DIR}
            pybabel extract -F ./../babel.cfg -o messages.pot .
            cd ..
        fi
    done