#!/bin/bash
# calculating euclidean distance
euclidean_distance()
{
echo "scale=2;sqrt(($1-$2)^2+($3-$4)^2)"|bc
}
# finding direction
find_direction()
{
   if [ $(echo "$1 >$2 && $3>$4"|bc -l) -eq 1 ];then
   echo "NE";
   elif [ $(echo "$1 >$2 && $3==$4"|bc -l) -eq 1 ];then
   echo "E";
   elif [ $(echo "$1 >$2 && $3<$4"|bc -l) -eq 1 ];then
   echo "SE";
   elif [ $(echo "$1 ==$2 && $3>$4"|bc -l) -eq 1 ];then
   echo "N";
   elif [ $(echo "$1 <$2 && $3>$4"|bc -l ) -eq 1 ];then
   echo "NW";
   elif [ $(echo "$1 <$2 && $3==$4"|bc -l) -eq 1 ];then
   echo "W";
   elif [ $(echo "$1 ==$2 && $3<$4"|bc -l) -eq 1 ];then
   echo "S";
   else
   echo "SW";
   fi
}
read xj yj
read xp yp
read h
temp=$(euclidean_distance "$xj" "$xp" "$yj" "$yp")
time=1
while [ "$time" -le "$h" ]; do
read xp yp
dist=$(euclidean_distance "$xj" "$xp" "$yj" "$yp")
direction=$(find_direction "$xj" "$xp" "$yj" "$yp")
if [ $(echo "$dist <2"|bc -l) -eq 1 ]; then
echo "Location Reached"
break
fi
if [ $(echo "$dist>=2 && $time==$h"|bc -l) -eq 1 ]; then
echo "Time over"
break;
fi
echo $dist $direction
time=$((time+1))
done;




