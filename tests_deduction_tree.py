import unittest
from natural_deduction import dict_to_latex

class TestConverter(unittest.TestCase):
    def test_simple_axiom(self):
        self.assertEqual(dict_to_latex({'a': ''}), r"\frac{}{a}")
            

    def test_simple_inference(self):
        self.assertEqual(dict_to_latex({'a': 'b'}), r"\frac{b}{a}")
            

    def test_nested_inference(self):
        self.assertEqual(dict_to_latex({'a': {'b': 'c'}}), r"\frac{\frac{c}{b}}{a}")
            

    def test_multiple_inferences(self):
        self.assertEqual(dict_to_latex({'a': {'b': 'c', 'd': 'e'}}), r"\frac{\frac{c}{b}\;\;\frac{e}{d}}{a}")
            

    def test_nested_and_multiple_inferences(self):
        self.assertEqual(dict_to_latex({'a': {'b': 'c', 'd': {'e': 'f'}, 'g': 'h'}}), r"\frac{\frac{c}{b}\;\;\frac{\frac{f}{e}}{d}\;\;\frac{h}{g}}{a}")
            

    def test_empty_dictionary(self):
        self.assertEqual(dict_to_latex({}), '')
            

    def test_deeply_nested_dictionary(self):
        self.assertEqual(dict_to_latex({'a': {'b': {'c': {'d': 'e'}}}}), r"\frac{\frac{\frac{\frac{e}{d}}{c}}{b}}{a}")
            

    def test_mix_of_empty_and_non_empty_values(self):
        self.assertEqual(dict_to_latex({'x': {'y': '', 'z': 'a'}}), r"\frac{\frac{}{y}\;\;\frac{a}{z}}{x}")
            

    def test_nested_dictionary_with_repeated_keys(self):
        self.assertEqual(dict_to_latex({'a': {'b': {'b': 'c'}}}), r"\frac{\frac{\frac{c}{b}}{b}}{a}")
            

    def test_multiple_nested_elements(self):
        self.assertEqual(dict_to_latex({'a': {'b': {'c': {'d': 'e'}, 'f': 'g'}, 'h': 'i'}}), r"\frac{\frac{\frac{\frac{e}{d}}{c}\;\;\frac{g}{f}}{b}\;\;\frac{i}{h}}{a}")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(loader.loadTestsFromTestCase(TestConverter))
