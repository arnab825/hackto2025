# Breadth First Search (BFS) implementation using Linked List (Queue)

# Node class to represent each vertex in the graph
class Node:
    def __init__(self, data):
        self.data = data  # Store node data
        self.next = None  # Pointer to next node in linked list

# Queue implementation using linked list for BFS traversal
class Queue:
    def __init__(self):
        self.front = None  # Points to the first node in queue
        self.rear = None   # Points to the last node in queue

    # Add element to queue (enqueue)
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            # If queue is empty, both front and rear point to new node
            self.front = self.rear = new_node
            return
        # Link the new node at the end and update rear
        self.rear.next = new_node
        self.rear = new_node

    # Remove element from queue (dequeue)
    def dequeue(self):
        if self.front is None:
            # If queue is empty, return None
            return None
        temp = self.front
        # Move front pointer to the next node
        self.front = temp.next
        # If queue becomes empty, set rear to None
        if self.front is None:
            self.rear = None
        return temp.data

    # Check if queue is empty
    def is_empty(self):
        return self.front is None

# BFS function to traverse graph
def bfs(graph, start):
    visited = set()        # Keep track of visited nodes
    queue = Queue()        # Create queue for BFS
    queue.enqueue(start)   # Enqueue starting node
    visited.add(start)     # Mark start node as visited

    print("BFS Traversal: ", end="")
    while not queue.is_empty():
        vertex = queue.dequeue()  # Dequeue a vertex from queue
        print(vertex, end=" ")    # Print current node

        # Visit all adjacent vertices
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.enqueue(neighbour)  # Enqueue unvisited neighbour
                visited.add(neighbour)    # Mark neighbour as visited

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call BFS starting from vertex 'A'
bfs(graph, 'A')
