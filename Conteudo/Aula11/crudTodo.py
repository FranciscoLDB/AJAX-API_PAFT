from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=True)
    phone = db.Column(db.String(20), nullable=True)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def dict(self):
        return {"id": self.id, "name": self.name, "phone": self.phone}

with app.app_context():
    db.create_all()    

contactsList = [{'id': 1, 'name': 'John Doe',  'phone': '555-555-5555'},
            {'id': 2, 'name': 'Alice Silva',  'phone': '222-225-2222'} ]

@app.route('/contact.html')
def contact():
    contacts = Contact.query.all()
    return render_template('contact.html', contact=contacts)

# GET request to retrieve all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts(): 
    contacts = Contact.query.all()
    return jsonify({'contacts': [contact.as_dict() for contact in contacts]}), 200

# GET request to retrieve one contacts
@app.route('/contacts/<int:id>', methods=['get'])
def get_contact(id):
    for contact in contactsList:
        if id == contact['id']:
            return jsonify({'contact': contact}),200
    return jsonify({'message':'contact not found'}), 404

# POST request to add a new contact with data of the new contact on a json file
@app.route('/contacts', methods=['POST'])
def add_contact():
    if not request.is_json:
        return jsonify({'message':'body is not a json'}), 415
    data = request.get_json()
    if not data or not all(key in data for key in ('name','phone')):
        return jsonify({'message':'bad request'}), 400
    

    contact = Contact(
        name = data['name'],
        phone = data['phone'],
    )
    db.session.add(contact)
    db.session.commit()

    return jsonify({'contact': contact.as_dict()}), 201

# PUT request to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    if not request.is_json:
        return jsonify({'message':'body is not a json'}), 415
    data = request.get_json()
    if not data or not all(key in data for key in ('name','phone')):
        return jsonify({'message':'bad request'}), 400
    for i,contact in enumerate(contactsList):
        if contact['id'] == id:
            contactsList[i] = {'id':id, 'name':data['name'],'phone':data['phone']}    
            return jsonify({'contact': contactsList[i]}),200

    db.session.add(contact)
    db.session.commit()
    
    return jsonify({'message':'contact not found'}), 404

# DELETE request to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    try:
        contact = Contact.query.get_or_404(id)
        db.session.delete(contact)
        db.session.commit()        
        return jsonify({'message':'contact deleted'}), 200
    finally:
        return jsonify({'message':'contact not found'}), 400

    
if __name__ == '__main__':
    app.run(debug=True)
