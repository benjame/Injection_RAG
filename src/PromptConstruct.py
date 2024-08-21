def construct_prompt(topic, tone, length):
    # Prompt options dictionary
    tone_options = {
        "formal": "Use professional language and avoid colloquialisms.",
        "casual": "Use a conversational tone and feel free to include idioms.",
        "humorous": "Include jokes and witty remarks throughout the piece."
    }
    
    length_options = {
        "short": "Keep it concise, around 100 words.",
        "medium": "Aim for about 250-300 words.",
        "long": "Elaborate on the topic with 500+ words."
    }
    
    # Base prompt structure
    prompt = f"Write a {length} {tone} piece about {topic}.\n\n"
    
    # Add instructions based on tone
    prompt += tone_options.get(tone, "Use an appropriate tone.") + " "
    
    # Add instructions based on length
    prompt += length_options.get(length, "Use an appropriate length.") + " "
    
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