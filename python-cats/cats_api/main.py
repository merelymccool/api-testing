import requests

class SimpleRequest:

	def send(self, call, endpoint):
		if call == "meta":
			response = requests.get(endpoint)
			return response.status_code
		else:
			response = requests.get(endpoint)
			return response.json()

