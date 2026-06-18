import ast
import unittest
from pathlib import Path


class AppStaticTest(unittest.TestCase):
    def test_app_py_exists_and_contains_italian_quiz_labels(self):
        app_path = Path("app.py")
        self.assertTrue(app_path.exists(), "app.py deve esistere")

        source = app_path.read_text(encoding="utf-8")
        ast.parse(source)

        required_labels = [
            "Quiz di Ingegneria del Software",
            "Invia risposta",
            "Prossima domanda",
            "Risposta corretta",
            "Fonte",
            "Punteggio",
        ]
        for label in required_labels:
            self.assertIn(label, source)


if __name__ == "__main__":
    unittest.main()
