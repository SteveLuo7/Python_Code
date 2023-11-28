import timeit

def test_append_speed():
    setup_code = "my_list = []"
    append_code = "my_list.append(1)"

    # Measure the time taken to execute the append operation
    time_taken = timeit.timeit(append_code, setup_code, number=1000000)
    print(f"Append time: {time_taken:.6f} seconds")

def test_insert_speed():
    setup_code = "my_list = [0] * 1000000"
    insert_code = "my_list.insert(500000, 1)"

    # Measure the time taken to execute the insert operation
    time_taken = timeit.timeit(insert_code, setup_code, number=1000)
    print(f"Insert time: {time_taken:.6f} seconds")

if __name__ == "__main__":
    # Test append speed
    test_append_speed()

    # Test insert speed
    test_insert_speed()
