from datasets import load_dataset

dataset = load_dataset("cais/mmlu", "formal_logic")

def formatRow(row, q_no):
    choices = '\n'.join([f'{i+1}. {choice}' for i, choice in enumerate(row['choices'])])
    return f"""Question {q_no}: {row['question']} \n\nChoices:\n {choices} \n\nAnswer: {row['answer']}"""

