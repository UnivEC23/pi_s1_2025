
const API_URL = 'http://localhost:5000/api';

// async function pegaClientes1() {
// 	const response = await fetch(`${API_URL}/clientes`);
// 	const clientes = await response.json();
// 	console.log("clientes:\n" + clientes);
// 	const list = document.getElementById('listaClientes');
// 	list.innerHTML = '';
// 	clientes[0].forEach(cliente => {
// 		const li = document.createElement('li');
// 		li.textContent = cliente.content;
// 		const deleteBtn = document.createElement('button');
// 		deleteBtn.textContent = 'Delete';
// 		// deleteBtn.onclick = () => deleteItem(cliente._id);
// 		deleteBtn.onclick = () => deleteItem(cliente.nome);
// 		li.appendChild(deleteBtn);
// 		list.appendChild(li);
// 	});
// }

async function pegaClientes() {

	fetch(`${API_URL}/clientes`)
		.then(response => {
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}
			return response.json();
		})
		.then(data => {
			// console.log(data.length);
			if (data.length > 0) {
				document.getElementById('listaCBox').classList.remove('is-hidden');
				const list = document.getElementById('listaClientes');
				list.innerHTML = '';
				console.log(data);
				console.log(typeof data);
				data.forEach(cliente => {
					const li = document.createElement('li');
					// li.textContent = cliente.nome 
					li.className = "list-item is-inline-flex";
					const nome_div = document.createElement('div');
					nome_div.textContent = cliente.nome
					nome_div.className = "list-item-content";
					// div.className = "list-item-title";
					li.appendChild(nome_div);

					const email_div = document.createElement('div');
					email_div.textContent = cliente.email
					email_div.className = "list-item-content";
					// div.className = "list-item-title";
					li.appendChild(email_div);

					const solicit_div = document.createElement('div');
					solicit_div.textContent = cliente.solicit
					solicit_div.className = "list-item-content";
					// div.className = "list-item-title";
					li.appendChild(solicit_div);

					const deleteBtn = document.createElement('button');
					deleteBtn.textContent = 'Delete';
					deleteBtn.className = "button is-danger list-item-controls";
					// deleteBtn.onclick = () => deleteItem(cliente._id);
					deleteBtn.onclick = () => deleteItem(cliente.nome);
					li.appendChild(deleteBtn);
					list.appendChild(li);
				});
			}
			else {
				document.getElementById('listaClientes').replaceChildren();
				document.getElementById('listaCBox').classList.add('is-hidden');
			}
		})
		.catch(error => {
			console.error('There was a problem with the fetch operation:', error);
		});
}

async function adiClientes() {
	const nome = document.getElementById('nome');
	const email = document.getElementById('email');
	const solicit = document.getElementById('solicit');

	if (!nome.value || !email.value || !solicit.value) {
		alert('Por favor, preencha todos os campos.');
		return;
	}

	// console.log(" adiclientes", nome, email, solicit)
	if (nome.value.trim() !== '') {
		const response = await fetch(`${API_URL}/clientes`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ nome: nome.value, email: email.value, solicit: solicit.value }),
		});
		if (response.ok) {
			nome.value = '';
			pegaClientes();
		}
	}
}

async function deleteItem(_nome) {
	const response = await fetch(`${API_URL}/clientes`, {
		method: 'DELETE',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({ nome: _nome }),
	});
	if (response.ok) {
		pegaClientes();
	}
}

pegaClientes();
