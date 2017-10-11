import operator


ofile = open("TheVictors.txt")
word_count = {}

for line in ofile:
	words = line.split()
	for word in words:
		word_count[word] = word_count.get(word, 0) + 1

lst = list()

print (word_count.items())

for key, value in word_count.items():
	newtup = (value, key)
	lst.append(newtup)
	


new_list = (sorted(lst, reverse = True))

for value, key in new_list[:15]:
	print (key, value)