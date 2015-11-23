import urllib.request
from urllib.error import HTTPError
import json

HOST = "http://hemochro.me"

def parseResponse(data):
    strData = data.decode('ascii')
    jsonData = json.loads(strData)
    if jsonData['status'] == 'error':
        raise HTTPError(fullUrl, 400, jsonData['data'], None, None)
    return jsonData['data']

def shorten(url, host=HOST):
    "Takes a url and returns a shortened."
    #Request shortened url
    fullUrl = host + "/shorten/json?url=" + url
    request = urllib.request.Request(fullUrl, method='PUT')
    response = urllib.request.urlopen(request)
    #Parse the answer
    data = response.read()
    return parseResponse(data)

def expand(urlId, host=HOST):
    "Takes the ID of a shortened url and retrieves the original."
    #Request shortened url
    fullUrl = host + "/expand/json/" + urlId
    request = urllib.request.Request(fullUrl, method='GET')
    response = urllib.request.urlopen(request)
    #Parse the answer
    data = response.read()
    return parseResponse(data)
    
if __name__ == "__main__":
    import sys
    args = sys.argv
    
    
    if len(args) == 2 and args[1] == "help":
        print("To shorten a url use -shorten url.\nTo expand a url use -expand id.")
        exit(0)

    if len(args) == 3:
        if args[1] == "-shorten":
            print(shorten(args[2]))
            exit(0)
        if args[1] == "-expand":
            print(expand(args[2]))
            exit(0)

    print("Incorrect arguments. Use queerlink help for usage information.")
    exit(1)
