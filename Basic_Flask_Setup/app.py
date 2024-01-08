from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # Det här är det som står i webbläsarens adressfält efter hemsidan, i detta fall ingenting
def index():
    return render_template('index.html') # Det här är för att hitta till rätt fil i programmet

@app.route('/page_2')
def customer_page():
    return render_template('page_2.html')

@app.route('/page_3')
def account_page():
    return render_template('page_3.html')

@app.route('/page_4')
def transaction_page():
    return render_template('page_4.html')

if __name__ == '__main__':
    app.run(debug=True)