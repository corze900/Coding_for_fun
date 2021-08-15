def ackermann(m,n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1,1)
    return ackermann(m-1, ackermann(m,n-1))



def main():
    val_m = int(input("Enter the value for M: "))
    val_n = int(input("Enter the value for N: "))
    
    print("The value of the Ackermann's function is: "+ str(ackermann(val_m,val_n)))
    

main()

#This will exced the resources of a computer.
#Taken from starting out with Python book. Page 525. Date is 2020-04-02