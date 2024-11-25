from typing import List
from models.process import Process

def fcfs_scheduling(processes: List[Process]) -> List[Process]:
    """
    Performs First Come First Serve scheduling on the given list of processes.

    Args:
        processes (List[Process]): The list of processes to schedule.

    Returns:
        List[Process]: The list of processes with updated scheduling attributes.
    """
    # Sort processes based on arrival time
    sorted_processes = sorted(processes, key=lambda p: p.arrival_time)
    current_time = 0
    for process in sorted_processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        # Record start time
        process.start_time = current_time
        # Update current time based on burst time
        current_time += process.burst_time
        # Record completion time
        process.completion_time = current_time
        # Calculate turnaround time
        process.turnaround_time = process.completion_time - process.arrival_time
        # Calculate waiting time
        process.waiting_time = process.start_time - process.arrival_time
    return sorted_processes
