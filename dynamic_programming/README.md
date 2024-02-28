# Dynamic programming

Dynamic programming (DP) is a problem-solving technique. Usually, problems where
you use DP can only be solved with DP (in a reasonable time complexity). For
many people, DP is the most feared topic. To be honest, there is a large stigma
around DP. This is likely a combination of:

1. If you don't know DP, then it is almost impossible to solve a DP problem,
   even if it's an easy one
1. DP isn't as common in interviews - some companies even ban it, which means
   people have less of an incentive to learn it.

## What is DP

In short, dynamic programming is just optimized recursion. Let's say you had
some recursive function that returned the answer to the original problem
treating whatever you call the function with as the input. We saw this idea
extensively in the tree section. For example, we would frequently define a
function dfs that took a node and returned the answer to the original problem as
if the input was the subtree rooted at node.

The idea behind dynamic programming is the exact same. We define some recursive
function, usually called dp, that returns the answer to the original problem as
if the arguments you passed to it were the input.

The arguments that a recursive function takes represents a state. When we looked
at tree problems, we never visited a node more than once in our DFS, which means
that a state was never repeated. The difference with DP is that states can be
repeated, usually an exponential number of times. To avoid repeating
computation, we use something called memoization. When we find the answer (the
return value) for a given state, we cache that value (usually in a hash map).
Then in the future, if we ever see the same state again, we can just refer to
the cached value without needing to re-calculate it.
