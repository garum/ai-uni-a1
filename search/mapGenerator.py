
import random
import string
import util

directions=[(0,1),(0,-1),(-1,0),(1,0)]

class mazeSymbols:
    EMPTY = '_'
    WALL = "%"
    PACMAN = "P"
    GHOST = "G"
    FOOD = "."
    

class mazeGenerator:

    def __init__ (self,width=10,height=10):
        self.maze=[[]]
        self.xmax=width
        self.ymax=height
        self.visited= [ [ False for _ in range(width+1)] for _ in range(height+1) ]
        self.listToRemove=[]

    def recursiveMethod( self,pos):
            
            x,y=pos
            self.visited[x][y]=True

            random.shuffle(directions)
            for direction in directions:
                newPos=pos + direction
                newPos=tuple( map(lambda x,y: x+y, pos,direction))
                newx,newy=newPos
                if self.isInsideTheMaze(newx,newy) == True:
                   
                    if self.visited[newx][newy] == False:
                    
                        self.listToRemove.append((newPos,pos))
                        self.recursiveMethod(newPos) 
               


            

    def generate(self):

        rooms=[]
        self.maze = [ [ mazeSymbols.WALL for _ in range(2*self.xmax+1)] for _ in range(2*self.ymax+1) ]
        for i in range(1,2*self.xmax,2):
            for j in range(1,2*self.ymax,2):
                rooms.append((i,j))
                self.maze[i][j]=mazeSymbols.EMPTY
        
        self.recursiveMethod((1,1))
        self.visited= [ [ False for _ in range(self.xmax+1)] for _ in range(self.ymax+1) ]
        self.recursiveMethod((5,5))
        for room1,room2 in self.listToRemove:
            self.removeWall(room1,room2)

        return self.maze

    def __writeMaze(self):
        pass

    def __randomName(self,codeLenght):
        code = "".join(random.choice(string.ascii_lowercase) for i in range(codeLenght))
        return code + "Maze.lay"

    def _printMaze(self):

        for rows in self.maze:
            for i in rows:
                print i,
            print "\n",
        print "\n",

    def isInsideTheMaze(self,x,y):
        return x > 0 and y > 0 and x <= self.xmax and y <= self.ymax 

    def _getRoomPosition(self,room):
        x,y=room
        return (2*(x-1)+1,2*(y-1)+1)

    def _getWallBetween(self,pos1,pos2):
        distance=tuple( map(lambda x,y: x-y, pos1,pos2))
        distance=tuple( map(lambda x: x/2, distance))
        wall=tuple( map(lambda x,y: x-y, pos1,distance))

        return wall

    def removeWall(self,room1,room2):
        position1 = self._getRoomPosition(room1)
        position2 = self._getRoomPosition(room2)
        x,y=self._getWallBetween(position1,position2)
        self.maze[x][y]=mazeSymbols.EMPTY

def runGenerator():
    pass



if __name__ == "__main__":
    gen=mazeGenerator(10,10)
    gen.generate()
    gen.maze[1][1]=mazeSymbols.FOOD
    gen.maze[1][3]=mazeSymbols.PACMAN
    gen._printMaze()


