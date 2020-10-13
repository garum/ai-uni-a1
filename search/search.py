# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()



def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
        """
    state= problem.getStartState()
    curentPath=[]
    frontier= util.Stack()
    frontier.push((state,[]))
    vistited=[]
    while not problem.isGoalState(state) or frontier.isEmpty():
     
        vistited.append(state)
        successors = problem.getSuccessors(state)
        for state,direction,_  in successors:
            if(state not in vistited):
                newPath = curentPath+ [direction]
                
                frontier.push((state,newPath))
        
        state,curentPath=frontier.pop()
    return curentPath
        

 


def randomSearch(problem):

    import random
    state= problem.getStartState()
    path=[]
    while not problem.isGoalState(state):
        successors = problem.getSuccessors(state)
        successor = random.choice(successors)
        state=successor[0]
        path.append(successor[1])

    return path
   

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    state= problem.getStartState()
    curentPath=[]
    frontier= util.Queue()
    frontier.push((state,[]))
    vistited=[]
    while ((not problem.isGoalState(state)) or frontier.isEmpty()):
     
        print(state, curentPath)
        vistited.append(state)
        successors = problem.getSuccessors(state)
        for state,direction,_  in successors:
            if(state not in vistited):
                newPath = curentPath+ [direction]
                
                frontier.push((state,newPath))
        state,curentPath=frontier.pop()
    print(curentPath)
    return curentPath

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    state= problem.getStartState()
    
    cost=0
    frontier= util.PriorityQueue()
    frontier.push((state),0)

    score=dict()
    score[state]=0
    paths=dict()
    paths[state] = [] 
    f=dict()
    f[state]= score[state] + heuristic(state,problem)
    while not problem.isGoalState(state) or frontier.isEmpty():

        for neighbor,direction,cost in problem.getSuccessors(state):
            
            if neighbor not in score:
                score[neighbor]=score[state]+cost
                paths[neighbor]= paths[state] + [direction]
                frontier.push(neighbor,score[neighbor] +heuristic(neighbor,problem)) 
            else:

                if(score[neighbor] > score[state]+cost ):
                    score[neighbor]= score[state] + cost
                    paths[neighbor]= paths[state] + [direction]
                    frontier.update(neighbor,score[neighbor] + heuristic(neighbor,problem)) 
        
        state = frontier.pop()
    return paths[state]

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
