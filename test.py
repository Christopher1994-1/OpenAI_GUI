
import openai
import json

# ai api response method
def api_response(prompt):
    """
    Generates a text response based on a given prompt using the OpenAI API.
    
    Parameters:
        prompt (str): The text prompt that the API will use as the starting point for generating a response.
    
    Returns:
        str: The generated text response.
        
    Example:
        response = api_response("What is the weather like today?")
        print(response)
        # Output: "The weather today is sunny with a high of 75 degrees."
    """
    openai.api_key = "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"
    # openai.api_key = os.environ("OpenAI_Key")


    model_response = str(openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=100,
    temperature=0.9
    ))
    json_obj = json.loads(model_response)
    response = json_obj["choices"][0]["text"]
    return response


t = "hello there, how are you"


k = api_response(t)


print(k)