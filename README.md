# Quiz di Ingegneria del Software

Piccola applicazione Streamlit per studiare dai PDF del corso tramite domande a risposta multipla.

## Contenuto

- `app.py`: applicazione web Streamlit.
- `questions.py`: pool di domande in italiano con risposta corretta e fonte.
- `requirements.txt`: dipendenza necessaria per avviare l'app.
- `tests/`: controlli automatici sulla struttura delle domande e sulle citazioni PDF.

## Come eseguire l'app

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Poi apri l'URL mostrato da Streamlit nel terminale.

## Come usare il quiz

L'app mostra una domanda alla volta. Dopo l'invio della risposta mostra subito se è corretta o sbagliata, la risposta corretta, la citazione originale dal PDF e il file con pagina/slide di provenienza. Il punteggio viene mantenuto durante la sessione.

## Verifica delle fonti

Le citazioni sono state estratte dai PDF in `source/` con `pdftotext -layout`, una pagina alla volta. Ogni domanda usa una citazione letterale copiata dal testo estratto, mantenendo la lingua originale della slide.

Il controllo automatico in `tests/test_questions.py` verifica che:

- ogni domanda abbia esattamente 4 opzioni;
- la risposta corretta sia una delle opzioni;
- ogni citazione non sia vuota;
- ogni citazione compaia realmente nel PDF e nella pagina indicati.

Per eseguire i controlli:

```bash
python3 -m unittest discover tests
```

Nota: i controlli richiedono il comando `pdftotext`, disponibile nel pacchetto `poppler-utils` su molte distribuzioni Linux.
