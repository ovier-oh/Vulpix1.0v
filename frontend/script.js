let token = "";

function registrar() {
const nombre = document.getElementById("reg-nombre").value;
const contraseña = document.getElementById("reg-contraseña").value;

fetch("http://localhost:5001/registro", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, contraseña })
})
    .then(res => res.json())
    .then(data => {
    document.getElementById("respuesta").innerHTML = `<div class="mensaje">Registro existoso.</div>`;
    })
    .catch(err => console.error(err));
}

function login() {
const nombre = document.getElementById("login-nombre").value;
const contraseña = document.getElementById("login-contraseña").value;

fetch("http://localhost:5001/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, contraseña })
})
    .then(res => res.json())
    .then(data => {
    token = data.token;
    document.getElementById("respuesta").innerHTML = `<div class="mensaje">Login exitoso. Token guardado.</div>`;
    console.log("Token recibido:", token); // útil para depurar
    })
    .catch(err => console.error(err));
}

function accederProtegido() {
    fetch("http://localhost:5001/protegido", {
        headers: {
        "Authorization": `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(data => {
    const mensaje = data.mensaje || "Acceso concedido";
    document.getElementById("respuesta").innerHTML = `<div class="mensaje">${mensaje}</div>`;
    })
    .catch(err => console.error(err));
}
