import subprocess
import unittest
from pathlib import Path


REQUIRED_KEYS = {
    "question",
    "options",
    "correct_answer",
    "source_quote",
    "source_file",
    "source_page",
}


def pdf_page_text(source_file: str, source_page: int, source_directory: str = "source") -> str:
    pdf_path = Path(source_directory) / source_file
    result = subprocess.run(
        [
            "pdftotext",
            "-layout",
            "-f",
            str(source_page),
            "-l",
            str(source_page),
            str(pdf_path),
            "-",
        ],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout


class QuestionPoolTest(unittest.TestCase):
    def test_question_pool_matches_required_structure_and_sources(self):
        from questions import questions

        self.assertTrue(questions, "Il pool di domande non deve essere vuoto")

        seen_questions = set()
        for index, item in enumerate(questions, start=1):
            self.assertEqual(set(item), REQUIRED_KEYS, f"Domanda {index}: chiavi non valide")
            self.assertTrue(item["question"], f"Domanda {index}: testo mancante")
            self.assertNotIn(item["question"], seen_questions, f"Domanda duplicata: {item['question']}")
            seen_questions.add(item["question"])

            self.assertEqual(len(item["options"]), 4, f"Domanda {index}: servono esattamente 4 opzioni")
            self.assertEqual(len(set(item["options"])), 4, f"Domanda {index}: opzioni duplicate")
            self.assertIn(
                item["correct_answer"],
                item["options"],
                f"Domanda {index}: la risposta corretta deve essere tra le opzioni",
            )

            self.assertTrue(item["source_quote"].strip(), f"Domanda {index}: citazione mancante")
            self.assertTrue(item["source_file"].endswith(".pdf"), f"Domanda {index}: PDF non valido")
            self.assertIsInstance(item["source_page"], int, f"Domanda {index}: pagina non valida")
            self.assertGreater(item["source_page"], 0, f"Domanda {index}: pagina non valida")

            pdf_text = pdf_page_text(item["source_file"], item["source_page"])
            self.assertIn(
                item["source_quote"],
                pdf_text,
                f"Domanda {index}: citazione non trovata nel PDF sorgente",
            )


if __name__ == "__main__":
    unittest.main()
