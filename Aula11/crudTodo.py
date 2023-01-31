from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, unique=True, nullable=False)



contactsDB = db.Table(
    "contacts",
    db.Column("user_id", db.ForeignKey(User.id), primary_key=True),
    db.Column("user_name", db.ForeignKey(User.name), primary_key=True),
    db.Column("user_phone", db.ForeignKey(User.phone), primary_key=True),
)


@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.name)).scalars()
    return render_template("contact.html", users=users)




contacts = [{'id': 1, 'name': 'John Doe',  'phone': '555-555-5555'},
            {'id': 2, 'name': 'Alice Silva',  'phone': '222-225-2222'} ]

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

# GET request to retrieve all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts(): 
    if not contacts:
        return jsonify({'message':'No contacts founded in server'}), 404
    return jsonify({'contacts': contacts}), 200

# GET request to retrieve one contacts
@app.route('/contacts/<int:id>', methods=['get'])
def get_contact(id):
    for contact in contacts:
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
    id = 1
    if len(contacts) > 0:
        id = contacts[-1]['id']+1
    c = {'id':id,'name':data['name'],'phone':data['phone']}
    contacts.append(c)

    #user = User(
    #    name = data['name'],
    #    phone = data['phone'],
    #)
    #db.session.add(user)
    #db.session.commit()

    return jsonify({'contact': c}), 201

# PUT request to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    if not request.is_json:
        return jsonify({'message':'body is not a json'}), 415
    data = request.get_json()
    if not data or not all(key in data for key in ('name','phone')):
        return jsonify({'message':'bad request'}), 400
    for i,contact in enumerate(contacts):
        if contact['id'] == id:
            contacts[i] = {'id':id, 'name':data['name'],'phone':data['phone']}    
            return jsonify({'contact': contacts[i]}),200
    return jsonify({'message':'contact not found'}), 404

# DELETE request to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    for i,contact in enumerate(contacts):
        if contact['id'] == id:
            del contacts[i]   
            return jsonify({'message': 'contact deleted'}),200
    return jsonify({'message':'contact not found'}), 404
    
with app.app_context():
    db.create_all()

app.run(debug=True)
