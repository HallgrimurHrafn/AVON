#!/bin/bash

cd ~/documents/AVON
read -rsp $'Press enter to continue...\n'
git fetch origin
read -rsp $'Press enter to continue...\n'
git checkout master
read -rsp $'Press enter to continue...\n'
git merge origin/master
read -rsp $'Press enter to continue...\n'
