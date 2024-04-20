import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = "./"

    suite = loader.discover(start_dir)
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)

    exit(0 if result.wasSuccessful() else 1)