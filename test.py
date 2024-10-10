import re

def analizza_stringa(stringa):
    # Step 1: Identificazione dell'ambiente
    if stringa[1].isdigit():
        ambiente = stringa[:2]
        resto = stringa[2:]
    else:
        ambiente = stringa[0]
        resto = stringa[1:]

    # Step 2: Identificazione della funzione (due caratteri successivi)
    funzione = resto[:2]
    resto = resto[2:]

    # Step 3: Identificazione del tipo di schedulazione (un carattere successivo)
    tipo_schedulazione = resto[0]
    resto = resto[1:]

    # Step 4: Identificazione dell'area (4 caratteri o WO o Generic subito dopo il tipo di schedulazione)
    area_match = re.match(r'(WO|Generic|\w{4})', resto)
    area = area_match.group(0)
    resto = resto[len(area):]  # Rimuoviamo l'area dalla stringa restante

    # Step 5: Identificazione della frequenza di schedulazione (ultimo carattere)
    frequenza_schedulazione = stringa[-1]
    resto = resto[:-1]  # Rimuoviamo l'ultimo carattere (frequenza) dalla parte restante

    # Step 6: Analisi Applicazione e Sorgente/Destinazione (o Altro)
    if 'MFT' in resto or 'SFT' in resto:
        # Applicazione trovata (MFT o SFT)
        match = re.search(r'(MFT|SFT)', resto)
        applicazione = match.group(0)
        resto = resto[match.end():]  # Rimuoviamo l'applicazione dalla stringa restante

        # Il resto è la sorgente/destinazione
        sorgente_destinazione = resto
    else:
        # Nessuna applicazione MFT o SFT trovata, quindi il resto va considerato come "Altro"
        applicazione = None
        sorgente_destinazione = None
        altro = resto

    # Creiamo il dizionario risultato
    risultato = {
        'ambiente': ambiente,
        'funzione': funzione,
        'tipo_schedulazione': tipo_schedulazione,
        'area': area,
        'frequenza_schedulazione': frequenza_schedulazione,
        'applicazione': applicazione if applicazione else 'N/A',
        'sorgente_destinazione' if applicazione else 'altro': sorgente_destinazione if applicazione else altro
    }

    return risultato

# Esempio di utilizzo
stringhe = [
    'R1INJCCCHMFTCCMSSAPG',
    'T3BAZCCCHAUTHDMDUFDAILYUPDG',
    'R1BAJCCCHB1AL3E'
]

for s in stringhe:
    risultato = analizza_stringa(s)
    print(f"Risultato per {s}: {risultato}\n")
