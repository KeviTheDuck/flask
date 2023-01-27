from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_website():
    return redirect('https://www.youtube.com/watch?v=dvHlC29ahgg')

if __name__ == '__main__':
    app.run(debug=True)
