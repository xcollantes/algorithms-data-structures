"""1235. Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done from start_time[i] to
end_time[i], obtaining a profit of profit[i].

You're given the start_time, end_time and profit arrays, return the maximum profit
you can take such that there are no two jobs in the subset with overlapping time
range.

If you choose a job that ends at time X you will be able to start another job
that starts at time X.

https://leetcode.com/problems/maximum-profit-in-job-scheduling/description
"""


def job_scheduling(
    start_time: list[int], end_time: list[int], profit: list[int]
) -> int:
    # Combine times into a list.
    jobs = []
    for i in range(len(start_time)):
        jobs.append([start_time[i], end_time[i], profit[i]])

    # Sort by the end time.
    # We want to sort by end time since we can find where jobs start and end.
    jobs.sort(key=lambda x: x[1])
    print(f"Sorted: {jobs}")

    # DP array.
    max_profits: list[int] = [0] * len(start_time)
    max_profits[0] = jobs[0][2]  # Initialize with end time.

    for i in range(1, len(start_time)):
        current_profit = jobs[i][2]  # Profit element.
        print(f"current_profit: {current_profit}; max_profits: {max_profits}")

        # Find latest job that doesn't conflict with current job.
        left = 0
        # This is closing in on the jobs before the current job to find the max
        # profitable job that is lined up before the current job.
        #
        #       job2_start.....end          job4_start.....end
        # job1_start.......end    job3_start.....end
        # ------------------------------------------------------
        # L                      R i
        #
        # If job3 was i, then L is earliest job and R is the job before i.
        right = i - 1
        # Where the right job starts less than or exactly when previous job
        # ends.
        while left <= right:
            mid = (left + right) // 2  # Binary search: find mid to split jobs by.

            # If end time is less than current job start time.
            if jobs[mid][1] <= jobs[i][0]:
                left = mid + 1
            else:
                right = mid - 1

        # Add valid job's profit.
        #
        # If right == -1, it means no previous job ends before the current job
        # starts. In this case, there is no profit from a previous job that can
        # be added to the current job's profit.
        #
        # If right != -1, it means we
        # found a valid job that does not overlap with the current job. Thus, we
        # can safely add the profit of this job (max_profits[right]) to the
        # current job's profit.
        #
        # The right index is the job that we have found.
        if right != -1:
            current_profit += max_profits[right]

        # Larger profit is stored in DP array: current or other larger profit
        # for job.
        max_profits[i] = max(max_profits[i - 1], current_profit)

    return max_profits[-1]


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.DYNAMIC_PROGRAMMING, Tags.ARRAY, Tags.SORTING, Tags.BINARY_SEARCH],
    difficulty=Difficulty.HARD,
)
