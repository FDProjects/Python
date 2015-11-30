#Author:Frank Dong
#Date: Sept 22, 2015
#Purpose: To create a parking program which will showcase our knowledge on python through the use of user input,
#         decisions, simple calculations and print statements.

programRestart = 'Y'
while programRestart.upper() == 'Y':
    customerName = input ("Please enter your customer name: ")
    classificationCode = ''
    classificationCode = input("Please enter your customer classification code: ")

    #Checks for correct classification code, if invalid the program halts
    if classificationCode.upper() != 'B' and classificationCode.upper() != 'D' and classificationCode.upper() != 'W':
        print ("=" * 50)
        print ("Error")
        print ("Invalid Code: " + classificationCode)
        print("Customer Name: " + customerName)
    else:
        numOfDays =  int(input("Please enter the number of days the vehicle has been rented: "))
        oStartReading = int(input("Please enter the vehicle's odometer reading at the start of the rental period: "))
        oEndReading = int(input("Please enter the vehicle's odmeter reading at the end of the rental period: "))
        kilosdriven = oEndReading - oStartReading
        avgKiloDrivenDay = kilosdriven/numOfDays

    #Calculation for number of weeks, if weeks are not whole take the int of number of weeks + 1
        if numOfDays % 7 == 0:
            numOfWeeks = int(numOfDays/7)
        else:
            numOfWeeks = int(numOfDays/7) + 1
            
    #Calculation for average kilometers driven per week        
        if numOfDays >= 7:
            avgKiloDrivenWeek = kilosdriven/(numOfWeeks)
        else:
            avgKiloDrivenWeek = kilosdriven/1
            
    #Classification Code decisions
        if classificationCode.upper() == 'B':
            chargeValue = (40 * numOfDays) + (kilosdriven * 0.25)
        elif classificationCode.upper() == 'D':
            if (avgKiloDrivenDay) > 100:
                chargeValue = (60 *numOfDays) + ((avgKiloDrivenDay - 100) * 0.25)* numOfDays
            else:
                chargeValue = 60 * numOfDays
        elif classificationCode.upper() == 'W':
            if avgKiloDrivenWeek > 900 and avgKiloDrivenWeek < 1500:
                chargeValue = (190 * numOfWeeks) + (50 * numOfWeeks)
            elif avgKiloDrivenWeek > 1500:
                chargeValue = (190 * numOfWeeks) + (100 * numOfWeeks) + (((avgKiloDrivenWeek - 1500) * 0.25)* numOfWeeks)
            else:
                chargeValue = 190 * numOfWeeks
        else:
            print ("Error. Please contact attendent.")
            
    #Print (User Output) Section
        print ("=" * 50)
        print ("Customer Name:",customerName)
        print ("Classification Code:",classificationCode.upper())
        print ("Number Of Days vehicle was rented:",numOfDays,"Days")
        print ("Odometers reading at the start of rental period:",oStartReading,"KM")
        print ("Odometers reading at the end of the rental period:",oEndReading,"KM")
        print ("The number of Kilometers driven:",kilosdriven,"KM")
        print ("Amount billed: $%.2f"%chargeValue)
    print ("============== Program has ended! ================")
    programRestart = input ("Please enter (Y) to restart the program, anything else to terminate it: ")
