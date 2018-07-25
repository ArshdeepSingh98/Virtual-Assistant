for i in *
do
	if [[ $i == *".pyc" ]]
		then
		rm $i
	fi
done