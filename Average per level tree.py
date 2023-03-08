class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(3)
nine = Node(9)
twen = Node(20)
fifteen = Node(15)
seven = Node(7)

root.left = nine
root.right = twen
twen.left = fifteen
twen.right = seven

queue = [root]
means_per_level = []

while len(queue) > 0:
    length = len(queue)
    sum = 0
    for _ in range(len(queue)):
        node = queue.pop(0)
        sum+= node.value
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    means_per_level.append(sum/length)

print(means_per_level)
