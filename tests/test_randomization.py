import unittest


class ReversingRandom:
    def shuffle(self, values):
        values.reverse()


class RandomizationTest(unittest.TestCase):
    def test_build_quiz_questions_shuffles_questions_and_options_before_rendering(self):
        from app import build_quiz_questions

        source_questions = [
            {
                "question": "Prima domanda",
                "options": ["Corretta 1", "Errata 1A", "Errata 1B", "Errata 1C"],
                "correct_answer": "Corretta 1",
                "source_quote": "Fonte 1",
                "source_file": "deck.pdf",
                "source_page": 1,
            },
            {
                "question": "Seconda domanda",
                "options": ["Corretta 2", "Errata 2A", "Errata 2B", "Errata 2C"],
                "correct_answer": "Corretta 2",
                "source_quote": "Fonte 2",
                "source_file": "deck.pdf",
                "source_page": 2,
            },
        ]

        prepared = build_quiz_questions(source_questions, rng=ReversingRandom())

        self.assertEqual("Seconda domanda", prepared[0]["question"])
        self.assertEqual(["Errata 2C", "Errata 2B", "Errata 2A", "Corretta 2"], prepared[0]["options"])
        self.assertEqual("Corretta 2", prepared[0]["correct_answer"])
        self.assertEqual(["Corretta 1", "Errata 1A", "Errata 1B", "Errata 1C"], source_questions[0]["options"])


if __name__ == "__main__":
    unittest.main()
