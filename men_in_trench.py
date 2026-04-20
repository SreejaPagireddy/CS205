
import copy
import heapq
end_matrix = [[ 1,2,3,4,5,6,7,8,9,0],
               [-1,-1,-1,0,-1,0,-1,0,-1,-1]]
start_matrix = [[0,2,3,4,5,6,7,8,9,1],
                [-1,-1,-1,0,-1,0,-1,0,-1,-1]]
uniform_cost = 1
class Node:    
    def __init__(self,state):
        #this is the state of the node, the matrix
        self.current_matrix = state
        #parent tracker
        self.parent = []
        #lets keep track of the cost 
        self.cost= 0
        #This is the herusitc cost for misplaced or manhatten
        self.heristic = 0
    
    def __str__(self):
        #This is representing the matrix of the object, it converts it to a string
        return str(self.current_matrix)

    
    def __repr__(self):
        # This method was used for debugging to see the herusitic value
        return str(self.heristic) +":" + str(self.current_matrix)

    
    def __lt__(self, other):
        # This method compares the herustic values of 2 objects
        return self.heristic < other.heristic
    

    #copied from my eight puzzle
    #for the children you can move it left, right, up, down. Only if 0 is there
    def calculate_manhatten(self, end_matrix):
        total_distance = 0
        for row in range(2):
            for column in range(10):
                if self.current_matrix[row][column] != 0:
                    if self.current_matrix[row][column] != -1:
                        if self.current_matrix[row][column] != end_matrix[row][column]:
                            #lets put a check
                            check=False
                            #get the row position of that misplaced tile
                            row_pos= row
                            #get the column position of that misplaced tile
                            column_pos = column
                            #we want to store that value of where it currently is in our matrix
                            num = self.current_matrix[row][column]
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
                            total_distance+=abs(row_pos-row_pos_goal) + abs(column_pos-column_pos_goal)
        return total_distance

    def children(self):
        #We want to get the possible moves, #We have to account the uniform plus the heruistic and then go take that path to goal state,
        #make a copy of the matrix
        children = []
        for row in range(2):
            for column in range(10):
                temp_matrix = copy.deepcopy(self.current_matrix)
                #print(temp_matrix)
                if self.current_matrix[row][column] == 0:
                    if column>0 and self.current_matrix[row][column-1] != -1:
                        #reffered to from my previous 8 puzzle code
                        temp_matrix[row][column], temp_matrix[row][column -1] = self.current_matrix[row][column-1], self.current_matrix[row][column]
                        children.append(temp_matrix)
                    if column<10 and self.current_matrix[row][column+1] != -1:
                        temp_matrix[row][column], temp_matrix[row][column +1] = self.current_matrix[row][column+1], self.current_matrix[row][column]
                        children.append(temp_matrix)
                    if row>0 and self.current_matrix[row-1][column] != -1 :
                        temp_matrix[row][column], temp_matrix[row-1][column] = self.current_matrix[row-1][column], self.current_matrix[row][column]
                        children.append(temp_matrix)
        #Now we want to convert all the matrixes to node because we want to store the nodes
        for row in range(len(children)): # now we want to traverse through all the children we appended
            create_node = Node(children[row]) # we want to convert it to a Node becasue we are creating these matrix as a node
            create_node.cost = self.cost + 1  # we add the cost, or depth to these children
            create_node.parent = self #we assign the intial node as the parent to these children
            children[row] = create_node #putting it back into return_children array as nodes
        return children
#copied from 8-puzzle
def queue_make_node(initial_state):
    #create a new quene and node
    queue = []
    #creating a node
    new_node = Node(initial_state)
    #using a heapq so we can order it based on the priority values or in other words the herustic + cost
    heapq.heappush(queue, new_node) 
    #queue.append(new_node)
    return queue

def general_search(problem, target ):
    # lets make a dictionary to keep track of the repeating states
    repeat = dict()
    # we are making the quene and adding the intial matrix to the quene
    nodes = queue_make_node(problem)
    #keeping track of the total_nodes, max_size, and count
    total_nodes=0
    max_size=0
    #this count is so I dont print the first intial matrix that the user enters
    count =0
    #check if the whole quene is empty, if its not empty than only going through the while loop
    while (len(nodes)!=0):
        #lets add the total_nodes that we are expanding and lets get the max size of the quene
        total_nodes=total_nodes+1
        max_size= max(len(nodes),max_size)
        curNode = nodes.pop(0) #remove the first element
        count = count+1 # increase count
        #add the matrix into the repeat dictionary
        repeat[hash(tuple(map(tuple, curNode.current_matrix)))] = 1
        #print all the matrix's except for the intiial one
        if(count>1):     
            print(curNode)

        
        if(curNode.current_matrix == target): #this is how we are checking if its a goal state
            #Lets print out all the of the following when we find the goal state
            print("Solution Depth",curNode.cost) 
            print("Number of nodes expanded", total_nodes)
            print("Max quene size", max_size)
            return curNode
        #now we want to go through the children
        for child in curNode.children(): #simmilar to expanding
            #lets set that inital matrix we expanding to the parent
            child.parent = curNode
            #make sure that the children are not a repeat, we dont wanna push repeates
            if(not (hash(tuple(map(tuple, child.current_matrix))) in repeat)):
                #if its uniform cost
                child.heristic = child.cost + child.calculate_manhatten(target)
                heapq.heappush(nodes, child) #appending children based on the herusitc values, priority quene
                #adding these to repeate so we dont repeate in any of the children
                repeat[hash(tuple(map(tuple, child.current_matrix)))] = 1
    #we are going to return failure if the quene was empty
    return "Failure"  
def main():
    #print(calculate_manhatten(start_matrix, end_matrix))
    general_search(start_matrix, end_matrix)
main()