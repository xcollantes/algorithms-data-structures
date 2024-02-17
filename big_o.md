# Big O

Big O notation is used as a metric to express efficiency for an algorithm.

[![Big
graph](https://miro.medium.com/max/700/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)](https://www.bigocheatsheet.com/)

<https://www.bigocheatsheet.com>

**NOTE:** This is an extremely important topic in interviews. You must
understand this concept.

> Imagine the following scenario: You've got a file on a hard drive and you need
> to send it to your friend who lives across the country. You need to get the
> file to your friend as fast as possible. How should you send it? Most people's
> first thought would be email, FTP, or some other means of electronic transfer.
> That thought is reasonable, but only half correct. If it's a small file,
> you're certainly right. It would take 5 - 10 hours to get to an airport, hop
> on a flight, and then deliver it to your friend. But what if the file were
> really, really large? Is it possible that it's faster to physically deliver it
> via plane? Yes, actually it is. A one-terabyte (1 TB) file could take more
> than a day to transfer electronically. It would be much faster to just fly it
> across the country. If your file is that urgent (and cost isn't an issue), you
> might just want to do that. What if there were no flights, and instead you had
> to drive across the country? Even then, for a really huge file, it would be
> faster to drive.

Excerpt from _Cracking The Coding Interview 6th Edition by Laakmann_.

Big O is useful since comparing an algorithm on a 2022 MacBook Pro will run
differently on a Commodore 64 from 1982. Further, depending on what other
programs are running on your computer, the algorithm may perform differently
depending on the day and time you run it. To eliminate as many variables when
measuring algorithms, Big O can be used since it measures an algorithm on Time
or Space Complexity, independent of uncontrolled variables.

## Time complexity

[Asymptotic relationship](https://en.wikipedia.org/wiki/Asymptotic_analysis)
between inputs and growth outputs.

## Space complexity

Recursive function add to Space complexity since each recursive call adds to the
call stack. If a binary tree is traversed, then complexity would be as large as
the height of the tree since returning from a level would remove the occupying
space.

## Dropping constants

A common mistake when calculating Big O is keeping constants as part of the
calculation. Consider the two examples:

**Example 1**

```python
for x in range(len(some_array)):
    if x < 10:
        print("some output")
    if x > 10:
        print("some output")
```

**Example 2**

```python
for x in range(len(some_array)):
    if x < 10:
        print("some output")

for x in range(len(some_array)):
    if x > 10:
        print("some output")
```

Example 1 has one loop of some array which performs two comparison operations
where Example 2 has two loops of the same array and each loop performs a single
comparison operation.

At first you might say Time Complexity of Example 1 is O(n) and Example 2 is
O(2n). But Big O doesn't consider the constants and the 2 is dropped.

Constants are dropped because the Big O measures the growth of results. Once the
inputs grow to huge values, then the constants are insignificant. That's how Big
O works.

That's not to say Example 1 is more efficient, Example 1 is more efficient. Big
O is concerned with the growth of inputs as opposed to overall efficiency.
