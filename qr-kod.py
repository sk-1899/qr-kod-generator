from flask import Flask, request, render_template
import qrcode
import io
import base64

app = Flask(__name__)

# Spara skapade QR-koder
generated_qr_codes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_img = None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            img = qrcode.make(url)
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            qr_img = base64.b64encode(buf.getvalue()).decode('utf-8')
            generated_qr_codes.append(qr_img)
    return render_template('index.html', qr_img=qr_img, qr_codes=generated_qr_codes)

if __name__ == '__main__':
    app.run(debug=True)