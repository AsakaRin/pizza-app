/*js trang chu*/
document.addEventListener('DOMContentLoaded', () => {

	var option = document.getElementsByName('option')[0].value;
	var course = document.getElementsByName('course')[0].value;

	//Add or subtract amount
	document.querySelector('.subtract').onclick = () => {

		var number = document.querySelector('.number').innerHTML;
		if (number > 1) {

			number--;
			document.querySelector('.number').innerHTML = number;
		}
		Cost();
	}
	document.querySelector('.add').onclick = () => {

		var number = document.querySelector('.number').innerHTML;
		if (number < 99) {

			number++;
			document.querySelector('.number').innerHTML = number;
		}
		Cost();
	}

	document.getElementsByName('size').forEach(ele => {
		
		ele.onclick = () => {

			Cost();
		}
	})

	//hide if size is unavailable
	var size = document.getElementsByName('size');
	for (let i = 0; i < size.length; i++) {

		if (size[i].value == "") {

			size[i].disabled = true;
			size[i + 1].checked = true;
		}
	}

	Cost();
	function Cost() {

		var radios = document.getElementsByName('size');
		var price;
		if (option == "pasta" || option == "salad") {

			price = document.querySelector('.unit').value;
		}
		else {

			for (let i = 0; i < radios.length; i++) {

				if (radios[i].checked) {

					price = radios[i].value;
					break;
				}
			}
		}

		// Price ad 0.5$ for each extra on sub
		if (option == "sub") {

			var checkbox = document.getElementsByName('topping');
			var count = 0;
			for (let i = 0; i < checkbox.length; i ++) {

				if (checkbox[i].checked) {

					count ++;
				}
			}
			price = parseFloat(price) + 0.5 * count;
		}

		var number = document.querySelector('.number').innerHTML;
		document.querySelector('.price').innerHTML = Math.round(parseFloat(price) * parseInt(number) * 100) / 100;
	}

	//Limit toppings select
	if (option == "regular_pizza" || option == "sicilian_pizza" || option == "sub") {

		var limit = document.querySelector('.limit').value;
		var checkbox = document.getElementsByName('topping');
		document.getElementsByName('topping').forEach(box => {

			box.onclick = () => {

				var count = 0;
				for (let i = 0; i < checkbox.length; i ++) {

					if (checkbox[i].checked) {

						count ++;
					}
				}

				if (count > limit) {

					box.checked = false;
				}

				Cost();
			}
		})
	}

	//Submit form
	document.querySelector('.add_cart').onclick = () => {

		if (option == "pasta" || option == "salad" || option == "dinner_platter") {

			document.getElementsByName('qty')[0].value = document.querySelector('.number').innerHTML;
			document.getElementsByName('price')[0].value = document.querySelector('.price').innerHTML;
			document.querySelector('form').submit();
		}

		var count = 0;
		for (let i = 0; i < checkbox.length; i ++) {

			if (checkbox[i].checked) {

				count ++;
			}
		}

		// Only nust select at least 1 toppings if buy reagular or sicilian pizza
		if (count == 0 && ((option == "regular_pizza") || (option == "sicilian_pizza"))) {

			alert('You must select at least 1 topping!')
		}
		else {

			document.getElementsByName('qty')[0].value = document.querySelector('.number').innerHTML;
			document.getElementsByName('price')[0].value = document.querySelector('.price').innerHTML;
			var radios = document.getElementsByName('size');
			for (let i = 0; i < radios.length; i++) {

				if (radios[i].checked) {

					document.getElementsByName('type')[0].value = radios[i].dataset.size;
					break;
				}
			} 
			document.querySelector('form').submit();
		}
	}
})
