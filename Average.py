if __name__ == '__main__':
    y = 0
    
    # get numbers
    for x in range(0,20):
        print("Input Number : ", end=" ")
        y += int(input())
        
    # print Average
    print("Calculate the average : "+str(y/20))

