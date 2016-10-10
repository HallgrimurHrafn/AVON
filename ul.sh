#!/bin/bash

cd ~/avon
git rebase
git add .
git commit -m "Updated through script"
git push origin master