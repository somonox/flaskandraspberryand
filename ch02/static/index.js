let ddong = 0;
counter = document.getElementById("counter")
cbutton = document.getElementById("cbutton")
sbutton = document.getElementById("sbutton")
cbutton.addEventListener("click", () => {
    ddong++;
    console.log(ddong)
    counter.innerText = ddong;
})

sbutton.addEventListener("click", function() {
    location.href='http://0.0.0.0:5050/'+ ddong;
    counter.innerText= 0;
    ddong = 0;
})