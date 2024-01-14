class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while current:
            if key == current.key:
                break
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    
    def search(self, key):
        current = self.root
        while current:
            if key == current.key:
                return True
            elif key>current.key:
                current = current.right
            else:
                current = current.left
        return False
    
    def preorder(self):
        if self.root is not None:
            stack = [self.root]
            while stack:
                current =  stack.pop()
                print(current.key, end=" ")
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
            print()

    def remove(self, key):
        self.root = self._remove(self.root,key)

    def _remove(self, root, key):
        if root is None:
            return root
        
        elif key > root.key:
            root.right = self._remove(root.right, key)
        elif key < root.key:
            root.left = self._remove(root.left, key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                root.key = self._findmax(root.left)
                root.left = self._removemax(root.left)
        return root
    
    def _findmax(self, node):
        if node.right is None:
            return node.key
        else:
            return self._findmax(node.right)
    
    def _removemax(self, node):
        if node.right is None:
            return node.left
        node.right =self._removemax(node.right)
        return node
    
    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key, end=" ")

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.key, end=" ")
            self._inorder(node.right)

    def breadthfirst(self):
        if self.root is None:
            return
    
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.key, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    




