import requests
import base64

# client ID and client secret provided by Spotify
CLIENT_ID = '269954c7ec33453282ceb838ac88947a'
CLIENT_SECRET = 'b5290248b6b7488b8e91d9f1e6b73ffb'

# Base64 encode the client ID and client secret
client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
client_credentials_base64 = base64.b64encode(client_credentials.encode())

# Request the access token
token_url = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': f'Basic {client_credentials_base64.decode()}'
}

data = {
    'grant_type': 'client_credentials'
}

# sending the request
response = requests.post(token_url, data=data, headers=headers)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Access token obtained successfully.")
else: 
    print("Error obtaining access token.")
    exit()
    
# Save the access token to a file for use in other scripts
with open('access_token.txt', 'w') as f:
    f.write(access_token)
    
    
# - The variables CLIENT_ID and CLIENT_SECRET store your unique credentials (you need to input your own credentials here) that identify the application interacting with the Spotify API. These credentials are provided when you register your application on Spotify’s developer dashboard. The Client ID identifies your application, while the Client Secret is a confidential key used for authentication.
# - The client ID and secret are concatenated into the client_credentials variable, separated by a colon (:). This string is then Base64 encoded to create a secure representation of the credentials. Following this, an access token is requested from the Spotify API.
# - A POST request is sent to the token_url (https://accounts.spotify.com/api/token) with the client credentials included in the Authorization header, which is necessary for client authentication. The grant_type parameter is set to 'client_credentials' to indicate that the application is requesting an access token using the client credentials flow.
# - With the obtained access token, the application can now make authorized requests to access music data such as tracks, albums, artists, and user information. This access is essential for building a music recommendation system using the Spotify API and Python.