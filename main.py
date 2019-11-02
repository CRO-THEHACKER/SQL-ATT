#!/usr/bin/python3

import requests, urllib2, os, sys

website = "google.com"
port = "80"
URL = "/index.html"
webforminputu = "USERNAME"
webforminputp = "PASSWORD"
TRYSQLI = "=,='"

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'
       

# menus
print( color.HEADER + """
   _____ ____    __         ___  ____________
  / ___// __ \  / /        /   |/_  __/_  __/
  \__ \/ / / / / /  ______/ /| | / /   / /   
 ___/ / /_/ / / /__/_____/ ___ |/ /   / /    
/____/\___\_\/_____/    /_/  |_/_/   /_/         
                      version: 1.5
""" + color.END)
    
print( color.RED + """

Setting HTTPS protocall; use 443 for SSL""" + color.END + """
Commands to use: 

 - """ + color.NOTICE + """HELP, SET, SHOW OPTIONS, CLEARALL, CLEAR, RUN, EXIT""" + color.END + """

Website:        {}
Web input user: {}
Web input pass: {}
Port:           {}
URL:            {}

""".format(website, webforminputu, webforminputp, port, URL))

# testing for SQLi-J for U+P
def RUN():
    print("Checking if website {} is online... ".format(website))
    os.system('ping {} -c 4 -s 150'.format(website))
    print("\n\nTesting for form input '{},{}' from website: {}(:{}){} | trying: {}".format(webforminputu, webforminputp, website, port, URL, TRYSQLI))

# end

while True:
    command = raw_input("SQL-ATT$> ")
    if command == "":
        pass
    elif command == " ":
        pass
    elif command == "RUN":
        RUN()
    elif command == "SET website":
        website = input("SQL-ATT:/website$> ")
    elif command == "EXIT":
        break
        sys.exit(1)
    else:
        print(color.LOGGING + "SORRY!" + color.END + " Command not found!")
