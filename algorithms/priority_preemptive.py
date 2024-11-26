from typing import List, Dict, Tuple
from models.process import Process

def priority_preemptive_scheduling(processes: List[Process]) -> Tuple[List[Process], List[Dict]]:
    """
    Performs Priority-Based Preemptive scheduling on the given list of processes.

    Args:
        processes (List[Process]): The list of processes to schedule.

    Returns:
        Tuple[List[Process], List[Dict]]: The list of processes with updated scheduling attributes and the execution timeline.
    """
    if not processes:
        return [], []

    current_time = 0
    completed_processes = 0
    n = len(processes)
    ready_queue = []
    gantt_chart = []

    # Initialize remaining burst times
    for process in processes:
        process.remaining_burst_time = process.burst_time

    while completed_processes < n:
        # Add all processes that have arrived by current_time to the ready queue
        for process in processes:
            if (process.arrival_time <= current_time and
                process.remaining_burst_time > 0 and
                process not in ready_queue):
                ready_queue.append(process)

        if ready_queue:
            # Select the process with the highest priority (lowest number)
            ready_queue.sort(key=lambda p: p.priority)
            current_process = ready_queue[0]

            # Record start_time if the process is executing for the first time
            if current_process.start_time is None:
                current_process.start_time = current_time

            # Record execution event for Gantt chart
            gantt_chart.append({
                'process_id': current_process.id,
                'start_time': current_time,
                'duration': 1
            })

            # Execute the process for one time unit
            current_process.remaining_burst_time -= 1
            current_time += 1

            # Remove the process from the queue if it is completed
            if current_process.remaining_burst_time == 0:
                current_process.completion_time = current_time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes += 1
                ready_queue.remove(current_process)
        else:
            # Advance time if no process is ready to execute
            current_time += 1

    return processes, gantt_chart
