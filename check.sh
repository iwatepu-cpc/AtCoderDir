#/bin/sh
cnt=0
ac=0

if [ -z "$1" ]; then
  echo "Not set executable file"
else
  echo "Running exec $1:"
fi

echo

for filename in testcases/in*.txt; do
  cnt=`expr $cnt + 1`
  num=`echo $filename | awk 'match($0,/in([0-9]+).txt/,a){print a[1]}'`
  re=0
  (time (cat $filename | ($1 1> /tmp/tmpout))) 2>/tmp/tmptime
  if [ $? = 0 ]; then
    (diff /tmp/tmpout testcases/out"$num".txt > /dev/null 3<&0) 1>/dev/null; res=$?
  else
    re=1
  fi
  if [ $re = 1 ]; then
    echo "#$num RE"
  elif [ $res = 0 ]; then
    echo "#$num AC" `cat /tmp/tmptime | grep real | cut -f 2`
    ac=`expr $ac + 1`
  else
    echo "#$num WA" `cat /tmp/tmptime | grep real | cut -f 2`
  fi
done

echo

if [ $ac = $cnt ]; then
  echo "Test Passed!!"
else
  echo "Failure..."
fi
