with open(r"123.png","rb") as f:
    with open (r"123cp.png","wb") as w:
        for line in f.readlines():
            w.write(line)
print("PNG COPY FINISHED")
f.close()
w.close()