#!/python3/bin/python3


## Function: find_coincidences
#  Description: find coincidences in list (string) of chars
#  Params: word
#      word: given list
#  Return: dictionary with coincidences
def find_coincidences(word):
    '''We are going to build a dictionary in which the key will be the letter
       based on that we are going to find the coincidences for a given word
    '''
    coincidences = {}
    # iterate through all letters in the word
    for letter in word:
        coincidence = coincidences.get(letter)
        # verify if the word is not in the dict then we set it to 1, otherwise
        # we add one to its value
        if(not coincidence):
            coincidence = 1
        else:
            coincidence += 1
        # save the coincidences in the dict
        coincidences[letter] = coincidence

    return coincidences


## Function: check_anagrams
#  Description: verify if two list of words are anagram by the position
def check_anagrams(first_words, second_words):
    number_words = len(first_words)
    word_index = 0
    #iterate trough all words in both lists
    while word_index < number_words:
        first_word = first_words[word_index]
        second_word = second_words[word_index]
        # find the coincidences for word from first list and word from second
        # list
        first_word_coincidences = find_coincidences(first_word)
        second_word_coincidences = find_coincidences(second_word)

        # verify if the dicts are equal, so based on that we analyze if they
        # are anagrams
        if(first_word_coincidences == second_word_coincidences):
            print(1)
        else:
            print(0)

        word_index += 1


if(__name__ == '__main__'):
    first_words = ['round', 'food', 'eat', 'cat']
    second_words = ['odunr', 'doof', 'ate', 'ldcat']

    # check if lists are anagrams
    check_anagrams(first_words, second_words)