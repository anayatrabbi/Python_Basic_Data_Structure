from collections import deque

# here passong a list in deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# fifo
queue.popleft()

if not queue:
    print("empty queue")
