import re

hand = open('regrexpress.txt')
y = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)

print (stuff)



[('Junior', 28), ('Senior', 26), ('Freshman', 23), ('Sophomore', 22)]
[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)]

[('Senior', 26), ('Junior', 25), ('Freshman', 20), ('Sophomore', 18)]
[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]