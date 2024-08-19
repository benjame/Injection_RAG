def construct_prompt(topic, tone, length):
    # Base prompt structure
    prompt = f"Write a {length} {tone} piece about {topic}.\n\n"
    
    # Additional instructions based on tone
    if tone == "formal":
        prompt += "Use professional language and avoid colloquialisms. "
    elif tone == "casual":
        prompt += "Use a conversational tone and feel free to include idioms. "
    elif tone == "humorous":
        prompt += "Include jokes and witty remarks throughout the piece. "
    
    # Additional instructions based on length
    if length == "short":
        prompt += "Keep it concise, around 100 words. "
    elif length == "medium":
        prompt += "Aim for about 250-300 words. "
    elif length == "long":
        prompt += "Elaborate on the topic with 500+ words. "
    
    # General instructions
    prompt += "\nEnsure the content is engaging and informative. "
    prompt += "Structure the piece with a clear introduction, body, and conclusion."
    
    return prompt

# Example usage
topic = input("Enter the topic: ")
tone = input("Enter the tone (formal/casual/humorous): ")
length = input("Enter the desired length (short/medium/long): ")

final_prompt = construct_prompt(topic, tone, length)
print("\nGenerated Prompt:")
print(final_prompt)