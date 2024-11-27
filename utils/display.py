from models.process import Process
from tabulate import tabulate
from typing import List

def display_process_info(processes: List[Process]):
    """
    Displays the scheduling information for each process.

    Args:
        processes (List[Process]): The list of processes with scheduling info.
    """
    if not processes:
        print("No processes to display.")
        return

    headers = ["Process", "Arrival", "Burst", "Priority", "Start", "Completion", "Waiting", "Turnaround"]
    table = []
    for process in processes:
        table.append([
            f"P{process.id}",
            process.arrival_time,
            process.burst_time,
            process.priority,
            process.start_time,
            process.completion_time,
            process.waiting_time,
            process.turnaround_time
        ])

    print(tabulate(table, headers=headers, tablefmt="grid"))

    total_waiting_time = sum(p.waiting_time for p in processes)
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    n = len(processes)
    if n > 0:
        print(f"\nAverage Waiting Time: {total_waiting_time / n:.2f}")
        print(f"Average Turnaround Time: {total_turnaround_time / n:.2f}")
    else:
        print("\nNo processes to calculate average times.")
