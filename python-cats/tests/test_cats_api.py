import pytest

from cats_api.main import SimpleRequest

def test_status_code():
	cats = SimpleRequest()

	result = cats.response("https://api.thecatapi.com/v1/images/search")

	assert result == 200

def test_response_length():
	cats = SimpleRequest()

	result = cats.body("https://api.thecatapi.com/v1/images/search")

	assert len(result) == 1

