from flask import Flask, render_template, redirect,\
flash, get_flashed_messages, url_for
from models import InForm, split_into_sentences, get_sorted_messages


#Initialization of Flask app.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
_text = ''

# Part that is responsible for different URLs

# In this function we create a form for user to input the text
# that we are going to sort.
@app.route('/', methods=['GET', 'POST'])
def index():
    global _text
    form = InForm()
    if form.validate_on_submit():
        _text = form.text.data
    #    flash(form.text.data)
        return redirect(url_for('choose'))
    return render_template('home.html', form = form)

# In this function we split text into sentences, display them open
# the screen and allow user to choose the "main" sentence for sorting.
@app.route('/choose')
def choose():
    global _text
    text = ''.join(_text)
    #text = ''.join(get_flashed_messages()[0])
    sentences = split_into_sentences(text)
    #flash(sentences)
    return render_template('choose.html', sentences = sentences)

# Sorting sentences using our function from models.py file
# and finally displaying them on the screen in the right order.
@app.route('/unswer/<sent>')
def unswer(sent):
    global _text
    text = _text
    #text = ''.join(get_flashed_messages()[0])
    sentences = split_into_sentences(text)
    sorted = get_sorted_messages(sentences,sent)
    return render_template('unswer.html', sentences = sorted)

# Starting the Flask app
if __name__ == '__main__':
    app.run()
