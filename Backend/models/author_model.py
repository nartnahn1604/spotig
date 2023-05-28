from utils.cloudinary_config import *

class Author():
    def __init__(self, id, author_name, author_bio, author_avt):
        self.id = id
        self.author_name =author_name
        self.author_bio = author_bio
        self.author_avt = author_avt
    
    def create_img_url(self):
        public_id = self.song_thumb  # Replace with your Cloudinary public ID
        result = cloudinary.api.resource(public_id)
        image_url = result['secure_url']
        return image_url