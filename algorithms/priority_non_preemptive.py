from typing import List
from models.process import Process

def priority_non_preemptive_scheduling(processes: List[Process]) -> List[Process]:
    """
    Performs Priority Non-Preemptive scheduling on the given list of processes.

    Args:
        processes (List[Process]): The list of processes to schedule.

    Returns:
        List[Process]: The list of processes with updated scheduling attributes.
    """
    completed_processes = []
    current_time = 0
    ready_queue = []
    processes_left = processes.copy()

    while processes_left or ready_queue:
        # Add all processes that have arrived by current_time to the ready queue
        arrived_processes = [p for p in processes_left if p.arrival_time <= current_time]
        for process in arrived_processes:
            ready_queue.append(process)
            processes_left.remove(process)

        if ready_queue:
            # Select the process with the highest priority (lower number indicates higher priority)
            ready_queue.sort(key=lambda p: p.priority)
            current_process = ready_queue.pop(0)

            # Record start time and calculate completion time
            if current_time < current_process.arrival_time:
                current_time = current_process.arrival_time
            current_process.start_time = current_time
            current_time += current_process.burst_time
            current_process.completion_time = current_time

            # Calculate turnaround time and waiting time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.start_time - current_process.arrival_time

            completed_processes.append(current_process)
        else:
            # Advance time to the next process arrival if ready queue is empty
            next_arrival = min(p.arrival_time for p in processes_left)
            current_time = next_arrival

    return completed_processes
