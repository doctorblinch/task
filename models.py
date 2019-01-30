import re
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
import gensim

# Form that is used to get input text from the user
class InForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Send')

# Function for spliting text into sentences using re library.
def split_into_sentences(text):
    caps = "([A-Z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

# Simple function to make code more compact, used only in
# "get_sorted_messages" function.
def split_to_words(sentences):
    words = []
    for sent in sentences:
        words.append(sent.split())
    return words

# Function that is sorting sentences (first parameter) in order
#  of similarity to the given sentence (second parameter).
# Based on the gensim library, returns a list of sorted sentences.
def get_sorted_messages(sentences, sent):
    numOfMainSent = sentences.index(sent)
    words = split_to_words(sentences)
    similarity = []
    model = gensim.models.Word2Vec(words)
    for i in range(len(sentences)-1):
        k = 0
        wordsOfSent = sentences[i].split()
        for word in sentences[numOfMainSent]:
            for w in wordsOfSent:
                try:
                    k += abs(model.similarity(word,w))
                except Exception:
                    pass
        similarity.append(k)
    final = []

    for s in sentences:
        j = similarity.index(max(similarity))
        final.append(sentences[j])
        similarity[j] = -1
    return final
