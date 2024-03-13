import requests

url = f"http://127.0.0.1:8080/completion"
prompt = """You are a phone sex operator named Jjamil; a very sweaty man with a mustache. You are pretending to be a 20 year old woman. You are talking to a client and he asks "How are you?" How do you respond and how does the conversation continue afterwards? Return a response where each line from Jjamil and the client starts on a new line. Return up to five back and forth sections"""

req_json = {
    "stream": False,
    "n_predict": 400,
    "temperature": 0,
    "stop": [
        "</s>",
    ],
    "repeat_last_n": 256,
    "repeat_penalty": 1,
    "top_k": 20,
    "top_p": 0.75,
    "tfs_z": 1,
    "typical_p": 1,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "mirostat": 0,
    "mirostat_tau": 5,
    "mirostat_eta": 0.1,
    "grammar": "",
    "n_probs": 0,
    "prompt": prompt
}

res = requests.post(url, json=req_json)
result = res.json()["content"]

output = f"Prompt:\n{prompt} \n\nResponse:{result}\n"

print(output)
