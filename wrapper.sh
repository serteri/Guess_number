#!/bin/bash

set -u

if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "No VIRTUAL_ENV set"
    pip install virtualenv 
else
    echo "VIRTUAL_ENV is set"
fi

if [[ "$(python3 -V)" =~ "Python 3" ]]
then
  echo "Python 3 installed"
else
 python3 -m ensurepip --default-pip 

fi
pip install -r requirements.txt

if [$(which python) = ""] 
then
    echo "You do not have python"
    python -m ensurepip --default-pip 
fi
pip install -r requirements.text

python3 ./src/game.py