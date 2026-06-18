import random

import streamlit as st

from questions import questions


def build_quiz_questions(source_questions: list[dict], rng=random) -> list[dict]:
    quiz_questions = []
    for question in source_questions:
        prepared_question = question.copy()
        prepared_question["options"] = question["options"].copy()
        rng.shuffle(prepared_question["options"])
        quiz_questions.append(prepared_question)

    rng.shuffle(quiz_questions)
    return quiz_questions


def reset_quiz() -> None:
    st.session_state.quiz_questions = build_quiz_questions(questions)
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_answer = None
    st.session_state.last_was_correct = False


def main() -> None:
    if "current_question" not in st.session_state:
        reset_quiz()

    st.set_page_config(page_title="Quiz di Ingegneria del Software", page_icon="📚")
    st.title("Quiz di Ingegneria del Software")

    total_questions = len(st.session_state.quiz_questions)
    current_index = st.session_state.current_question

    st.write(f"Punteggio: {st.session_state.score} / {total_questions}")

    if current_index >= total_questions:
        st.success(f"Quiz completato. Punteggio finale: {st.session_state.score} / {total_questions}")
        if st.button("Ricomincia"):
            reset_quiz()
            st.rerun()
        st.stop()

    item = st.session_state.quiz_questions[current_index]
    st.subheader(f"Domanda {current_index + 1} di {total_questions}")
    st.markdown(f"**{item['question']}**")

    with st.form(key=f"question_{current_index}"):
        selected = st.radio(
            "Scegli una risposta",
            item["options"],
            index=None,
            disabled=st.session_state.answered,
        )
        submitted = st.form_submit_button("Invia risposta", disabled=st.session_state.answered)

    if submitted and not st.session_state.answered:
        if selected is None:
            st.warning("Seleziona una risposta prima di continuare.")
        else:
            st.session_state.selected_answer = selected
            st.session_state.last_was_correct = selected == item["correct_answer"]
            st.session_state.answered = True
            if st.session_state.last_was_correct:
                st.session_state.score += 1
            st.rerun()

    if st.session_state.answered:
        if st.session_state.last_was_correct:
            st.success("Corretto!")
        else:
            st.error("Sbagliato.")

        st.write(f"Risposta corretta: **{item['correct_answer']}**")
        st.markdown("**Fonte**")
        st.code(item["source_quote"], language=None)
        st.caption(f"{item['source_file']}, pagina/slide {item['source_page']}")

        if st.button("Prossima domanda"):
            st.session_state.current_question += 1
            st.session_state.answered = False
            st.session_state.selected_answer = None
            st.session_state.last_was_correct = False
            st.rerun()


if __name__ == "__main__":
    main()
