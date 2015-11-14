#!/bin/sh


#workon tcc3-venv
#pip freeze > requirements.txt

type workon >/dev/null 2>&1 || { echo >&2 "I require workon but it's not installed.  Aborting.";return; }

workon tcc3-venv
pip freeze > requirements.txt