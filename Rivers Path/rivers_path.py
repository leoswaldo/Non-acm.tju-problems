#!/python3/bin/python3


## Function: search_rivers
#  Description: find all possible paths for rivers flow
#  Parameters:
#      land: land representing the world a matrix (mxn)
#      height: heihgt of the land (matrix)
#      width: widht of the land (matrix)
#      current_h: current node height position
#      current_w: current node widht position
def search_rivers(land, height, width, current_h, current_w,):

    current_node = land[current_h][current_w]

    # verifying if the current position has arrived to an ocean
    if(current_h == 0 or current_h == (land_height - 1) or current_w == 0 or
        current_w == (land_width - 1)):
        print("Arrived to a Ocean, well on the edge which means that :)")
    else:
        ''' verifying if from the current position you can move to other (lower)
            remember only up, right, right, down and left directions are allowed
        '''
        # up
        if(current_h > 0 and current_node > land[current_h - 1][current_w]):
            pass

        # right
        if(current_w < (width - 1) and current_node > land[current_h]
            [current_w + 1]):
            pass

        # down
        if(current_h < (height - 1) and current_node > land[current_h + 1]
            [current_w]):
            pass

        # left
        if(current_w > 0 and current_node > land[current_h][current_w - 1]):
            pass


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

    search_rivers(land, land_height, land_width, water_position_h,
        water_position_w,)