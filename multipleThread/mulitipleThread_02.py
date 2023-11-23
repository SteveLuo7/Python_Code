from multiprocessing import Process

def run_test():
    print('Its Testing...')


if __name__ == '__main__':
    print('Main Process is on')
    p = Process(target=run_test())

    p.start()
