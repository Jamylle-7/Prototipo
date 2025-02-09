window.addEventListener('load', function(){
    var atalhoMenu = document.querySelectorAll('header a')
    var elScroll
    var elOff
    var att

    for(var i = 0; i < atalhoMenu.length; i++){
        atalhoMenu[i].addEventListener('click', function(e){
            e.preventDefault()
            att = this.getAttribute("section")
            if(att == "header"){
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                })
            }else{
                elScroll = document.querySelector('.' + att)
                elOff = elScroll.offsetTop;
                window.scrollTo({
                    top: elOff,
                    behavior: 'smooth'
                })
            }

            document.body.click()
        })
    }
})
