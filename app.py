import asyncio
from flask import Flask, request, jsonify
from rasa.core.agent import Agent

app = Flask(__name__)

agent = Agent.load("models\\20240103-215314-hot-flat.tar.gz")

async def handle_user_message(user_message):
    return await agent.handle_text(user_message)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    user_message = data["message"]

    # Cria um novo loop de eventos
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Use asyncio para aguardar a conclusão da corrotina
    response = loop.run_until_complete(handle_user_message(user_message))

    # Extrai a resposta do Rasa
    response_text = response[0]['text'] if response and len(response) > 0 else ""

    # Limpa o loop de eventos
    loop.close()

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(port=5005)
