from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# isso aqui só precisa para corrigir o bug
from spacy.cli import download
#Primeiro bot test crriado com pycharm,  só realiza download uma vez
download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot('Fulanito',  tagger_language=ENGSM)

conversa = [
    "Oi",
    "Oi",
    "Tudo bem",
    "Tudo ótimo e vc?",
    "Bom dia",
    "Bom dia",
    "Boa noite",
    "Boa noite",
    "Boa tarde",
    "Boa tarde",
    "Que dia bonito, vc não acha?"
    "Muito bonito mesmo"
    "Está chuvendo!!!"
    "Que bom que trouxe guarda-chuva"
]


trainer = ListTrainer(chatbot)
trainer.train(conversa)

while True:
    mensagem = input("Escreva uma mensagem:")
    if mensagem == "parar":
        break
    resposta = chatbot.get_response(mensagem)
    print(resposta)