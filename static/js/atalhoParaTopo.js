alert('testsetest)



window.addEventListener('load', function(){
    var atalhoTopo = document.querySelector('.atalho-topo')
    var topo

    window.onscroll = function(){
        topo = window.scrollY
        if (topo >= 400){
            atalhoTopo.style.display = "block"
        }else{
            atalhoTopo.style.display = "none"
        }
    }

    atalhoTopo.onclick = function(){
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        })
    }
})window.addEventListener('load', function(){
    var atalhoTopo = document.querySelector('.atalho-topo')
    var topo

    window.onscroll = function(){
        topo = window.scrollY
        if (topo >= 400){
            atalhoTopo.style.display = "block"
        }else{
            atalhoTopo.style.display = "none"
        }
  }

    atalhoTopo.onclick = function(){
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        })
    }
}