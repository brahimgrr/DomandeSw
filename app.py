import random

import streamlit as st

from questions import questions


def prepare_options(question_index: int) -> list[str]:
    if "option_orders" not in st.session_state:
        st.session_state.option_orders = {}

    if question_index not in st.session_state.option_orders:
        options = questions[question_index]["options"].copy()
        random.shuffle(options)
        st.session_state.option_orders[question_index] = options

    return st.session_state.option_orders[question_index]


def reset_quiz() -> None:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_answer = None
    st.session_state.last_was_correct = False
    st.session_state.option_orders = {}


if "current_question" not in st.session_state:
    reset_quiz()

st.set_page_config(page_title="Quiz di Ingegneria del Software", page_icon="📚")
st.title("Quiz di Ingegneria del Software")

total_questions = len(questions)
current_index = st.session_state.current_question

st.write(f"Punteggio: {st.session_state.score} / {total_questions}")

if current_index >= total_questions:
    st.success(f"Quiz completato. Punteggio finale: {st.session_state.score} / {total_questions}")
    if st.button("Ricomincia"):
        reset_quiz()
        st.rerun()
    st.stop()

item = questions[current_index]
st.subheader(f"Domanda {current_index + 1} di {total_questions}")
st.markdown(f"**{item['question']}**")

with st.form(key=f"question_{current_index}"):
    selected = st.radio(
        "Scegli una risposta",
        prepare_options(current_index),
        disabled=st.session_state.answered,
    )
    submitted = st.form_submit_button("Invia risposta", disabled=st.session_state.answered)

if submitted and not st.session_state.answered:
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
