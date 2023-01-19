function load(){
    let inputText = document.getElementById("usuario_input");
    let nomeUsuario = inputText.value;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var objetoResposta = JSON.parse(this.response);
            document.getElementById("usuario_git").innerHTML = objetoResposta.login;
            document.getElementById("foto_git").setAttribute("src", objetoResposta.avatar_url);
        }
    }
    xhttp.open("GET", `https://api.github.com/users/${nomeUsuario}`);
    xhttp.send();
}
