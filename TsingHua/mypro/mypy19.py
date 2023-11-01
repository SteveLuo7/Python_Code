str = 'global is running'

def outer():

    # str = 'outter is running'
    def inner():
        # str = 'inner is running'
        print(str)

    inner()


outer()