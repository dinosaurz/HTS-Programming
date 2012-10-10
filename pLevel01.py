wrdList = "wordlist.txt"
scrList = "pLevel01.txt"
blank = ('    ', {' ': 4})


def count_letters(word):
    return dict((char, word.count(char)) for char in word)


def analyze(filename, trim):
    wordList = []
    f = open(filename)

    for line in iter(f):
        word = line[:-trim]
        wordList.append((word, count_letters(word)))
    f.close()
    return wordList


def unscramble(scramble, wordlist):
    for word in wordlist:
        if word[1] == scramble[1]:
            return word[0]
    return 'None'

unscrambledList = analyze(wrdList, 1)
scrambledList = analyze(scrList, 1)

unscrambled = []
for scramble in scrambledList:
    if scramble == blank:
        continue

    unscrambled_word = unscramble(scramble, unscrambledList)
    unscrambled.append(unscrambled_word)

print ','.join(unscrambled)
