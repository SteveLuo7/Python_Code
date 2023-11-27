def test(n):
    count = 0;
    for i in range(count,n):
        for j in range(count,n):
            count += 1

    for k in range(0,2*n):
        count += 1

    icount = 10
    while icount > 0:
        count += 1
        icount -= 1

    print(count,icount)

test(5)
