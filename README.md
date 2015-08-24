
# Dashyn

This is a quick Sunday project inspired and mostly leveraging the code from Ted Benson's initial Amazon Dash Hack(http://medium.com/@eduardbenson) 

The Purpose of this take is to simulate the functionality of popular services such as LiveAlert which assist elderly in contacting emergency services which they wear at all times. 

The scope of such a device can be broaden to other use cases such as someone who is sick in bed at home, children performing an outdoor activity in the backyard among others. 

The goal of this is to elaborate on the versatility of the Amazon Dash device and show how with the large number of services and APIs available today, one could simulate what at firt appears to be a complex device. 

The code here is broken down in two parts:
1. The Alerts engine and listener, which picks up the signal when the Amazon Dash button is prssed when it connects to the WiFi router and executes the messaging commands which are very extensible.
2. The messaging commands themselves. At the moment just email (using MailGun) which combined with IFTTT.COM capabilities can provide additional alert mediums such as PushBullet and the Twilio API to send SMS.

Architecture Diagram:
![](http://i60.tinypic.com/qqx1t3.png)
