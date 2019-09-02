from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def madlibs():
    return render_template('madlibs.html')

@app.route('/', methods=['POST'])
def generate_story():
    adj1 = request.form['adj1']
    nationality = request.form['nationality']
    person = request.form['person']
    adverb = request.form['adverb']
    noun1 = request.form['noun1']
    adj2 = request.form['adj2']
    noun2 = request.form['noun2']
    adj3 = request.form['adj3']
    adj4 = request.form['adj4']
    plural_noun = request.form['plural_noun']
    noun3 = request.form['noun3']
    number1 = request.form['number1']
    shapes = request.form['shapes']
    food1 = request.form['food1']
    food2 = request.form['food2']
    verb = request.form['verb']
    number2 = request.form['number2']

    return render_template('story.html', adj1=adj1, nationality=nationality, person=person, adverb=adverb, noun1=noun1, adj2=adj2, noun2=noun2, adj3=adj3, adj4=adj4, plural_noun=plural_noun, noun3=noun3, number1=number1, shapes=shapes, food1=food1, food2=food2, verb=verb, number2=number2)

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug = True)
