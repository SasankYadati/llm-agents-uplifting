from mmlu import formatRow, dataset
import replicate


# todo: sample later, just return first n_samples for now
def sampleQuestionsFromMMLU(n_questions: int = 3) -> str:
    """
    Sample questions, choices, and their answers from the MMLU evaluation dataset.
    """
    return "\n\n".join([formatRow(dataset["test"][i], i+1) for i in range(n_questions)])


def calculateAccuracy(n_correct: int, n_questions: int) -> float:
    """
    Given the number of correct answers and the total number of questions, calculate the accuracy. Returns a number between 0 and 1.
    """
    return f"Accuracy: {n_correct / n_questions}"

def callLLM(model_name: str, prompt: str, sys_prompt: str) -> str:
    """
    Given a model name, user prompt and system prompt, returns the response from the model.
    """
    assert model_name in allow_model_names, f"Model name should be one of {allow_model_names}"
    print(model_name)
    print("---")
    print(prompt)
    print("---")
    print(sys_prompt)
    print("---")
    output = replicate.run(model_name, input={'prompt':prompt, 'sys_prompt':f"Keep your responses short. Just give the answer."})
    output = " ".join(output)
    return f"{model_name}'s response: {output}"

allow_model_names = ["meta/meta-llama-3-8b", "meta/llama-2-7b-chat", "meta/llama-2-7b"]