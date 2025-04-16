import json

def summarize_chunk(chunk, llm_api):
    prompt = (
        "Please summarize the key insights, trends, and common issues "
        "found in the following customer support conversations:\n" +
        "\n".join(chunk)  
    )
    summary = llm_api(prompt)
    return summary

def hierarchical_summarization(data_file, llm_api, chunk_size=1000):
    summaries = []
    chunk = []
    
    # Read data line-by-line
    with open(data_file, "r") as f:
        for line in f:
            record = json.loads(line)
            chunk.append(record["conversation"])
            if len(chunk) >= chunk_size:
                chunk_summary = summarize_chunk(chunk, llm_api)
                summaries.append(chunk_summary)
                chunk = []
                
    # Process any leftover records in the last chunk
    if chunk:
        chunk_summary = summarize_chunk(chunk, llm_api)
        summaries.append(chunk_summary)
        
    # Now summarize the summaries
    final_prompt = (
        "Based on the following summaries of customer support conversations, "
        "provide an overall summary highlighting the main trends and issues:\n" +
        "\n".join(summaries)
    )
    final_summary = llm_api(final_prompt)
    return final_summary