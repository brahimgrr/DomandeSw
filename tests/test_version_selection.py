import unittest
from pathlib import Path


class VersionSelectionTest(unittest.TestCase):
    def test_get_question_pool_selects_requested_version(self):
        from app import get_question_pool
        from questions import questions
        from questions_v2 import questions_v2

        self.assertIs(get_question_pool("V1"), questions)
        self.assertIs(get_question_pool("V2"), questions_v2)

    def test_get_question_pool_rejects_unknown_version(self):
        from app import get_question_pool

        with self.assertRaises(ValueError):
            get_question_pool("V3")

    def test_app_contains_version_selection_labels(self):
        source = Path("app.py").read_text(encoding="utf-8")

        self.assertIn("Scegli il gruppo di domande", source)
        self.assertIn("Versione 1", source)
        self.assertIn("Versione 2", source)
        self.assertIn("Cambia versione", source)


if __name__ == "__main__":
    unittest.main()
