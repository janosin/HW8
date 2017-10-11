import os

import csv
import re 


fh = open("P1DataA.csv")
	
lst = list()
dates = list()
ages = list()

for line in fh:
	item = line.split(",")
	new_dic = {}
	new_dic["First"] = item[0]
	new_dic["Last"] = item[1]
	new_dic["Email"] = item[2]
	new_dic["Class"] = item[3]
	new_dic["DOB"] = item[4]
	lst.append(new_dic)
	


new_list = sorted(lst[1:], key = lambda x: [x["Last"]])
print (new_list)








