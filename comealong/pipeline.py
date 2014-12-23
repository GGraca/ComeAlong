from django.core.files.base import ContentFile
import json
import urllib2
from pprint import pprint

def save_profile_picture(strategy, user, response, details,
                         is_new=False,*args,**kwargs):

    if is_new and "id" in response:
        url = "http://graph.facebook.com/{0}/picture?type=large&redirect=false".format(response['id'])
        data = json.load(urllib2.urlopen(url))
        image_url = data["data"]["url"]

        user.avatar.save('{0}_social.jpg'.format(user.username), ContentFile(urllib2.urlopen(image_url).read()))
        user.save()
