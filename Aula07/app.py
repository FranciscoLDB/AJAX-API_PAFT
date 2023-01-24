from flask import Flask, jsonify, request, render_template, Response
app = Flask(__name__)

contacts = [{'id': 1, 'name': 'John Doe', 'phone': '555-555-5555'},
            {'id': 2, 'name': 'Pedro Junior', 'phone': '123-123-1234'}]

@app.route('/',methods=['GET'])
def date():
    return render_template('index.html')

# GET request to retrieve all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    return {'contacts': contacts}

# GET request to retrieve one contacts
@app.route('/contacts/<int:id>', methods=['get'])
def get_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            return {'contact': contact}

    return Response("400-BAD REQUEST - ID not find", status = 400)

# POST request to add a new contact with data of the new contact on a json file
@app.route('/contacts', methods=['POST'])
def add_contact():
    #id is created here 
    if request.is_json and 'name' in request.json and 'phone' in request.json:
        id = len(contacts) + 1
        contactNew = {
            'id': id,
            'name': request.json['name'],
            'phone': request.json['phone']
        }
        for contact in contacts:
            if contactNew['name'] == contact['name']:
                return Response("400-BAD REQUEST - Usuario já cadastrado", status = 400)
        
        contacts.append(contactNew)

        return {'contact': contactNew}

    return Response("400-BAD REQUEST - Error on input",status = 400)


# PUT request to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    if request.is_json and ('name' in request.json or 'phone' in request.json):
        for contact in contacts:
            if contact['id'] == id:
                if 'name' in request.json:
                    contact['name'] = request.json['name']
                if 'phone' in request.json:
                    contact['phone'] = request.json['phone']

                return {'contact': contact}

        return Response("400-BAD REQUEST - ID não localizado",status = 400)

    return Response("400-BAD REQUEST - Input error",status = 400)

# DELETE request to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    return {'message': ''}


app.run(debug=True)
