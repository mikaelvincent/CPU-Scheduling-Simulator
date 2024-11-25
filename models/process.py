class Process:
    """
    Represents a process with its scheduling attributes.

    Attributes:
        arrival_time (int): The arrival time of the process.
        burst_time (int): The execution time required by the process.
        priority (int): The priority level of the process.
        start_time (int): The time at which the process starts execution.
        completion_time (int): The time at which the process completes execution.
        turnaround_time (int): Total time taken from arrival to completion.
        waiting_time (int): Total time the process has been in the ready queue.
    """

    def __init__(self, arrival_time: int, burst_time: int, priority: int):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
