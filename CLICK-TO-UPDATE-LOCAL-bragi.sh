#!/bin/bash

cd ~/documents/AVON
git fetch upstream
git checkout master
git merge upstream/master
