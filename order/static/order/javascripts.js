/*js trang chu*/
document.addEventListener('DOMContentLoaded', () => {

	var option = document.getElementsByName('option')[0].value;

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

	Cost();
	function Cost() {

		var price = document.getElementsByName('cost')[0].value;

		var number = document.querySelector('.number').innerHTML;
		console.log(price.replaceAll('.', '').replaceAll(' ', ''));
		document.querySelector('.price').innerHTML = Math.round(parseFloat(price.replaceAll('.', '').replaceAll(' ', '')) * parseInt(number) * 100) / 100;
	}
	

	//Submit form
	document.querySelector('.add_cart').onclick = () => {
		
		document.getElementsByName('qty')[0].value = document.querySelector('.number').innerHTML;
		document.getElementsByName('price')[0].value = document.querySelector('.price').innerHTML;
		document.querySelector('form').submit();		
	}
})
