
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
    PAIR_TELEPORT = "A"
    

class mazeGenerator:

    def __init__ (self,width=10,height=10):
        self.maze=[[]]
        self.imax=height
        self.jmax=width
        self.visited= [ [ False for _ in range( self.jmax+1)] for _ in range(self.imax+1) ]
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
        self.maze = [ [ mazeSymbols.WALL for _ in range(2*self.jmax+1)] for _ in range(2*self.imax+1) ]
 
        for i in range(1,2*self.imax,2):
            for j in range(1,2*self.jmax,2):
                rooms.append((i,j))
                self.maze[i][j]=mazeSymbols.EMPTY

        self._printVisited()
        self.recursiveMethod((1,1))
        self.visited= [ [ False for _ in range(self.jmax+1)] for _ in range(self.imax+1) ]
        self.recursiveMethod((5,5))
        for room1,room2 in self.listToRemove:
            self._removeWall(room1,room2)
        
        self.deleteSingleCorners()
        self.distributeItems()
        
        return self.maze
    
    def distributeItems(self):
        foodx,foody=self._getRoomPosition((random.randint(1,self.imax),random.randint(1,self.jmax)))
        self.maze[foodx][foody]=mazeSymbols.GHOST

        foodx,foody=self._getRoomPosition((random.randint(1,self.imax),random.randint(1,self.jmax)))
        self.maze[foodx][foody]=mazeSymbols.FOOD
       # self.maze[1][1]=mazeSymbols.PACMAN

        foodx,foody=self._getRoomPosition((random.randint(1,self.imax),random.randint(1,self.jmax)))
        self.maze[foodx][foody]=mazeSymbols.PAIR_TELEPORT
        foodx,foody=self._getRoomPosition((random.randint(1,self.imax),random.randint(1,self.jmax)))
        self.maze[foodx][foody]=mazeSymbols.PAIR_TELEPORT
        self.maze[1][1]=mazeSymbols.PACMAN



    def writeMaze(self,name="randomTest.lay",file=False):
        file = open("layouts/"+ name, "w")

        str_maze=""
        for rows in self.maze:
            str_row=""
            for elem in rows:
                str_row+=elem
            str_row+='\n'
            str_maze+=str_row
        if file:
            file.write(str_maze)
        return str_maze
          

    def __randomName(self,codeLenght):
        code = "".join(random.choice(string.ascii_lowercase) for i in range(codeLenght))
        return code + "Maze.lay"

    def _printMaze(self):

        for rows in self.maze:
            for i in rows:
                print i,
            print "\n",
        print "\n",

    def _printVisited(self):
        for rows in self.visited:
            for i in rows:
                print i,
            print "\n",
        print "\n",

    def isInsideTheMaze(self,x,y):
        return x > 0 and y > 0 and x <= self.imax and y <= self.jmax 

    def _getRoomPosition(self,room):
        x,y=room
        return (2*(x-1)+1,2*(y-1)+1)

    def _getWallBetween(self,pos1,pos2):
        distance=tuple( map(lambda x,y: x-y, pos1,pos2))
        distance=tuple( map(lambda x: x/2, distance))
        wall=tuple( map(lambda x,y: x-y, pos1,distance))

        return wall

    def _removeWall(self,room1,room2):
        position1 = self._getRoomPosition(room1)
        position2 = self._getRoomPosition(room2)
        x,y=self._getWallBetween(position1,position2)
        self.maze[x][y]=mazeSymbols.EMPTY

    def isSingleCorner(self,i,j):
        if (self.maze[i][j] != mazeSymbols.WALL):
            return False 
        dir8=[(0,1),(0,-1),(-1,0),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        for direction in dir8:
            addi,addj= direction
            newi=addi+i
            newj=addj+j
            if(newi < 1 or newj < 1):
                return False 
            elif (self.maze[newi][newj] == mazeSymbols.WALL):
                return False

        return True

    def deleteSingleCorners(self):
        for i in range(1,2*self.imax,1):
            for j in range(1,2*self.jmax,1):
                
                if(self.isSingleCorner(i,j)):
                    self.maze[i][j] = mazeSymbols.EMPTY
     

def runGenerator(mapName,level=1):
    x= random.randint(3,8)
    y= random.randint(3,5)
    print x,y
    gen=mazeGenerator(2*x,2*y)
    gen.generate()

    gen._printMaze()
    gen.writeMaze("randomTest.lay",True)



if __name__ == "__main__":
   runGenerator("randomMap.lay")