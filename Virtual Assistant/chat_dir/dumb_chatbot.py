from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import sys
sys.path.insert(0,'../src')
import text_speech
# # Uncomment the following line to enable verbose logging
# # import logging
# # logging.basicConfig(level=logging.INFO)
#
# # Create a new instance of a ChatBot
# bot = ChatBot(
#     "Terminal",
#     storage_adapter="chatterbot.storage.SQLStorageAdapter",
#     input_adapter="chatterbot.input.TerminalAdapter",
#     output_adapter="chatterbot.output.TerminalAdapter"
# )
# bot.set_trainer(ChatterBotCorpusTrainer)
#
# bot.train("chatterbot.corpus.english")
#
#
# CONVERSATION_ID = bot.storage.create_conversation()
#
#
# def get_feedback():
#     from chatterbot.utils import input_function
#
#     text = input_function()
#
#     if 'yes' in text.lower():
#         return False
#     elif 'no' in text.lower():
#         return True
#     else:
#         print('Please type either "Yes" or "No"')
#         return get_feedback()
#
#
# print("Type something to begin...")
#
# # The following loop will execute each time the user enters input
# while True:
#     try:
#         input_statement = bot.input.process_input_statement()
#         statement, response = bot.generate_response(input_statement, CONVERSATION_ID)
#
#         bot.output.process_response(response)
#         print('\n Is "{}" a coherent response to "{}"? \n'.format(response, input_statement))
#         if get_feedback():
#             print("please input the correct one")
#             response1 = bot.input.process_input_statement()
#             bot.learn_response(response1, input_statement)
#             bot.storage.add_to_conversation(CONVERSATION_ID, statement, response1)
#             print("Responses added to bot!")
#
#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break
chatbot = ChatBot('Corolla', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
def train():
	chatbot.train("chatterbot.corpus.english")
# chatbot = ChatBot('Alexa', trainer='chatterbot.trainers.UbuntuCorpusTrainer')
# chatbot.train()
def chat():
	while True:
	    user_input = raw_input('You : ')
	    # print(user_input)
	    if user_input == str('quit'):
	        break
	    try:
	        response = chatbot.get_response(user_input)
	        #print(response)
	        text_speech.say(str(response))
	    except(KeyboardInterrupt, EOFError, SystemExit):
	        text_speech.say("Sorry An Error has occured.")
	    

#train()
#chat()