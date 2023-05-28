import cloudinary
# Import the cloudinary.api for managing assets
import cloudinary.api
# Import the cloudinary.uploader for uploading assets
import cloudinary.uploader

cloudinary.config(
    cloud_name="YOUR_CLOUD_NAME",
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET",
    secure=True,
)

def create_img_url(edit_image, public_id):
    result = cloudinary.api.resource(public_id)
    image_url = str(result['secure_url'])
    image_url = image_url.replace('upload/', 'upload/' + edit_image)
    return image_url