import time
def sum_of_n(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i

    end = time.time()
    return the_sum, (end - start)


print(sum_of_n(100000))

def sum_of_n2(n):
    return (n*(n+1)/2)


print(sum_of_n2(100000))
