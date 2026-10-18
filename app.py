import os
from flask import Flask, render_template_string

app = Flask(__name__)


MY_NAME = "mohamed and hassan"

MY_BIO ="manger"
MY_LINKS =[ https://t.me/Moham607080
           ]
    


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>موقع {{ name }}</title>
    <!-- استيراد Bootstrap للتصميم السريع العريض -->
    <link href="https://jsdelivr.net" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
        }
        .profile-card {
            background: white;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            padding: 40px 30px;
            margin-top: 100px;
            text-align: center;
        }
        .profile-name {
            color: #0d6efd;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .btn-custom {
            margin: 5px;
            border-radius: 20px;
            padding: 10px 25px;
            transition: 0.3s;
        }
        .btn-custom:hover {
            transform: translateY(-3px);
        }
        footer {
            margin-top: 5px;
            font-size: 0.9s;
            color: #777;
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6 profile-card">
                <!-- اسمك -->
                <h1 class="profile-name">{{ name }}</h1>
                
                <!-- نبذة عنك -->
                <p class="lead mb-4">{{ bio }}</p>
                
                <hr class="my-4">
                class="btn btn-outline-success btn-custom"

                <!-- روابط التواصل الاجتماعي -->
                <h5 class="mb-3">تواصل معي:</h5>
                <div class="d-flex justify-content-center flex-wrap">
                    {% for link in links %}
                        <a href="{{ link.url }}" target="_blank" class="btn btn-outline-primary btn-custom">{{ link.name }}</a>
                    {% endfor %}
                </div>
                
                <footer class="mt-5">
                    <p>© 2026 جميع الحقوق محفوظة لـ {{ mohamed and hossan }}</p>
                </footer>
            </div>
        </div>
    </div>

    <script src="https://jsdelivr.net"></script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, name=MY_NAME, bio=MY_BIO, links=MY_LINKS)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
