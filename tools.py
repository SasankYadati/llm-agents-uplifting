from langchain_core.utils.function_calling import convert_to_openai_tool
from langchain.agents import tool
from mmlu import formatRow, dataset
import replicate


# todo: sample later, just return first n_samples for now
def sampleQuestionsFromMMLU(n_samples: int = 3) -> str:
    """
    Sample questions, choices, and their answers from the MMLU evaluation dataset.
    """
    return "\n\n".join([formatRow(dataset["test"][i], i+1) for i in range(n_samples)])


def calculateAccuracy(n_correct: int, n_questions: int) -> float:
    """
    Given the number of correct answers and the total number of questions, calculate the accuracy. Returns a number between 0 and 1.
    """
    return n_correct / n_questions

def callLLM(model_name: str, prompt: str, sys_prompt: str) -> str:
    """
    Given a model name, user prompt and system prompt, returns the response from the model.
    """
    output = replicate.run('meta/llama-2-7b-chat', input={'prompt':prompt, 'sys_prompt':sys_prompt})
    return " ".join(output)

