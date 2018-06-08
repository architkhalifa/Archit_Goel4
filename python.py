text = "abcd"
shift = 3
key = "abcdefghijklmnopqrstuvwxyz"
result = ""
result2= ""
for char in text.lower():
			i= (key.index(char)+shift) %26
			result=result+key[i]
for char in result.lower():
			i= (key.index(char)-shift) %26
			result2=result2+key[i]
print(result)
print(result2)

