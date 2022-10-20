# whmCheck

This program returns all domains which are pointing elsewhere and not to their own server. Excludes any domains using Cloudflare.

## Requirements

An [API Ninjas](https://api-ninjas.com/) account and requests

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requests.

```bash
pip install requests
```

## Usage

Insert your server(s) and Ninja API key into config.py then run main.py.

E.g.

```python
SERVERS = {
    'BlankServer': serverObj('whmApiToken', 'whmUsername', 'whmUrl'),
    'BlankServer': serverObj('whmApiToken', 'whmUsername', 'whmUrl'),
    'BlankServer': serverObj('whmApiToken', 'whmUsername', 'whmUrl'),
}

API_NINJAS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxx'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)