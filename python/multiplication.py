def printN(x,y):
    if x == 1:
        return y
    else:
        return y + printN(x-1,y)
        



def main():
    val_x = int(input("Enter the value for X: "))
    val_y = int(input("Enter the value for Y: "))
    print(printN(val_x,val_y))

main()

#Taken from starting out with Python book. Page 525. Date is 2020-04-02