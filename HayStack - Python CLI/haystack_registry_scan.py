#Program: HayStack - Registry Scan
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
    print "HayStack - Registry Scan"
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
foundRegistryKeys = False
foundRegistryKeysData = []
numberOfLinesWithRegistryKeys = 0
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
print "Scanning for registry keys:"
time.sleep(1)
for currentLine in fileObject:
    #If a registry key is found within the current line, add it to
    #the foundRegisryKeysData list
    if currentLine.find("HKEY") > 0:
	#Set found registry keys flag
        foundRegistryKeys = True
		
	#Strip new line characters before appending to storage
        currentLine = currentLine.strip()
        foundRegistryKeysData.append(currentLine)
		
	#Count total registry keys found
        numberOfLinesWithRegistryKeys = numberOfLinesWithRegistryKeys + 1
	
    #Count total lines scanned
    totalLinesScanned = totalLinesScanned + 1

#Determine if registry keys were found or not
if foundRegistryKeys == True:
    print "Found Registry Keys:"
    for currentElement in foundRegistryKeysData:
        print currentElement
    print ""
    print "Scan Statistics:"
    print numberOfLinesWithRegistryKeys,"/",totalLinesScanned,"lines had registry keys...\n"
    print "Total Lines Scanned:",totalLinesScanned
else:
    print "No registry keys found..."
	
#Close file object
fileObject.close()

#Generate results file with time stamp
fileWriteTime = time.localtime(time.time())
fileWriteTimeFormat = str(fileWriteTime[0]) + "-" +  str(fileWriteTime[1]) + "-" + str(fileWriteTime[2]) + "-H" \
    + str(fileWriteTime[3]) \
    + "M" + str(fileWriteTime[4]) + "S" + str(fileWriteTime[5])
resultsFileName = "registry_key_scan_results-" + fileWriteTimeFormat + ".txt"
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
if foundRegistryKeys == True:
    resultsFileObject.write("Found Registry Keys:\n")				
    for currentElement in foundRegistryKeysData:
        tempFileLine = ""
        tempFileLine = currentElement + "\n"
        resultsFileObject.write(tempFileLine)
    resultsFileObject.write("\n\n")
    resultsFileObject.write("Scan Statistics:\n")
    tempFileLine = str(numberOfLinesWithRegistryKeys) + "/" \
	+ str(totalLinesScanned) + " lines had registry keys...\n"
    resultsFileObject.write(tempFileLine)
    tempFileLine = ""
    tempFileLine = "Total Lines Scanned:"+str(totalLinesScanned)
    resultsFileObject.write(tempFileLine)
if foundRegistryKeys == False:
	resultsFileObject.write("No registry keys were found within the specimin file...")

#Close file object once file is written
resultsFileObject.close()

#Move report file to Scan Report Files directory
sourceDirectory = "C:\Users\Richard\Desktop\HayStack\\" + resultsFileName
destinationDirectory = "C:\Users\Richard\Desktop\HayStack\Scan Report Files\Registry key Scans\\" + resultsFileName
shutil.move(sourceDirectory, destinationDirectory)
