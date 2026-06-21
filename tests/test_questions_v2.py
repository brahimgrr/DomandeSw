import unittest

from tests.test_questions import REQUIRED_KEYS, pdf_page_text


class QuestionPoolV2Test(unittest.TestCase):
    def test_question_pool_v2_matches_required_structure_and_sources(self):
        from questions_v2 import questions_v2

        self.assertTrue(questions_v2, "Il pool V2 non deve essere vuoto")

        seen_questions = set()
        for index, item in enumerate(questions_v2, start=1):
            self.assertEqual(set(item), REQUIRED_KEYS, f"Domanda V2 {index}: chiavi non valide")
            self.assertTrue(item["question"], f"Domanda V2 {index}: testo mancante")
            self.assertNotIn(item["question"], seen_questions, f"Domanda V2 duplicata: {item['question']}")
            seen_questions.add(item["question"])

            self.assertEqual(len(item["options"]), 4, f"Domanda V2 {index}: servono 4 opzioni")
            self.assertEqual(len(set(item["options"])), 4, f"Domanda V2 {index}: opzioni duplicate")
            self.assertIn(item["correct_answer"], item["options"])

            self.assertTrue(item["source_quote"].strip(), f"Domanda V2 {index}: citazione mancante")
            self.assertGreater(item["source_page"], 0)
            pdf_text = pdf_page_text(
                item["source_file"],
                item["source_page"],
                source_directory="sourceV2",
            )
            self.assertIn(
                item["source_quote"],
                pdf_text,
                f"Domanda V2 {index}: citazione non trovata nel PDF sorgente",
            )


if __name__ == "__main__":
    unittest.main()
