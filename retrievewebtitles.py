# ****************************************************************************************************************************************************************
# Batch Retrieve Web Titles From URLs
# 
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# The code that gets the Web page titles is based on code from:
# 
# Extract the title from a webpage using the python 3 standard lib - Code Review Stack Exchange
# https://codereview.stackexchange.com/questions/183160/extract-the-title-from-a-webpage-using-the-python-3-standard-lib

#!/usr/bin/python3

#-*-coding:utf8;-*-
#qpy:3
#qpy:console
# ^^^ NO IDEA WHAT THESE 3 LINES ARE?? 

import os
import re
import urllib
from urllib.request import urlopen  
from html.parser import HTMLParser
from pathlib import Path

from urllib.request import Request 
from urllib.error import URLError, HTTPError

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Time out process code from: 
# Python 101: How to timeout a subprocess | The Mouse Vs. The Python
# https://www.blog.pythonlibrary.org/2016/05/17/python-101-how-to-timeout-a-subprocess/

import subprocess

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Continuation of code from 
# Extract the title from a webpage using the python 3 standard lib - Code Review Stack Exchange
# https://codereview.stackexchange.com/questions/183160/extract-the-title-from-a-webpage-using-the-python-3-standard-lib

def error_callback(*_, **__):
    pass

def is_string(data):
    return isinstance(data, str)

def is_bytes(data):
    return isinstance(data, bytes)

def to_ascii(data):
    if is_string(data):
        try:
            data = data.encode('ascii', errors='ignore')
        except:
            try:
                data = str(data).encode('ascii', errors='ignore')
            except:
                try:
                    data = str(data)
                except:
                    data = "(could not encode data string)"
    elif is_bytes(data):
        try:
            data = data.decode('ascii', errors='ignore')
        except:
            try:
                data = str(data).encode('ascii', errors='ignore')
            except:
                try:
                    data = str(data)
                except:
                    data = "(could not encode data bytes)"
    else:
        try:
            data = str(data).encode('ascii', errors='ignore')
        except:
            data = "(could not encode data)"

    return data

class Parser(HTMLParser):

    def __init__(self, url):
        self.title = None
        self.rec = False

        HTMLParser.__init__(self)

        try:
            # Added urlopen Timeout parameter so script doesn't freeze up:
            #self.feed(to_ascii(urlopen(url).read()))
            self.feed(to_ascii(urlopen(url, None, 5).read()))
        except Exception as err:
            # Not sure if I am handling exception right, script sometimes dies here:
            try:
                self.feed(str(err))
            except:
                self.feed("(unknown error in urlopen)")

        self.rec = False
        self.error = error_callback

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.rec = True

    def handle_data(self, data):
        if self.rec:
            self.title = data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.rec = False

def get_title(url):
    try:
        return Parser(url).title
    except:
        return "(unknown error in Parser)"


def fileLen(sFilePath):
    try:
        num_lines = sum(1 for line in open(sFilePath))
    except UnicodeDecodeError as ude:
        try:
            num_lines = sum(1 for line in open(sFilePath, encoding="utf8"))
        except:
            num_lines = -1
    return num_lines

def getFileEncoding(sFilePath):
    sType = ""
    try:
        sType = "ascii"
        num_lines = sum(1 for line in open(sFilePath))
    except UnicodeDecodeError as ude:
        try:
            sType = "utf8"
            num_lines = sum(1 for line in open(sFilePath, encoding="utf8"))
        except:
            sType = "other"
            num_lines = -1
    return sType

def getTitles(sInputFile, sStatus):
    sResult = ""
    iLineNum = 0
    iCount = 0
    iTitle = 0
    iNull = 0
    iTimeouts = 0

    if Path(sInputFile).is_file():
        sInputFile = str(sInputFile)
        sOutputFile = sInputFile.replace(".txt", ".out.txt")

        iLineCount = fileLen(sInputFile)
        print("File \"" + sInputFile + "\" has " + str(iLineCount) + " lines.")
        #print("File \"" + sInputFile + "\":")

        sEncoding = getFileEncoding(sInputFile)
        if (sEncoding == "ascii"):
            print("File encoding = ASCII")
            #fIn = open("url.txt", "r")
            fIn = open(sInputFile, "r")
        elif (sEncoding == "utf8"):
            print("File encoding = UTF8")
            fIn = open(sInputFile, "r", encoding="utf8")
        else:
            print("*** File encoding unknown ***")

        fOut = open(sOutputFile,"w+", encoding="utf-8")

        fLines = fIn.readlines()
        for sLine in fLines:
            iLineNum += 1

            sLine = str(sLine)
            sLine = repr(sLine)

            #print(get_title('http://www.google.com'))

            #fOut.write("This is line %d\r\n" % (i+1))
            #fOut.write(get_title('http://www.google.com') + "\r\n")
            sLine = sLine.lstrip('\'')
            sLine = sLine.rstrip('\'')

            sLine = sLine.strip('\\n')
            sLine = sLine.strip('\\r')
            sLine = sLine.strip('\\n')

            if sLine != "":
                iCount += 1
                sTitle = get_title(sLine)
                if sTitle is None:
                    iNull += 1
                    sTitle = ''
                else:
                    iTitle += 1

                # If title is blank then just use the URL as the description for now.
                if str(sTitle)=="":
                    sTitle = sLine

                sTitle = sTitle.replace('\n', ' ').replace('\r', ' ')
                sTitle = re.sub('\s+', ' ', sTitle).strip()

                print(sStatus + "Line " + str(iLineNum) + " of " + str(iLineCount))
                #print(str(iLineNum) + " of " + str(iLineCount) + ": " + sLine + '\t' + sTitle)
                #print(sLine + '\t' + sTitle)

                ##print(sLine)
                ##print(sTitle)
                #print("")

                ##fOut.write(get_title(sLine) + "\r\n")

                #fOut.write(sLine + '\t' + sTitle + '\r\n')
                fOut.write(sLine + '\t' + sTitle + '\n')
            else:
                print (str(iLineNum) + " of " + str(iLineCount) + ": (Skipping blank line.)")
                #print("(Skipping blank line.)")
        fIn.close()
        fOut.close()

        sResult = "Retrieved " + str(iTitle) + " titles, " + str(iNull) + " empty, " + str(iTimeouts) + " timeouts, " + "from \"" + sInputFile + "\", output to \"" + sOutputFile + "\"."
    else:
        sResult = "File \"" + sInputFile + "\" not found."

    return sResult

    # END getTitles

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def main():

    script_dir = os.path.dirname(__file__) # <-- absolute dir the script is in
    sSubfolder = "url"

    # For now just add file names here hardcoded:
    # TODO: automatically process all *.txt files in "url" folder that don't end in ".out.txt"
    arrList = []
    arrList.append("links1.txt")
    arrList.append("links2.txt")
    arrList.append("links3.txt")

    iCount = 0
    sTotal = str(len(arrList))
    for sInputFile in arrList:
        iCount += 1
        sStatus = "File " + str(iCount) + " of " + sTotal + ", "

        # Get filename with full path, and fix forward/back slashes in path
        # (I am on Windows so some parts have backslashes and not others):
        sInputFile = str(Path(os.path.join(script_dir, sSubfolder, sInputFile)))
        #print(str(iCount) + ". " + sInputFile)

        # Get the web titles for all the urls in the file:
        sResult = getTitles(sInputFile, sStatus)

        # Ouptut summary of results for the current file:
        print(str(iCount) + ". " + sResult)

        # Test output fileLen:
        #print("    fileLen: " + str(fileLen(sInputFile)) )

    print("Done.")


if __name__== "__main__":
    main()