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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    currentState = problem.getStartState()
    set = {currentState}
    stack = [currentState]
    """
    a. Create set that contains all visited nodes
    b. Create stack that contains history of moves
    1. Scan current successors. 
        For each successor, check if it has been visited.
    2. If a successor hasn't been visited (isn't in set), go there, updating set & stack
    3. If all successors have been visited, reverse by popping history stack and repeat step 1        
    """

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    while not problem.isGoalState(currentState): # Until the goal is found,
        print("here")
        noPath = 1
        possiblePaths = problem.getSuccessors(currentState)
        for possiblePath in possiblePaths:
            coordinates = possiblePath[0]
            if coordinates not in set:
                set.add(coordinates)
                stack.push(possiblePath)
                """views top of stack"""
                print(stack)
                currentState = stack[-1][0]
                noPath = 0
                break

        if (noPath == 1): # If no more routes, backtrack and repeat
            stack.pop()
            print(stack)
            currentState = stack[-1][0]

    history = []
    while (not stack.isEmpty()): # Extract the directions only
        history.append(stack[-1][1])
    history.reverse()
    print(history)

    return history


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    startPos = problem.getStartState()
    visited = [startPos]
    queue = [([startPos], ["n/a"])]

    while queue: # While the queue is not empty,
        posList, dirList = queue.pop(0)
        lastPos = posList[-1]
        possiblePaths = problem.getSuccessors(lastPos)
        for possiblePath in possiblePaths:
            possiblePos, possibleDir, x = possiblePath
            neighbours = []
            if possiblePos not in visited:
                neighbours.append(possiblePath)
                visited.append(possiblePos)
                for newCoords, newDir, newCost in neighbours:
                    newPath = dirList + [newDir]
                    newPathCoords = posList + [newCoords]
                    if problem.isGoalState(newCoords):
                        print("newpath is...")
                        newPath.pop(0) # Unnecessary, but I added "n/a" to the path at the starting position.
                        print(newPath)
                        return newPath

                    node = (newPathCoords, newPath)
                    queue.append(node)
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startPos = problem.getStartState()
    visited = [startPos]
    'queue = [([startPos], ["n/a"])]'
    prioQueue = util.PriorityQueue()
    tupleTest = ([startPos], [], 0)
    prioQueue.push(tupleTest, 0)

    while prioQueue: # While the priority queue is not empty,
        posList, dirList, cost = prioQueue.pop()
        lastPos = posList[-1]
        possiblePaths = problem.getSuccessors(lastPos)
        for possiblePath in possiblePaths:
            possiblePos, possibleDir, nextCost = possiblePath
            neighbours = []
            if possiblePos not in visited or cost < nextCost:
                neighbours.append(possiblePath)
                visited.append(possiblePos)
                for newCoords, newDir, oldCost in neighbours:
                    newPath = dirList + [newDir]
                    newPathCoords = posList + [newCoords]
                    newCost = nextCost + oldCost
                    if problem.isGoalState(newCoords):
                        #print("newpath is...")
                        #print(newPath)
                        return newPath
                    node = (newPathCoords, newPath, newCost)
                    prioQueue.push(node, newCost)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    startPos = problem.getStartState()
    visited = [startPos]
    'queue = [([startPos], ["n/a"])]'
    prioQueue = util.PriorityQueue()
    tupleTest = ([startPos], [], 0)
    prioQueue.push(tupleTest, heuristic(startPos,problem))
    print(heuristic(startPos,problem))
    while prioQueue: # While the priority queue is not empty,
        posList, dirList, cost = prioQueue.pop()
        lastPos = posList[-1]
        possiblePaths = problem.getSuccessors(lastPos)
        for possiblePath in possiblePaths:
            possiblePos, possibleDir, nextCost = possiblePath
            neighbours = []
            if possiblePos not in visited or cost < nextCost:
                neighbours.append(possiblePath)
                visited.append(possiblePos)
                for newCoords, newDir, oldCost in neighbours:
                    newPath = dirList + [newDir]
                    newPathCoords = posList + [newCoords]
                    newCost = heuristic(possiblePos,problem) + oldCost

                    if problem.isGoalState(newCoords):
                        #print("newpath is...")
                        #print(newPath)
                        return newPath
                    node = (newPathCoords, newPath, newCost)
                    prioQueue.push(node, newCost)
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
