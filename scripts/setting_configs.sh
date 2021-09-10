#!/bin/bash

cd ~
# Copying the Emacs repository
git clone https://github.com/EgorTolbaev/.emacs.d.git
# Copying the dotfiles repository
git clone https://github.com/EgorTolbaev/dotfiles.git
# Move the qutebrowser config to its place
cp ~/dotfiles/qutebrowser/config/*.py ~/.config/qutebrowser/
# Move home page to home folder
cp -r ~/dotfiles/homepage ~/