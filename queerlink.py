import urllib.request
from urllib.error import HTTPError
import json

HOST = "http://hemochro.me"

def fetchAndParse(request):
    response = urllib.request.urlopen(request)   
    data = response.read()
    strData = data.decode('ascii')
    jsonData = json.loads(strData)
    if jsonData['status'] == 'error':
        raise HTTPError(request.get_full_url(), 400, jsonData['data'], None, None)
    return jsonData['data']

def shorten(url, host=HOST):
    "Takes a url and returns a shortened url."
    #Request shortened url
    fullUrl = host + "/shorten/json?url=" + url
    request = urllib.request.Request(fullUrl, method='PUT')
    return fetchAndParse(request)

def expand(urlId, host=HOST):
    "Takes the ID of a shortened url and retrieves the original."
    #Request shortened url
    fullUrl = host + "/expand/json/" + urlId
    request = urllib.request.Request(fullUrl, method='GET')
    return fetchAndParse(request)
    
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
