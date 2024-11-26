# CPU Scheduling Simulator

## Overview

This application simulates various CPU scheduling algorithms, including First Come First Serve (FCFS), Shortest Job First (SJF), Priority Scheduling (both preemptive and non-preemptive), Shortest Remaining Time First (SRTF), and Round Robin. It calculates and displays key metrics such as turnaround time and waiting time for each process, and visualizes the execution timeline using Gantt charts.

## Installation

Install the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Prepare the Input File

Create a text file containing process data. Each line should represent a process with three integers separated by spaces: `arrival_time`, `burst_time`, and `priority`. For example:

```
0 5 2
2 3 1
4 1 3
```

### 2. Run the Application

Execute the main application script:

```bash
python main.py
```

### 3. Provide Input When Prompted

- **Enter the path to the input file:** Specify the path to your process data file.
- **Select Scheduling Algorithm:** Choose the desired scheduling algorithm by entering the corresponding number:
  - `1`: First Come First Serve Scheduling
  - `2`: Priority Non-Preemptive Scheduling
  - `3`: Priority Preemptive Scheduling
  - `4`: Shortest Remaining Time First Scheduling
  - `5`: Round Robin Scheduling
  - `6`: Shortest Job First Scheduling
- **Enter Time Quantum (for Round Robin):** If you select Round Robin Scheduling, input the time quantum value when prompted.

### 4. View Results

- The application will display a table summarizing key scheduling metrics for each process:
  - **Arrival Time**
  - **Burst Time**
  - **Priority**
  - **Start Time**
  - **Completion Time**
  - **Waiting Time**
  - **Turnaround Time**
- The average waiting time and turnaround time will also be shown.
- A Gantt chart visualizing the execution timeline will be displayed.
