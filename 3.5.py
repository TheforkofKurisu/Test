if __name__ == '__main__':
    Num = int(input("请输入一个五位整数："))
    print(Num)
    list1 = []
    for i in range(4, -1):
        list1.append(Num // (10 ** i))
    print(list1)

