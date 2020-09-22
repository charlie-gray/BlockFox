import sys
import requests

args = sys.argv

class Unblocker:
    def __init__(self, links):
        self.links = links
        self.dnsEntry={}

    #takes in dictionary formatted as ip:domain name
    def addHostConf(self, dnsEntry):
        try:
            with open('C:/Windows/System32/drivers/etc/hosts', 'a') as f:
                for ip in dnsEntry:
                    print("Unblocking {}".format(dnsEntry[ip]))
                    f.write('{} {}\n'.format(ip, dnsEntry[ip]))
        except:
            print("ERROR: Please run script as admin")
            exit()

        

    
    #query for address and add to dictionary
    def addDNSEntry(self, domain):
        url="https://www.whoisxmlapi.com/whoisserver/DNSService?apiKey=at_DPWE8Mq4LACELo5OEhdoFDp9GVcHN&domainName={}&type=1&outputFormat=JSON".format(domain)

        r = requests.get(url = url) 
        data = r.json() 

        address = data["DNSData"]['dnsRecords'][0]['address']
        
        self.dnsEntry[address] = domain

unblock = Unblocker(args[1:])

print(unblock.links)
for i in args[1:]:
    unblock.addDNSEntry(i)

unblock.addHostConf(unblock.dnsEntry)

print("done!")