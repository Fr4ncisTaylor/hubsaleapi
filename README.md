
<p align="center"><img src="logotipo.png" alt="hubsale"></p>
<p align="center"><a href="https://api.hub.sale/1.0/documentation/">HubSale APi</a></p>
<p align="center"><strong>Version 1.0</strong></p>

* * *
[![PyPI](https://img.shields.io/badge/python-3.6-blue.svg)]()
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()

* * *
## Instalation

``` bash
pip install HubSale
```

* * *
## Connection
``` python
from HubSale import HubSale
from pprint  import pprint

client_id     = ""
client_secret = ""

hubsale       = HubSale(client_id, client_secret)
code, message = hubsale.connect()

if code:
	print("Success!!!")
else:
	print('Oops,', message)
```

* * *
## Examples

* [Connect](https://github.com/Fr4ncisTaylor/HubSale-api/blob/main/exemplos/connect.py)
* [Consult sales by last transaction register date](https://github.com/Fr4ncisTaylor/HubSale-api/blob/main/exemplos/consult%20sales%20by%20last%20transaction%20register%20date.py)
* [Consult sales by transaction register data](https://github.com/Fr4ncisTaylor/HubSale-api/blob/main/exemplos/consult%20sales%20by%20transaction%20register%20date.py)
* [Consult sales by buy code](https://github.com/Fr4ncisTaylor/HubSale-api/blob/main/exemplos/Consult%20sale.py)
