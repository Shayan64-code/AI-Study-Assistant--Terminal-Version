from openai import OpenAI
import Keys

client= OpenAI(api_key= Keys.KEY1,
base_url= "https://openrouter.ai/api/v1")

messages= [{"role": "system", "content": ("You are a kindful study assistant.",
                                          "You tell them all the important points to memorize for exam.", 
                                          "You also solve their code related problems in easy way.")
                                          }]

while True:

    message = input("User: ")
    print("-" * 40)

    if message.lower() == "exit":
        print("Good Luck for Exams")
        print("-" * 40)
        break

    messages.append({"role": "user", "content": message})

    try:
        chat = client.chat.completions.create(
            messages=messages,
            model= "nvidia/nemotron-3-nano-30b-a3b:free",
            temperature= 0.5,
            max_tokens= 400,
        )
        reply = chat.choices[0].message.content

        messages.append({"role": "assistant", "content": reply})

        print("Nvidia: ", reply)

    except Exception as e:
        print("Error: ", e)