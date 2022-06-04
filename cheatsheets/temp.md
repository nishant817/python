=== PYTHON ====
x = divmod(5, 2) # Display the quotient and the remainder
X: (2,1)

Maxval = float('inf')
low=-math.inf, high=math.inf

String split
txt = "apple#banana#cherry#orange"
txt.split(“#”)  → ['apple', 'banana', 'cherry', 'orange']
txt(split(“#”, 1)    → ['apple', 'banana#cherry#orange'] 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



=== SYSTEM DESIGN ===

Features of distributed system
  Scalability
  Reliability
  Availability
  Efficiency: Measured by
    Latency (response time)
    Throughput (bandwidth) - number of items delivered per unit time
  Maintainability or serviceability


Scale Horizontally: Cassandra, MongoDB
Scale Vertically: MyAQL

System Design Steps
  Design Consideration
    Read Heavy or write heavy?
    Read/Write ratio
    Min, Max, Avg size of API call
    Number of new posts per unit time
  Capacity estimation
    Database size
    Network bandwidth / traffic estimate 

