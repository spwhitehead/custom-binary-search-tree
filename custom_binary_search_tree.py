# Implement a BST. It should include these methods:
# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
class Node():
    def __init__(self, value):
        self.value: int = value
        self.left: Node = None
        self.right: Node = None

class BST():
    def __init__(self, root: Node=None):
        self.root: Node = root

    def insert(self, value: int):
        """inserts a number into the tree"""
        if self.root is None:
            self.root = Node(value)
        else:
            self.ins_recursive(value, self.root)
      

    def ins_recursive(self, value: int, current_node: Node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.ins_recursive(value, current_node.left)
        else:
            if value > current_node.value:
                if current_node.right is None:
                    current_node.right = Node(value)
                else:
                    self.ins_recursive(value, current_node.right)
            

    def search(self, value: int) -> bool:
        """returns whether or not a value is in the tree"""
        if self.root is None:
            return False
        else:
            return self.search_recursive(value, self.root)

    def search_recursive(self, value: int, current_node: Node):
        if current_node.value == value:
            return True
        else:
            if value < current_node.value:
                if current_node.left == None:
                    return False
                else:
                    return self.search_recursive(value, current_node.left)
                         
            if value > current_node.value:
                if current_node.right == None:
                    return False
                else: 
                    return self.search_recursive(value, current_node.right)


    def in_order_traversal(self, current_node: Node=None) -> list[int]:
        """returns a list of all the values in sorted order"""
        values = []
        v_left = []
        v_right = []
        if current_node == None:
            current_node = self.root
        if current_node == None:
            return []

        else:
            if current_node.left != None:
                v_left = self.in_order_traversal(current_node.left)   

            v_left.append(current_node.value)

            if current_node.right != None:
                v_right = self.in_order_traversal(current_node.right)
            
            values = v_left + v_right
            
            return values


    def find_min(self, current_node: Node=None) -> int:
        """returns the smallest number in the tree(you cannot turn the tree into a list then return an element from the list, you must do it by traversing the tree)"""
        if current_node == None:
            current_node = self.root

        if self.root == None:
            return current_node.value
        
        while current_node.left != None:
            current_node = current_node.left
        return current_node.value


    def find_max(self, current_node: Node=None) -> int:
        """returns the largest number in the tree(you cannot turn the tree into a list then return an element from the list, you must do it by traversing the tree)"""
        if current_node == None:
            current_node = self.root

        if self.root == None:
            return current_node.value
        
        while current_node.right != None:
            current_node = current_node.right
        return current_node.value 


    def height(self, current_node: Node=None) -> int:
        """returns the depth of the tree(how far is the furthest node from the root node?)"""
        if current_node is None:
            current_node = self.root
        if self.root is None:
            return 0
        else:
            lcount = 0
            rcount = 0
            if current_node.left != None:
                lcount = self.height(current_node.left)
                
            if current_node.right != None:
                rcount = self.height(current_node.right)

        return max(lcount, rcount) + 1
       

    def count_leaves(self, current_node: Node=None) -> int:
        """returns the number of leaf nodes in the tree(leaf nodes are nodes without any children)"""
        if current_node is None:
            current_node = self.root
        if current_node is None:
            return 0
        if current_node.left is None and current_node.right is None:
            return 1
        else:
            lcount = 0
            rcount = 0
            if current_node.left != None:
                lcount = self.count_leaves(current_node.left)
            if current_node.right != None:
                rcount = self.count_leaves(current_node.right)
        return lcount + rcount


    def serialize(self, current_node: Node=None) -> str:
        """turn the BST into a string that can be deserialized into the same tree"""
        if current_node == None:
            current_node = self.root
        if current_node == None:
            return ""
        else:
            serialized_list = []
            serialized_list.append(str(current_node.value))
            if current_node.left != None:
                serialized_list.append(self.serialize(current_node.left))
            if current_node.right != None:
                serialized_list.append(self.serialize(current_node.right))
            return "\xa0".join(serialized_list)

    def deserialize(self, serialized_nums: str) -> None:
        """deserialize a serialized BST(take a string version of a BST and make an empty BST filled with those values). The new tree should match the tree that was serialized."""
        self.root = None
        serialized_nums = serialized_nums.split("\xa0")
        for value_str in serialized_nums:
            value = int(value_str)
            self.insert(value)