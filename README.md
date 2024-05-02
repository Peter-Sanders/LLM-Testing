# LLM-Testing
Playing around with LLama2 on my laptop



Requirements:
    install coda environment from environment.yml
    download and install the llama2 7b models from Meta
        can easily modify to pass an auth token and retrieve from hugging face
        This will create the llama directory which contians the llama python package
    create a models directory next to llama 
        run something like this to get the gguf model file from huggingface
            huggingface-cli download TheBloke/Llama-2-13B-chat-GGUF llama-2-13b-chat.q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
    create an images directory if you want to try and use the multi-modal model 
        (NOTE: I don't think passing an image actually works with my current config, and the model just hallucinates a beach or something)

Execution:
    change to the function of your choice in __main__
    the run;

    conda activate llm 
    python llmcpptest.py

Can now also run from llama.cpp server:
    run this in one terminal;
        ./server -m ../../models/llama-2-7b-chat.Q2_K.gguf -c 2048 -t 8 -ngl 33 -mg 0 -spf system_prompt.json
    edit server_interact.py to change the prompt, then run;
        python server_interact.py

server_interact.py is depreceated and I'll delete it once  I'm confident I won't need it in the near future (probs the enxt commit it goes)
the system prompt file is stored in the same llama.cpp repo that the ./server command should be run from


This now requires the llama.cpp repository stored in the /cpp dir 
You'll need to checkout and store that repo there;


FastAPI Integration:

Can now pass in a prompt from FastAPI. Ain't that neat
localhost/chat/prompt will return a prompt of your choosing
just make sure to run uvicorn main:app --reload or somethig to spool up FastAPI in addition to the llamacpp server. It should return a 500 if the llama server isn't running but I'm dumb so the check probably isn't very robust




TODO: dockerize this OR create a makefile so these instructions can be run by just doing a "make -f makefile" 
TODO: get llama3 in here. Maybe not 2-bit quantized but for sure the 8 billion version
TODO: do some RAG somehow
