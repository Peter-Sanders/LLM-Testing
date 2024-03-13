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
        ./server -m ../../models/llama-2-7b-chat.Q2_K.gguf -c 2048 -t 8 -ngl 33 -mg 0
    edit server_interact.py to change the prompt, then run;
        python server_interact.py

This now requires the llama.cpp repository stored in the /cpp dir 
You'll need to checkout and store that repo there;

TODO: dockerize this OR create a makefile so these instructions can be run by just doing a "make -f makefile" 

