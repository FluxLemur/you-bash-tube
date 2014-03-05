#! /bin/bash

echo "Please enter title: "
a=`python simple_search.py`
echo "Beginning download..."
youtube-dl -xtq $a
