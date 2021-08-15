import click
import adafruit_thermal_printer
import serial

@click.command()
def ToDoListInterface():
    #This first  Section begins with the first selection for the user
    #Currently only using a ToDo list template
    click.echo('Welcome to the Therminal Printer Interface!')
    click.echo('\n \n')
    click.echo('TODOlist (t), etc (work in progress), Quit (q)\n')
    user_input = click.prompt("Please enter the appropriate selection")
    if user_input == 'q':
        exitScreen()
    elif user_input == 't':
        toDoList()
        print('kappa')
    else:
        print('Wrong selection, Now exiting')
        exitScreen()



#simple exitScreen message whenever the program terminates
def exitScreen():
    print('Thanks for using the Therminal Printer Interface!\n')
    print('Bye now :)')
    exit(0)

#adds two lines of whitespace
def whiteSpace():
    print('\n\n')

#the core funtionality
@click.command()
def toDoList():
    whiteSpace()
    title = click.prompt("Please Enter a To Do list Title")
    subtitleArr = []
    subtitle_explanationArr = []
    for x in range(5):
        subtitle = click.prompt("Please Enter a To Do list item")
        subtitle_explanation = click.prompt("Please Enter a definition for "+str(subtitle))
        quit = click.prompt("Would you like to add another item [y/n]?")
        subtitleArr.append(subtitle)
        subtitle_explanationArr.append(subtitle_explanation)
        if quit == 'n':
            #tell the printer will now print the to do list
            #send the array here
            break
        #if user uses all 5 items
        #send arrays here instead
    #Tested this it works as needed
    #print(*subtitleArr,sep = ", ")
    #print(*subtitle_explanationArr, sep =", ")
    sendForPrint(title,subtitleArr,subtitle_explanationArr)
    print("Now sending to printer")

def sendForPrint(t,st,ste):
    #set the printer
    #can find examples of this on the thermal_printer_simpletest.py
    TP = adafruit_thermal_printer.get_printer_class(2.69)
    uart = serial.Serial("/dev/ttyUSB0", baudrate=19200, timeout=3000)
    pT = TP(uart,auto_warm_up=False)
    pT.warm_up()
    #Start Printing
    pT.size = adafruit_thermal_printer.SIZE_LARGE
    pT.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    pT.print(t)
    pT.feed(2)
    #change printer settings
    for x in range(len(st)):
        pT.justify = adafruit_thermal_printer.JUSTIFY_LEFT
        pT.bold = True
        pT.size = adafruit_thermal_printer.SIZE_MEDIUM
        pT.print(st[x])
        pT.bold = False
        pT.feed(1)
        #seperated by settings
        pT.size = adafruit_thermal_printer.SIZE_SMALL
        pT.print(ste[x])
        pT.feed(1)
    pT.feed(2)

    print("print done")
    exitScreen()






if __name__ == '__main__':
    ToDoListInterface() 
