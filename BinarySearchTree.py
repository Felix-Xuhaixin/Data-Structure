# property: Every key to the left of node is smaller than node, 
#  every key to the right of node is larger than node

class Node:
    
    def __init__(self,key):
        self.left = None
        self.right = None
        self.parent = None  
        self.key = key
        self.value = None

    def  __repr__(self):
        print (f"({self.key},{self.value})")

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __contains__(self,key):
        current_node = self.root

        while current_node is not None:
            if current_node < key:
                current_node = current_node.left
            elif current_node > key:
                current_node = current_node.right
            else:
                return True
        
        return False
        

    def __iter__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else:
            current_node = self.root
            while True:
                if current_node.key > key:
                    if current_node.left is None:
                        current_node.left = Node(key)
                        current_node.left.value = value
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                elif current_node.key < key:
                    if current_node.right is None:
                        current_node.right = Node(key)
                        current_node.right.value = value
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    current_node.value = value
                    break
                    
             

    def search(self, key):
        current_node =  self.root

        while True:         
            if current_node is None or current_node.key == key:
                return current_node
            elif key < current_node.key:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right
                    
                


    def delete(self,key):
        node = self.search(key)
        
        if node is None:
            print(KeyError('Node with this key does not exist'))

        self._delete(node)

    def traverse(self, order):
        pass

    def _delete(self,node):  # helper fuction to delete() function
        # Node is leaf node 

        if node.left is None and node.right is None: # Node has no child node
            if node.parent is None:
                self.node = None
            else:
                if node.parent.right is None:
                    node.parent.left = None
                else:
                    node.parent.right = None 
                node.parent = None
        elif node.left is None or node.right is None : # Node has only one child node
         
            child_node = node.left if node.left is not None else node.right
            if node.parent.right == node:
                node.parent.right = child_node
            else:
                node.parent.left = child_node
            child_node.parent = node.parent
            
            node.parent = node.left = node.right = None
        else:     # Node has two child nodes
            pass

 
                    
    
    def _successor(self,node): 
        """
        the smallest node key among the larger node key.

        """
        pass
    
    def _predecessor(self,node):
        pass

    def _in_order_traversal(self):
        pass
 
    def _pre_order_traversal(self):
        pass
    
    def _post_order_traversal(self):
        pass 