Python script to fetch the collection days for garbage in the Netherlands.

Configuration
- Enter your zipcode and housenumber.
- Enter the device refernce from the 2 HomeSeer virtual devices

I created 2  virtual devices in Homeseer.
  - Garbage today collected = True or None
  - Wastetype. This can be more wastetypes on 1 day so the script is converting the array to an string.

Then the result is send with a JSON request to HomeSeer.
Im running this script every hour so the virtual devices are updated frequently.
