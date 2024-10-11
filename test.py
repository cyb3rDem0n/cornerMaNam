import re
from data import *

def appl_substring_find(dict, appl_string):
    # Variabili per salvare i risultati
    no_in_appl = ""
    other = appl_string

    # Loop per cercare le chiavi del dizionario nella stringa
    for chiave, valore in dict.items():
        if chiave in appl_string:
         no_in_appl += f"{chiave}: {valore}, "
        # Rimuovi la sottostringa trovata dalla variabile other
        other = other.replace(chiave, "")

    # Rimuoviamo l'ultima virgola e spazio extra in no_in_appl
    no_in_appl = no_in_appl.rstrip(", ")

    return no_in_appl + "," + other



#####
def naming_analyzer(stringa):
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
        # Devo cercare un applicazione presente in appl{}
        temp_string = appl_substring_find(appl,resto).split(',')
        applicazione = temp_string[0].strip()
        sorgente_destinazione = None
        altro = temp_string[1].strip()

    # Creiamo il dizionario risultato
    
    if sorgente_destinazione != None:
        risultato = {
            'ambiente': ambiente,
            'funzione': funzione,
            'tipo_schedulazione': tipo_schedulazione,
            'area': area,
            'frequenza_schedulazione': frequenza_schedulazione,
            'applicazione': applicazione, #if applicazione else 'N/A',
            'sorgente_destinazione' : sorgente_destinazione #if applicazione else 'altro': sorgente_destinazione if applicazione else altro
        }
    else:
        risultato = {
            'ambiente': ambiente,
            'funzione': funzione,
            'tipo_schedulazione': tipo_schedulazione,
            'area': area,
            'frequenza_schedulazione': frequenza_schedulazione,
            'applicazione': applicazione,
            'other_info' : altro 
            }


    return risultato




# TEST
jobs = [
    'PSMJEBANDATAFEEDCEREPORTCHE',
    'R1INJCCCHMFTCCMSSAPG',
    'T3BAZCCCHAUTHDMDUFDAILYUPDG',
    'R1BAJCCCHB1AL3E'
]

for s in jobs:
    risultato = naming_analyzer(s)
    print(f"|JOB NAME: {s}|")
    for key, value in risultato.items():
        print(f"{key}: {value}")
    print("#" * 40)
    
