"""Maximum Profit in Job Scheduling.

We have n jobs, where every job is scheduled to be done from start_time[i] to
end_time[i], obtaining a profit of profit[i].

You're given the start_time, end_time and profit arrays, return the maximum profit
you can take such that there are no two jobs in the subset with overlapping time
range.

If you choose a job that ends at time X you will be able to start another job
that starts at time X.
"""


def job_scheduling(
    start_time: list[int], end_time: list[int], profit: list[int]
) -> int:
    # Combine times into a list.
    jobs = []
    for i in range(len(start_time)):
        jobs.append([start_time[i], end_time[i], profit[i]])

    # Sort by the end time.
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
        if right != -1:
            current_profit += max_profits[right]

        # Larger profit is stored in DP array: current or other larger profit
        # for job.
        max_profits[i] = max(max_profits[i - 1], current_profit)

    return max_profits[-1]