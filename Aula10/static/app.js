function createContact(){
    console.log("create");
    let name = document.getElementById("name").value;
    let phone = document.getElementById("phone").value;
    axios.post('http://127.0.0.1:5000/contacts',{name , phone})
    .then(response => {
        console.log(response);
        location.reload();
    })
    .catch(error => console.log(error));

}
function deleteContact(id){
    axios.delete(`http://127.0.0.1:5000/contacts/${id}`)
    .then(response =>{
        console.log(response);
        location.reload();
    }).catch(error => console.log(error));
}
function updateContact(id){
    const name = prompt("Insert the new name");
    const phone = prompt("Insert the new phone");

    axios.put(`http://127.0.0.1:5000/contacts/${id}`,{name , phone})
    .then(response =>{
        console.log(response);
        location.reload();
    }).catch(error => console.log(error));
}
axios.get('http://127.0.0.1:5000/contacts')
.then(response => {
    
    let data = response.data;
    let tbody = document.getElementById("contacts-table-body");
    for(let contact of data.contacts){
        console.log(contact);
        let row = tbody.insertRow();
        let idCell = row.insertCell();
        idCell.innerHTML = contact.id;
        let nameCell = row.insertCell();
        nameCell.innerHTML = contact.name;
        let phoneCell = row.insertCell();
        phoneCell.innerHTML = contact.phone;
        let actionsCell = row.insertCell();
        actionsCell.innerHTML = `<button type="button" onclick="updateContact(${contact.id})">Update</button><button type="button" onclick="deleteContact(${contact.id})">Delete</button>`;
    }
})
.catch(error => console.log(error));