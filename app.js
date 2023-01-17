const listaProdutos = [
    {
        nome: "Coxinha",
        quantidade: 15,
        tipo: "Un."
    }, {
        nome: "Carne",
        quantidade: 20,
        tipo: "Kg"
    }
]

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

let btAdd = document.getElementById('form__button');
btAdd.addEventListener('click', () => {
    try {
        let nomeP = document.querySelector("#nomeProduto");
        let quantP = document.querySelector("#quantidadeProduto");
        let tipoP = document.querySelector("#tipoProduto");
        let medida = tipoP.value == "peso" ? "Kg": "Un.";

        let item = document.createElement('tr');
        item.innerHTML = 
            `<td><input type="checkbox"></td>
            <th>${nomeP.value}</th>
            <th>${quantP.value} ${medida}</th>
            <td><img src="./images/trash-solid.svg" class="icon__trash" id="trash${listaProdutos.length}"></td>`;
        let tBody = document.querySelector('.lista__table__tbody');
        tBody.appendChild(item);        

        let iconExcluir = document.querySelector(`#trash${listaProdutos.length}`);
        iconExcluir.addEventListener('click', () => {
            try {
                console.log("Removendo item " + listaProdutos.length + " da lista");
                listaProdutos.pop(listaProdutos[listaProdutos.length]);
                console.log("listaProdutos: " + listaProdutos);
                atualizaLista();
            } catch (error) {
                console.log("Erro remover item da lista: " + error);
            }
        });

        listaProdutos.push({nome: nomeP.value, quantidade: quantP.value, tipo: medida});
        console.log("listaProdutos: " + listaProdutos);
    } catch (error) {
        console.log("Erro ao inserir na lista: " + error);
    }
});
