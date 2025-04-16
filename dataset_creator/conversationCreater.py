from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.storage import SQLStorageAdapter
from sqlalchemy import create_engine

class CustomSQLStorageAdapter(SQLStorageAdapter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Recreate the engine with custom pool settings
        self.engine = create_engine(
            self.database_uri,
            pool_size=20,        
            max_overflow=20,      
            connect_args={"check_same_thread": False}
        )

def setup_chatbot():
    chatbot = ChatBot(
        'CustomerSupportBot',
        logic_adapters=['chatterbot.logic.BestMatch'],
        storage_adapter='dataset_creator.customStorage.CustomSQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'
    )
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    return chatbot

chatbot_instance = setup_chatbot()

def generate_realistic_conversation():
    conversation_lines = []
    
    # Define a list of conversation prompts simulating customer messages.
    customer_prompts = [
        "Hi, I need help with my order.",
        "I've been waiting for my delivery for over a week.",
        "Thank you for your help, but I still need a resolution."
    ]
    
    # Start the conversation with the customer's initial prompt.
    current_input = customer_prompts[0]
    conversation_lines.append("Customer: " + current_input)
    
    # For each customer prompt, simulate an agent response and then a follow-up from the customer.
    for prompt in customer_prompts[1:]:
        # Get the agent's response based on the previous customer input.
        agent_response = chatbot_instance.get_response(current_input)
        conversation_lines.append("Agent: " + str(agent_response))
        
        # Now simulate the next customer message.
        current_input = prompt
        conversation_lines.append("Customer: " + current_input)
    
    # Final agent response for the last customer input.
    agent_response = chatbot_instance.get_response(current_input)
    conversation_lines.append("Agent: " + str(agent_response))
    
    return "\n".join(conversation_lines)
