def checkMagicNumber(m,d,y):
    if (m * d) == y:
        print("Yes this is a magic date")
        print(format(d,'d')+"/"+format(m,'d')+"/"+format(y,'d'))
    else:
        print("This is not a magic date")
    

def main():
    print("This is the magic date finder! Please enter a Month, Day, and Year")
    m = int(input("Please enter the Month in numeric form: "))
    d = int(input("Please enter the Day: "))
    y = int(input("Please enter the Year, last 2 digits: "))
    checkMagicNumber(m,d,y)
    

main()

#Taken from starting out with Python book. Page 116. Date is 2020-04-03