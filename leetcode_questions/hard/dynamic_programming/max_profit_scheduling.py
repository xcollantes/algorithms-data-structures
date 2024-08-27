"""Maximum Profit in Job Scheduling.

We have n jobs, where every job is scheduled to be done from startTime[i] to
endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit
you can take such that there are no two jobs in the subset with overlapping time
range.

If you choose a job that ends at time X you will be able to start another job
that starts at time X.
"""


from bisect import bisect_left


def job_scheduling(
    start_time: list[int], end_time: list[int], profit: list[int]
) -> int:
    jobs = []
    for i in range(len(start_time)):
        jobs.append([start_time[i], end_time[i], profit[i]])

    max_profits: list[int] = [-1] * len(start_time)

    jobs.sort(key=lambda x: x[0])
    start_time.sort()

    return find(0, jobs, start_time, len(start_time), max_profits)


def find(job_idx, jobs, start_time, n, max_profits):
    print(f"job_idx: {job_idx}; n: {n}, max_profits: {max_profits}")
    if job_idx >= n:
        return 0

    if max_profits[job_idx] != -1:
        return max_profits[job_idx]

    index = bisect_left(start_time, jobs[job_idx][1])

    pick = jobs[job_idx][2] + find(index, jobs, start_time, n, max_profits)
    dont_pick = find(index + 1, jobs, start_time, n, max_profits)

    print(f"pick: {pick}; not pick: {dont_pick}")

    max_profits[index] = max(pick, dont_pick)

    return max_profits[index]
