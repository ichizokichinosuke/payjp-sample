import os
import payjp

from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request

load_dotenv(find_dotenv())

SECRET_KEY = os.getenv("SECRET_KEY")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")

payjp.api_key = SECRET_KEY

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', public_key=PUBLIC_KEY)


@app.route('/pay', methods=['POST'])
def pay():
    amount = 1000
    customer = payjp.Customer.create(
        email='example@pay.jp',
        card=request.form.get('payjp-token')
    )

    payjp.Charge.create(
        amount=amount,
        currency='jpy',
        customer=customer.id,
        description='flask example charge'
    )
    return render_template('pay.html', amount=amount)


if __name__ == "__main__":
    app.run(port=4242)