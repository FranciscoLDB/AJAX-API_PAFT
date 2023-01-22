function loadDatas(){
    let datai = document.getElementById('data_inicio');
    let dataf = document.getElementById('data_fim');

    fetch(`http://127.0.0.1:5000/data/${datai.value}/${dataf.value}`, {
        method: "GET",
        headers: {"Access-Control-Allow-Origin": "*"}
    })
        .then((response) => response.json())
        .then((data) => {
            document.getElementById('dif_dias').innerText = data.diferencaDias + " dia(s)";
            document.getElementById('dif_sem').innerText = data.diferencaSemanas + " semana(s)";
            document.getElementById('dif_mes').innerText = data.diferencaMeses + " mes(ses)";
            console.log(data);
        });
}

function loadNumeros(){
    let input = document.getElementById('input_num');
    
    fetch(`http://127.0.0.1:5000/numeros/${input.value}`)
        .then((response) => response.json())
        .then((data) => {
            document.getElementById('ordem_cresce').innerText = data.ordemCrescente;
            document.getElementById('ordem_decresce').innerText = data.ordemDecrescente;
            document.getElementById('num_par').innerText = data.numerosPares;
            console.log(data);
        });
}