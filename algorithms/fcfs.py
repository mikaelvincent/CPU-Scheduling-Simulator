from typing import List, Dict, Tuple
from models.process import Process

def fcfs_scheduling(processes: List[Process]) -> Tuple[List[Process], List[Dict]]:
    """
    Performs First Come First Serve scheduling on the given list of processes.

    Args:
        processes (List[Process]): The list of processes to schedule.

    Returns:
        Tuple[List[Process], List[Dict]]: The list of processes with updated scheduling attributes and the execution timeline.
    """
    if not processes:
        return [], []

    # Sort processes based on arrival time
    sorted_processes = sorted(processes, key=lambda p: p.arrival_time)
    current_time = 0
    gantt_chart = []
    completed_processes = []

    for process in sorted_processes:
        if current_time < process.arrival_time:
            # Record idle time in Gantt chart
            gantt_chart.append({
                'process_id': 'Idle',
                'start_time': current_time,
                'duration': process.arrival_time - current_time
            })
            current_time = process.arrival_time

        # Record execution event for Gantt chart
        gantt_chart.append({
            'process_id': process.id,
            'start_time': current_time,
            'duration': process.burst_time
        })

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

        completed_processes.append(process)

    return completed_processes, gantt_chart
