from flask_wtf import Form
from wtforms import TextField
from wtforms.fields import DateTimeField, StringField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, ValidationError
import json, urllib2

def valid_address(form, field):
    url_safe_address = urllib2.quote(field.data)
    base_url = "http://maps.googleapis.com/maps/api/geocode/json?address="
    sensor_parameter = "&sensor=false"

    full_url = base_url + url_safe_address + sensor_parameter

    print full_url

    raw_json = urllib2.urlopen(full_url)
    json_dict = json.loads(raw_json.read())

    try:
        coords = json_dict['results'][0]['geometry']['location']
    except:
        raise ValidationError('Invalid Address')

class CreateEventForm(Form):
    name = StringField(u'Name', [InputRequired()])
    location = StringField(u'Location', [InputRequired(), valid_address])
    description = TextAreaField(u'Description', [InputRequired()])
    sponsor = StringField(u'Sponsor')
    food = StringField(u'Food')
    # start_time = DateTimeField('Start Time', validators=[DataRequired()])
    # end_time = DateTimeField('End Time', validators=[DataRequired()])
    contact = StringField(u'Contact')