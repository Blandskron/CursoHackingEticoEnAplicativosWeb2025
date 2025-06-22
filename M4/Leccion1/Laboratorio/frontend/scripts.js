document.getElementById("login-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    const res = await fetch("/login", {
        method: "POST",
        body: formData
    });
    const data = await res.json();
    alert(JSON.stringify(data)); // Muestra incluso token y rol
});

async function search() {
    const query = document.getElementById("search-box").value;
    const res = await fetch(`/search?q=${encodeURIComponent(query)}`);
    const data = await res.json();
    const container = document.getElementById("results");
    container.innerHTML = data.results.map(p => `<p>${p.name}: ${p.description}</p>`).join('');
}
