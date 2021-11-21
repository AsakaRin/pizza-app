document.addEventListener('DOMContentLoaded', () => {

	// accept or refuse order
	var user = document.querySelector('.user').value;

	if (user != "superuser") {

		var prices = document.getElementsByName('price');
		var total = 0;
		for (let i = 0; i < prices.length; i++) {

			total += parseFloat(prices[i].value);
		}

		document.querySelector('.number').innerHTML = Math.round(parseFloat(total) * 100) / 100;
	}

	if (user == "superuser") {


		var counter = 0;
		var orders = document.querySelectorAll('.buy');

		for (let i = 0; i < orders.length; i++) {

			const input = document.createElement('input');
			input.type = 'hidden';
			input.name = 'position';
			input.value = counter;
			orders[i].append(input);
			counter++;
		}

		document.querySelectorAll('.accept').forEach(button => {

			button.onclick = () => {

				const input = document.createElement('input');
				input.type = 'hidden';
				input.name = 'command';
				input.value = 'accept';
				button.parentNode.append(input);

				button.parentNode.style.height = "0px";

				return true;
			}
		})
		document.querySelectorAll('.refuse').forEach(button => {

			button.onclick = () => {

				const input = document.createElement('input');
				input.type = 'hidden';
				input.name = 'command';
				input.value = 'refuse';
				button.parentNode.append(input);

				button.parentNode.style.height = "0px";

				return true;
			}
		})	
	}
	
})
