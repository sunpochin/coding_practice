Solution
Approach #1 Using Recursion [Accepted]
We can traverse both the given trees in a preorder fashion. At every step, we check if the current node exists(isn't null) for both the trees. If so, we add the values in the current nodes of both the trees and update the value in the current node of the first tree to reflect this sum obtained. At every step, we also call the original function mergeTrees() with the left children and then with the right children of the current nodes of the two trees. If at any step, one of these children happens to be null, we return the child of the other tree(representing the corresponding child subtree) to be added as a child subtree to the calling parent node in the first tree. At the end, the first tree will represent the required resultant merged binary tree.

The following animation illustrates the process.

Current
1 / 15

Complexity Analysis

Time complexity : O(m)O(m). A total of mm nodes need to be traversed. Here, mm represents the minimum number of nodes from the two given trees.

Space complexity : O(m)O(m). The depth of the recursion tree can go upto mm in the case of a skewed tree. In average case, depth will be O(logm)O(logm).

Approach #2 Iterative Method [Accepted]
Algorithm

In the current approach, we again traverse the two trees, but this time we make use of a stackstack to do so instead of making use of recursion. Each entry in the stackstack strores data in the form [node_{tree1}, node_{tree2}][node 
tree1
​	
 ,node 
tree2
​	
 ]. Here, node_{tree1}node 
tree1
​	
  and node_{tree2}node 
tree2
​	
  are the nodes of the first tree and the second tree respectively.

We start off by pushing the root nodes of both the trees onto the stackstack. Then, at every step, we remove a node pair from the top of the stack. For every node pair removed, we add the values corresponding to the two nodes and update the value of the corresponding node in the first tree. Then, if the left child of the first tree exists, we push the left child(pair) of both the trees onto the stack. If the left child of the first tree doesn't exist, we append the left child(subtree) of the second tree to the current node of the first tree. We do the same for the right child pair as well.

If, at any step, both the current nodes are null, we continue with popping the next nodes from the stackstack.

The following animation depicts the process.

Current
1 / 15

Complexity Analysis

Time complexity : O(n)O(n). We traverse over a total of nn nodes. Here, nn refers to the smaller of the number of nodes in the two trees.

Space complexity : O(n)O(n). The depth of stack can grow upto nn in case of a skewed tree.

Analysis written by: @vinod23