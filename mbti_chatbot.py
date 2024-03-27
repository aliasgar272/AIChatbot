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
        self.scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
        self.mbti_types = {
            'ESTJ': ['E', 'S', 'T', 'J'], 'ESTP': ['E', 'S', 'T', 'P'],
            'ESFJ': ['E', 'S', 'F', 'J'], 'ESFP': ['E', 'S', 'F', 'P'],
            'ENTJ': ['E', 'N', 'T', 'J'], 'ENTP': ['E', 'N', 'T', 'P'],
            'ENFJ': ['E', 'N', 'F', 'J'], 'ENFP': ['E', 'N', 'F', 'P'],
            'ISTJ': ['I', 'S', 'T', 'J'], 'ISTP': ['I', 'S', 'T', 'P'],
            'ISFJ': ['I', 'S', 'F', 'J'], 'ISFP': ['I', 'S', 'F', 'P'],
            'INTJ': ['I', 'N', 'T', 'J'], 'INTP': ['I', 'N', 'T', 'P'],
            'INFJ': ['I', 'N', 'F', 'J'], 'INFP': ['I', 'N', 'F', 'P']
        }

    def ask_question(self, question):
        while True:
            response = input(question + " (Enter 'A' or 'B'): ").strip().upper()
            if response == 'A' or response == 'B':
                return response
            else:
                print("Please enter 'A' or 'B'.")

    def ask_questions(self):
        for question in self.questions:
            response = self.ask_question(question)
            if response == 'A':
                self.scores['E'] += 1
            else:
                self.scores['I'] += 1
            if response == 'A':
                self.scores['S'] += 1
            else:
                self.scores['N'] += 1
            if response == 'A':
                self.scores['T'] += 1
            else:
                self.scores['F'] += 1
            if response == 'A':
                self.scores['J'] += 1
            else:
                self.scores['P'] += 1

    def determine_type(self):
        mbti_type = ""
        for mbti, preferences in self.mbti_types.items():
            match = True
            for pref in preferences:
                if (pref in ['E', 'I'] and self.scores[pref] <= 7) or \
                        (pref in ['S', 'N'] and self.scores[pref] <= 7) or \
                        (pref in ['T', 'F'] and self.scores[pref] <= 7) or \
                        (pref in ['J', 'P'] and self.scores[pref] <= 7):
                    match = False
                    break
            if match:
                mbti_type = mbti
                break
        return mbti_type

    def run(self):
        print("Welcome to the MBTI Chatbot!")
        print("Please answer the following questions to determine your MBTI type.")
        self.ask_questions()
        mbti_type = self.determine_type()
        if mbti_type:
            print("Your MBTI type is:", mbti_type)
        else:
            print("Sorry, unable to determine your MBTI type.")


if __name__ == "__main__":
    chatbot = MBTIChatbot()
    chatbot.run()
