#!/usr/bin/env bash
#
# Builds python3.5 using pyenv
# If you get a zlib error, uncomment the two lines below
# This is meant for Mac, see here for linux solution:
# https://unix.stackexchange.com/a/334103


if test "$(uname)" = "Darwin"
then
  # xcode-select --install
  # sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
  brew install pyenv
  python3 -m pip install pipenv
  pyenv install 3.5.5
else # linux
  echo "Not on Mac, see here for installation instructions: "
  echo "https://www.tecmint.com/pyenv-install-and-manage-multiple-python-versions-in-linux/"
  echo "..or use this:"
  echo "https://github.com/pyenv/pyenv-installer"
fi
  
