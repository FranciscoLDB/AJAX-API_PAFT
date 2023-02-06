from flask import Flask, jsonify, request, render_template, Response, json
app = Flask(__name__)

contacts = [{'id': 1, 'name': 'John Doe', 'phone': '555-555-5555'},
            {'id': 2, 'name': 'Pedro Junior', 'phone': '123-123-1234'}]

@app.route('/',methods=['GET'])
def date():
    return render_template('index.html')

# GET request to retrieve all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    #arq = open('contacts.json')
    #data = json.load(arq)
    #contactsJson = data['contacts']
    #arq.close()
    return jsonify({"contacts": contacts}), 200

# GET request to retrieve one contacts
@app.route('/contacts/<int:id>', methods=['get'])
def get_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            return {'contact': contact}

    return Response("400-BAD REQUEST - ID not find", status = 400)

def write_json(new_data, filename='contacts.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["contacts"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

# POST request to add a new contact with data of the new contact on a json file
@app.route('/contacts', methods=['POST'])
def add_contact():
    if request.is_json:
        data = request.get_json()
        if not all(key in data for key in('name', 'phone')):
            return jsonify({'message': 'bad request'}), 400

        contactNew = {
            'id': contacts[-1]['id'] + 1,
            'name': data['name'],
            'phone': data['phone']
        }
        #write_json(contactNew)
        contacts.append(contactNew)
        return jsonify({'contact': contactNew}), 201
        
    return jsonify({'message': 'body is not a json'}), 415

def upload_json(index, data):
    filename = 'contacts.json'
    with open(filename,'r+') as file:
        file_data = json.load(file)
        if 'name' in data:    
            file_data["contacts"][index]['name'] = data['name']
        if 'phone' in data:
            file_data["contacts"][index]['phone'] = data['phone']
        file.seek(0)
        json.dump(file_data, file, indent = 4)

# PUT request to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    if request.is_json and ('name' in request.json or 'phone' in request.json):
        cont = 0
        for contact in contacts:
            if contact['id'] == id:
                data = {}
                if 'name' in request.json:
                    contact['name'] = request.json['name']
                    data['name'] = request.json['name']
                if 'phone' in request.json:
                    contact['phone'] = request.json['phone']
                    data['phone'] = request.json['phone']

                #upload_json(cont, data)

                return {'contact': contact}

            cont = cont + 1

        return Response("400-BAD REQUEST - ID não localizado",status = 400)

    return Response("400-BAD REQUEST - Input error",status = 400)

# DELETE request to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    for i in range(len(contacts)):
        if contacts[i]['id'] == id:
            del contacts[i]
            return {'message': 'Usuario removido com sucesso'}

    return Response("400-BAD REQUEST - ID não localizado",status = 400)


app.run(debug=True)
