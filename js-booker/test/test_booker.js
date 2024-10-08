var assert = require('assert');
const apiUrl = 'https://restful-booker.herokuapp.com/booking'

describe('API Testing restful=booker', function () {
	it('should have status 200', function () {
		fetch(apiUrl)
		.then(response => {
			assert.equal(response.status,200);
		});
	});

	it('should not have empty data', function () {
                fetch(apiUrl)
                .then(response => {
			return response.json()
                })
		.then(data => {
			assert.isNotEmpty(data);
		});
        });
});

