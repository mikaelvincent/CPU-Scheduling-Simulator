from models.process import Process

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

def main():
    # Entry point for the scheduling application.
    input_file = input("Enter the path to the input file: ")
    try:
        processes = read_process_data(input_file)
        print(f"Successfully read {len(processes)} processes.")
        # Proceed with scheduling algorithms or further processing
    except Exception:
        print("Failed to read process data due to an error.")
        # Handle the exception appropriately

if __name__ == "__main__":
    main()
