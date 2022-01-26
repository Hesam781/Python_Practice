if __name__ == '__main__':
    y = 0
    z = -1

    # get 20 numbers
    for x in range(0,20):
        print("Input Number : ", end=" ")
        y = int(input())
        if y > z:
            z = y

    # print highest number
    print("high Number : " + str(z))

