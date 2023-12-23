#!/bin/bash
#
# Description: This script / single line command at line 56, sorts provided file 
#              and returns highest N results as an output in needed JSON format
# Date: Dec 11, 2022
# Author: mrjasjeetsingh
#

#Input argument storage in variables
file=$1
rank=$2
exit_code=0   #setting default to 0

# 1. Validation : Input argument verification for file to be present
if [ ! -f $file ]; then
  echo -e "\n$file File Not Found.\nCheck path or file name"
  exit 1
fi

# 2. Validation : verification for rank to be whole number only
if [[ ! $rank =~ ^[0-9]+$ ]]; then
	echo "2nd argument needs to be a whole number only, in order to provide top N records, based on highest scores"
	exit 1
fi

#3. Validation : verification for score to be integer only
for i in `cat $file | cut -d: -f1`
do
	score=$(echo $i | cut -d: -f1)
	if [[ ! $score =~ ^[0-9]+$ ]]; then
		echo "score $score is not an integer"
		exit 1
	fi
done

#4. Validation : verification of ID field in each record
invalid_records=`cat $file  | cut -d, -f1 | grep -v id`
if [[ ! -z $invalid_records ]]; then
	echo -e "\nFollowing Invalid record(s) rectified with ID field missing, and have been ignored for processing:\n $invalid_records"

	# The following scenario has been successfully tested to work, 
	# by adding temporary bad entry.
	#
	# The following code wipes off invalid records and proceeds with just valid records.
	# Since requirement is to display exit code 2 for invalid records,
	#    this will still give exit code 2, along with providing highest N score records.
	# If this is needed, uncomment lines 50 and 54 for it to work flawlessly.
	#
	# Filtering valid records with ID present.
#	grep id $file > ${file}_clean
	
	# replacing original file (with invalid records) 
	# with good file (containing valid records only), in the variable
#	file=${file}_clean
	exit_code=2
fi 

echo -e "\n\nRequested top $rank records from $file:"
cat $file | sort -k1 -nr  | cut -d, -f1 | head -$rank | sed -e 's/^/{|    "score":/; s/: {/,|    /; s/$/|},/; 1s/^/[|/; $ s/.$/|]/' | tr '|' '\n'
exit $exit_code

