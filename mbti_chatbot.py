class MBTIChatbot:
    def __init__(self):
        self.questions = [
            "Do you prefer spending time with others (E) or alone (I)?",
            "Do you focus on concrete facts and details (S) or on abstract ideas and possibilities (N)?",
            "When making decisions, do you rely more on logic and reason (T) or on your values and emotions (F)?",
            "Do you prefer a planned, organized approach to life (J) or a flexible, spontaneous approach (P)?",
            "Are you more outgoing and sociable (E) or reserved and reflective (I)?",
            "Do you enjoy routine and predictability (J) or prefer flexibility and adaptability (P)?",
            "Do you prefer to work with your hands and practical tasks (S) or with ideas and concepts (N)?",
            "Are you more interested in the present reality (S) or future possibilities (N)?",
            "Are you more focused on details and specifics (S) or big-picture thinking (N)?",
            "Do you value harmony and cooperation (F) or objective analysis and fairness (T)?",
            "Do you prefer to plan and schedule activities (J) or keep things open-ended (P)?",
            "Do you find it easy to speak up in groups (E) or prefer one-on-one conversations (I)?",
            "Do you tend to follow a schedule and stick to plans (J) or prefer to go with the flow (P)?",
            "Do you trust your gut feelings and instincts (F) or rely more on logic and reason (T)?",
            "Do you enjoy exploring new ideas and possibilities (N) or prefer to focus on what's practical and achievable (S)?"
        ]
        self.responses = []
        self.current_question_index = 0

    def get_next_question(self):
        """
        Get the next question from the list of questions.
        """
        if self.current_question_index < len(self.questions):
            next_question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return next_question
        else:
            return None

    def process_response(self, response):
        """
        Process the user's response and store it in the responses list.
        """
        self.responses.append(response)

    def has_more_questions(self):
        """
        Check if there are more questions to ask.
        """
        return self.current_question_index < len(self.questions)

    def determine_type(self):
        """
        Determine the MBTI type based on the user's responses.
        """
        if len(self.responses) != len(self.questions):
            # If all questions have not been answered, return None
            return None
        
        # Analyze the responses and determine the MBTI type
        extrovert_count = self.responses.count('E')
        introvert_count = self.responses.count('I')
        sensing_count = self.responses.count('S')
        intuition_count = self.responses.count('N')
        thinking_count = self.responses.count('T')
        feeling_count = self.responses.count('F')
        judging_count = self.responses.count('J')
        perceiving_count = self.responses.count('P')

        mbti_type = ""
        # Determine the preference for each dimension based on counts
        if extrovert_count > introvert_count:
            mbti_type += 'E'
        else:
            mbti_type += 'I'
        
        if sensing_count > intuition_count:
            mbti_type += 'S'
        else:
            mbti_type += 'N'
        
        if thinking_count > feeling_count:
            mbti_type += 'T'
        else:
            mbti_type += 'F'
        
        if judging_count > perceiving_count:
            mbti_type += 'J'
        else:
            mbti_type += 'P'

        return mbti_type
