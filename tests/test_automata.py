# tests/test_automata.py
import unittest
import json
from app.automata import Automata
from main import app

class TestAutomata(unittest.TestCase):

    def setUp(self):
        self.data_ok = {
            'id': 1,
            'name': 'Test Automata',
            'initial_state': 'q0',
            'acceptance_states': ['q1'],
            'alphabet': ['0', '1'],
            'states': ['q0', 'q1'],
            'transitions': [
                {'from_state': 'q0', 'symbol': '0', 'to_state': 'q1'},
                {'from_state': 'q1', 'symbol': '1', 'to_state': 'q0'}
            ],
            'test_strings': ['0', '01', '1']
        }

        self.data_bad = {
            'id': 2,
            'name': 'Bad Automata',
            'initial_state': '',
            'acceptance_states': ['q1'],
            'alphabet': ['0'],
            'states': ['q0', 'q1'],
            'transitions': [],
            'test_strings': []
        }

    def test_validate_ok(self):
        automata = Automata(self.data_ok)
        self.assertTrue(automata.validate(), 'El autómata con información correcta debe pasar la validación')

    def test_validate_bad(self):
        automata = Automata(self.data_bad)
        self.assertFalse(automata.validate(), 'El autómata sin estado inicial debe fallar')

    def test_process_string_accepts(self):
        automata = Automata(self.data_ok)
        automata.validate()
        self.assertTrue(automata.process_string('0'), 'La cadena "0" debe ser aceptada')

    def test_process_string_rejects(self):
        automata = Automata(self.data_ok)
        automata.validate()
        self.assertFalse(automata.process_string('11'), 'La cadena "11" no debe ser aceptada')


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_process_automata_missing_file(self):
        response = self.app.post('/process-automata')
        self.assertEqual(response.status_code, 400)

        data = json.loads(response.get_data(as_text=True))
        self.assertIn('No se envió archivo', data['error'])


if __name__ == '__main__':
    unittest.main()
