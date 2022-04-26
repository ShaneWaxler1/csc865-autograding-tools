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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # I feel insane for writing the code like this.
    return generic_search(problem, util.Stack)



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return generic_search(problem, util.Queue)


def generic_search(problem, data_structure):
    frontier = data_structure()
    visited = [problem.getStartState()]
    for node in problem.getSuccessors(problem.getStartState()):
        frontier.push(node)
        # visited.append()
    # Visited should have the coordinate
    path = []
    # Path should just contain direction
    temp_node = problem.getStartState()
    while not frontier.isEmpty():

        print("*********DEBUG*********\n"
              "path: ", path, "\n",
              "visited: ", visited, "\n",
              "frontier: ", frontier.list, "\n",)
        # temp_node # = curr.parent
        curr = frontier.pop()
        coordinate = curr[0]
        direction = curr[1]
        cost = curr[2]
        print("\nCurrent node: \n\n", curr, "\n\n")
        print("Node has children? ", len(problem.getSuccessors(coordinate)))
        temp_list = []

        # Check if all of node's children have been visited.
        for state in problem.getSuccessors(coordinate):
            temp_list.append(state[0] in visited)

        print("temp_list: ", temp_list)
        print("all(temp_list)", all(temp_list))

        if coordinate not in visited:
            visited.append(coordinate)
            path.append(curr)
            # Return the path to the goal when the goal is achieved.
            print("Is the current node a goal state? ", problem.isGoalState(coordinate))
            if problem.isGoalState(coordinate):
                print("Returning: ", path)
                break
            print("problem.getSuccessors(coordinate): ", problem.getSuccessors(coordinate))
            for node in problem.getSuccessors(coordinate):
                print("node: ", node)
                if node[0] not in visited:
                    print("Adding ", node[0])
                    frontier.push(node)
            # Remove item from path if there are no children + it is not a goal state

        if all(temp_list):
            # If all node's children have been visited, remove node from path.
            path.remove(curr)
            frontier.push(curr)
            # visited.remove(popped_value[0])
        temp_list.clear()
        temp_node = path[-1]
    else:
        print("Goal node not found.")
    return_list =[]
    for element in path:
        return_list.append(element[1])
    return return_list


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
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
