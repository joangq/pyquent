import unittest
from natural_deduction import dict_to_latex

class TestConverter(unittest.TestCase):
    def test_simple_axiom(self):
        self.assertEqual(dict_to_latex({'a': ''}), r"\displaystyle\frac{}{a}")
            

    def test_simple_inference(self):
        self.assertEqual(dict_to_latex({'a': 'b'}), r"\displaystyle\frac{b}{a}")
            

    def test_nested_inference(self):
        self.assertEqual(dict_to_latex({'a': {'b': 'c'}}), r"\displaystyle\frac{\displaystyle\frac{c}{b}}{a}")
            

    def test_multiple_inferences(self):
        self.assertEqual(dict_to_latex({'a': {'b': 'c', 'd': 'e'}}), r"\displaystyle\frac{\displaystyle\frac{c}{b}\;\;\displaystyle\frac{e}{d}}{a}")
            

    def test_nested_and_multiple_inferences(self):
        self.assertEqual(dict_to_latex({'a': {'b': 'c', 'd': {'e': 'f'}, 'g': 'h'}}), r"\displaystyle\frac{\displaystyle\frac{c}{b}\;\;\displaystyle\frac{\displaystyle\frac{f}{e}}{d}\;\;\displaystyle\frac{h}{g}}{a}")
            

    def test_empty_dictionary(self):
        self.assertEqual(dict_to_latex({}), '')
            

    def test_deeply_nested_dictionary(self):
        self.assertEqual(dict_to_latex({'a': {'b': {'c': {'d': 'e'}}}}), r"\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{e}{d}}{c}}{b}}{a}")
            

    def test_mix_of_empty_and_non_empty_values(self):
        self.assertEqual(dict_to_latex({'x': {'y': '', 'z': 'a'}}), r"\displaystyle\frac{\displaystyle\frac{}{y}\;\;\displaystyle\frac{a}{z}}{x}")
            

    def test_nested_dictionary_with_repeated_keys(self):
        self.assertEqual(dict_to_latex({'a': {'b': {'b': 'c'}}}), r"\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{c}{b}}{b}}{a}")
            

    def test_multiple_nested_elements(self):
        self.assertEqual(dict_to_latex({'a': {'b': {'c': {'d': 'e'}, 'f': 'g'}, 'h': 'i'}}), r"\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{\displaystyle\frac{e}{d}}{c}\;\;\displaystyle\frac{g}{f}}{b}\;\;\displaystyle\frac{i}{h}}{a}")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(loader.loadTestsFromTestCase(TestConverter))
    exit(0 if result.wasSuccessful() else 1)
