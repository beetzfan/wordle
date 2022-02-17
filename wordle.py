from random_word import RandomWords

def wordle(word,guessedWord):
	clueString = ""
	for i,ch in enumerate(guessedWord):
		if ch == word[i]:
			clueString += "G"
		elif ch not in word:
			clueString += "X"
		else:
			clueString += "Y"
	return clueString

r = RandomWords()
word = r.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=5)
print(word)
for i in range(6):
	guess = input()
	response = wordle(word,guess.upper())
	print(response)
	if response == "GGGGG":
		break