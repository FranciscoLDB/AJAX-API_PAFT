function load(){    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var objetoResposta = JSON.parse(this.response);
            document.getElementById("foto_pato").setAttribute("src", objetoResposta.image);
        }
    }
    xhttp.open("GET", `https://randomfox.ca/floof/`);
    xhttp.send();
}
