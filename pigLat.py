# English to pig latin
print('Enter the English message to be translated into pig latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []   # A list of words in pig latin
for word in message.split():
    # Seperate the non-letters at the start of the word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Seperate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word is upper case or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower # Make the word lower case for the translation

    #Seperate the consonants at the start of the word
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add pig latin ending to word
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to upper case or title case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.istitle()

    # Add the non letters back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all words back together into single string
print(' '.join(pigLatin))
