from flask import Flask, render_template, redirect, flash, get_flashed_messages, url_for
from models import InForm, split_into_sentences, getSortedMessages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InForm()
    if form.validate_on_submit():
        flash(form.text.data)
        return redirect(url_for('choose'))
    return render_template('home.html', form = form)

@app.route('/choose')
def choose():
    text = ''.join(get_flashed_messages()[0])
    sentences = split_into_sentences(text)
    flash(sentences)
    return render_template('choose.html', sentences = sentences)

@app.route('/unswer/<sent>')
def unswer(sent):
    text = ''.join(get_flashed_messages()[0])
    sentences = split_into_sentences(text)
    sorted = getSortedMessages(sentences,sent)
    return render_template('unswer.html', sentences = sorted)

if __name__ == '__main__':
    app.run()
