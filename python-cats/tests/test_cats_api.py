import pytest
import json

from cats_api.main import SimpleRequest

cats = SimpleRequest()

def test_status_code():
	result = cats.response("https://api.thecatapi.com/v1/images/search")

	assert result == 200

def test_response_length():
	result = cats.body("https://api.thecatapi.com/v1/images/search")

	assert len(result) == 1

def test_body_data():
	result = cats.body("https://api.thecatapi.com/v1/images/search")

	result_json = json.dumps(result, indent = 4)

	assert "https://cdn2.thecatapi.com/images/" in result_json

