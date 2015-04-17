# Rivers Path

### Description
Usuaylly the water start falling from the mountains and following paths building
rivers, those rivers that end in the sea. You will need to find the paths
(rivers) that can be form and have an ending in the sea, remember that there
are rivers which dont end in the sea, forming lakes.


### Input

+ A line representing the position (coordinates) of the water to start falling.

+ A two dimensional matrix wich represents the land with values representing the
height of the land.

### Output

> NOTE

> Up and Left edges represent the Pacific Ocean, and Down and Right represent
> the Atlantic Ocean, the rivers can only go up, left, down and right positions


+ First N lines: All possible paths which form a river ending in the sea
+ Last two lines: The number of rivers ending in the Pacific Ocean and the next
line the number of rivers ending in the Atlantic Ocean

### Sample input
line 1

     2 14 23 2  9
     1  4  6 1  9
    22  3  3 9  1

Line 2

    (1, 1)


### Sample output

    (1, 1), (1, 0)
    (1, 1), (2, 1)
    1
    1

### Explanation
Line 2 indicates to start at position 1,1 which makes reference to the value '4'
so from ther the water would try to move to up, left, down and right, but since
only left and down are equal or less that itself, then they water will flow to
there, the first path belongs to the path that ends in the Pacific Ocean and the
second to the one that ends in the Atlantic Ocean