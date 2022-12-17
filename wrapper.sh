#!/bin/bash

set -u

if [[ "$(python3 -V)" =~ "Python 3" ]]
then
  echo "Python 3 installed"
else
 python3 -m ensurepip --default-pip 

fi
pip install -r requirements.txt
