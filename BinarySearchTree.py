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
        yield from self._in_order_traversal(self.root)

    def __repr__(self):
        return str(list(self._in_order_traversal(self.root)))

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
        if order == 'inorder':
            yield from self._in_order_traversal(self.root)
        elif order == 'preorder':
            yield from self._pre_order_traversal(self.root)
        elif order == 'postorder':
            yield from self._post_order_traversal(self.root)
        else:
            print("Unknown Order")


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
            successor = self._successor(node)

            node.key = successor.key
            node.value = successor.value

            self._delete(successor)

 
                    
    
    def _successor(self,node): 
        """
        the smallest node key among the larger node key.
        first go right ,then keep going left until None
        """
        if node is None:
            print ('cannot find successor of None')
        else:
            if node.right is None:
                return None
            else:
                current_node = node.right
                while current_node.left is not None:
                    current_node = current_node.left
                return current_node
            
                   
    
    def _predecessor(self,node):
        
        if node is None:
            print ('cannot find predecessor of None')
        else:
            if node.left is None:
                return None
            else:
                current_node = node.left
                while current_node.right is not None:
                    current_node = current_node.right 
                return current_node



    def _in_order_traversal(self,node):
        """
        left -> root -> right
        from the smallest to the largest
        ascending order
        """
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key,node.value)
            yield from self._in_order_traversal(node.right)
            
 
    def _pre_order_traversal(self,node):
        """
        root -> left -> right
        """
        if node is not None:
            yield (node.key,node.value)
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)


    def _post_order_traversal(self,node):
            
       if node is not None:
            yield from self._post_order_traversal(node.left)
            yield from self._post_order_traversal(node.right)
            yield (node.key,node.value)

if __name__ == "__main__":
     bst = BinarySearchTree()
     bst.insert(10,"Felix")
     bst.insert(5,"Jia")
     bst.insert(22,"Liya")
     bst.insert(2,"Lena")
     bst.insert(9,"Mia")
     bst.insert(12,"Stacy")
     bst.insert(30,"Andrew")
     bst.insert(11,"Alberto")
     bst.insert(15,"Autumn")
     bst.insert(23,"Ellie")
     bst.insert(35,"Gabbie")
     bst.insert(11,"Leah")
     bst.insert(17,"Hallo")
     bst.insert(29,"Sonya")
     bst.delete(17)
    
     for i in bst.traverse('inorder'):
         print(i)

     print(bst)
     


