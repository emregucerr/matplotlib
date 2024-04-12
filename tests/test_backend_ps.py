
import unittest
from unittest.mock import MagicMock
from matplotlib.figure import Figure
from matplotlib.backends.backend_ps import FigureCanvasPS

class TestPostScriptBackend(unittest.TestCase):
    def setUp(self):
        self.figure = Figure()
        self.canvas = FigureCanvasPS(self.figure)

    def test_auto_paper_size_standard_A4(self):
        # Assume the figure has A4 dimensions and 'get_paper_size' should return that.
        expected_paper_size = 'A4'
        self.canvas.get_paper_size = MagicMock(return_value=expected_paper_size)
        actual_paper_size = self.canvas.get_paper_size(self.figure.get_size_inches())
        self.canvas.get_paper_size.assert_called_once_with((8.267, 11.692))  # A4 size in inches
        self.assertEqual(actual_paper_size, expected_paper_size)

    def test_auto_paper_size_custom(self):
        # Assume the figure has custom dimensions and 'get_paper_size' should return "Custom".
        expected_paper_size = 'Custom'
        custom_size = (10, 12)  # Custom paper size in inches
        self.canvas.get_paper_size = MagicMock(return_value=expected_paper_size)
        actual_paper_size = self.canvas.get_paper_size(custom_size)
        self.canvas.get_paper_size.assert_called_once_with(custom_size)
        self.assertEqual(actual_paper_size, expected_paper_size)

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import MagicMock
from matplotlib.figure import Figure
from matplotlib.backends.backend_ps import FigureCanvasPS

class TestPostScriptBackend(unittest.TestCase):
    def test_auto_paper_size_standard_A4(self):
        # Create an A4 size figure which is 8.3 x 11.7 inches
        fig = Figure(figsize=(8.3, 11.7))
        canvas = FigureCanvasPS(fig)
        # Use MagicMock to avoid actual file I/O
        canvas.print_ps = MagicMock()
        # Trigger the _print_figure logic
        canvas.print_figure('unused_filename.ps', papertype=None)
        # Check if the auto-selected paper size is A4
        canvas.print_ps.assert_called_once()
        _, kwargs = canvas.print_ps.call_args
        self.assertEqual(kwargs['papertype'], 'A4')

    def test_auto_paper_size_custom(self):
        # Create a custom size figure of 10 x 10 inches
        fig = Figure(figsize=(10, 10))
        canvas = FigureCanvasPS(fig)
        # Use MagicMock to avoid actual file I/O
        canvas.print_ps = MagicMock()
        # Trigger the _print_figure logic
        canvas.print_figure('unused_filename.ps', papertype=None)
        # Check if the auto-selected paper size is Custom
        canvas.print_ps.assert_called_once()
        _, kwargs = canvas.print_ps.call_args
        self.assertEqual(kwargs['papertype'], 'Custom')

if __name__ == '__main__':
    unittest.main()
