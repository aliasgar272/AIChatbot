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
        self.current_question_index = 0

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            next_question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return next_question
        else:
            return None

    # Implement other necessary methods like process_response, has_more_questions, determine_type, etc.
