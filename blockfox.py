import sys
import requests

args = sys.argv

class Unblocker:
    def __init__(self):

        self.dnsEntry={}

    #takes in dictionary formatted as ip:domain name
    def addHostConf(self, dnsEntry):
        try:
            with open('C:/Windows/System32/drivers/etc/hosts', 'a') as f:
                for ip in dnsEntry:
                    print("Unblocking {}".format(dnsEntry[ip]))
                    f.write('{}       {}\n'.format(ip, dnsEntry[ip]))
        except:
            print("ERROR: Please run script as admin")
            exit()

        

    
    #query for address and add to dictionary
    def addDNSEntry(self, domain):
        print("Querying api")
        url="https://www.whoisxmlapi.com/whoisserver/DNSService?apiKey=at_DPWE8Mq4LACELo5OEhdoFDp9GVcHN&domainName={}&type=1&outputFormat=JSON".format(domain)

        r = requests.get(url = url) 
        data = r.json() 

        address = data["DNSData"]['dnsRecords'][0]['address']
        
        self.dnsEntry[address] = domain

links = args[1:]


#format links list
for i, value in enumerate(links):
    links[i] = value.replace("www.","")
leng = len(links)
i=0
while i < leng:
    links.append("www." + str(links[i])) 
    i+=1


unblock = Unblocker()

for i in links:
    print(i)
    unblock.addDNSEntry(i)

unblock.addHostConf(unblock.dnsEntry)

print("done!")