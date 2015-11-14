#!/bin/sh

# pybabel update -i messages.pot -d translations

type pybabel >/dev/null 2>&1 || { echo >&2 "I require pybabel but it's not installed.  Aborting.";return; }

for DIR in ./*
    do
        if  [ -d ./${DIR} ] &&[ ! `expr match ${DIR} ./__` -eq 4 ]; then
            cd ${DIR}
            pybabel update -i messages.pot -d translations
            cd ..
        fi
    done
