if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    array = []
    p = 0
    for one in range(x + 1):
        for two in range(y + 1):
            for three in range(z + 1):
                if one + two + three != n:
                    array.append([])
                    array[p] = [one, two, three]
                    p += 1
    print(array)