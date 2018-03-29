def parse_nums(test):
	from word2number import w2n
	newString = ''
	# test = input().split()
	test = test.split()
	for i in test:
		try:
			newString = newString + str(w2n.word_to_num(i)) + " "
		except ValueError:
			newString = newString + i + " "

	newList = newString.split()

	for i in range(len(newList)):
		# print(str(newList) + " " + str(i))
		if i <= len(newList)-2 and newList[i].isdigit() and newList[i+1].isdigit() and (int(newList[i+1]) == 100 or int(newList[i+1]) == 1000 or int(newList[i+1]) == 10000 or int(newList[i+1]) == 100000 or int(newList[i+1]) == 1000000 or int(newList[i+1]) == 10000000 or int(newList[i+1]) == 10000000 or int(newList[i+1]) == 1000000):
			temp = int(newList[i]) * int(newList[i+1])
			newList[i] = str(temp)
			newList.remove(newList[i+1])
			#delete next index
		elif i <= len(newList)-2 and newList[i].isdigit() and newList[i+1].isdigit():
			temp = int(newList[i]) + int(newList[i+1])
			newList[i] = str(temp)
			newList.remove(newList[i+1])

	for i in range(len(newList)):
		if i <= len(newList)-3 and newList[i].isdigit() and newList[i+1].lower() == 'and':
			temp = str(int(newList[i+2]) + int(newList[i]))
			newList[i] = str(temp)
			newList.remove(newList[i+2])
			newList.remove(newList[i+1])
			#delete next two indices

	i = len(newList)-1
	while(len(newList) > 1 and i >= 0):
		if(newList[i].isdigit() and newList[i-1].isdigit()):
			temp = int(newList[i]) + int(newList[i-1])
			newList[i-1] = str(temp)
			newList.remove(newList[i])
		i = i-1

	finalString = ''
	for i in newList:
		finalString = finalString + i + " "
	# print(finalString)
	return finalString