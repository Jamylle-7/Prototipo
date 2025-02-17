function cadastrou() {
    var idade = document.getElementById("idade").value;
    var altura = document.getElementById("altura").value;
    var peso = document.getElementById("peso").value;
    var genero = document.getElementById("genero").value;


    if (idade && altura && peso && genero) {
        if (dadosJaCadastrados(idade, altura, peso, genero)) {
            alert("Você já cadastrou seus dados de saúde.");
        } else {
            alert("Dados cadastrados com sucesso");
        }
    } else {
        alert("Por favor, preencha todos os campos.");
    }
}


function recuperar_dados_user(idade, altura, peso, genero) {
    return false;
}
