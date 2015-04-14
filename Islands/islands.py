#!/python3/bin/python3


## Function: find_island
#  Description: recursively find all spaces beloging to the island in the
#      positions right, down, left and up
#  Parameters: world, height, widht, current_h, current_w
#      world: matrix with the current values of the islands
#      height: height of the matrix
#      width: width of the matrix
#      current_h: current height position in the matrix
#      current_w: current width position in the matrix
def find_island(world, height, width, current_h=0, current_w=0):

    # mark the current position as visited
    world[current_h][current_w] = -1

    #right
    if(current_w < width - 1 and world[current_h][current_w + 1] == 1):
        world = find_island(world, height, width, current_h, current_w + 1)

    #down
    if(current_h < height - 1 and world[current_h + 1][current_w] == 1):
        world = find_island(world, height, width, current_h + 1, current_w)

    #left
    if(current_w > 0 and world[current_h][current_w - 1] == 1):
        world = find_island(world, height, width, current_h, current_w - 1)

    #up
    if(current_h > 0 and world[current_h - 1][current_w] == 1):
        world = find_island(world, height, width, current_h - 1, current_w)

    # return the modified world with new values of the islands
    return world


if __name__ == '__main__':
    width = 5
    height = 4
    world = [[0, 0, 1, 0, 0],
            [0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1]]

    islands_counter = 0

    # we iterate through all positions if the world in the positions is 1 still
    for i in range(0, height):
        for j in range(0, width):
            if(world[i][j] == 1):
                islands_counter += 1
                world = find_island(world, height, width, i, j)

    # print the result of number of islands
    print(islands_counter)