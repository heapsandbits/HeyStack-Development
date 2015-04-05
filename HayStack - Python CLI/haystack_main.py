#Program: HayStack - Main Application
#Developer: Rich Hoggan (GhostBit Cyber Assurance)
#Creation Date: 12-02-2013
#Description: Scans suspected malware files for strings and registry keys.

###Import Directives###
import subprocess

###Function Code###
#Function Name: printProgramInformation
#Function Description: Print's the program's initial information.
def printProgramInformation():
    print "HayStack"
    print "Developed By: Rich Hoggan"
    print "C2013 GhostBit Cyber Assurance"
    print ""
	
#Function Name: printMainMenu()
#Function Description: Prints the program's main menu.
def printMainMenu():
	print "Main Menu:"
	print "String Scan"
	print "Registry Scan"
	print "Function Scan"
	print "URL Scan"
	print "Quit"
	
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
#Variable declarations
selection = ""

printProgramInformation()

while selection != "quit":
	printMainMenu()
	
	#Get input from user - selection
	print ""
	selection = raw_input("Selection: ")
	if selection != "string scan" and selection != "registry scan" and selection != "function scan" \
		and selection != "url scan" and selection != "quit":
		printErrorMessage("INVALID_MENU_OPTION")
		while selection != "string scan" and selection != "registry scan" and selection != "function scan" \
			and selection != "url scan" and selection != "quit":
			#Get input from user - selection
			selection = raw_input("Selection: ")
	
	#Determine user selection
	if selection == "string scan":
		subprocess.call("python haystack_string_scan.py")
		print ""
	elif selection == "registry scan":
		subprocess.call("python haystack_registry_scan.py")
		print ""
	elif selection == "function scan":
		subprocess.call("python haystack_function_scan.py")
		print ""
	elif selection == "url scan":
		subprocess.call("python haystack_url_scan.py")
		print ""
	elif selection == "quit":
		print "Program exited successfully..."
