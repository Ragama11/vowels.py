vowels = ['a', 'e', 'i','o', 'u']
sentence = (input("input your sentence"))

print(list(sentence.split()))
['hello', 'world']
print(sentence.split())
['hello', 'world']
word = sentence.split()
list(word)
['hello', 'world']
sentence
'hello world'
for vowel in vowels:
    for letter in sentence:
		   if vowel == letter:
			   print(letter)


