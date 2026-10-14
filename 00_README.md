# Automatisierte Konzeption digitaler Marketingkampagnen – Multi-Agenten-System in LangFlow

Begleitmaterial zum Abschlussbericht des Semesterprojekts im Modul Digital Finance (DIFA),
Master of Science in Wirtschaftsinformatik, Hochschule Luzern (HSLU), Herbstsemester 2026.
Verfasser: Kevin Oetiker, Modulleiter: Raul Gimeno.

## Worum geht es?

Eine Kette aus vier KI-Agenten (Recherche → Strategie → Content → Zusammenführung) erstellt
aus wenigen Eingaben (Zielgruppe, Angebot, Budget, Zeitraum) eine vollständige
Kampagnenplanung für einen **fiktiven** Anbieter von Gymi-Vorbereitungskursen in Zürich.
Verglichen werden zwei Varianten der Recherche:

- **Variante A:** Der Recherche-Agent erhält eine vorgegebene Liste von 21 Anbietern.
- **Variante B:** Der Recherche-Agent sucht die Wettbewerber selbständig im Web.

Ziel, Methodik, Ergebnisse und Reflexion stehen im Abschlussbericht.

## Inhalt des Repositories

| Datei | Inhalt |
|---|---|
| `Marketing_Agent_Flow_Version-A.json` | Finaler, verketteter Flow, Variante A |
| `Marketing_Agent_Flow_Version-B.json` | Finaler, verketteter Flow, Variante B |
| `Marketing Search Agent - Variante A.json` | Einzelflow Recherche-Agent, Variante A |
| `Marketing Search Agent - Variante B.json` | Einzelflow Recherche-Agent, Variante B |
| `Marketing Strategie Agent.json` | Einzelflow Strategie-Agent |
| `Marketing Content Agent.json` | Einzelflow Content-Agent |
| `MarketingAgent_FirstOutput.json` | Erste Version der gesamten Kette |
| `kampagnen_eingaben_komponente.py` | Quellcode der eigenen Komponente «Kampagnen-Eingaben» |
| `prompt_recherche_A.txt`, `prompt_recherche_B.txt` | Prompts Recherche-Agent |
| `prompt_strategie.txt`, `prompt_content.txt`, `prompt_zusammenfuehrung.txt` | Prompts Strategie, Content, Zusammenführung |
| `anbieterliste_komplett_21.csv` | Eingabeliste mit 21 Anbietern (Variante A) |
| `Ground_Truth_Liste.pdf` | Referenzliste: 40 geprüfte Anbieter, davon 35 aufgenommen |
| `Kampagnenplanung_Variante_A.pdf`, `Kampagnenplanung_Variante_B.pdf` | Finale Ausgaben der beiden Läufe |

## Voraussetzungen

- LangFlow Desktop, Version 1.12.0 (macOS oder Windows)
- Google-Gemini-API-Schlüssel mit aktivierter Abrechnung (der Gratis-Tarif reichte für die Aufgabe nicht aus)
- Internetzugang (Websuche des Recherche-Agenten)
- Modell: Gemini 3.8 Flash

## Einrichtung und Ausführung

1. LangFlow Desktop installieren und starten.
2. Den gewünschten Flow importieren: `Marketing_Agent_Flow_Version-A.json` (vorgegebene
   Anbieterliste) oder `Marketing_Agent_Flow_Version-B.json` (autonome Suche).
3. Den API-Schlüssel hinterlegen, entweder als globale Variable in den LangFlow-Einstellungen
   oder direkt im Sprachmodell-Baustein jedes Agenten. Die exportierten Flows enthalten
   **keine** Schlüssel. Als Modell «Gemini 3.8 Flash» wählen.
4. Nur Variante A: Den Inhalt von `anbieterliste_komplett_21.csv` in den Baustein «Text Input»
   einfügen.
5. In der Komponente «Kampagnen-Eingaben» Zielgruppe, Angebot, Budget und Zeitraum festlegen.
   Eingaben der finalen Läufe: Zielgruppe «Eltern und Schüler:innen des Lang- und
   Kurzzeitgymnasiums», Budget CHF 2'000, Zeitraum 1. September 2026 bis 5. März 2027.
6. Den Flow im Playground starten. Die Ausgabe erscheint als Markdown-Text und kann ausserhalb
   von LangFlow in Word oder PDF umgewandelt werden.

Ein Lauf dauert ca. fünf Minuten und kostete ca. CHF 1.00.

## Wichtige Einstellungen

| Einstellung | Variante A | Variante B |
|---|---|---|
| Max Iterations (verketteter Flow) | 100 | 80 |
| Aufruflimit im Recherche-Prompt | höchstens 1 Seitenaufruf je Anbieter, höchstens 35 Aufrufe | höchstens 2 Websuchen je Anbieter, höchstens 25 Websuchen |
| Temperature | LangFlow-Standard 0.1 | LangFlow-Standard 0.1 |

## Hinweise

- Die Läufe streuen: Wiederholte Läufe mit denselben Eingaben liefern unterschiedliche Ergebnisse.
- Faktenaussagen in den Ausgaben (Prüfungsablauf, Termine, Anbieterangaben) sind nicht lückenlos
  extern geprüft und müssen vor einer Veröffentlichung kontrolliert werden.
- Der Anbieter und die Eingaben sind fiktiv. Es werden keine Personendaten verarbeitet.
- Der Prompt-Text und die Eingaben werden an die Gemini-API von Google übermittelt.
