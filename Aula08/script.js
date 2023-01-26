function loadContatos(){
    let tBody = document.querySelector('.table__tbody');
    tBody.innerHTML = "";
    fetch('http://127.0.0.1:5000/contacts', {
        method: "GET"
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
        });
}
console.log('Gello')

function atualizaLista(){
    let tBody = document.querySelector('.lista__table__tbody');
    tBody.innerHTML = "";
    for (const key in listaProdutos) {
        let item = document.createElement('tr');
        item.id = `item${key}`;
        item.innerHTML = 
            `<td><input type="checkbox"></td>
            <th>${listaProdutos[key].nome}</th>
            <th>${listaProdutos[key].quantidade} ${listaProdutos[key].tipo}</th>
            <td><img src="./images/trash-solid.svg" class="icon__trash" id="trash${key}"></td>`;
        tBody.appendChild(item);
    
        let iconExcluir = document.querySelector(`#trash${key}`);
        iconExcluir.addEventListener('click', () => {
            try {
                console.log("Removendo item " + key + " da lista");
                listaProdutos.splice(listaProdutos.indexOf(listaProdutos[key]), 1);
                console.log("listaProdutos: " + listaProdutos);
                atualizaLista();
            } catch (error) {
                console.log("Erro remover item da lista: " + error);
            }
        });   
    }
}
atualizaLista();