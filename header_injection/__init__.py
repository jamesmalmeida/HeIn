from fastapi import FastAPI, Request, Response
import requests

def TestInjection(key,value):
    address = 'http://127.0.0.1:8000/keyvalue/' + key + '/' + value #Composing the address
    req = requests.get(address) #Perform the request, storing to the variable req
    return req.headers #Print the headers from req

def HeaderInjection(app):
    @app.get("/keyvalue/{newkey}/{newvalue}")   #Pass the key and value as http://localhost:8000/keyvalue/KEY/VALUE, where KEY is the desired key, and VALUE is the desired value.
    def read_item(newkey: str, newvalue: str, response: Response):
        response.headers[newkey] = newvalue #Inserting the key in the header
        storednewvalue = response.headers.get(newkey) #Just geeting the value of the new key from the headers to test the code
        return {newkey: storednewvalue} #Return the newkey and the value got from the header
