var assert = require('assert');
const apiUrl = 'https://restful-booker.herokuapp.com/booking'

describe('API Testing restful=booker', function () {
	it('should pass', function () {
		fetch(apiUrl)
		.then(response => {
			return response.json();
		})
		.then(data => {
			assert(data);
		});
	});
});

