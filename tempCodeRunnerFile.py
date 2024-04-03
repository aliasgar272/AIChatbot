from flask import Flask, render_template, request
from mbti_chatbot import MBTIChatbot

app = Flask(__name__)
chatbot = MBTIChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    chatbot.run()
    mbti_type = chatbot.determine_type()
    return render_template('result.html', mbti_type=mbti_type)

if __name__ == '__main__':
    app.run(debug=True)
