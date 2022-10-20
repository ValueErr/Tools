import requests
import config

class serverObj():

    def getWHMDomains(self) -> list:
            
        url = f'https://{self.whmURL}:2087/json-api/listaccts'

        headers = {
            'Authorization': f'whm {self.whmUser}:{self.whmToken}',
        }

        params = (
            ('api.version', '1'),
        )

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=params
        )

        data = response.json()

        domainsList = {}

        for site in data['data']['acct']:
            if site['suspended'] == 1:
                domainsList[site['domain']] = 1
            else:
                domainsList[site['domain']] = 0
        
        return domainsList

    def __init__(self, whmToken, whmUser, whmURL) -> None:
        self.whmToken = whmToken
        self.whmUser = whmUser
        self.whmURL = whmURL
        self.domains = self.getWHMDomains()

def DNSCheck(website):
    url = 'https://api.api-ninjas.com/v1/dnslookup'

    header = {
        'X-Api-Key': config.API_NINJAS_KEY,
        }

    params = {
        'domain': website,
    }

    response = requests.request(
        "GET",
        url,
        headers=header,
        params=params
        )

    data = response.json()

    ARECORDS = []
    usingCLOUDFLARE = False

    if response.status_code == requests.codes.ok and data:
        for record in data:
            if record['record_type'] == 'A':
                ARECORDS.append(record['value'])
            #Check Cloudflare in use by looking for 'cloudflare' in nameservers
            if record['record_type'] == 'NS' and 'cloudflare' in record['value']:
                usingCLOUDFLARE = True
        return({'aRecords': ARECORDS, 'usingcloudflare': usingCLOUDFLARE})

    elif response.status_code == requests.codes.ok and not data:
        return

    else:
        print("Error:", response.status_code, response.text)