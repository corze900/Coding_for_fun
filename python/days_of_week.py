def dayOfWeek(n):
    weekday = {
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thurday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }
    print(weekday.get(n,"Invalid Input"))
        

    

def main():
    x = int(input("Enter the day of the week in #: "))
    dayOfWeek(x)

    

main()

#Taken from starting out with Python book. Page 115. Date is 2020-04-03