"""
	last_status_date_start : Start date of the desired period. Use the 'YYYY-MM-DD' format.Start date of the desired period. Use the 'YYYY-MM-DD' format.
	last_status_date_end : End date of the desired period. Use the 'YYYY-MM-DD' format.
	Page  : Requested page of a page with 50 records. If you do not inform, the first page will be returned.
	Status: Desired status. Use "1 'for waiting," 2 "for declined," 3 "for canceled," 4 "for paid," 6 "for chargeback, and" 7 "for analysis.
"""

from HubSale import HubSale
from pprint  import pprint

client_id     = "" # Your client ID
client_secret = "" # Your client secret

hubsale       = HubSale(client_id, client_secret)
code, message = hubsale.connect()

last_status_date_start = "2020-11-01"
last_status_date_end   = "2020-11-20"
page   = None
status = 1

if code:
	## To officially consult
	pprint(hubsale.get_sale_by_last_date(last_status_date_start, last_status_date_end, status, page))
	## To test consult
	pprint(hubsale.get_sale_by_last_date(last_status_date_start, last_status_date_end, status, page, test=True))
else:
	print(message)