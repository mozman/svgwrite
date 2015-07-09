#!/bin/sh
for f in `ls *.py`
do
echo running $f ...
python $f
done

