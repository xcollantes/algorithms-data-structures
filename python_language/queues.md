# Queues

## deque

Used for Stack data structure.

```python
from collections import deque

def reverse_words_deque(sentence: str) -> list[str]:
    """Use deque library."""
    stack: deque = deque(sentence.split(" "))

    result: list[str] = []
    while len(stack) > 0:
        result.append(stack.pop())

    print(result)
    return result
```

## Queue

Practically the same as deque except used for managing Threads.

Threads run within a Process.

```python
import queue
import threading
import time

q = queue.Queue()

def my_thread():
    while True:
        item = q.get()
        print(f"start: {item}")
        time.sleep(2)
        print(f"end: {item}")
        q.task_done()

t = threading.Thread(target=my_thread, daemon=True)
t.start()

for item in ["hello", 10, 99, 200]:
    q.put(item)

# Threads wait until all are done
q.join()
print("ALL DONE")
```
