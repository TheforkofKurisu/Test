if __name__ == '__main__':
    list1 = list(range(1, 10))
    list2 = list(range(1, 10))
    for i in list1:
        for j in list2:
            print(i * j,end="")
            print(" ",end="")
        print("\n")