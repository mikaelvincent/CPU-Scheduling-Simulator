from typing import List, Dict
import shutil


def generate_gantt_chart(gantt_chart: List[Dict]):
    """
    Generates and displays the Gantt chart based on the execution timeline.

    Args:
        gantt_chart (List[Dict]): The execution timeline as a list of dictionaries.
    """
    if not gantt_chart:
        print("No Gantt chart to display.")
        return

    # Merge consecutive events with the same process_id
    merged_events = []
    for event in gantt_chart:
        if not merged_events:
            merged_events.append(event.copy())
        else:
            last_event = merged_events[-1]
            if (
                event['process_id'] == last_event['process_id']
                and event['start_time'] == last_event['start_time'] + last_event['duration']
            ):
                merged_events[-1]['duration'] += event['duration']
            else:
                merged_events.append(event.copy())

    # Determine the length of the longest time value
    time_values = [event['start_time'] for event in merged_events]
    time_values.append(merged_events[-1]['start_time'] + merged_events[-1]['duration'])
    max_time_length = max(len(str(time)) for time in time_values)

    # Get terminal width and adjust for time labels
    columns, _ = shutil.get_terminal_size(fallback=(80, 24))
    max_width = columns - (max_time_length + 1)

    # Determine the length of the longest process name
    process_names = [f"P{event['process_id']}" for event in merged_events if event['process_id'] != 'Idle']
    longest_process_name = max((len(name) for name in process_names), default=2)
    unit_width = 4 + longest_process_name  # 4 additional spaces for padding

    # Calculate maximum units per line
    max_units_per_line = max(1, (max_width) // (unit_width + 1))  # +1 for '+'

    chart_lines = []
    index = 0
    current_time = merged_events[0]['start_time']

    while index < len(merged_events):
        line_top = "+"
        line_middle = "|"
        line_bottom = "+"
        time_positions = []
        units_in_line = 0

        while units_in_line < max_units_per_line and index < len(merged_events):
            event = merged_events[index]
            duration = event['duration']

            # Calculate units to draw in the current line
            remaining_units = max_units_per_line - units_in_line
            units_to_draw = min(duration, remaining_units)
            cell_width = units_to_draw * unit_width

            # Build top and bottom lines without labels
            line_top += "-" * cell_width + "+"
            line_bottom += "-" * cell_width + "+"

            # Prepare the label centered in the cell
            process_id = event['process_id']
            if process_id == 'Idle':
                label = "Idle"
            else:
                label = f"P{process_id}"
            label = label.center(cell_width)

            # Add the label to the middle line
            line_middle += label + "|"

            # Record the position of the '+' sign for time labels
            position = len(line_top) - cell_width - 1
            time_positions.append((position, current_time))

            # Update counters and event details
            current_time += units_to_draw
            units_in_line += units_to_draw

            if units_to_draw < duration:
                # Update event for remaining duration
                merged_events[index]['duration'] -= units_to_draw
            else:
                index += 1  # Move to the next event

        # Append the final '+' position and time with an extra space
        time_positions.append((len(line_top) - 1, current_time))

        # Build the time line
        time_line = [' '] * len(line_top)
        for i, (pos, time_value) in enumerate(time_positions):
            # Add an extra space before the last time value
            if i == len(time_positions) - 1:
                time_str = f" {time_value}"
            else:
                time_str = str(time_value)
            time_start = pos
            time_end = time_start + len(time_str)
            if time_end > len(time_line):
                time_line.extend([' '] * (time_end - len(time_line)))
            for j, char in enumerate(time_str):
                if time_start + j < len(time_line):
                    time_line[time_start + j] = char
                else:
                    time_line.append(char)

        time_line_str = ''.join(time_line).rstrip()

        # Remove leading space from the first time line only
        if not chart_lines:
            time_line_str = time_line_str.lstrip()
        else:
            time_line_str = time_line_str.lstrip()

        # Append the current segment to chart_lines
        chart_lines.extend([line_top, line_middle, line_bottom, time_line_str])

    # Print the Gantt chart
    print("\nGantt Chart:")
    for line in chart_lines:
        print(line)
    print()
