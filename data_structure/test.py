import time

def cpu_intensive_task():
    result = 0
    for _ in range(10**7):  # Adjust the range based on your CPU's processing power
        result += 1

if __name__ == "__main__":
    start_time = time.time()

    # Run the CPU-intensive task
    cpu_intensive_task()

    end_time = time.time()

    # Calculate and print the execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
