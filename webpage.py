from flask import Flask, render_template
My_app_name = Flask(__name__) 

import requests

url = "https://priceline-com-provider.p.rapidapi.com/v1/flights/search"

querystring = {"sort_order":"PRICE","location_departure":"SFO","date_departure":"2021-12-01","class_type":"ECO","location_arrival":"LAX","itinerary_type":"ONE_WAY","price_max":"400","date_departure_return":"2021-12-07","duration_max":"2051","price_min":"100","number_of_passengers":"1"}

headers = {
    'x-rapidapi-host': "priceline-com-provider.p.rapidapi.com",
    'x-rapidapi-key': "65883da924msh6ba88bc3488610ep1b9f8fjsn4f24748cac6e"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

res_json = response.json()
#print(res_json)

responses = [] 

for r in res_json['segment']:
    if r['origAirport'] == 'SFO' and r['destAirport'] == 'LAX':
        responses.append('Flight ' + r['flightNumber'] + ' from ' + r['origAirport'] + ' to ' + r['destAirport'] + ' leaving: ' + r['departDateTime'] + ' arriving: ' + r['arrivalDateTime'])
  
print(responses)  
print(len(responses))

@My_app_name.route('/') 

def homE_pagE():  
    return render_template("index.html", len = len(responses), responses = responses) 
  
if __name__ == '__main__':
    My_app_name.run(use_reloader = True, debug = True)