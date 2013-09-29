import json, urllib2

def get_coords(address):
    #url_safe_address = urllib2.quote(address)
    url_safe_address = address.replace(' ', '+');
    base_url = "http://maps.googleapis.com/maps/api/geocode/json?address="
    sensor_parameter = "&sensor=false"

    full_url = base_url + url_safe_address + sensor_parameter

    print full_url

    raw_json = urllib2.urlopen(full_url)
    json_dict = json.loads(raw_json.read())

    return json_dict

