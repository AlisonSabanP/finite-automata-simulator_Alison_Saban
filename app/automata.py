class Automata(): 
    def __init__(self, data_automata):
        self.id = data_automata['id']
        self.name = data_automata['name']
        self.initial_state = data_automata['initial_state']
        self.acceptance_states = data_automata['acceptance_states']
        self.alphabet = data_automata['alphabet']
        self.states = data_automata['states']
        self.transitions = data_automata['transitions']
        self.test_strings = data_automata.get('test_strings', [])
        self.error = ''
        self.is_valid = False

    
    def validate(self):
        if not self.initial_state:
            self.error = 'No existe estado inicial para el automata.'    
            return False

        if self.initial_state not in self.states:
            self.error = f'El estado inicial {self.initial_state} no está en la lista de estados'
            return False
        
        if not self.acceptance_states:
            self.error = 'No existen estados de aceptación en automata.'
            return False
        
        for state in self.acceptance_states:
            if state not in self.states:
                self.error = f'El estado de aceptación {state} no existe entre los estados validos.'
                return False
                
        if len(self.alphabet) == 0:
            self.error = 'En el automata no existe un alfabeto.'
            return False
        
        for transition in self.transitions:
            symbol = transition['symbol']
            if symbol not in self.alphabet:
                self.error = f'El carácter {symbol} no está definido en el alfabeto del autómata'
                return False

            if transition['from_state'] not in self.states or transition['to_state'] not in self.states:
                self.error = 'Algunos de los estados en las transiciones no están definidos'
                return False

        for state in self.states:
            has_transition = any(t['from_state'] == state for t in self.transitions)
            if not has_transition:
                self.error = f'El estado {state} no tiene transiciones definidas'
                return False
        
        self.is_valid = True
        return True

    def process_string(self, string):
        state = self.initial_state
        for character in string:
            valid = False
            for transition in self.transitions:
                if transition["from_state"] == state and transition["symbol"] == character:
                    state = transition["to_state"]
                    valid = True
                    break
            if not valid:
                return False
        for acc_state in self.acceptance_states:
            if state == acc_state:
                return True
        return False

    def validate_inputs(self):
        results = []
        for string in self.test_strings:
            result = self.process_string(string)
            results.append({"string": string, "resultado": result})
        return results
