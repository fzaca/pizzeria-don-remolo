import os

from flask import Flask, render_template, session, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cart')
def cart():
    if 'cart' not in session or len(session['cart']) == 0:
        cart = []
    cart = session['cart']
    total = sum([product['price'] for product in cart])
    return render_template('cart.html', cart=cart, total=total)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    name = request.form['name']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    title = request.form['title']

    if 'cart' not in session:
        session['cart'] = []

    for product in session['cart']:
        if product['name'] == name:
            product['quantity'] += quantity
            product['price'] = price * product['quantity']

            flash("El producto se ha actualizado correctamente.")
            return redirect('/cart')

    product = {
        'name': name, 
        'title': title,
        'price': price * quantity,
        'quantity': quantity,
        'image_path': url_for('static', filename=f'images/{name.lower()}.jpg'),
    }

    session['cart'].append(product)

    flash("El producto se ha agregado al carrito correctamente.")
    return redirect('/cart')

@app.route('/delete_to_cart', methods=['POST'])
def delete_to_cart():
    pos = request.form['pos']
    session['cart'].pop(int(pos))
    flash("El producto se ha eliminado del carrito correctamente.")
    return redirect('/cart')
    
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
