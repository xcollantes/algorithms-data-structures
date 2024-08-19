"""Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Then return the
number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get
accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the
elements which are not equal to val. The remaining elements of nums are not
important as well as the size of nums.

Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
"""


def remove_element(nums: list[int], val: int) -> int:
    current = 0
    for i in range(len(nums)):
        if nums[i] != val:
            # Just replace current with non-val value.
            nums[current] = nums[i]
            current += 1

    return current


print(remove_element(nums=[3, 2, 2, 3], val=3))
print(remove_element(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
