from models.process import Process
from algorithms.priority_non_preemptive import priority_non_preemptive_scheduling
from algorithms.priority_preemptive import priority_preemptive_scheduling

def read_process_data(file_path: str):
    """
    Reads process data from the specified input file.

    Args:
        file_path (str): The path to the input file containing process data.

    Returns:
        List[Process]: A list of Process instances created from the input data.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the input data is invalid or incomplete.
    """
    processes = []
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                stripped_line = line.strip()
                if not stripped_line:
                    continue  # Skip empty lines
                parts = stripped_line.split()
                if len(parts) != 3:
                    raise ValueError(
                        f"Line {line_number}: Expected 3 values per line (arrival_time burst_time priority)."
                    )
                try:
                    arrival_time = int(parts[0])
                    burst_time = int(parts[1])
                    priority = int(parts[2])
                except ValueError:
                    raise ValueError(
                        f"Line {line_number}: All values must be integers."
                    )
                if arrival_time < 0 or burst_time <= 0 or priority < 0:
                    raise ValueError(
                        f"Line {line_number}: Invalid values. Arrival time and priority must be non-negative; burst time must be positive."
                    )
                process = Process(arrival_time, burst_time, priority)
                processes.append(process)
    except FileNotFoundError:
        print(f"Error: Input file '{file_path}' not found.")
        raise
    except ValueError as ve:
        print(f"Error: {ve}")
        raise
    return processes

def display_process_info(processes):
    """
    Displays the scheduling information for each process.

    Args:
        processes (List[Process]): The list of processes with scheduling info.
    """
    print("Process\tArrival\tBurst\tPriority\tStart\tCompletion\tWaiting\tTurnaround")
    for idx, process in enumerate(processes):
        print(f"P{idx+1}\t{process.arrival_time}\t{process.burst_time}\t{process.priority}\t"
              f"{process.start_time}\t{process.completion_time}\t"
              f"{process.waiting_time}\t{process.turnaround_time}")
    total_waiting_time = sum(p.waiting_time for p in processes)
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    n = len(processes)
    print(f"\nAverage Waiting Time: {total_waiting_time / n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround_time / n:.2f}")

def main():
    # Entry point for the scheduling application.
    input_file = input("Enter the path to the input file: ")
    try:
        processes = read_process_data(input_file)
        print(f"Successfully read {len(processes)} processes.\n")

        # Provide options to select the desired scheduling algorithm
        print("Select Scheduling Algorithm:")
        print("1. Priority Non-Preemptive Scheduling")
        print("2. Priority Preemptive Scheduling")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            # Perform Priority Non-Preemptive scheduling
            scheduled_processes = priority_non_preemptive_scheduling(processes)
            print("\nPriority Non-Preemptive Scheduling Results:\n")
        elif choice == '2':
            # Perform Priority Preemptive scheduling
            scheduled_processes = priority_preemptive_scheduling(processes)
            print("\nPriority Preemptive Scheduling Results:\n")
        else:
            print("Invalid choice. Exiting.")
            return

        # Display scheduling results
        display_process_info(scheduled_processes)
    except Exception:
        print("Failed to read process data due to an error.")

if __name__ == "__main__":
    main()
