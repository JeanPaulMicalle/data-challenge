import os
from dataset_creator.createFakeData import generate_customer_support_data
from config.configLoader import load_config
from ollama.apiCall import my_llm_api
from summarizor.chunkSummarizer import hierarchical_summarization

def main():
    # Load configuration from the YAML file.
    config = load_config()
    
    # Retrieve the output directory from the config.
    output_dir = config["output_dir"]
    
    # Define the data file path where the JSON Lines file will be generated.
    data_file = os.path.join(output_dir, "customer_support_conversations.jsonl")
    
    # Ensure the output directory exists.
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate fake customer support data.
    #print("Generating fake data...")
    #generate_customer_support_data(output_dir)
    #print("Data generation complete!")
    
    # Run hierarchical summarization on the generated data using your API call wrapper.
    print("Summarizing data using Ollama API...")
    final_summary = hierarchical_summarization(data_file, my_llm_api)
    
    # Output the final summary.
    print("\nFinal Summary of Customer Support Conversations:")
    print(final_summary)

if __name__ == "__main__":
    main()
