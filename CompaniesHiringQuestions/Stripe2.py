__author__ = "deepika"

import json
import requests

user_mapping = dict()
def read_file(filename):
    with open(filename) as json_file:
        return json.load(json_file)

def process_request(requests_data):
    cus_id = None
    ch_id = None

    for request_charges in requests_data:
        request_charge = request_charges["request"]
        if cus_id is not None and ch_id is not None:
            print "reaching here"
            #for (k, v) in request_charge.items():
            #    v.replace("ch_27U5scLw6ytdrHzio6iksSLE", ch_id)
            #request_charge.replace("ch_27U5scLw6ytdrHzio6iksSLE", id)
        response_charge = request_charges["response"]
        headers = request_charge["headers"]
        url = "https://api.stripe.com" + request_charge["url"]
        r = requests.post(url, data=request_charge["body"], headers=headers)
        assert r.status_code == response_charge["code"]
        if r.status_code == 200:
        
            print "Trying to fetch id: ", response_charge["body"]
            json_object = json.JSONDecoder().decode(response_charge["body"])
            id = json_object["id"]
            if "cus_" in id:
                cus_id = id
            elif "ch_" in id:
                ch_id = id




    print "Passed"

request_charges_data = read_file("requestlog-charges.json")
data_customer_charges = read_file("requestlog-customer-charges.json")

#process_request(request_charges_data)
#print "Processed: ", "requestlog-charges.json"
process_request(data_customer_charges)
