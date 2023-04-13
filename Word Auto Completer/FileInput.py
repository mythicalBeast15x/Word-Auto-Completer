'''
This is used to create and modify the text files
that will hold all the word information.
'''


'''
An example on how to use this is
appendToFile('UpdatedTemporaryWords.txt', 'phrases.txt')
in which the data from phrases will be added to the
UpdatedTemporaryWords.txt and it is important to make
sure the path is correct.
'''
# This takes a file and appends all the information within 
# it to another file.
def appendToFile(addToFile: str, fileData: str) -> None:
    # Creates a list that will hold all the data from the data file.
    wordList = []
    with open(fileData, 'r') as fileRead:
        for line in fileRead:
            # Adds each word to the list.
            for word in line.split():
                wordList.append(word.lower())
    # This will be used to make sure there are no duplicate words.
    uniqueWords = []
    with open(addToFile, 'a') as fileWrite:
        for word in wordList:
            if word not in uniqueWords:
                # Writes the word the existing file.
                fileWrite.write(word + "\n")
                uniqueWords.append(word)



