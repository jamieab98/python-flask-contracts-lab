#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

@app.route('/contract/<int:id>')
def contractorinfo(id):
    if id in [contract['id'] for contract in contracts]:
        status = 200
        contract = [contract for contract in contracts if contract["id"] == id][0]
        response = f'{contract["contract_information"]}'
        return make_response(response, status)
    else:
        status = 404
        response = 'Contract not found'
        return make_response(response, status)

@app.route('/customer/<string:customer_name>')
def customername(customer_name):
    if customer_name in customers:
        status = 204
        response = ''
        return make_response(response, status)
    else:
        status = 404
        response = 'Customer not found'
        return make_response(response, status)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

