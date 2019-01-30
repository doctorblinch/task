Semantic afficiency test.
=====================
### Purpose
Made as the the test task, can be used to sort sentences of the text in proximity to the given sentence.
### Requirements
Python3 (Tested on python 3.7.0 version)
And installed python3 libraries:
* flask
* flask_wtf
* gensim
### How to use it?
First you need to download main.py and models.py files. Activate your virtual environmet and install all the libraries
above. Use comands:

> export FLASK_APP=main.py
>
> flask run

After that the website will be activated and you will need to go over the link 'http://127.0.0.1:5000/' where you will
be able to see the 1st page of the app. There will be text area field in witch you input your text, after that you press
submit button and go to 2nd page on which you will see all the sentences separately, now you are required to choose the
base (main) sentence. After you choose - click on it. And on the finall 3rd page you will get an ordered list of sorted
sentences.
