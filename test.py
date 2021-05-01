
from imgurpython import ImgurClient
from rest_framework import authentication
from datetime import datetime

client_id = '###'
client_secret = '###'


def get_input(string):
    return input(string)

'''
def authenticate():
    # Get client ID and secret from config.py
    client = ImgurClient(client_id, client_secret)

    # Authorization flow, pin example (see docs for other auth types)
    authorization_url = client.get_auth_url('pin')

    print(f"Go to the following URL: {authorization_url}")

    # Read in the pin, handle Python 2 or 3 here.
    pin = get_input("Enter pin code: ")

    # ... redirect user to `authorization_url`, obtain pin (or code or token) ...
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

    print("Authentication successful! Here are the details:")
    print(f"   Access token:  {credentials['access_token']}")
    print(f"   Refresh token: {credentials['refresh_token']}")
    auth_tokens = {" Access token": credentials['access_token'],
                   " Refresh token": credentials['refresh_token']}

    return client, auth_tokens


# If you want to run this as a standalone script, so be it!
if __name__ == "__main__":
     client , auth_token = authenticate()
     access_token = auth_token[" Access token"]
     refresh_token = auth_token[" Refresh token"]
'''

# Pull authentication from the auth example (see auth.py)


album = 'a/MGSdS0d' # You can also enter an album ID here
image_path = 'p.jpg'

def upload_image(client):
	'''
		Upload a picture of a kitten. We don't ship one, so get creative!
	'''

	# Here's the metadata for the upload. All of these are optional, including
	# this config dict itself.
	config = {
		'album': album,
		'name':  'Renhe!',
		'title': 'Renhe!',
		'description': 'Cute PIC being cute on {0}'.format(datetime.now())
	}

	print("Uploading image... ")
	image = client.upload_from_path(image_path, config=config, anon=False)
	print("Done")
	print()

	return image


# If you want to run this as a standalone script
if __name__ == "__main__":
	client = authenticate()
	image = upload_image(client)

	print("Image was posted! Go check your images!")
	print("You can find it here: {0}".format(image['link']))
