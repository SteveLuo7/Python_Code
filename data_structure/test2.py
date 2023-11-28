
import time

def cpu_intensive_task():
    result = 0
    iterations = 10**4

    for _ in range(iterations):
        for _ in range(100):  # Increase the nested loop iterations
            result = (result + 1) * 2  # Intensive computation

if __name__ == "__main__":
    start_time = time.time()

    # Run the CPU-intensive task
    cpu_intensive_task()

    end_time = time.time()

    # Calculate and print the execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
