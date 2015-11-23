import urllib.request
from urllib.error import HTTPError
import json

HOST = "http://hemochro.me"

def shorten(url, host=HOST):
    "Takes an url and returns a shortened."
    #Request shortened url
    fullUrl = host + "/shorten/json?url=" + url
    request = urllib.request.Request(fullUrl, method='PUT')
    result = urllib.request.urlopen(request)
    #Parse the answer
    if result.status == 200:
        binData = result.read()
        strData = binData.decode('ascii')
        jsonData = json.loads(strData)
        if jsonData['status'] == 'error':
            raise HTTPError(fullUrl, 400, jsonData['data'], None, None)
        return jsonData['data']

def expand(urlId, host=HOST):
    "Takes the ID of a shortened url and retrieves the original."
    #Request shortened url
    fullUrl = host + "/expand/json/" + urlId
    request = urllib.request.Request(fullUrl, method='GET')
    result = urllib.request.urlopen(request)
    #Parse the answer
    if result.status == 200:
        binData = result.read()
        strData = binData.decode('ascii')
        jsonData = json.loads(strData)
        if jsonData['status'] == 'error':
            raise HTTPError(fullUrl, 400, jsonData['data'], None, None)
        return jsonData['data']
    
