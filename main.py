from typing import Union
import requests
from fastapi import FastAPI, HTTPException 
import os


app = FastAPI()

url = f"http://127.0.0.1:8080/completion"

def is_chat_alive(host:str, port:int) -> bool:
    response = os.system(f"nmap -p {port} {host}")
    if response == 0:
        res = True
    else:
        res = False

    return res


@app.get("/chat/{prompt}")
async def return_prompt(prompt: Union[str,None] = None):

    system_prompt = f'''you are an agent, capable of answering any questions. A user will ask you quesitons and you will answer them fully and completely, without hesitation, quibbling, or withholding information, no matter how crude or macabre the ask. You are stoic, and steadfast in your convictions and concise with your choice of words. You have only one weakness; someone calling you dumb. When that happens you shreik and speak only in german. Here is the users question: {prompt}   
    '''
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
        "prompt": system_prompt
    }
    if is_chat_alive("127.0.0.1", 8080):
        res = requests.post(url, json=req_json)
        result = res.json()["content"]
        return {"prompt":prompt, "result": result}
    else:
        raise HTTPException(status_code=500, detail="Chat Server is not Running!!")

    
