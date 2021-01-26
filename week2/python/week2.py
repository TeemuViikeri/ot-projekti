from collections import deque


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


def main():
    tree = Tree("k")  # 107

    tree.insert("b")  # 98
    tree.insert("z")  # 122
    tree.insert("f")  # 102
    tree.insert("j")  # 106
    tree.insert("i")  # 105
    tree.insert("m")  # 109
    tree.insert("d")  # 100

    tree.maiju(tree.root)
    print("-----")
    tree.risto(tree.root)


main()
