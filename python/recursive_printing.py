def printN(n):
    if n == 1:
        print(n)
    else:
        printN(n-1)
        print(n)
        



def main():
    val_n = int(input("Enter the value for N: "))
    printN(val_n)

main()

#Taken from starting out with Python book. Page 525. Date is 2020-04-02