env = {
    "P": "Prod",
    "R": "Pre-Prod",
    "I": "Test",
    "T": "Test",
    "M": "Pre-Prod",
    "P1": "Prod",
    "P2": "Prod",
    "P3": "Prod",
    "R1": "Pre-Prod",
    "R2": "Pre-Prod",
    "R3": "Pre-Prod",
    "T1": "Test",
    "T2": "Test",
    "T3": "Test",
    "I1": "Test Dev",
    "I2": "Test Dev",
    "I3": "Test Dev",
    "M1": "Pre-Prod",
    "M2": "Pre-Prod",
}

fun = {
    "BA": "BATCH",
    "SM": "TECNICI",
    "EV": "EVENTI",
    "BK8": "KUBERNETES",
    "IN": "IN",
    "":"Backup",
    "":"DEPS Delivery",
    "":"File Transfer",
    "":"FT DEPS",
    "":"Gestione Code MQ",
    "":"Job Applicativi",
    "":"Tecnici DB2",
    "":"Tecnici DEPS",
    "":"Tecnici Sistema",
    "":"Tecnici Test",
    "":"Tecnici UC4",
    "SR":""
}

sched_type = {
    "J": "JOBS",
    "Z": "APPLICAZIONE",
    "G": "GUI",
    "F": "FILE EVENT",
    "H": "TIME EVENT",
    "P": "POST-PROCESS"
}

area = {
    "CCCH": "Svizzerland",
    "CCEU": "Europe",
    "CCUK": "United Kingdom",
    "CCWO": "",
    "CBCH": "",
    "CBEU": "",
    "CBUK": "",
    "CBWO": "",
    "GENERIC" : "No Sepcific Area",
    "WO": "Common for all geographic areas"
}

# Sono 64 Applicativi ma ne abbiamo 74 in realtà
appl = {
    "COLLATERAL":"Collaterlali CCMS",
    "Unknown2":"Corner Online",
    "Unknown3":"MySQL",
    "Unknown4":"Corner Direct",
    "AGNITAS": "Agnitas EMM",
    "ALL": "Allocare",
    "AUTH": "AUTHENTIC",
    "AF": "Area Finanza",
    "BA": "Sap Bank Analyzer",
    "BANA": "Sap Bank Analyzer",
    "BASH": "Microsoft Share Point", # da verificare
    "BLADE": "Bladelogic",
    "CASH": "èCash",
    "CARO": "Caronte",
    "CC": "CCMS", # CC + AREA
    "CLOUDDTLK": "Data Lake",
    "CD": "CONNECT DIRECT", # da verificare
    "CRED": "Credoc Windows",
    "CTRA": "CornèrTrader",
    "DEB": "Debit",
    "DWH": "DWH - SDH",
    "DYN": "Dynacos",
    "DEC": "Decisioning",
    "EAM": "Infor Eam",
    "EBAN": "eBanking",
    "EBPP": "Ebpp",
    "EDWH": "eDWH Banca, eDWH CornerTrader",
    "FIRE": "FIRE",
    "FIT": "FIT",
    "FRAC": "FRACTALS",
    "GALI": "GALI",
    "GHIB": "DataOne",
    "GILCDWH": "GILC DWH",
    "GTF": "GTFrame",
    "HPD": "Holistic Pay",
    "IBO": "IBO",
    "INSP": "Inspire",
    "JAZZ": "Jazz",
    "LCS": "LCS (Loyalty Cornèr Suite)",
    "KFX": "Kofax",
    "MAS": "Master Finance",
    "MF": "Master Finance", # da verificare
    "MQ": "MQ SERIES",
    "MY": "myCorner",
    "NEVIS": "Nevis",
    "ODI": "ODI (Oracle Data Integrator)",
    "PEGA": "Pega",
    "PYT": "PYTHAGORAS",
    "PYTH": "PYTHAGORAS",
    "RMAN": "Recovery Management",
    "S4HANA": "Sap S4Hana",
    "SAP": "SAP",
    "SDH": "SDH",
    "SEN": "SEN",
    "SMS": "SMS Router",
    "SOLR": "SOLR",
    "SONQ": "Sonar Qube",
    "SAINT": "Special Applications", # Anche come SAP, verificare
    "SPLUNK": "Splunk",
    "SPSS": "Spss",
    "TECH": "Tecnici / DEPS / File Transfer DEPS",
    "_DBA": "Tecnici DB2",
    "_TEST": "Tecnici Test",
    "TECHUC4": "Tecnici UC4",
    "_SYS": "Tecnici Sistema",
    "TOTEM": "TOTEM (Firme elett.-Cert.Email)",
    "TRAC": "Trade Risk Active Control (TRAC)",
    "UC": "UC4",
    "VODI": "Voluntary Disclosure",
    "WHBO":"White Board - Lavagna Elettronica",
    "WOCK": "World - Check",
    "XR": "XReport",
    "NZEK": "ZEK",
    # CASO File Transfer
    "MFT":"",
    "SFT":""
}

sched_freq = {
    "E": "estemporanea",
    "G": "giornaliera",
    "L": "settimanale",
    "M": "mensile",
    "T": "trimestrale",
    "S": "semestrale",
    "A": "annuale",
    "I": "guI",
    "F": "file event"
}

batch_exe_func = {"empty":"empty"} 