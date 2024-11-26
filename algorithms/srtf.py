from typing import List, Dict, Tuple
from models.process import Process

def srtf_scheduling(processes: List[Process]) -> Tuple[List[Process], List[Dict]]:
    """
    Performs Shortest Remaining Time First scheduling on the given list of processes.

    Args:
        processes (List[Process]): The list of processes to schedule.

    Returns:
        Tuple[List[Process], List[Dict]]: The list of processes with updated scheduling attributes and the execution timeline.
    """
    n = len(processes)
    completed = 0
    current_time = 0
    ready_queue = []
    processes_left = processes.copy()
    gantt_chart = []

    # Initialize remaining burst times
    for process in processes:
        process.remaining_burst_time = process.burst_time

    while completed < n:
        # Add processes that have arrived to the ready queue
        for process in processes_left:
            if process.arrival_time <= current_time and process not in ready_queue:
                ready_queue.append(process)
        # Remove added processes from the list
        processes_left = [p for p in processes_left if p not in ready_queue]

        if ready_queue:
            # Select the process with the shortest remaining burst time
            ready_queue.sort(key=lambda p: p.remaining_burst_time)
            current_process = ready_queue[0]

            # Set start_time if the process is starting for the first time
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

            # If the process is completed
            if current_process.remaining_burst_time == 0:
                current_process.completion_time = current_time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                ready_queue.remove(current_process)
                completed += 1
        else:
            # Advance time if no processes are ready to execute
            current_time += 1

    return processes, gantt_chart
