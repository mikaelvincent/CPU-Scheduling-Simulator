from algorithms.fcfs import fcfs_scheduling
from algorithms.priority_non_preemptive import priority_non_preemptive_scheduling
from algorithms.priority_preemptive import priority_preemptive_scheduling
from algorithms.round_robin import round_robin_scheduling
from algorithms.sjf import sjf_scheduling
from algorithms.srtf import srtf_scheduling
from utils.display import display_process_info
from utils.gantt_chart import generate_gantt_chart
from utils.input_handler import read_process_data

def run():
    input_file = input("Enter the path to the input file: ")
    try:
        processes = read_process_data(input_file)
        print(f"Successfully read {len(processes)} processes.\n")

        print("Select Scheduling Algorithm:")
        print("1. First Come First Serve Scheduling")
        print("2. Priority Non-Preemptive Scheduling")
        print("3. Priority Preemptive Scheduling")
        print("4. Shortest Remaining Time First Scheduling")
        print("5. Round Robin Scheduling")
        print("6. Shortest Job First Scheduling")
        choice = input("Enter your choice (1, 2, 3, 4, 5, or 6): ")

        if choice == '1':
            scheduled_processes, gantt_chart = fcfs_scheduling(processes)
            print("\nFirst Come First Serve Scheduling Simulation Results:\n")
        elif choice == '2':
            scheduled_processes, gantt_chart = priority_non_preemptive_scheduling(processes)
            print("\nPriority Non-Preemptive Scheduling Simulation Results:\n")
        elif choice == '3':
            scheduled_processes, gantt_chart = priority_preemptive_scheduling(processes)
            print("\nPriority Preemptive Scheduling Simulation Results:\n")
        elif choice == '4':
            scheduled_processes, gantt_chart = srtf_scheduling(processes)
            print("\nShortest Remaining Time First Scheduling Simulation Results:\n")
        elif choice == '5':
            time_quantum_input = input("Enter the time quantum for Round Robin Scheduling: ")
            try:
                time_quantum = int(time_quantum_input)
                if time_quantum <= 0:
                    print("Time quantum must be a positive integer.")
                    return
            except ValueError:
                print("Invalid time quantum. Exiting.")
                return
            scheduled_processes, gantt_chart = round_robin_scheduling(processes, time_quantum)
            print("\nRound Robin Scheduling Simulation Results:\n")
        elif choice == '6':
            scheduled_processes, gantt_chart = sjf_scheduling(processes)
            print("\nShortest Job First Scheduling Simulation Results:\n")
        else:
            print("Invalid choice. Exiting.")
            return

        display_process_info(scheduled_processes)
        generate_gantt_chart(gantt_chart)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
