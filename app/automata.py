class Automata  : 
    def __init__(self, data_automata):
        self.id = data_automata['id'],
        self.name = data_automata['name'],
        self.initial_state = data_automata['initial_state'],
        self.acceptance_states = data_automata['acceptance_states'],
        self.alphabet = data_automata['alphabet'],
        self.states = data_automata['states'],
        self.transitions = data_automata['transitions'],
        self.test_string = data_automata.get('test_string', [])
