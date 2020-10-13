
import random
import string
import util

directions=[(0,1),(0,-1),(-1,0),(1,0)]

class mazeGenerator:

    def __init__ (self,width=10,height=10):
        self.maze=[[]]
        self.xmax=width
        self.ymax=height
        self.visited= [ [ False for _ in range(width)] for _ in range(height) ]
        self.listToRemove=[]

    def recursiveMethod( self,pos):
            
            x,y=pos
            self.visited[x][y]=True

            random.shuffle(directions)
            for direction in directions:
                newPos=pos + direction
                newPos=tuple( map(lambda x,y: x+y, pos,direction))
                newx,newy=newPos
                print self.isInsideTheMaze(newx,newy) 
                if self.isInsideTheMaze(newx,newy) == True:
                   
                    if self.visited[newx][newy] == False:
                    
                        self.listToRemove.append((newPos,pos))
                        self.recursiveMethod(newPos) 
               


            

    def generate(self):
        """Create maze

        Paramaters
        ----------
        name : str
            Name for the maze
        width : int

        Returns
        -------

        """
        rooms=[]
        self.maze = [ [ '%' for _ in range(3*self.xmax+1)] for _ in range(3*self.ymax+1) ]
        for i in range(1,3*self.xmax,2):
            for j in range(1,3*self.ymax,2):
                rooms.append((i,j))
                self.maze[i][j]='_'
        print rooms
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
        return x > 0 and y > 0 and x < self.xmax and y<self.ymax 

    def getRoom(self,x,y):
        pass
        









def runGenerator():
    pass



if __name__ == "__main__":
    gen=mazeGenerator(11,11)
    gen.generate()
    gen._printMaze()


