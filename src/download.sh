#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Need a song title"
    exit 1;
fi

python simple_search.py $1
