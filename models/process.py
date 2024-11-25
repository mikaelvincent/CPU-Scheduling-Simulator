class Process:
    """
    Represents a process with its scheduling attributes.

    Attributes:
        arrival_time (int): The arrival time of the process.
        burst_time (int): The execution time required by the process.
        priority (int): The priority level of the process.
    """

    def __init__(self, arrival_time: int, burst_time: int, priority: int):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
