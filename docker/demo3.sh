S=`seq 50`
echo "real,user,sys" > docker_classifier_time.csv && (for i in $S; do TIMEFORMAT=%R','%U','%S && time ./demos/classifier.py infer ./models/openface/celeb-classifier.nn4.small2.v1.pkl images/examples/{carell,adams,lennon}* ;done)>classifier_output.txt  2>> docker_classifier_time.csv
