#pip install instagrapi
from instagrapi import Client

cl = Client()
cl.login("your_username", "your_password")

cl.photo_upload("photo.jpg", "Caption from Python!")
