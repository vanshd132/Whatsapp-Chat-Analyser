import re
import pandas as pd

def startWithDateAndTimeAndroid(s):
    pattern = r'^(\d{1,2}/\d{1,2}/\d{1,2}), (\d{1,2}:\d{2})[ ]?(AM|PM|am|pm)? -'
    result = re.match(pattern, s)
    return bool(result)

def FindAuthor(s):
    s = s.split(":")
    return len(s) == 2

def getDataPointAndroid(line):
    splitLine = line.split(' - ')
    dateTime, message = splitLine[0], ' '.join(splitLine[1:])
    
    date, time = None, None
    if ',' in dateTime:
        date_time_components = dateTime.split(', ')
        if len(date_time_components) == 2:
            date, time = date_time_components
            
    author = None
    if FindAuthor(message):
        splitMessage = message.split(':')
        author = splitMessage[0]
        message = ' '.join(splitMessage[1:])
    
    return date, time, author, message
