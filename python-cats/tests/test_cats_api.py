import pytest

from cats_api.main import SimpleRequest

def test_status_code():
	cats = SimpleRequest()

	result = cats.response("https://api.thecatapi.com/v1/images/search")

	assert result == 200

