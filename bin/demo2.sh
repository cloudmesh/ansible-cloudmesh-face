echo "real,user,sys" > compare_time.csv && (for i in `seq 10`; do TIMEFORMAT=%R','%U','%S && time ./demos/compare.py images/examples/{lennon*,clapton*};done)>compare_output.txt  2>> compare_time.csv
