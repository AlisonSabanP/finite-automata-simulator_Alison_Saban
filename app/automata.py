class Automata(): 
    def __init__(self, data_automata):
        self.id = data_automata['id'],
        self.name = data_automata['name'],
        self.initial_state = data_automata['initial_state'],
        self.acceptance_states = data_automata['acceptance_states'],
        self.alphabet = data_automata['alphabet'],
        self.states = data_automata['states'],
        self.transitions = data_automata['transitions'],
        self.test_string = data_automata.get('test_string', [])
    
    def validate(self):
        required_fields = ["id", "name", "initial_state", "acceptance_states", "alphabet", "states", "transitions"]
        for field in required_fields:
            if not hasattr(self, field) or getattr(self, field) is None:
                return False

        if not self.initial_state:
            return False

        if self.initial_state not in self.states:
            return False
        
        if not self.acceptance_states:
            return False
        
        for state in self.acceptance_states:
            if state not in self.states:
                return False
                
        if len(self.alphabet) == 0:
            return False
            
        
