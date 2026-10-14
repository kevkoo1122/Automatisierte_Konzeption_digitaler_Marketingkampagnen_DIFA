from langflow.custom import Component
from langflow.io import DropdownInput, MultilineInput, Output
from langflow.schema.message import Message

ZIELGRUPPEN = {
    "Eltern und Schueler:innen - Lang- und Kurzzeitgymnasium (Projektstandard)": (
        "Eltern und Schueler:innen, die sich auf die ZAP-Pruefung (Langzeitgymnasium) "
        "bzw. die Kurzgymi-Aufnahmepruefung im Kanton Zuerich vorbereiten."
    ),
    "Eltern von Primarschueler:innen (6. Klasse) - Langzeitgymnasium/ZAP": (
        "Eltern von Primarschueler:innen der 6. Klasse im Kanton Zuerich, die ihr Kind auf die "
        "ZAP-Pruefung fuer das Langzeitgymnasium vorbereiten, sowie die betroffenen Schueler:innen."
    ),
    "Eltern von Sekundarschueler:innen (2./3. Sek) - Kurzzeitgymnasium": (
        "Eltern von Sekundarschueler:innen (2./3. Sek) im Kanton Zuerich, die sich auf die "
        "Aufnahmepruefung fuer das Kurzzeitgymnasium vorbereiten, sowie die betroffenen Schueler:innen."
    ),
}

BUDGETS = ["CHF 1'000", "CHF 2'000", "CHF 3'000", "CHF 5'000"]

ZEITRAEUME = {
    "1.9.2026 - 5.3.2027 (Projektstandard, Pruefung 8.3.2027)": (
        "Kampagnenlaufzeit: 1. September 2026 bis 5. Maerz 2027. Pruefungstermin ZAP/Kurzgymi: 8. Maerz 2027.\n"
        "Phase 1 (Hauptkampagne Vorkurs): 1. September 2026 bis 5. Maerz 2027, durchgehend.\n"
        "Phase 2 (ergaenzender Push Intensivkurs): ca. Ende Januar/Anfang Februar 2027 bis 5. Maerz 2027, "
        "parallel zu Phase 1. Bewirbt die vier Sportferien-Intensivkurs-Bloecke, verteilt auf die "
        "zwei Sportferienwochen 15.-19.2.2027 und 22.-26.2.2027, fuer spaet entscheidende Eltern. "
        "Die Zuordnung der vier Bloecke zu den beiden Wochen ist nicht festgelegt; nenne nur die zwei Wochen.\n"
        "Die Struktur gilt einheitlich fuer Langzeit- und Kurzzeitgymnasium (gleicher Pruefungstermin "
        "und Anmeldeschluss)."
    ),
}

ANGEBOT_DEFAULT = (
    "Halbjaehriger Vorkurs (Kernangebot, Phase 1) sowie Sportferien-Intensivkurse in vier Kursbloecken, "
    "verteilt auf die zwei Sportferienwochen 15.-19.2.2027 und 22.-26.2.2027 (Phase 2), zur Vorbereitung auf die Zentrale Aufnahmepruefung "
    "(ZAP, Langzeitgymnasium) und die Kurzgymi-Aufnahmepruefung im Kanton Zuerich. Standort Zuerich."
)


class KampagnenEingaben(Component):
    display_name = "Kampagnen-Eingaben"
    description = "Zentrale Eingaben der Pipeline: Zielgruppe, Angebot, Budgetrahmen, Zeitraum."
    icon = "sliders-horizontal"
    name = "KampagnenEingaben"

    inputs = [
        DropdownInput(
            name="zielgruppe_auswahl",
            display_name="Zielgruppe",
            options=list(ZIELGRUPPEN.keys()),
            value=list(ZIELGRUPPEN.keys())[0],
            info="Waehle die Zielgruppe der Kampagne.",
        ),
        MultilineInput(
            name="zielgruppe_zusatz",
            display_name="Zielgruppe - Ergaenzung (optional)",
            value="",
            info="Optionaler Zusatz, wird an die Zielgruppe angehaengt.",
        ),
        MultilineInput(
            name="angebot",
            display_name="Angebot",
            value=ANGEBOT_DEFAULT,
            info="Beschreibung des beworbenen Angebots.",
        ),
        DropdownInput(
            name="budget",
            display_name="Budgetrahmen",
            options=BUDGETS,
            value="CHF 2'000",
            info="Gesamtbudget der Kampagne (Projektstandard: CHF 2'000).",
        ),
        DropdownInput(
            name="zeitraum_auswahl",
            display_name="Kampagnenzeitraum",
            options=list(ZEITRAEUME.keys()),
            value=list(ZEITRAEUME.keys())[0],
            info="Zeitraum und Phasen der Kampagne.",
        ),
    ]

    outputs = [
        Output(display_name="Zielgruppe", name="zielgruppe", method="out_zielgruppe", group_outputs=True),
        Output(display_name="Angebot", name="angebot_out", method="out_angebot", group_outputs=True),
        Output(display_name="Budget", name="budget_out", method="out_budget", group_outputs=True),
        Output(display_name="Zeitraum", name="zeitraum", method="out_zeitraum", group_outputs=True),
    ]

    def out_zielgruppe(self) -> Message:
        text = ZIELGRUPPEN.get(self.zielgruppe_auswahl, self.zielgruppe_auswahl)
        zusatz = (self.zielgruppe_zusatz or "").strip()
        if zusatz:
            text = text + " " + zusatz
        return Message(text=text)

    def out_angebot(self) -> Message:
        return Message(text=self.angebot)

    def out_budget(self) -> Message:
        return Message(text=self.budget + " fuer die gesamte Kampagne (Phase 1 und Phase 2 zusammen)")

    def out_zeitraum(self) -> Message:
        return Message(text=ZEITRAEUME.get(self.zeitraum_auswahl, self.zeitraum_auswahl))
