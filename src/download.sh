#! /bin/bash

echo "Please enter title: "
a=`python simple_search.py`
youtube-dl -xtq $a
