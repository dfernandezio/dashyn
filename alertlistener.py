from scapy.all import *

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == 'xx:xx:xx:xx:xx:xx': #Your Amazon Dash's Mac Address 
        print"Alert triggered"
        execfile("mailsend.py") #Script that sends email
        execfile("sendsms.py") #Script that sends text
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
print sniff (prn=arp_display, filter="arp", store=0, count=10)
