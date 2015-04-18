#!/python3/bin/python3


## Function: search_rivers
#  Description: find all possible paths for rivers flow
#  Parameters:
#      land: land representing the world a matrix (mxn)
#      height: heihgt of the land (matrix)
#      width: widht of the land (matrix)
#      current_h: current node height position
#      current_w: current node widht position
def search_rivers(land, height, width, current_h, current_w, path=''):

    current_node = land[current_h][current_w]
    new_path = path + "(" + str(current_h) + "," + str(current_w) + ") "

    # verifying if the current position has arrived to an ocean
    if(current_h == 0 or current_h == (height - 1) or current_w == 0 or
        current_w == (width - 1)):
        print(new_path)

        # verify if it ended on Pacific or Atlantic ocean
        if(current_h == 0 or current_w == 0):
            global pacific_rivers
            pacific_rivers += 1
        else:
            global atlantic_rivers
            atlantic_rivers += 1
    else:
        ''' verifying if from the current position you can move to other (lower)
            remember only up, right, right, down and left directions are allowed
        '''

        '''NOTE:
            If we want this algorithm to work with values not only lower if not
            also equal, then we need to modify the current node in the land, it
            wont affect the flow of the function because we access to the
            current node value through the variable current_node, to do this we
            only need to modify the value by adding one or anything to make it
            bigger that its initial value
        '''
        # in case an equal value and we need to modify it and pass as argument
        land[current_h][current_w] += 1

        # up
        if(current_h > 0 and current_node >= land[current_h - 1][current_w]):
            search_rivers(land, height, width, current_h - 1, current_w,
                new_path)

        # right
        if(current_w < (width - 1) and current_node >= land[current_h]
            [current_w + 1]):
            search_rivers(land, height, width, current_h, current_w + 1,
                new_path)

        # down
        if(current_h < (height - 1) and current_node >= land[current_h + 1]
            [current_w]):
            search_rivers(land, height, width, current_h + 1, current_w,
                new_path)

        # left
        if(current_w > 0 and current_node >= land[current_h][current_w - 1]):
            search_rivers(land, height, width, current_h, current_w - 1,
                new_path)


if __name__ == "__main__":
    water_position_h = 3
    water_position_w = 2

    land_height = 7
    land_width = 7

    land = [[8, 10, 13, 8, 12, 45, 3],
            [1, 29, 13, 2, 15, 19, 4],
            [3, 14, 9, 3, 9, 7, 1],
            [16, 36, 57, 84, 32, 29, 14],
            [87, 49, 42, 42, 33, 27, 29],
            [2, 2, 8, 5, 4, 2, 12],
            [45, 9, 5, 2, 78, 0, 2]]

    pacific_rivers = atlantic_rivers = 0

    # call to find all possible rivers which end on the sea
    search_rivers(land, land_height, land_width, water_position_h,
        water_position_w,)

    # print the number or fivers ending on each ocean
    print(pacific_rivers)
    print(atlantic_rivers)