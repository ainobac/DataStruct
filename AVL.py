class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.balance = 0

class AVL:
    def __init__(self) -> None:
        self.root = None
        self.is_balanced = True

    def insert(self, key):
        self.root = self.insert_help(self.root, key)

    def insert_help(self, root, key):
        if not root:
            root = AVLNode(key)
            self.is_balanced = False
        elif key < root.key:
            root.left = self.insert_help(root.left, key)
            if not self.is_balanced:
                if root.balance >= 0:
                    self.is_balanced = root.balance == 1
                    root.balance -= 1
                else:
                    if root.left.balance == -1:
                        root = self.right_rotation(root)
                    else:
                        root = self.left_right_rotation(root)
                    self.is_balanced = True
        elif key > root.key:
            root.right = self.insert_help(root.right, key)
            if not self.is_balanced:
                if root.balance <= 0:
                    self.is_balanced = root.balance == -1
                    root.balance += 1
                else:
                    if root.right.balance == 1:
                        root = self.left_rotation(root)
                    else:
                        root = self.right_left_rotation(root)
                    self.is_balanced = True
        return root
    
    def right_rotation(self, root):
        child = root.left
        root.left = child.right
        child.right = root
        child.balance = root.balance = 0
        return child
    
    def left_rotation(self, root):
        child = root.right
        root.right = child.left
        child.left = root
        child.balance = root.balance = 0
        return child

    def left_right_rotation(self, root):
        child = root.left
        if not child:
            return root
        grandchild = child.right
        if not grandchild:
            return root
        root.left = grandchild.right
        grandchild.right = root
        child.right = grandchild.left
        grandchild.left = child
        if grandchild.balance == -1:
            root.balance = 1
            child.balance = 0
        elif grandchild.balance == 1:
            root.balance = 0
            child.balance = -1
        else:
            root.balance = child.balance = 0
        grandchild.balance = 0
        return grandchild
    
    def right_left_rotation(self, root):
        child = root.right
        if not child:
            return root
        grandchild = child.left
        if not grandchild:
            return root
        root.right = grandchild.left
        grandchild.left = root
        child.left = grandchild.right
        grandchild.right = child
        if grandchild.balance == -1:
            root.balance = 0
            child.balance = 1
        elif grandchild.balance == 1:
            root.balance = -1
            child.balance = 0
        else:
            root.balance = child.balance = 0
        grandchild.balance = 0
        return grandchild
    
    def preorder(self):
        if self.root is not None:
            stack = [self.root]
            while stack:
                current =  stack.pop()
                print(f"{current.key};{current.balance}", end=" ")
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
            print()

