# For more information about Flask, I watched the video https://www.youtube.com/watch?v=pJ8V51XJuf0
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def madlibs():
    return render_template('madlibs.html')

# For more information about sending data from a textbox into Flask, I read https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
@app.route('/', methods=['POST'])
def generate_story():
    template_vars = {
        'adj1': request.form['adj1'],
        'nationality': request.form['nationality'],
        'person': request.form['person'],
        'adverb': request.form['adverb'],
        'noun1': request.form['noun1'],
        'adj2': request.form['adj2'],
        'noun2': request.form['noun2'],
        'adj3': request.form['adj3'],
        'adj4': request.form['adj4'],
        'plural_noun': request.form['plural_noun'],
        'noun3': request.form['noun3'],
        'number1': request.form['number1'],
        'shapes': request.form['shapes'],
        'food1': request.form['food1'],
        'food2': request.form['food2'],
        'verb': request.form['verb'],
        'number2': request.form['number2'],
    }
    return render_template('story.html', adj1=template_vars.get('adj1'),
                                        nationality=template_vars.get('nationality'),
                                        person=template_vars.get('person'),
                                        adverb=template_vars.get('adverb'),
                                        noun1=template_vars.get('noun1'),
                                        adj2=template_vars.get('adj2'),
                                        noun2=template_vars.get('noun2'),
                                        adj3=template_vars.get('adj3'),
                                        adj4=template_vars.get('adj4'),
                                        plural_noun=template_vars.get('plural_noun'),
                                        noun3=template_vars.get('noun3'),
                                        number1=template_vars.get('number1'),
                                        shapes=template_vars.get('shapes'),
                                        food1=template_vars.get('food1'),
                                        food2=template_vars.get('food2'),
                                        verb=template_vars.get('verb'),
                                        number2=template_vars.get('number2'))

if __name__ == '__main__ ':
    app.run(debug = True)
