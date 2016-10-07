#!/bin/bash

cd ~/avon
git fetch upstream
git checkout master
git merge upstream/master
