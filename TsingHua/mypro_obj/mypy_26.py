import pickle

with open(r"123.png","rb") as f:
    a1 = pickle.load(f)
    a2 = pickle.load(f)
    a3 = pickle.load(f)

    print(a1)
    print(a2)
    print(a3)