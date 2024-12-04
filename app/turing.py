class TuringMachine:
    def __init__(self, tape, rules):
        self.tape = list(tape)
        self.head = 0
        self.state = 'q0'
        self.rules = rules

    def step(self):
        symbol = self.tape[self.head]
        rule = self.rules.get((self.state, symbol))

        if rule:
            new_state, write_symbol, direction = rule
            self.tape[self.head] = write_symbol
            self.state = new_state
            self.head += 1 if direction == 'R' else -1

    def run(self):
        while self.state != 'halt':
            self.step()
        return ''.join(self.tape).strip('_')


def validate_url(url):
    # Tape: URL padded with underscores
    tape = f"_{url}_"
    rules = {
        # Define rules for the machine
        ('q0', '_'): ('halt', '_', 'R'),
        # Example: Add specific rules to validate format
    }
    tm = TuringMachine(tape, rules)
    return tm.run()
