
# end_matrix = [[ 1,2,3,4,5,6,7,8,9,0],
#                [-1,-1,-1,0,-1,0,-1,0,-1,-1]]
# start_matrix = [[0,2,3,4,5,6,7,8,9,1],
#                 [-1,-1,-1,0,-1,0,-1,0,-1,-1]]
end_matrix = [[ 1,2,3,4,5,6,7,8,9,0],
               [-1,-1,-1,0,-1,0,-1,0,-1,-1]]
start_matrix = [[0,2,3,4,5,6,7,8,9,0],
                [-1,-1,-1,0,-1,0,-1,1,-1,-1]]
uniform_cost = 1

#for the children you can move it left, right, up, down. Only if 0 is there

def calculate_manhatten(current_matrix, end_matrix):
    total_distance = 0
    print(end_matrix[1][7])
    for row in range(2):
        for column in range(10):
            if current_matrix[row][column] != end_matrix[row][column]:
                print(row,column)
                print("Hello")
                print(current_matrix[row][column])
                if current_matrix[row][column] != 0:
                    print("hello")
                    if current_matrix[row][column] != -1:
                        print("hello")
                        #lets put a check
                        check=False
                        #get the row position of that misplaced tile
                        row_pos= row
                        #get the column position of that misplaced tile
                        column_pos = column
                        #we want to store that value of where it currently is in our matrix
                        num = current_matrix[row][column]
                        #intilizing values
                        row_pos_goal=0
                        column_pos_goal=0
                        #go through the goal state matrix
                        for row in range(2):
                            for column in range(10): 
                                #now we find where that tile is we stored in the goal state
                                if end_matrix[row][column]==num:
                                    #now we can set our check to true after we find the tile in goal state
                                    check=True
                                    # we get the new locations of the goal state of that tile for row and column
                                    row_pos_goal= row
                                    column_pos_goal = column
                                    break
                                #lets break out of the loop so we dont account for mutliple checks after we find the tile
                                if check:
                                    break
                            #Now simple we take the difference of the locations in the intial matrix and the goal matrix
                        print(row_pos, column_pos)
                        print(row_pos_goal, column_pos_goal)
                        total_distance+=abs(row_pos-row_pos_goal) + abs(column_pos-column_pos_goal)
        
        return total_distance

def main():
    print(calculate_manhatten(start_matrix, end_matrix))
main()