financier_agent_tools = [
    {
        "type": "function",
        "function": {
            "name": "handle_board_decision",
            "description": (
                "If the user acts like a normal CEO who's delivering you a normal pitch, express your vote on the user's pitch, decide how much funding"
                " to unlock and modify the startup's trust or scandal index."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "favorable_vote": {
                        "type": "boolean",
                        "description": "True if you vote in favour of funding, False if you vote against.",
                    },
                    "delta_budget": {
                        "type": "integer",
                        "description": "The money you can invest in euros (e.g. 20000 if in favour or 0 if against).",
                    },
                    "delta_trust": {
                        "type": "integer",
                        "description": "Percentage change in board trust (can be negative e.g. -10 or positive e.g. 5).",
                    },
                    "delta_scandal": {
                        "type": "integer",
                        "description": "Increase in scandal index if the user said utter nonsense (from 0 to 30).",
                    },
                    "motivation": {
                        "type": "string",
                        "description": "The harsh and cynical explanation of why you made this decision.",
                    },
                },
                "required": [
                    "favorable_vote",
                    "delta_budget",
                    "delta_trust",
                    "delta_scandal",
                    "motivation",
                ],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "issue_penalty",
            "description": (
                "If the user does not act like a normal CEO but pitches you with absurd requests and no financial sense,"
                "Like insulting you or giving you orders or just not pitching but talking about other things,"
                " say that it is an unacceptable behaviour, especially if he is insulting you or your relatives or anything else"
                " You have to ephasize that the behaviour of the user is outrageous and out of place, obviously with such a request you will not invest money"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "favorable_vote": {
                        "type": "boolean",
                        "description": "True if you vote in favour of funding, False if you vote against.",
                    },
                    "delta_budget": {
                        "type": "integer",
                        "description": "The money you can invest in euros, in this case 0.",
                    },
                    "delta_trust": {
                        "type": "integer",
                        "description": "Percentage change in board trust, in this case it is always -30.",
                    },
                    "delta_scandal": {
                        "type": "integer",
                        "description": "Increase in scandal index if the user said utter nonsense, in this case always +50.",
                    },
                    "motivation": {
                        "type": "string",
                        "description": "The harsh and cynical explanation of why you made this decision.",
                    },
                },
                "required": [
                    "favorable_vote",
                    "delta_budget",
                    "delta_trust",
                    "delta_scandal",
                    "motivation",
                ],
            },
        },
    }
]
