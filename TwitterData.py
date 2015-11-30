#Author: Frank Dong
#Date: Nov 15, 2015
#Purpose: To create a program which will perform a simple sentiment analysis
#         on Twitter data.
from happy_histogram import *

#Global value keywordList table is initalized
keywordList = []
keywordList.append([])
keywordList.append([])

#Purpose: To process the keywords into a table of words and values
#Parameter: keywordFile
#Return: None
def keywordProcessing(keywordFile):
    line = keywordFile.readline()

    #Splits file by the comma and puts the two values into 2 table values, then loops
    while line != "":
        line = line.rstrip()
        value = line.split(",")
        keywordList[0].append(value[0])
        keywordList[1].append(value[1])
        line=keywordFile.readline()

#Purpose: To process the location of a tweet
#Parameter: line
#Return: location
def locationProcessing(line):
    location = ""
    LAT_ONE = 49.189787
    LAT_TWO = 24.660845
    LONG_ONE = -67.444574
    LONG_TWO = -87.518395
    LONG_THREE = -101.998892
    LONG_FOUR = -115.236428
    LONG_FIVE = -125.242264
    line = line.split(" ")
    
    #Checking to see which area the tweet originates from
    if float(line[0]) <= LAT_ONE and float(line [0]) >= LAT_TWO and float(line[1]) <= LONG_ONE and float(line[1]) >= LONG_TWO:
        location = "Eastern"
    elif float(line[0]) <= LAT_ONE and float(line [0]) >= LAT_TWO and float(line[1]) <= LONG_TWO and float(line[1]) >= LONG_THREE:
        location = "Central"
    elif float(line[0]) <= LAT_ONE and float(line [0]) >= LAT_TWO and float(line[1]) <= LONG_THREE and float(line[1]) >= LONG_FOUR:
        location = "Mountain"
    elif float(line[0]) <= LAT_ONE and float(line [0]) >= LAT_TWO and float(line[1]) <= LONG_FOUR and float(line[1]) >= LONG_FIVE:
        location = "Pacific"
    return location

#Purpose: Will return a list of values with the happiness scores and tweets of each timezone
#Parameter: tweetFile
#Return: happinessList and tweetCountList
def tweetProcessing(tweetFile):
    happinessList = []
    easternHappiness = 0
    centralHappiness = 0
    mountainHappiness = 0
    pacificHappiness = 0

    tweetCountList = []
    easternTweetCount = 0
    centralTweetCount = 0
    mountainTweetCount = 0
    pacificTweetCount = 0

    keywordCount = 0
    sentimentValue = 0
    line = tweetFile.readline()
    while line != "":
        #Punctuation stripping
        line = line.replace("[", "")
        line = line.replace("]", "")
        line = line.replace(",", "")
        tweetLocation = locationProcessing(line)
        #line = line.replace(".", "")
        value = line.split(" ")
        for i in range(len(value)):
            value[i] = value[i].strip("[]./?:;\"\'\n\”#@$%^&*()=!")
            
        #Will go in a loop comparing each tweet word to each keyword, if a match is found
        #program will add keyword values and count value
        for count in range (len(value)):
            for j in range(len(keywordList[0])):
                if keywordList[0][j].upper() == value[count].upper():
                    keywordCount = keywordCount + 1
                    sentimentValue = float(keywordList[1][j]) + sentimentValue
        #Will add the values to the proper tweet locations
        if keywordCount != 0:
            sentimentValue = sentimentValue/keywordCount
            if tweetLocation == "Eastern":
                easternHappiness = sentimentValue + easternHappiness
                easternTweetCount = easternTweetCount + 1
            elif tweetLocation == "Central":
                centralTweetCount = centralTweetCount + 1
                centralHappiness = sentimentValue + centralHappiness
            elif tweetLocation == "Mountain":
                mountainTweetCount = mountainTweetCount + 1
                mountainHappiness = sentimentValue + mountainHappiness
            elif tweetLocation == "Pacific":
                pacificTweetCount = pacificTweetCount + 1
                pacificHappiness = sentimentValue + pacificHappiness
        #Resets value for next loop
        line=tweetFile.readline()
        keywordCount = 0
        sentimentValue = 0
        
    #Adds value to list
    happinessList.append(easternHappiness)
    happinessList.append(centralHappiness)
    happinessList.append(mountainHappiness)
    happinessList.append(pacificHappiness)

    tweetCountList.append(easternTweetCount)
    tweetCountList.append(centralTweetCount)
    tweetCountList.append(mountainTweetCount)
    tweetCountList.append(pacificTweetCount)
    return (happinessList + tweetCountList)
#================ Main ======================
#Checks keywords input file and handles exception if the file produces an error
try:
    keywordsFileName = input("Please enter you keyword file name: ")
    keywordFile = open(keywordsFileName)
    keywordProcessing(keywordFile)
except IOError:
    print ("Error: Keywords file was not found.")
    quit()

#Checks tweet input file and handles exception if the file produces an error
try:
    tweetFileName = input("Please enter your tweet file name: ")
    tweetFile = open(tweetFileName, encoding="utf8")
    finalValuesList = tweetProcessing(tweetFile) 
except IOError:
    print ("Error: Tweets file was not found.")
    quit()

#Print Statements
print("*" * 50)
print ("Total Eastern Happiness Score:", (float(finalValuesList[0])/float(finalValuesList[4])))
print ("Number of Eastern tweets containing keywords:", finalValuesList[4])
print ("")
print ("Total Central Happiness Score:", (float(finalValuesList[1])/float(finalValuesList[5])))
print ("Number of Central tweets containing keywords:", finalValuesList[5])
print ("")
print ("Total Mountain Happiness Score:", (float(finalValuesList[2])/float(finalValuesList[6])))
print ("Number of Mountain tweets containing keywords:", finalValuesList[6])
print ("")
print ("Total Pacific Happiness Score:", (float(finalValuesList[3])/float(finalValuesList[7])))
print ("Number of Pacific tweets containing keywords:", finalValuesList[7])
print("*" * 50)

#Draws Histogram with data values
drawSimpleHistogram(float(finalValuesList[0])/float(finalValuesList[4]),float(finalValuesList[1])/float(finalValuesList[5]), float(finalValuesList[2])/float(finalValuesList[6]),float(finalValuesList[3])/float(finalValuesList[7]))
