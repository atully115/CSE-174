import unittest
from io import StringIO
from unittest.mock import patch
from Project2.polish_notation_calculator import main

class TestPolishNotationCalculator(unittest.TestCase):

    @patch('builtins.input', return_value='test_input.txt')
    @patch('sys.stdout', new_callable=StringIO)
    def test_addition(self, mock_stdout, mock_input):
        with patch('builtins.open', unittest.mock.mock_open(read_data="+ 5 3 2\n")):
            main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Result of Line 1: 10")

    @patch('builtins.input', return_value='test_input.txt')
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtraction(self, mock_stdout, mock_input):
        with patch('builtins.open', unittest.mock.mock_open(read_data="- 10 3 2\n")):
            main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Result of Line 1: 5")

    @patch('builtins.input', return_value='test_input.txt')
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication(self, mock_stdout, mock_input):
        with patch('builtins.open', unittest.mock.mock_open(read_data="* 2 3 4\n")):
            main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Result of Line 1: 24")

    @patch('builtins.input', return_value='test_input.txt')
    @patch('sys.stdout', new_callable=StringIO)
    def test_division(self, mock_stdout, mock_input):
        with patch('builtins.open', unittest.mock.mock_open(read_data="/ 20 5 2\n")):
            main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Result of Line 1: 2")

    @patch('builtins.input', return_value='test_input.txt')
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_by_zero(self, mock_stdout, mock_input):
        with patch('builtins.open', unittest.mock.mock_open(read_data="/ 10 0\n")):
            main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Result of Line 1: Error: / by zero")

    @patch('builtins.input', return_value='test_input.txt')
    @patch('sys.stdout', new_callable=StringIO)
    def test_non_integer_input(self, mock_stdout, mock_input):
        with patch('builtins.open', unittest.mock.mock_open(read_data="+ 5 a 2\n")):
            main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Result of Line 1: Non-integer input on this Line")

    @patch('builtins.input', return_value='test_input.txt')
    @patch('sys.stdout', new_callable=StringIO)
    def test_no_operator(self, mock_stdout, mock_input):
        with patch('builtins.open', unittest.mock.mock_open(read_data="5 3 2\n")):
            main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Result of Line 1: No operator 5 3 2\n")

    @patch('builtins.input', return_value='test_input.txt')
    @patch('sys.stdout', new_callable=StringIO)
    def test_previous_total_addition(self, mock_stdout, mock_input):
        with patch('builtins.open', unittest.mock.mock_open(read_data="+ 5 3\n<+ 2\n")):
            main()
        expected_output = "Result of Line 1: 8\nResult of Line 2: 10"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='non_existent_file.txt')
    @patch('sys.stdout', new_callable=StringIO)
    def test_file_not_found(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "File 'non_existent_file.txt' not found.")

if __name__ == '__main__':
    unittest.main()
