from graphviz import Digraph
import time
import os

def generate_diagram(automaton):
    if not automaton.is_valid:
        return

    timestamp = int(time.time())
    filename = f"generated_diagrams/automata_{automaton.id}_{timestamp}"
    
    dot = Digraph()
    dot.attr(rankdir='LR')

    dot.node('start', '', shape='none')
    dot.edge('start', automaton.initial_state, color='#B0B0B0')

    # Nodos
    for state in automaton.states:
        if state in automaton.acceptance_states:
            dot.node(state, state, shape='doublecircle', color='#77DD77', style='filled', fillcolor='#DFFFD6', fontcolor='#000000')
        else:
            dot.node(state, state, shape='circle', color='#AEC6CF', style='filled', fillcolor='#E0F7FA', fontcolor='#000000')

    for transition in automaton.transitions:
        dot.edge(transition["from_state"], transition["to_state"], label=transition["symbol"], color='#CBA0DC')

    if not os.path.exists("generated_diagrams"):
        os.makedirs("generated_diagrams")

    dot.render(filename, format='png', cleanup=True)
