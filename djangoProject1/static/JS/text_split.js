
function split(data){
    const my_ingr= data.split(',');     //array of ingredience
    const dumper = document.getElementById("dumper");
    for (let ingr of my_ingr) {
        let vessel = document.createElement("li");
        let checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        vessel.appendChild(checkbox);
        vessel.appendChild(document.createTextNode(ingr.trim()));
        dumper.appendChild(vessel);
    }
}