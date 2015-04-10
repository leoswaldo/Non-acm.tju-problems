#!/python3/bin/python3


## Function: find coincidences
#  Description: find all coicidences of characters in the words_list of the
#      license plate, except for dashes and return the number of coincidences
#      in the fastest way (not case sensitive)
#  Parameters: license_plate, words_list
#      license_plate: characters to be searched
#      words_list: list of string to search in
def find_coincidences(license_plate, words_list):
    '''
    find all coicidences of characters in the words_list of the
    license plate, except for dashes and return the number of coincidences
    in the fastest way (not case sensitive)
    '''

    # remove all dashes '-' from license_plate
    license_plate = license_plate.replace('-', '')

    '''
    We are going to iterate through all chars of the license_plate and if we
    dont find the char in the word from the list, then remove it to save time
    for next iteration (thats the magic of this algorithm, since we remove it
    every time we dont find an element so there is not need to keep looking
    in it)
    '''
    for char in license_plate:
        char = char.lower()
        words_pending = len(words_list)
        while(words_pending > 0):
            if(not char in words_list[words_pending - 1].lower()):
                # remove the word in the list if char not found
                words_list.pop(words_pending - 1)
            words_pending -= 1

    return len(words_list)


if __name__ == '__main__':
    license_plate = "PY-34-THON"
    words_list = ["ASDF3490PASaTh", "TH3214Py0on", "TH3214Py0N", "TH3214Py0o"]

    print(find_coincidences(license_plate, words_list))