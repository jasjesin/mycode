def manipulate_generator(generator, n):
    # Enter your code here
    str1 = [1]
    for num in range(2, 100):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    str1.append(num)
                    break
            if len(str1) == n:
                # for x in str1:
                print(str1)

    else:
        None

    pass


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)
