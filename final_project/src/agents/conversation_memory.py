class ConversationMemory:
    def __init__(self):
        self.history = []

    def add(self, message: str):
        self.history.append(message)

    def format(self):
        formatted = []
        for i, msg in enumerate(self.history):
            role = "user" if i % 2 == 0 else "assistant"
            formatted.append({"role": role, "content": msg})
        return formatted
