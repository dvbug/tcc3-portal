#!/bin/sh

# pybabel compile -d translations

# if u can't compile to '.mo' file, try del '#, fuzzy' from '.po' file

type pybabel >/dev/null 2>&1 || { echo >&2 "I require pybabel but it's not installed.  Aborting.";return; }

for DIR in ./*
    do
        if  [ -d ./${DIR} ] &&[ ! `expr match ${DIR} ./__` -eq 4 ]; then
            cd ${DIR}
            pybabel compile -d translations
            cd ..
        fi
    done