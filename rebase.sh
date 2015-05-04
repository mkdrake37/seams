#!/bin/bash
git stash
git pull --rebase upstream gh-pages
git stash apply
