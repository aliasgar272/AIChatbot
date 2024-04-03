from flask import Flask, render_template, request
from mbti_chatbot import MBTIChatbot

app = Flask(__name__)
chatbot = MBTIChatbot()

@app.route('/')
def index():
    # Render the index.html template with the first question
    question_text = chatbot.get_next_question()
    return render_template('index.html', question_text=question_text)

@app.route('/result', methods=['POST'])
def result():
    if 'response' in request.form:
        response = request.form['response']
        chatbot.process_response(response)
    
    if chatbot.has_more_questions():
        # If there are more questions, render index.html with the next question
        question_text = chatbot.get_next_question()
        return render_template('index.html', question_text=question_text)
    else:
        # If no more questions, determine the MBTI type and render result.html
        mbti_type = chatbot.determine_type()
        return render_template('result.html', mbti_type=mbti_type)

if __name__ == '__main__':
    app.run(debug=True)
