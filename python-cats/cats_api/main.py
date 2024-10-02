import requests

class SimpleRequest:

	def response(self, endpoint):
		response = requests.get(endpoint)
		return response.status_code

