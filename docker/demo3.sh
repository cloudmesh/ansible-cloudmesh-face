echo "real,user,sys" > classifier_time.csv && (for i in `seq 10`; do TIMEFORMAT=%R','%U','%S && time ./demos/classifier.py infer ./models/openface/celeb-classifier.nn4.small2.v1.pkl images/examples/{carell,adams,lennon}* ;done)>classifier_output.txt  2>> classifier_time.csv
