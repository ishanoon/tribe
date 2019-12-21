from  flask import Flask,render_template,redirect,request
import request as r
import os

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text/', methods=['GET','POST'])
def text():
    if request.method == 'POST':
        text_file = request.form['text_file']
        email =  request.form['email-user']
    else:
        return render_template('text.html')

@app.route('/audio/',methods=['GET','POST'])
def audio():
    return render_template('audio.html')
    
if __name__=='__main__':
    app.run(debug=True)