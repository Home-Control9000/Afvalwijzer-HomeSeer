#!/usr/bin/env python3
##############################################################################
# Functional Description:
# -----------------------
# - Haal Afvalwijzer gegevens op voor de ingegeven postcode en huisnummer
# - Zend 'vandaag opgehaald' status en 'soort afval' naar HomeSeer virtual devices
# Script wordt ieder uur opgestart door Node-RED
# Als 'notify' = True dan wordt er op de HUIDIGE dag afval opgehaald.
# Als 'notify' = None dan niet 
#
##############################################################################
#
from Afvalwijzer import Afvalwijzer
import requests

# Your adress info (Netherlands)
zipcode = 'xxxxxx'
number = xx

# Get the info
garbage = Afvalwijzer(zipcode, number)
#pickupdate, wastetype = garbage.garbage
#wastetype = garbage.garbage
#pickupdates = garbage.pickupdates
wastetypes = garbage.wastetypes
notify = garbage.notify

# Format it for HomeSeer use
# Wanneer er meer afvalsoorten opgehaald worden op een dag dan maak van dit array een string geschikt voor HomeSeer  
wastetypes_formatted = ' en '.join([str(elem) for elem in wastetypes])

# Debug
print ('vandaag opgehaald?:', notify)
print ('wastetypes array:', wastetypes)
print ('wastetypes_formatted:', wastetypes_formatted)
#print (wastetype)
#print (pickupdates)
#print (pickupdate)

# send waste pickup today status to HS
if notify == True:
    response = requests.get('http://192.168.1.61:8083/JSON', params = (('request', 'controldevicebyvalue'), ('ref', '1862'), ('value', '1')) )
elif notify == None:
    response = requests.get('http://192.168.1.61:8083/JSON', params = (('request', 'controldevicebyvalue'), ('ref', '1862'), ('value', '0')) )

response = requests.get('http://192.168.1.61:8083/JSON', params = (('request', 'setdevicestatus'), ('ref', '1863'), ('string', wastetypes_formatted)) )
