from WordTree import Tree


file = open('Words.txt', 'r')
words = file.readlines()

tree = Tree()
for word in words:
    tree.insert_word(word)
tree.insert_word('byte')

word_part = input('enter a word: ')
print(tree.find_closest_word(word_part))
