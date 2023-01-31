window.addEventListener('DOMContentLoaded', (event) => {
    console.log("page loaded ");
    document.getElementById("expAll").addEventListener("click", ExpAll);



});


function ExpAll(){
    console.log("This worked!")
    var x, i;
    x = document.querySelectorAll("details");

    for (i = 0; i < x.length; i++) {
        x[i].open = false;
    }
}