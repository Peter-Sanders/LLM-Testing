def lang(model_path:str):
    from langchain.callbacks.manager import CallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate
    from langchain_community.llms import LlamaCpp


    template = """Question: {question}

    Answer: Let's work this out in a step by step way to be sure we have the right answer."""

    prompt = PromptTemplate.from_template(template)

# Callbacks support token-wise streaming
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

    llm = LlamaCpp(
        model_path=model_path,
        n_gpu_layers=-1,
        n_ctx=2048,
        n_batch=512,
        temperature=0.75,
        max_tokens=2000,
        top_p=1,
        callback_manager=callback_manager,
        verbose=True,  # Verbose is required to pass to the callback manager
    )

    prompt = """
    Question: A rap battle between Stephen Colbert and John Oliver
    """
    llm.invoke(prompt)



def chat(model_path:str):
    from llama_cpp import Llama 
    llm = Llama(model_path=model_path,
                chat_format="llama-2",
                n_ctx=100,
                n_batch=100,
                n_gpu_layers=-1,
                main_gpu=0,
                )

    # output = llm(
    #       "Q: Name the planets in the solar system? A: ", # Prompt
    #       max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
    #       stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
    #       echo=True # Echo the prompt back in the output
    # ) # Generate a completion, can also call create_completion
    # print(output)


def multi(model_path:str):
    import os
    from llama_cpp import Llama
    from llama_cpp.llama_chat_format import Llava15ChatHandler
    chat_handler = Llava15ChatHandler(clip_model_path="./models/mmproj-model-f16.gguf")

    n_batch = 512
    llm = Llama(
      model_path=model_path,
      chat_handler=chat_handler,
      n_ctx=512, # n_ctx should be increased to accomodate the image embedding
      logits_all=True,# needed to make llava work
      main_gpu=1,
      n_batch=n_batch,
    )
    image_dir = "./images/"
    for img in os.listdir(image_dir):
        print(img)
        if img.endswith(".jpg"):
            img_path = os.path.join(os.getcwd(), image_dir)
            img_path = os.path.join(img_path, img)

            output = llm.create_chat_completion(
                messages = [
                    {"role": "system", "content": "You are an assistant who perfectly describes images."},
                    {
                        "role": "user",
                        "content": [
                            {"type": "image_url", "image_url": {"url": f"file://{img_path}"}},
                            {"type" : "text", "text": "Describe this image in detail please."}
                        ]
                    }
                ]
            )
            print(output)


def ctrans(model_path:str):
    from ctransformers import AutoModelForCausalLM
    llm = AutoModelForCausalLM.from_pretrained(model_path, 
                                               model_type="llama", gpu_layers=50)

    print(llm("AI is going to"))


if __name__ == "__main__":
    model_path="./models/llama-2-7b-chat.Q2_K.gguf"#"./models/llama-2-7b-chat.q4_K_M.gguf"
    chat(model_path)
