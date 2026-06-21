# Quiz di Ingegneria del Software

Piccola applicazione Streamlit per studiare dai PDF del corso tramite domande a risposta multipla.

## Contenuto

- `app.py`: applicazione web Streamlit.
- `questions.py`: pool V1 di domande in italiano con risposta corretta e fonte.
- `questions_v2.py`: pool V2 generato dai PDF in `sourceV2/`.
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

All'apertura, l'app chiede se usare le domande della Versione 1 o della Versione 2. Dopo la scelta mostra una domanda alla volta in ordine casuale e mescola anche le risposte. Dopo l'invio mostra subito se la risposta è corretta o sbagliata, la risposta corretta, la citazione originale dal PDF e il file con pagina/slide di provenienza. Il punteggio viene mantenuto durante la sessione.

Il pulsante `Cambia versione` torna alla schermata iniziale e azzera il quiz corrente. Il pulsante `Ricomincia` avvia nuovamente la versione selezionata con un nuovo ordine casuale.

## Verifica delle fonti

Le citazioni sono state estratte dai PDF in `source/` e `sourceV2/` con `pdftotext -layout`, una pagina alla volta. Ogni domanda usa una citazione letterale copiata dal testo estratto, mantenendo la lingua originale della slide.

Il controllo automatico in `tests/test_questions.py` verifica che:

- ogni domanda abbia esattamente 4 opzioni;
- la risposta corretta sia una delle opzioni;
- ogni citazione non sia vuota;
- ogni citazione compaia realmente nel PDF e nella pagina indicati.

Gli stessi controlli vengono applicati al pool V2 tramite `tests/test_questions_v2.py`.

Per eseguire i controlli:

```bash
python3 -m unittest discover tests
```

Nota: i controlli richiedono il comando `pdftotext`, disponibile nel pacchetto `poppler-utils` su molte distribuzioni Linux.
