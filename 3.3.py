if __name__ == '__main__':
    Num = 0
    Count = 0
    for i in range(1, 5):
        for j in range(1, 5):
            if j != i:
                for k in range(1, 5):
                    if k != i and k != j:
                        Num = 100 * i + 10 * j + k
                        Count = Count + 1
                        print(Num)
    print("共有", Count, "个数")
