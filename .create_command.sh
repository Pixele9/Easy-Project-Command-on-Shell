#!/bin/bash

function create() {
	cd;
	# create proj with github repo
	if [ $1 = "-r" ]
	then 
		python3 .create.py $1 $2 $3
	else
		# create basic porj, no repo
		python3 .create.py $1 $2
	fi
	cd /change/this/to/your/projects/directory;
}