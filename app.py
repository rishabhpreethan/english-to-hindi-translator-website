from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    english_text = request.form['english_text']
    translator = Translator(to_lang="hi")
    hindi_text = translator.translate(english_text)
    return render_template('index.html', hindi_text=hindi_text)

if __name__ == '__main__':
    app.run()
