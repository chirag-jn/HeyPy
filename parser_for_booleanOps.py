text = input().split()

ans = ''
for i in range(len(text)):
	if 'great' in text[i]:
		if 'than' in text[i+1]:
			if i+3 < len(text) and 'equal' in text[i+3]:
				ans = ans + "gte"
				break
				i = i+5
			else:
				ans = ans + "gt"
				break
				i = i+3
	elif 'less' in text[i]:
		if 'than' in text[i+1]:
			if i+3 < len(text) and 'equal' in text[i+3]:
				ans = ans + "lte"
				break
				i = i+5
			else:
				ans = ans + "lt"
				break
				i = i+3
	elif 'equal' in text[i]:
		ans = ans + "eq"

print(ans)