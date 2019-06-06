a=input()
if a.lower() in "aeiou":
	print("Vowel")
elif 97<=ord(a)<=122:
	print("Consonent")
else:
	print("invalid")
