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
            <td><img src="./images/trash-solid.svg" class="icon"></td>`;
        let tBody = document.querySelector('.lista__table__tbody');
        tBody.appendChild(item);

        let icTrash = document.querySelector(".icon");

    } catch (error) {
        console.log("Erro ao inserir na lista: " + error);
    }
});



