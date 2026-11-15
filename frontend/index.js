function hello(){
    alert("Hello")
}
const list = document.getElementById("items_list")
async function get_items() {
    const response = await fetch("/items");
    const data = response.json()
    list.innerHTML = "";
    data.items.forEach(item => {
                const li = document.createElement("li");
                li.textContent = item;
                list.appendChild(li);
            });
}