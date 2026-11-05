# 🛡️ Phishing & Click Simulation Demo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Made for Education](https://img.shields.io/badge/Purpose-Educational-red.svg)](#)

Un progetto didattico locale pensato per **educare** utenti — familiari, amici o colleghi — sui pericoli del web. Include una simulazione di furto di credenziali e una simulazione di click su un link malevolo, mostrando in tempo reale quali dati il browser condivide automaticamente.

> ⚠️ **DISCLAIMER ETICO E LEGALE**  
> Questo progetto è a scopo puramente **educativo e difensivo**. Non è affiliato ad Amazon, Microsoft o a nessun altro marchio.  
> Le credenziali e i dati inseriti **non vengono inviati a nessun server esterno o di terze parti**: vengono registrati esclusivamente in locale, sul tuo computer, per mostrare all'utente quanto sia facile per un sito web tracciare le sue azioni.  
> **Non utilizzare questo codice per scopi illeciti o per ingannare persone a loro insaputa.** Usa la demo solo su persone che hanno dato il consenso esplicito.

## ✨ Caratteristiche

| File / Componente | Descrizione |
|---|---|
| **`demo-login.html`** | Pagina di login in stile e-commerce che mostra come i dati inseriti viaggiano verso il server. Include validazione dei campi in tempo reale, ad esempio i requisiti della password, e redirect al sito ufficiale al termine della finta procedura. |
| **`click.html`** | Pagina che simula un allarme virus. Mostra all'utente — e a te — quante informazioni il browser condivide automaticamente solo aprendo un link, tramite fingerprinting. |
| **`server.py`** | Server HTTP Python leggero e multithread che serve le pagine, intercetta i dati e li stampa in modo leggibile nel terminale, salvandoli anche in un file locale `log.txt`. |

## 🛠️ Prerequisiti

- **Python 3.8** o superiore.
- *(Opzionale)* **Cloudflare `cloudflared`**, se vuoi esporre la demo su internet in modo sicuro tramite un tunnel HTTPS.

## 💻 Installazione e Avvio

1. **Clona la repository:**

   ```bash
   git clone https://github.com/tuo-utente/nome-repo.git
   cd nome-repo
   ```

2. **Aggiungi il tuo logo — importante per l'aspetto visivo:**

   Per evitare problemi di copyright e garantire che la repository non venga scambiata per un sito di phishing reale, non sono inclusi loghi ufficiali.

   Se vuoi che la pagina `demo-login.html` mostri un logo, invece dell'icona di immagine rotta, inserisci un file chiamato **`logo.png`** direttamente nella cartella principale del progetto.

3. **Avvia il server locale:**

   ```bash
   python3 server.py
   ```

   Su Windows, se `python3` non è disponibile, puoi usare:

   ```bash
   python server.py
   ```

   Il terminale mostrerà l'indirizzo IP locale.

4. **Apri le demo nel browser:**

   - Simulazione di login: [http://localhost:8000/demo-login.html](http://localhost:8000/demo-login.html)
   - Simulazione di click: [http://localhost:8000/click.html](http://localhost:8000/click.html)

## 📁 Struttura del progetto

```text
.
├── demo-login.html
├── click.html
├── server.py
├── logo.png          # opzionale
├── log.txt           # generato dal server, ignorato da Git
├── .gitignore
└── LICENSE
```

## 🌍 Esportare la demo online con Cloudflare Tunnel

Se vuoi mandare il link a qualcuno che non è sulla tua stessa rete Wi-Fi, ad esempio in 5G, puoi usare Cloudflare Quick Tunnel. È gratuito e non richiede un account.

Lascia il server in esecuzione e apri un secondo terminale:

```bash
cloudflared tunnel --url http://localhost:8000
```

Copia il link `https://...trycloudflare.com` che appare e aggiungi `/demo-login.html` o `/click.html` per far accedere la persona alla demo desiderata.

> ⚠️ Esponi la demo online solo se necessario e sempre con il consenso delle persone coinvolte. Non raccogliere credenziali reali.

## 🧹 Pulizia e Privacy

Durante la demo, il server salva tutti i dati ricevuti nel file `log.txt`, nella stessa cartella del progetto. Questo file **non viene caricato su GitHub** grazie al file `.gitignore`.

Per evitare di lasciare dati sensibili, come credenziali reali digitate per errore, dopo aver concluso la demo cancella il file con:

```bash
rm log.txt
```

Su Windows:

```powershell
del log.txt
```

## 📄 Licenza

Questo progetto è distribuito sotto la licenza **MIT**. Consulta il file [`LICENSE`](LICENSE) per i dettagli.

---

*Creato per rendere il web un posto un po' più sicuro.*
