from io import BytesIO
from PIL import Image
from flask import Flask, request, url_for, render_template
import random
import base64
import requests

app = Flask(__name__, template_folder="")
FLAG_PATH = "flag.png"
flag_img = Image.open(FLAG_PATH)
RECAPTCHA_SECRET_KEY = "6LeRZQYfAAAAALfL7wbPk68fbC8gL3jRPfiFYYSd"

def encrypt_img(img: Image, key: int) -> Image:
    """Code stub goes here."""
    w, h = img.size
    pixels = []
    for x in range(w):
        for y in range(h):
            pixels.append(img.getpixel((x, y)))
    random.seed(key)
    random.shuffle(pixels)
    im2 = img.copy()
    for x in range(w):
        for y in range(h):
            im2.putpixel((x, y), pixels[x + y * w])
    return im2

def img_to_data_url(img: Image) -> str:
    f = BytesIO()
    img.save(f, format="PNG")
    img_base64 = base64.b64encode(f.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{img_base64}"

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/upload", methods=["POST"])
def upload():
    if "g-recaptcha-response" not in request.form:
        return "Captcha not found", 403
    try:
        capt_r = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", data={
                "secret": RECAPTCHA_SECRET_KEY,
                "response": str(request.form["g-recaptcha-response"]),
            })
        capt_r_j = capt_r.json()
    except Exception as e:
        return "Internal server error", 500
    if capt_r_j.get("action", "") != "sekai_ctf_image_encryption_upload":
        return "Invalid captcha action", 403
    if not capt_r_j.get("success", False):
        return f"Captcha failed: {', '.join(capt_r_j['error-codes'])}", 403

    if "image" not in request.files:
        return "Image not found", 403
    file = request.files["image"]
    try:
        im1 = Image.open(file.stream)
    except Exception as e:
        return "Invalid image", 403
    if im1.format != "PNG":
        return "Invalid image format", 403

    key = random.randint(0, 0xffffffff)
    im1_encrypted = encrypt_img(im1, key)
    url1 = img_to_data_url(im1_encrypted)
    url2 = img_to_data_url(encrypt_img(flag_img, key))

    return render_template("upload.html", url1=url1, url2=url2)

if __name__ == "__main__":
    app.run(debug=False)
