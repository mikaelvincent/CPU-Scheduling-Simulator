from typing import List, Dict

def generate_gantt_chart(gantt_chart: List[Dict]):
    """
    Generates and displays the Gantt chart based on the execution timeline.

    Args:
        gantt_chart (List[Dict]): The execution timeline as a list of dictionaries.
    """
    if not gantt_chart:
        print("No Gantt chart to display.")
        return
    print("\nGantt Chart:")
    chart = ""
    time_line = ""
    current_time = 0
    for event in gantt_chart:
        start_time = event['start_time']
        process_id = event['process_id']
        duration = event['duration']

        # Add idle time if there's a gap
        if start_time > current_time:
            idle_duration = start_time - current_time
            chart += " " * (5 * idle_duration)
            time_line += f"{current_time:<5}"
            current_time = start_time

        chart += f"|P{process_id}" + "—" * (5 * duration - 5)
        time_line += f"{current_time:<5}"
        current_time += duration

    chart += "|"
    time_line += f"{current_time:<5}"
    print(chart)
    print(time_line)
