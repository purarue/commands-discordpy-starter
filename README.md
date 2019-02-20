### commands-discordpy-starter

Boilerplate code for creating a bot in [discordpy](https://github.com/Rapptz/discord.py), using python3.5.5

##### Installation

`./install-python-35.sh` and `./setup.sh` installs python3.5.5 and sets up a virtual environment to run discordpy in. 

```
git clone https://github.com/seanbreckenridge/commands-discordpy-starter discord-bot
cd discord-bot
# If you don't have python3.5 installed on your system, install it using pyenv:
# If you get zlib errors check the comments in `install-python-35.sh`
./install-python-35.sh
# Setup creates a virtualenvironment using pyenv and pipenv
# This is meant for mac, but there are instructions for linux
# If python3.5 is not at default pyenv location
# edit setup.sh and replace "${HOME}/.pyenv/versions/3.5.5/bin/python3.5" with
# its location on your system
./setup.sh
# If you're going to post this to your own github, feel free to re-initialize the git repo:
rm -rf .git
git init
```

Use `pipenv shell` to enter the virtual environment when in the directory.

See [here](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) for how to create the bot and get your token; put your token it in a file named: `.token.yaml`, like so:

```
token: !!str YOUR_TOKEN_HERE
```

To run:

```
pipenv shell
python3.5 bot.py
```

Feel free to create an issue or pull request if you have a suggestion or something to add.
