#!/python3/bin/python3

#Find a peak element
#Description
#Given an array of integers. Find a peak element in it. An array element is peak
#if it is NOT smaller than its neighbors. For corner elements, we need to
#consider only one neighbor.
#For example, for input array {5, 10, 20, 15}, 20 is the only peak element. For
#input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and
# 90.
#Note that we need to return any one peak element.


## Function: find_peak
#  Description: find a peak in the list
def find_peak(pos, left_limit, right_limit):
    '''Find a peak in the list'''
    # first we validate if the right position exists, the compare it with the
    # right position
    if(pos < (peak_length - 1) and peak_list[pos] <= peak_list[pos + 1]):
        left_limit = pos + 1
        pos = int((left_limit + right_limit) / 2)
        find_peak(pos, left_limit, right_limit)
    # if the right is not greater, then  validate if the left edge postion
    # exists to compare with
    elif(pos > peak_length and peak_list[pos] <= peak_list[pos - 1]):
        right_limit = pos - 1
        pos = int((left_limit + right_limit) / 2)
        find_peak(pos, left_limit, right_limit)
    # if right and left is not greater, then the elmement in the list at pos is
    # a peak
    else:
        print('%s is a peak at position %s' % (peak_list[pos], pos))


if(__name__ == '__main__'):
    # test escenarios
    #peak_list = [1, 5]
    #peak_list = [2]
    peak_list = [4, 5, 7, 3, 2, 78, 9, 43, 1]

    # define the lencht of the list as global scope to use it in functions to
    # avoid re-calculating it
    peak_length = len(peak_list)

    # validate if the list hast at least one element
    if(peak_length > 0):
        pos = int((peak_length / 2))
        # search a peak in the list
        find_peak(pos, 0, peak_length - 1)
    else:
        print('The list must contain at least one element')
