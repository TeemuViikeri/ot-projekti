from collections import deque
import time


class Node:
    # Initialize a Node with no left or right child
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    # Initialize an empty tree with a root node
    def __init__(self, value):
        self.root = Node(value)
        self.count = 1

    def size(self):
        return self.count

    def min(self):
        current_node = self.root

        while(current_node.left):
            current_node = current_node.left

        return current_node.value

    def max(self):
        current_node = self.root

        while(current_node.right):
            current_node = current_node.right

        return current_node.value

    def contains(self, value):
        current_node = self.true

        while (current_node):
            if (value == current_node.value):
                return True

            if (value < current_node.value):
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False

    # Non-recursive insert function
    def insert(self, value):
        self.count += 1

        # If root node is empty
        if self.root == None:
            # Insert 'value' as root node
            self.root = Node(value)
        # Otherwise...
        else:
            # Call recursive _insert() that starts from root node
            self._insert(value, self.root)

    # Private recursive insert function that does the job
    def _insert(self, value, current_node):
        # If value is less than current node's value...
        if value < current_node.value:
            # If current node doesn't have a left child
            if current_node.left == None:
                # Insert a new Node as left child
                current_node.left = Node(value)
            # Otherwise...
            else:
                # Call recursive _insert(): go deeper into tree
                # Current node's left child becomes current_node
                self._insert(value, current_node.left)
        # If value is higher than current node's value...
        elif value > current_node.value:
            # If current node doesn't have a right child
            if current_node.right == None:
                # Insert a new Node as a right child
                current_node.right = Node(value)
            # Otherwise...
            else:
                # Call recursive _insert(): go deeper into tree
                # Current node's right child becomes current_node
                self._insert(value, current_node.right)
        # If value is the same as current node's value
        else:
            # Don't insert any values to the tree and...
            print("WARNING: duplicate value which was not inserted")

    # BREADTH-FIRST TRAVERSAL
    # alkutila = BST root node/current node
    def maiju(self, alkutila=None):
        # Set variable to be root of the tree
        root = self.root if alkutila is None else alkutila
        # Iniatilize 'nodes' list with root node
        level = [root]
        # Loop through 'nodes' list as long as there are nodes in BST, start with root
        while level:
            # PRINTING
            # A list of values from nodes in current level
            values = (node.value for node in level)
            # Print values in one line
            print(" ".join(map(str, values)))

            # TRAVERSAL
            # Initialize an empty list for next level nodes
            next_level = []
            # Iterate over nodes in level
            for node in level:
                # Store next level nodes to states
                successors = self.seuraajat(node)
                # Iterate over successors: appends successors to 'next_level'
                for s in successors:
                    next_level.append(s)
            # Insert next level nodes to 'next_level' list
            level = next_level

    # DEPTH-FIRST TRAVERSAL, PREORDER
    # alkutila = BST root node/current node
    def risto(self, alkutila):
        # Display current node's value
        print(alkutila.value)
        # Make a list of successor nodes
        successors = self.seuraajat(alkutila)
        # Iterate successors
        for s in successors:
            # If successor node's value is less than current node's value
            if s.value < alkutila.value:
                # call risto() again recursively with current node's left child as the argument
                self.risto(alkutila.left)
            # If successor node's value is less than current node's value
            elif s.value > alkutila.value:
                # call risto() again recursively with current node's right child as the argument
                self.risto(alkutila.right)

    # HELPER FUNCTION TO BFS/DFS FUNCTIONS
    # tilatunnus = current node
    def seuraajat(self, tilatunnus):
        # Initialize an empty list
        successors = []
        # If state has left child...
        if tilatunnus.left:
            # Append left child to list
            successors.append(tilatunnus.left)
        # If state has right child...
        if tilatunnus.right:
            # Append right child to list
            successors.append(tilatunnus.right)

        # Return list
        return successors


class State:
    def __init__(self, students, bogeys, elevator):
        # Amount of students on the ground floor [0, 1, 2]
        self.students = students
        # Amount of bogeys in the ground floor [0, 1, 2]
        self.bogeys = bogeys
        # Is elevator on the second or ground floor [0, 1]
        self.elevator = elevator

    def successors(self):
        # If elevator is on the ground floor == 1
        if self.elevator == 1:
            # Make sign variable/operator minus so that the elevator goes to second floor next
            sign = -1
            # Part of the string which will be displayed
            direction = "from the ground floor to the second floor"
        # Oftherwise (elevator is on the second floor == 2)
        else:
            # Make sign operator plus so that the elevator goes to ground floor next
            sign = 1
            # Part of the string which will be displayed
            direction = "back from the second floor to the ground floor"
        # Loops through all possibilities of how many students can go to the elevator [0..2]
        for s in range(3):
            # Loops through all possibilities of how many bogeys can go to the elevator [0..2]
            for b in range(3):
                # Create a new state which may or may not be valid
                newState = State(self.students + sign * s,
                                 self.bogeys + sign * b, self.elevator + sign * 1)
                # Validate: check if movement values and the new state itself are valid
                # Note: s + b must be 1 or 2
                # If they are valid...
                if s + b >= 1 and s + b <= 2 and newState.isValid():
                    # Store the action as a to-be-displayed string to variable
                    action = "take %d students and %d bogeys %s." % (
                        s, b, direction)
                    # Yield current action and new State for iteration
                    yield action, newState

    def isValid(self):
        # Check that there are no less than 0 or more than 3 students/bogeys on any state
        # Check that the elevator values is 0 (second floor) or 1 (ground floor)
        if self.students < 0 or self.bogeys < 0 or self.students > 3 or self.bogeys > 3 or (self.elevator != 0 and self.elevator != 1):
            return False
        # Check there aren't more bogeys than students on the ground floor if there are also students
        if self.bogeys > self.students and self.students > 0:
            return False
        # Check there aren't more bogeys than students on the second floor floor if there are also students
        if self.bogeys < self.students and self.students < 3:
            return False
        # Return True if none of the previous validation checks return False
        return True

    def is_goal_state(self):
        # If there are no bogeys or students on the ground floor and elevator is on the second floor
        return self.bogeys == 0 and self.students == 0 and self.elevator == 0


class NodeL:
    def __init__(self, parent_node, state, action, depth):
        # Parent node of this node
        self.parent_node = parent_node
        # State of this node
        self.state = state
        # An action that leads to a successor state
        self.action = action
        # Depth/step of current node
        self.depth = depth

    # Create all successor nodes
    def expand(self):
        # Iterate over actions and successor states yielded from successors() generator
        for (action, successor_state) in self.state.successors():
            # Create a successor node
            # parent_node = this instance
            # state = valid state created from generator
            # action = valid action created from generator
            # depth = current depth + 1
            successor_node = NodeL(
                parent_node=self,
                state=successor_state,
                action=action,
                depth=self.depth + 1
            )
            # Yield successor Node for iteration
            yield successor_node

    def extract_solution(self):
        # Initialize an empty list
        solution = []
        # Store this instance to a variable
        node = self
        # Loop through to the point when node has no parent node
        while node.parent_node is not None:
            # Append current node's action to 'solution' list
            solution.append(node.action)
            # Change current node to current node's parent node
            node = node.parent_node
        # Reverse the order of 'solution' list
        solution.reverse()
        # Return 'solution' list
        return solution


def breadth_first_tree_search(initial_state):
    # Create an initial node
    # parent_node = no parent node for root node
    # state = initial state which is created is passed as an argument
    # action = no action yet
    # depth = depth is 0 for root node
    initial_node = NodeL(
        parent_node=None,
        state=initial_state,
        action=None,
        depth=0)
    # Initialize a queue with initial node as its only value at this point
    queue = deque([initial_node])
    # Initialize a variable for max depth
    max_depth = -1
    # Endless loop...
    while True:
        # If queue is empty...
        if not queue:
            # Returns None
            return None
        # Pop leftmost Node from queue to variable as the current node
        node = queue.popleft()
        # If current node's depth is higher than max depth...
        if node.depth > max_depth:
            # Max depth gets value from current node's depth
            max_depth = node.depth
        # If current node's state is the wanted goal state...
        if node.state.is_goal_state():
            # Store all actions from root to current node on 'solution' list
            solution = node.extract_solution()
            # Return solution
            return solution
        # Extend queue with current node's successor node
        queue.extend(node.expand())


def liisa():
    # Initialize the initial state
    initial_state = State(3, 3, 1)
    # Get solution from breadth_first_tree_search()
    solution = breadth_first_tree_search(initial_state)
    # If there is no solution...
    if solution is None:
        # Display there is no solution
        print("no solution")
    # Otherwise...
    else:
        # Display how many steps solution took
        print("solution (%d steps):" % len(solution))
        # Iterate over solution's actions
        for step in solution:
            # Display action
            print("%s" % step)


def main():
    # INITIALIZING BST FOR THE FIRST TWO  EXERCISES
    bst = Tree("k")  # 107
    bst.insert("b")  # 98
    bst.insert("z")  # 122
    bst.insert("f")  # 102
    bst.insert("j")  # 106
    bst.insert("i")  # 105
    bst.insert("m")  # 109
    bst.insert("d")  # 100

    # START OF MAIJA MATELIJA
    print("BREADTH-FIRST TRAVERSAL")
    bst.maiju(bst.root)
    # END OF MAIJA MATELIJA
    # START OF RISTO REPTIILI
    print("DEPTH-FIRST TRAVERSAL")
    bst.risto(bst.root)
    # END OF RISTO REPTIILI
    # START OF LIISA LUIKERO
    print("STUDENTS AND BOGEYS PROBLEM")
    liisa()
    # END OF LIISA LUIKERO


main()
