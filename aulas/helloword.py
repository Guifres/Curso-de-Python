from flask import Flask
app = Flask(__name__)
@app.route('/')
def helloword():
    return 'Te amo, voçê é o amor da minha vida'
if __name__ == '__main__':
    app.run(debug=True)
