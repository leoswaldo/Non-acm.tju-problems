#!/python3/bin/python3

import sys


## Function: is_palindrome
#  Description: find if the parameter is a palindrome
#  Params: word
#      word: list of characters to validate if they form a palindrome
def is_palindrome(word):
    word_len = len(word)
    # we need to find the limit since we are only going to iterate
    # until the half of the word
    limit = int(word_len / 2)
    for i in range(0, limit):
        if(not word[i] == word[word_len - 1 - i]):
            return False
    return True


## Function: main
#  Description: iterate through list of words passed trhough command line
#      to determine if joining it to other word in the same list form a
#      palindomer
def main(words):
    words_len = len(words)
    for i in range(0, words_len):
        for j in range(0, words_len):
            # we avoid joining the word to itself by verifyin the iterator
            if(not i == j):
                word = words[i] + words[j]
                if(is_palindrome(word)):
                    print("%s + %s is palindrome" % (words[i], words[j]))


if(__name__ == "__main__"):
    words = sys.argv[1:]
    main(words)
