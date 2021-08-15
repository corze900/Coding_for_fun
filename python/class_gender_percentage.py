def getInput():
    return input()

def classPercent(x,n):
    print(format(x/n,'.0%'))
    

def main():
    print("Enter the number of males in class :")
    maleN = int(getInput())
    print("Enter the number of females in class :")
    femalesN = int(getInput())
    print("The % of males is: ")
    classPercent(maleN,maleN+femalesN)
    print("The % of females is: ")
    classPercent(femalesN,maleN+femalesN)
    

main()

#Taken from starting out with Python book. Page 525. Date is 2020-04-02