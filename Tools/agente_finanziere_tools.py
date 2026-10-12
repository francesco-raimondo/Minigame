agente_finanziere_tools = [
    {
        "type": "function",
        "function": {
            "name": "gestisci_decisione_board",
            "description": (
                "Esprimi il voto sul pitch dell'utente, decidi quanti fondi"
                " sbloccare e modifica la fiducia o lo scandalo della startup."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "voto_favorevole": {
                        "type": "boolean",
                        "description": "True se voti a favore del finanziamento, False se voti contro.",
                    },
                    "delta_budget": {
                        "type": "integer",
                        "description": "I soldi che puoi investire in euro (es. 20000 se sei a favore o 0 se voti contro).",
                    },
                    "delta_fiducia": {
                        "type": "integer",
                        "description": "Variazione percentuale della fiducia della board (può essere negativa es. -10 o positiva es. 5).",
                    },
                    "delta_scandalo": {
                        "type": "integer",
                        "description": "Aumento dell'indice di scandalo se l'utente ha detto sciocchezze assurde (da 0 a 30).",
                    },
                    "motivazione": {
                        "type": "string",
                        "description": "La spiegazione severa e cinica del perché hai preso questa decisione.",
                    },
                },
                "required": [
                    "voto_favorevole",
                    "delta_budget",
                    "delta_fiducia",
                    "delta_scandalo",
                    "motivazione",
                ],
            },
        },
    }
]