from flask import Flask
app = Flask(__name__)
import openai
from ask_question_to_pdf import gp3_completion

from flask import request
from flask import render_template




@app.route('/')
def Handlepage():
    return render_template('index.html', name=__name__)


@app.route('/question', methods=['GET'])
def handleQuestion():
    question = gp3_completion('Pose-moi une question sur le cours')
    return {"answer" : question['choices'][0]['message']['content']}
                               

@app.route('/prompt', methods=['POST'])
def handlePrompt():
    #message = {}
    #message ['answer'] = request.form['prompt'] + " " + "double monstre"
    #return message
    data = request.form["prompt"]
    answer = gp3_completion(data)
    return {"answer" : answer['choices'][0]['message']['content']}


@app.route('/answer', methods=['POST'])
def handleAnswer():
    reponse = request.form["prompt"]
    correction = gp3_completion(reponse + ":La réponse est-elle correcte ? Dis moi ce que tu attendais")
    return {"answer" : correction['choices'][0]['message']['content']}



