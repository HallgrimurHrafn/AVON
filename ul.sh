#!/bin/bash

cd ~/avon
git debase
git add .
git commit -m "Updated through script"
git push origin master