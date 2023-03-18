def announce(f):
    def wrappper():
        print("about to run the function...")
        f()
        print("Done with the function.")
    return wrappper()

    @announce
    def hello():
        print("Hello, World")

    hello()