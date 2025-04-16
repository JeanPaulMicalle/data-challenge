import os
import json
import random
from faker import Faker
from dataset_creator.conversationCreater import generate_realistic_conversation

def generate_customer_support_data(output_dir, output_filename="customer_support_conversations.jsonl", num_records=10):
    fake = Faker()
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, output_filename)
    
    with open(output_file, "w") as f_out:
        for i in range(num_records):
            conversation_text = generate_realistic_conversation()

            record = {
                "datetime": fake.iso8601(),          
                "agent_name": fake.name(),             
                "customer_id": fake.uuid4(),          
                "conversation": conversation_text, 
                "status": random.choice(["open", "closed"]),
                "resolved": random.choice([True, False])
            }
            f_out.write(json.dumps(record) + "\n")
            
            if i % 10000 == 0 and i > 0:
                print(f"Generated {i} records.")
    print("Data generation complete. File saved at:", output_file)
