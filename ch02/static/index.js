let ddong = 0;
counter = document.getElementById("counter")
cbutton = document.getElementById("cbutton")
cbutton.addEventListener("click", () => {
    ddong++;
    console.log(ddong)
    counter.innerText = ddong;
})