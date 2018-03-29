
def parse_bool(text):
# text = input().split()
	text = text.split()
	ans = ''
	i = 0
	while i < len(text):
		# print(text[i])
		if 'great' in text[i]:
			if 'than' in text[i+1]:
				if (i+2 <len(text) and 'equal' in text[i+2]):
					text[i] = 'gte'
					text.remove(text[i+1])
					text.remove(text[i+1])
					text.remove(text[i+1])
					i = i+1
				elif (i+3 < len(text) and 'equal' in text[i+3]):
					text[i] = 'gte'
					text.remove(text[i+1])
					text.remove(text[i+1])
					text.remove(text[i+1])
					text.remove(text[i+1])
					i = i+1
				else:
					text[i] = 'gt'
					text.remove(text[i+1])
					i = i+1
		elif 'less' in text[i]:
			if 'than' in text[i+1]:
				if (i+2 <len(text) and 'equal' in text[i+2]):
					text[i] = 'lte'
					text.remove(text[i+1])
					text.remove(text[i+1])
					text.remove(text[i+1])
					i = i+1
				elif i+3 < len(text) and 'equal' in text[i+3]:
					text[i] = 'lte'
					text.remove(text[i+1])
					text.remove(text[i+1])
					text.remove(text[i+1])
					text.remove(text[i+1])
					i = i+1
				else:
					text[i] = 'lt'
					text.remove(text[i+1])
					i = i+1
		elif 'equal' in text[i]:
			if i > 3 and ('great' in text[i-3] or 'less' in text[i-3]):
				continue
			elif 'not' in text[i-1]:
				text[i-1] = 'ne'
				text.remove(text[i])
				text.remove(text[i])
				i = i+2
			else:
				text[i] = 'eq'
				text.remove(text[i+1])
				i = i+2
		i += 1

	for i in text:
		ans = ans + i + " "

	# print(ans)
	return ans