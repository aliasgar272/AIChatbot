// script.js

document.addEventListener("DOMContentLoaded", function () {
    const chatInput = document.querySelector('.chat-input');
    const questionForm = document.getElementById('question-form');
    const questionContainer = document.getElementById('question-container');
    const sendBtn = document.getElementById('sendBTN');
    let questionIndex = 0;

    const questions = [
        "Do you prefer spending time with others (E) or alone (I)?",
        "Do you focus on concrete facts and details (S) or on abstract ideas and possibilities (N)?",
        // Add more questions here...
    ];

    // Function to create radio button options for the current question
    function createQuestionOptions(question) {
        const questionDiv = document.createElement('div');
        questionDiv.classList.add('question');

        const questionText = document.createElement('p');
        questionText.textContent = question;
        questionDiv.appendChild(questionText);

        const optionA = createOption('A', 'response-A');
        const optionB = createOption('B', 'response-B');

        questionDiv.appendChild(optionA);
        questionDiv.appendChild(optionB);

        return questionDiv;
    }

    // Function to create radio button option
    function createOption(value, id) {
        const option = document.createElement('input');
        option.type = 'radio';
        option.name = 'response';
        option.value = value;
        option.id = id;
        return option;
    }

    // Function to clear previous question options
    function clearQuestionOptions() {
        questionContainer.innerHTML = '';
    }

    // Function to handle form submission
    function handleSubmit(event) {
        event.preventDefault();
        const selectedOption = document.querySelector('input[name="response"]:checked');
        if (selectedOption) {
            const userResponse = selectedOption.value;
            // Handle user response (e.g., process, display next question)
            console.log("User response:", userResponse);
            questionIndex++;
            if (questionIndex < questions.length) {
                clearQuestionOptions();
                const nextQuestion = createQuestionOptions(questions[questionIndex]);
                questionContainer.appendChild(nextQuestion);
            } else {
                console.log("No more questions. Show result or end conversation.");
                // Implement logic to show result or end conversation
            }
        } else {
            console.log("Please select an option.");
        }
    }

    // Initial question
    const initialQuestion = createQuestionOptions(questions[0]);
    questionContainer.appendChild(initialQuestion);

    // Event listener for form submission
    questionForm.addEventListener('submit', handleSubmit);

    // Other functions (e.g., cancel)...
});
