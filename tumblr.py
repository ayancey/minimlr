# This is where the thing that connects to Tumblr is.
# It's not pretty.

import json
import requests

def get_post(id):
	r = requests.get('http://alexm.moe/api/read/json', params={'id':id})
	# Tumblr gives us an ugly Javascript variable instead of the raw JSON
	return json.loads(r.text.replace('var tumblr_api_read = ','').replace(';',''))


print get_post('114254764075')['posts'][0]['url']
