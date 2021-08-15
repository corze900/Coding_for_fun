#Function to find a perticular string in a string and changing said string to * the amount of times it find it
#For example string s= stringstring and p=in and it will replace s with str*ngstr**ng by the amount of times it finds p
def myfunc(s,p):
    results =''
    a = s.split(p)
    #the amount of times we find p
    b = s.count(p)
    counter = 1
    for i in a:
        results += i
        if counter <= b:
            #checking if our counter is less/equal to b and mutiplying the amount of time * by the counter!! No idea you could mutiply stings in python
            results += '*'*counter
        counter += 1 
            
    print(results)

myfunc("stringstringstringstring", "in")