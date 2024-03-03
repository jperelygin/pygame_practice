class GameState:
    def __init__(self):
        self.states = ["START", "RUNNING", "END"]
        self.state = 0

    def next_state(self):
        self.state += 1
        if self.state >= len(self.states):
            self.state = 0

    def get_state(self):
        return self.states[self.state]
