#!/python3/bin/python3


## Function: find_peak
#  Description: find a peak in a matrix, order to look (up, left, right, down)
#  Parameters: matrix, curr_n, curr_m
#      matrix: matrix containing the elements
#      curr_n: current position (row)
#      curr_m: current position (colums)
def find_peak(matrix, curr_n, curr_m):
    current_val = matrix[curr_n][curr_m]
    # first we compare the <A> position is not iqual or greater, if we move to
    # that position
    # <A> = up
    if(curr_n > 0 and current_val <= matrix[curr_n - 1][curr_m]):
        find_peak(matrix, curr_n - 1, curr_m)
    # <A> = left
    elif(curr_m > 0 and current_val <= matrix[curr_n][curr_m - 1]):
        find_peak(matrix, curr_n, curr_m - 1)
    # <A> = right
    elif(curr_m < (m - 1) and current_val <= matrix[curr_n][curr_m + 1]):
        find_peak(matrix, curr_n, curr_m + 1)
    # <A> = down
    elif(curr_n < (m - 1) and current_val <= matrix[curr_n + 1][curr_m]):
        find_peak(matrix, curr_n + 1, curr_m)
    # otherwise it is a peak
    else:
        # print the answer
        print("Peak found %s in position {n:%s, m:%s}" % (current_val, curr_n,
            curr_m))


if __name__ == '__main__':

    # rows of test scenario
    n = 4
    # cols of test scenario
    m = 5
    matrix = [[3, 6, 1, 5, 7],
                [9, 3, 1, 8, 3],
                [2, 4, 5, 7, 0],
                [4, 8, 2, 6, 3]]

    # pass the matrix and the starting point (could be also n, m (any))
    find_peak(matrix, int(n / 2), int(m / 2))