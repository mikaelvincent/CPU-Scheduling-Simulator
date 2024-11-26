from typing import List, Dict, Tuple
from models.process import Process
from collections import deque

def round_robin_scheduling(processes: List[Process], time_quantum: int) -> Tuple[List[Process], List[Dict]]:
    """
    Performs Round Robin scheduling on the given list of processes.

    Args:
        processes (List[Process]): The list of processes to schedule.
        time_quantum (int): The time quantum for Round Robin scheduling.

    Returns:
        Tuple[List[Process], List[Dict]]: The list of processes with updated scheduling attributes and the execution timeline.
    """
    if not processes:
        return [], []

    # Initialize remaining burst times and set start_time to None
    for process in processes:
        process.remaining_burst_time = process.burst_time
        process.start_time = None

    time = 0
    ready_queue = deque()
    processes_left = processes.copy()
    completed_processes = 0
    n = len(processes)
    gantt_chart = []

    while completed_processes < n:
        # Enqueue processes that have arrived by the current time
        for process in processes_left:
            if process.arrival_time <= time and process not in ready_queue:
                ready_queue.append(process)
        processes_left = [p for p in processes_left if p not in ready_queue]

        if ready_queue:
            current_process = ready_queue.popleft()
            # Record start_time at first CPU allocation
            if current_process.start_time is None:
                current_process.start_time = time
            # Execute the process for a time quantum or until completion
            exec_time = min(time_quantum, current_process.remaining_burst_time)

            # Record execution event for Gantt chart
            gantt_chart.append({
                'process_id': current_process.id,
                'start_time': time,
                'duration': exec_time
            })

            time += exec_time
            current_process.remaining_burst_time -= exec_time

            # Enqueue any newly arrived processes during execution
            for process in processes_left:
                if process.arrival_time <= time and process not in ready_queue:
                    ready_queue.append(process)
            processes_left = [p for p in processes_left if p not in ready_queue]

            if current_process.remaining_burst_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes += 1
            else:
                # Re-enqueue the current process
                ready_queue.append(current_process)
        else:
            # Advance time to the next process arrival
            if processes_left:
                next_arrival = min(p.arrival_time for p in processes_left)
                time = next_arrival

    return processes, gantt_chart
