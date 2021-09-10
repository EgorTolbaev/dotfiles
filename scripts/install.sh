#!/bin/bash

package=qutebrowser
if pacman -Qs $package > /dev/null ; then
  echo "The package $package is installed"
else
  echo "The package $package is not installed"
  pacman -S qutebrowser
fi

package=pandoc
if pacman -Qs $package > /dev/null ; then
  echo "The package $package is installed"
else
  echo "The package $package is not installed"
  pacman -S pandoc
fi

font= fc-list | grep "Source Code Pro"
if [ ! $font > /dev/null ]; then
     echo "There are fonts"
else
     echo "No fonts"
     wget -O scp https://fonts.google.com/download?family=Source%20Code%20Pro
     mkdir /usr/share/fonts/source-code-pro/
     unzip scp -d /usr/share/fonts/source-code-pro/
     rm -R scp
fi