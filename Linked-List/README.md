
## Linked List


* Definition: A collection of nodes where each node contains:
- Data (the value).
- A pointer/reference to the next node (in singly linked lists).

* Dynamic Size: The size of a linked list can grow or shrink dynamically by adding or removing nodes.

* Sequential Access: You traverse the list node by node to access elements (e.g., starting from the head and following pointers).

### Memory Allocation

- Non-Contiguous Allocation: Each node is allocated separately, and the nodes can be scattered in memory.
- Dynamic Memory Allocation: New nodes are created dynamically during runtime, allowing for flexible growth.



#### Advantages:
- Dynamic Size: Can grow or shrink dynamically without predefining the size.
- Efficient Insertions/Deletions: Adding or removing nodes doesn't require shifting elements if you have a pointer to the node (O(1) complexity).
- Memory Utilization: No wasted memory due to over-allocation (each node is allocated as needed).

#### Disadvantages:
- Slow Access: Sequential access makes indexing slow (O(n) complexity).
- Memory Overhead: Each node requires extra memory for the pointer/reference.
- Cache Unfriendliness: Non-contiguous memory makes linked lists less efficient for CPU caching compared to arrays.


### Linked List Use Cases.

- When you need dynamic resizing (e.g., a playlist where songs are added/removed frequently).
- Frequent insertions or deletions (e.g., implementing queues, stacks).
- When memory fragmentation is a concern (e.g., systems where memory blocks are allocated dynamically).


## Difference Between Array and LinkedList 

| Feature | Array | Linked List |
| :---------|:-------| :------------- |
| Memory  | Contiguous | Non-contiguous |
| Access Time | O(1) (Direct Access) | O(n) (Sequential Access) |
| Insertion/Deletion	| Costly (due to shifting)	| Efficient if node reference known |
| Resizing | Fixed size or costly to resize |	Dynamic resizing |
| Extra Memory Overhead |	No |	Yes (pointers/references) |
| Cache Efficiency |	High	| Low |
| use | When you need fast random access (e.g., accessing elements by index). Fixed or  predictable size datasets (e.g., storing a list of temperatures for each hour of a day).| When you need dynamic resizing (e.g., a playlist where songs are added/removed frequently).Frequent insertions or deletions (e.g., implementing queues, stacks) |
