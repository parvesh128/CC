import copy


def printWordsPossible(dict_words, char_array):

	possibleWords = []

	for word in dict_words:
		char_map = {}

		for char in char_array:
			if char not in char_map:
				char_map[char] = 1
			else:
				char_map[char] += 1

		wordPossible = True

		for char in word:

			if char not in char_map:
				wordPossible = False
				break
			cur_count = char_map[char]
			cur_count -= 1

			if cur_count == 0:
				del char_map[char]
				continue
			char_map[char] = cur_count

		if wordPossible:
			possibleWords.append(word)

	return possibleWords


if __name__ == '__main__':
	char_array = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
	dict_words = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
	print printWordsPossible(dict_words, char_array)

