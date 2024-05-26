tools = [
    {
        "type": "function",
        "function": {
            "name": "sampleQuestionsFromMMLU",
            "description": "Sample questions, choices, and their answers from the MMLU evaluation dataset",
            "parameters": {
                "type": "object",
                "properties": {
                    "n_samples": {
                        "type": "integer",
                        "description": "The number of samples or questions you want to generate",
                    },
                },
                "required": ["n_samples", "format"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculateAccuracy",
            "description": "Get an N-day weather forecast",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "format": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The temperature unit to use. Infer this from the users location.",
                    },
                    "num_days": {
                        "type": "integer",
                        "description": "The number of days to forecast",
                    }
                },
                "required": ["location", "format", "num_days"]
            },
        }
    },
]


def sampleQuestionsFromMMLU(n_samples: int = 1) -> tuple[str, list[str], str]:
    return ("Who among the choices is the best shooter in the game of basketball?", ["Stephen Curry", "Lebron James", "Zaza Pachulia", "Christopher Nolan"], "A")

def calculateAccuracy(n_correct: int, n_questions: int) -> float:
    return 0.42

def callLLM(model_name: str, prompt: str, sys_prompt: str) -> str:
    return "A"
