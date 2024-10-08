import pytest
import json
import os

from cats_api.main import SimpleRequest

cats = SimpleRequest()

def test_image_status_code():
	result = cats.send("meta","https://api.thecatapi.com/v1/images/search")

	assert result == 200

def test_image_response_length():
	result = cats.send("body","https://api.thecatapi.com/v1/images/search")

	assert len(result) == 1

def test_image_body_data():
	result = cats.send("body","https://api.thecatapi.com/v1/images/search")

	result_json = json.dumps(result, indent = 4)

	assert "https://cdn2.thecatapi.com/images/" in result_json

def test_image_limit():
	result = cats.send("body","https://api.thecatapi.com/v1/images/search?limit=11")

	assert len(result) == 10

def test_image_limit_with_key():
	token = os.environ.get("CAT_API_TOKEN")
	endpoint = "https://api.thecatapi.com/v1/images/search?limit=11&api_key=" + token
	result = cats.send("body",endpoint)

	assert len(result) == 11

def test_breed_status_code():
	result = cats.send("meta","https://api.thecatapi.com/v1/breeds")

	assert result == 200

