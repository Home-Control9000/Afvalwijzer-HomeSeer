Python script to fetch the collection days for garbage in the Netherlands and send it to HomeSeer.

Configuration:
- Enter your zipcode and housenumber.
- Enter the device reference numbers from the 2 HomeSeer virtual devices. You wil find this numer in the devices page.

I created 2  virtual devices in Homeseer.
  - Garbage TODAY collected? = True or None
  - Wastetype(s) This can be more wastetypes on 1 day so the script is converting the array to an string.

Then the result is send with a JSON request to HomeSeer.
Im running this script every hour so the virtual devices are updated frequently.
