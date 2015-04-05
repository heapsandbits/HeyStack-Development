#Program: HayStack - String Scan
#Developer: Rich Hoggan (GhostBit Cyber Assurance)
#Creation Date: 12-02-2013
#Description: Scans suspected malware files for strings and registry keys.

###Import Directives###
import time
import shutil

###Function Code###
#Function Name: printProgramInformation
#Function Description: Print's the program's initial information.
def printProgramInformation():
    print "HayStack - String Scan"
    print "Developed By: Rich Hoggan"
    print "C2013 GhostBit Cyber Assurance"
    print ""

#Function Name: printErrorMessage()
#Function Description: Prints an error message based on the error flag.
#Function Argument(S): errorFlag
def printErrorMessage(errorFlag):
    if errorFlag == "INVALID_MENU_OPTION":
        print "Invalid menu option entered.  Double check input and try again."
    elif errorFlag == "INVALID_INPUT":
        print "Invalid input entered. Double check input and try again."
    elif errorFlag == "EMPTY_INPUT":
        print "Invalid input.  No input was provided..."
    else:
        print "Invalid argument passed to printErrorMessage() function."

###Application Code###
#Another comment
#Variable declarations
fileName = ""
fileObject = ""
foundStrings = False
foundStringsData = []
numberOfLinesWithStrings = 0
totalLinesScanned = 0
resultsFileName = ""
resultsFileObject = ""
tempFileLine = ""
sourceDirectory = ""
destinationDirectory = ""
fileWriteTime = ""
fileWriteTimeFormat = ""

printProgramInformation()

#Get input from user - fileName
fileName = raw_input("File name: ")
if fileName == "":
    printErrorMessage("EMPTY_INPUT")
		
    while fileName == "":
	#Get input from user - fileName
        fileName = raw_input("File name: ")
                    
#Load file
fileObject = open(fileName,"r")

#Iterate through file and search for strings
print ""
print "Scanning for strings..."
time.sleep(1)
for currentLine in fileObject:
    #If a double quote or single quote is found with the current line
    #add it to the foundStringsData list
    if currentLine.find("\"") > 0 or currentLine.find("'") > 0:
	#Set foundStrings flag to true
        foundStrings = True
		
	#String new line characters before appending to storage
        currentLine = currentLine.strip()
        foundStringsData.append(currentLine)
		
	#Count lines that have strings
        numberOfLinesWithStrings = numberOfLinesWithStrings + 1
	
    #Count total number of lines scanned
    totalLinesScanned = totalLinesScanned + 1
		
#Print to the command line
#Determine if strings were found in the specimen file
if foundStrings == True:
    print "Found Strings:"
    for currentElement in foundStringsData:
        print currentElement
    print ""
    print "Scan Statistics:"
    print numberOfLinesWithStrings,"/",totalLinesScanned,"had strings..."
    print "Total Lines Scanned:",totalLinesScanned
if foundStrings == False:
    print "No strings were found within the specimin file..."
		
#Close input file object
fileObject.close()

#Generate results file with time stamp
fileWriteTime = time.localtime(time.time())
fileWriteTimeFormat = str(fileWriteTime[0]) + "-" +  str(fileWriteTime[1]) + "-" + str(fileWriteTime[2]) + "-H" \
    + str(fileWriteTime[3]) \
    + "M" + str(fileWriteTime[4]) + "S" + str(fileWriteTime[5])
resultsFileName = "string_scan_results-" + fileWriteTimeFormat + ".txt"
resultsFileObject = open(resultsFileName,"w")
    
#Write scan report
#Write file information header
tempFileLine = ""
tempFileLine = "Scan Report:\n"
resultsFileObject.write(tempFileLine)

tempFileLine = ""
tempFileLine = "Specimen File:" + fileName + "\n"
resultsFileObject.write(tempFileLine)

tempFileLine = ""
tempFileLine = "Scan Date: " + time.asctime(time.localtime(time.time())) + "\n"
resultsFileObject.write(tempFileLine)
		
#Determine if strings were found and write to the file otherwise write
#a message stating no strings were found
if foundStrings == True:
    resultsFileObject.write("Found Strings:\n")
    for currentElement in foundStringsData:
        tempFileLine = ""
        tempFileLine = currentElement + "\n"
        resultsFileObject.write(tempFileLine)
    resultsFileObject.write("\n\n")
    resultsFileObject.write("Scan Statistics:\n")
    tempFileLine = str(numberOfLinesWithStrings) + "/" + str(totalLinesScanned) \
	+ " lines had strings...\n"
    resultsFileObject.write(tempFileLine)
    tempFileLine = ""
    tempFileLine = "Total Lines Scanned:"+str(totalLinesScanned)
    resultsFileObject.write(tempFileLine)
if foundStrings == False:
    resultsFileObject.write("No strings were found within the specimen file...")

#Close file object once file is written
resultsFileObject.close()

#Move report file to Scan Report Files directory
sourceDirectory = "C:\Users\Richard\Desktop\HayStack\\" + resultsFileName
destinationDirectory = "C:\Users\Richard\Desktop\HayStack\Scan Report Files\String Scans\\" + resultsFileName
shutil.move(sourceDirectory, destinationDirectory)
