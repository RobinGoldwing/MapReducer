#!/usr/bin/python

import sys
#
salesTotal = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
	# Something has gone wrong. Skip this line.
		continue
	total, thisSale = data_mapped
	if total not in salesTotal.keys():
		salesTotal[total] = float(thisSale)
	else:
		salesTotal[total] += float(thisSale)
  
for key, value in salesTotal.items():
	print(key+"\t"+str(value))
