class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        def traverse(node):
            if value < node.value:
                if node.left:
                    traverse(node.left)
                else:
                    node.left = BinarySearchTree(value)
            else:
                if node.right:
                    traverse(node.right)
                else:
                    node.right = BinarySearchTree(value)


        traverse(self)
    
    def contains(self, target):
        def find(node):
            if node is None:
                return False
            elif target == node.value:
                return True
            elif target < node.value:
                return find(node.left)
            else:
                return find(node.right)

        return find(self)