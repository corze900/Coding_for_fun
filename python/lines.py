def showAsterixs(n):
    if n == 1:
        print("*")
    else:
        showAsterixs(n-1)
        print("*"*n)
        #Apparently this is a thing in python, where you can times
        #the number of charaters in a string
       
def main():
    val = int(input("Enter the value for *: "))
    showAsterixs(val)

main()

#Taken from starting out with Python book. Page 525. Date is 2020-04-02