from ipaddress import ip_address
import re
import time
import os
import dns.resolver
import spf
import dns
import socket

class SenderFrameworkPolicy:
    
    def SPF_Record():
        pass

    def MX_Record(domain_name):
        for record in dns.resolver.resolve(domain_name, "MX"):
            results = []
            results.append(record)
            return results


    def Resolve_IP(domain_name):
        domain_name_final = "www." + domain_name
        ip_address = socket.gethostbyname(domain_name_final)
        return ip_address
        


    def main():
        # spf.check(IP_Address, "Mail-From", "Helo")
        pass


if __name__ == "__main__":
    SenderFrameworkPolicy.main()
    tobykillen_ip = SenderFrameworkPolicy.Resolve_IP("ulster.ac.uk")
    mx_Record = SenderFrameworkPolicy.MX_Record("ulster.ac.uk")
    spf_check = spf.check(i=tobykillen_ip, s="tobykillen.com", h=mx_Record)
    print(spf_check)
