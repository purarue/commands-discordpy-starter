#!/usr/bin/env bash

pipenv --python "${HOME}/.pyenv/versions/3.5.5/bin/python3.5" install
# install requirements
curl https://raw.githubusercontent.com/Rapptz/discord.py/async/requirements.txt > requirements.txt
echo "discord.py" >> requirements.txt
echo "requests" >> requirements.txt
echo "pyyaml" >> requirements.txt
pipenv install -r requirements.txt
echo "Use 'pipenv shell' to enter the virtualenv"
