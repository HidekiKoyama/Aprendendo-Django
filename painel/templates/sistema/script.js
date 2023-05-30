function botao_open_menu(){
    var element = document.getElementById("ul-menu");
    element.classList.toggle("on-menu");
    var element_icon = document.getElementById("button-defull-menu");
    element_icon.classList.toggle("button-on")
}
function botao_open_dash(){
    var element = document.getElementById("ul-dashboard");
    element.classList.toggle("on-menu");
    var element_icon = document.getElementById("button-defull-dashboard");
    element_icon.classList.toggle("button-on")
}
function botao_open_configuracao(){
    var element = document.getElementById("ul-configuracao");
    element.classList.toggle("on-menu");
    var element_icon = document.getElementById("button-defull-configuracao");
    element_icon.classList.toggle("button-on")  
}

