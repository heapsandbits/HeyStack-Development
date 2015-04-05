#Program: HayStack - URL Scan
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
    print "HayStack - URL Scan"
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
		
#Variable declarations
fileName = ""
fileObject = ""
foundURLS = False
foundURLSData = []
numberOfLinesWithURLS = 0
totalLinesScanned = 0

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

#Iterate through the file
print ""
print "Scanning for URL's:"
print ""
time.sleep(1)
for currentLine in fileObject:
    #If a URL is found within the current line, add it to the foundURISData list
    if currentLine.find("http") > 0 or currentLine.find(".exe") > 0:
        foundURLS = True

        #Strip new line characters before appending to storage
        currentLine = currentLine.strip()
        foundURLSData.append(currentLine)
	
        #Count total functions found
        numberOfLinesWithURLS = numberOfLinesWithURLS + 1
	
    #Count total lines scanned
    totalLinesScanned = totalLinesScanned + 1
	
#Determine if functions were found 
if foundURLS == True:
	print "Found URL'S:"
	for currentElement in foundURLSData:
		print currentElement
	print ""
	print "Scan Statistics:"
	print numberOfLinesWithURLS,"/",totalLinesScanned,"lines had URL's..."
	print "Total Lines Scanned: ",totalLinesScanned
else:
	print "No functions found..."
	
#Close file object
fileObject.close()

#Generate results file with time stamp
fileWriteTime = time.localtime(time.time())
fileWriteTimeFormat = str(fileWriteTime[0]) + "-" +  str(fileWriteTime[1]) + "-" + str(fileWriteTime[2]) + "-H" \
    + str(fileWriteTime[3]) \
    + "M" + str(fileWriteTime[4]) + "S" + str(fileWriteTime[5])
resultsFileName = "url_scan_results-" + fileWriteTimeFormat + ".txt"
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

#Determine if functions were found and write to the file otherwise write a message stating no
#strings were found
if foundURLS == True:
	resultsFileObject.write("Found URL's:\n")
	for currentElement in foundURLSData:
		tempFileLine = ""
		tempFileLine = currentElement + "\n"
		resultsFileObject.write(tempFileLine)
	resultsFileObject.write("\n\n")
	resultsFileObject.write("Scan Statistics:\n")
	tempFileLine = str(numberOfLinesWithURLS) + "/" \
		+ str(totalLinesScanned) + " lines had URL's...\n"
	resultsFileObject.write(tempFileLine)
	tempFileLine = ""
	tempFileLine = "Total Lines Scanned: " + str(totalLinesScanned)
	resultsFileObject.write(tempFileLine)
if foundURLS == False:
	resultsFileObject.write("No URL's were found within the specimen file...")
	
#Close file object once file is written
resultsFileObject.close()

#Move report file to Scan Report Files directory
sourceDirectory = "C:\Users\Richard\Desktop\HayStack\\" + resultsFileName
destinationDirectory = "C:\Users\Richard\Desktop\HayStack\Scan Report Files\URL Scans\\" + resultsFileName
shutil.move(sourceDirectory, destinationDirectory)
