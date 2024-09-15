# tests/test_gguf_model.py

import unittest
from modules.gguf_model import GGUFModel

class TestGGUFModel(unittest.TestCase):
    def setUp(self):
        # Provide a valid model path or mock if necessary
        self.model = GGUFModel(model_path='models/sample.gguf')

    def test_load_model(self):
        try:
            self.model.load_model()
            self.assertIsNotNone(self.model.model)
        except Exception as e:
            self.fail(f"load_model() raised Exception unexpectedly: {e}")

    def test_generate(self):
        self.model.load_model()
        prompt = "Hello, how are you?"
        response = self.model.generate(prompt)
        self.assertIsInstance(response, str)
        self.model.unload_model()

if __name__ == '__main__':
    unittest.main()
