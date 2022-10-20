import config
import functions

# Main Loop
for server in config.SERVERS:
    #Retreive ServerIP
    SERVERIP = functions.DNSCheck(config.SERVERS[server].whmURL)['aRecords'][0]
    print(server)
    for domain in config.SERVERS[server].domains:
        #Run DNSCheck() on domain
        domainINFO = functions.DNSCheck(domain)
        if domainINFO is not None:
            #Check SERVERIP is not apart of domain's A records + check to see if Cloudflare is in use + check to see its not already suspended
            if SERVERIP not in domainINFO['aRecords'] and domainINFO['usingcloudflare'] is False and config.SERVERS[server].domains[domain] != 1:
                print(domain, domainINFO)
        else:
            print(domain, 'No Records Found')