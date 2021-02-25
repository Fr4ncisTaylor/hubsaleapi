import requests
import base64
import json

from pprint import pprint

TOKEN  = None

def convert_key_to_base64(client_id, client_secret):
	auth_string = f"{client_id}:{client_secret}"
	return base64.b64encode(auth_string.encode()).decode()

def make_request_auth(method, auth, data=None, content_type="application/x-www-form-urlencoded"):
	headers = { 'Authorization': auth,
				'Content-type' : content_type,
			  }
	if "self" in data:
		del data['self']

	return requests.post(f'https://api.hub.sale/1.0/{method}/', headers=headers, data=data)


def make_request_http(url):
	headers = { 'Authorization': f"Bearer {TOKEN}",
				'Content-type' :  "application/json",
		  		}
	return requests.get(url, headers=headers).json()

class HubSale:
	def __init__(self, client_id:str, client_secret:str):
		self.client_id     = client_id
		self.client_secret = client_secret
		self.auth_string   = convert_key_to_base64(client_id, client_secret)
		self.connection    = False

	def connect(self):
		auth = make_request_auth("auth", "Basic "+self.auth_string, data={"grant_type": "client_credentials"}).json()
		if auth['success'] != True:
			return False, auth['error']
		else:
			global TOKEN
			self.token      = auth['data']['token']
			TOKEN 			= self.token
			self.token_type = auth['data']['token_type']
			self.connection = True
			return True, auth['message']

	def get_sale_by_code(self, code, test=False):
		#code : Sale transaction code. Enter numbers only.
		
		if self.connection:
			if test:
				return make_request_http(f'https://api.hub.sale_test/1.0/sales_test/{code}/')
			else:
				return make_request_http(f'https://api.hub.sale/1.0/sales/{code}/')
		else:
			return False, "make a connection first"

	def get_sale_by_date(self, registration_date_start, registration_date_end, status, page=None, test=False):
		"""
		registration_date_start : Start date of the desired period. Use the 'YYYY-MM-DD' format.Start date of the desired period. Use the 'YYYY-MM-DD' format.
		registration_date_end : End date of the desired period. Use the 'YYYY-MM-DD' format.
		Page  : Requested page of a page with 50 records. If you do not inform, the first page will be returned.
		Status: Desired status. Use "1 'for waiting," 2 "for declined," 3 "for canceled," 4 "for paid," 6 "for chargeback, and" 7 "for analysis.
		"""
		page = "&page="+str(page) if page != None else ""

		if self.connection:
			if test:
				return make_request_http(f'https://api.hub.sale/1.0/sales_test/?registration_date_start={registration_date_start}&registration_date_end={registration_date_end}&status={status}{page}')
			else:
				return make_request_http(f'https://api.hub.sale/1.0/sales/?registration_date_start={registration_date_start}&registration_date_end={registration_date_end}&status={status}{page}')
		else:
			return False, "make a connection first"

	def get_sale_by_last_date(self, last_status_date_start, last_status_date_end, status, page=None, test=False):
		"""
		last_status_date_start : Start date of the desired period. Use the 'YYYY-MM-DD' format.Start date of the desired period. Use the 'YYYY-MM-DD' format.
		last_status_date_end : End date of the desired period. Use the 'YYYY-MM-DD' format.
		Page  : Requested page of a page with 50 records. If you do not inform, the first page will be returned.
		Status: Desired status. Use "1 'for waiting," 2 "for declined," 3 "for canceled," 4 "for paid," 6 "for chargeback, and" 7 "for analysis.
		"""
		page = "&page="+str(page) if page != None else ""

		if self.connection:
			if test:
				return make_request_http(f'https://api.hub.sale/1.0/sales_test/?last_status_date_start={last_status_date_start}&last_status_date_end={last_status_date_end}&status={status}{page}')
			else:
				return make_request_http(f'https://api.hub.sale/1.0/sales/?last_status_date_start={last_status_date_start}&last_status_date_end={last_status_date_end}&status={status}{page}')
		else:
			return False, "make a connection first"