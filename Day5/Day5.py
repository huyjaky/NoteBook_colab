def Question_1():
    emptyList = []
    for i in range(11):
        emptyList.append(i)
    return emptyList


def Question_2():
    for i in range(5):
        print(Question_1()[i])
    pass


def Question_3():
    for i in Question_1():
        if i % 2 == 0:
            print(i)
    pass


def Question_4():
    sum = 0
    for i in Question_1():
        sum += i
    return sum
