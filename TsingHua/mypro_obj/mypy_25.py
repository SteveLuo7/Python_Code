import pickle
with open(r"123.png","wb") as f:
    a1 = "Luoshibin"
    a2 = 123
    a3 = [10,20,30]

    pickle.dump(a1,f)
    pickle.dump(a2,f)
    pickle.dump(a3,f)