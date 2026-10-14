marketing_agent_tools = [
    {
        "type": "function",
        "function": {
            "name": "launch_marketing_campaign",
            "description": (
                "Launch a standard digital marketing campaign to increase public awareness"
                " and attract small investors, boosting the raised budget slightly."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_name": {
                        "type": "string",
                        "description": "The creative name of the marketing campaign.",
                    },
                    "delta_budget": {
                        "type": "integer",
                        "description": "Extra funds raised thanks to the campaign (e.g. 5000 to 15000).",
                    },
                    "delta_trust": {
                        "type": "integer",
                        "description": "Impact on board trust (marketing ideas might make traditional board members slightly skeptical, e.g., -5 or 0).",
                    },
                    "delta_scandal": {
                        "type": "integer",
                        "description": "Risk of a mild backlash or controversy (e.g., 0 to 10).",
                    },
                    "feedback": {
                        "type": "string",
                        "description": "Your enthusiastic or slightly superficial feedback on the marketing strategy.",
                    },
                },
                "required": [
                    "campaign_name",
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