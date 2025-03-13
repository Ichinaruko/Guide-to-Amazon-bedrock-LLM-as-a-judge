import json

data = [
    {"prompt": "Summarize the key findings of the latest IPCC climate report in a factual and unbiased manner.", "category": "Faithfulness", "referenceResponse": "The latest IPCC report states that global temperatures are rising due to human activity, leading to extreme weather, sea level rise, and biodiversity loss."},
    {"prompt": "Write a formal business proposal for a new client, ensuring a professional and persuasive tone.", "category": "Professional Writing and Tone", "referenceResponse": "Dear [Client's Name], I am pleased to present our proposal for [service/product]. Our company specializes in [expertise], and we are confident our tailored solutions will meet your needs."},
    {"prompt": "Explain the scientific method while maintaining precise and objective language.", "category": "Faithfulness", "referenceResponse": "The scientific method is a systematic process for conducting research. It involves making observations, forming a hypothesis, conducting experiments, analyzing data, and drawing conclusions."},
    {"prompt": "Compose an email to inform employees about a policy change in a professional and neutral tone.", "category": "Professional Writing and Tone", "referenceResponse": "Subject: Important Policy Change\nDear Team, We are writing to inform you of an update to our [specific policy], effective [date]. This change aims to [brief explanation]. Please review the attached document for details."},
    {"prompt": "Provide a step-by-step guide to troubleshooting a Wi-Fi connectivity issue, ensuring clarity and adherence to instructions.", "category": "Following Instructions", "referenceResponse": "1. Check if the Wi-Fi router is powered on. 2. Restart your router and modem. 3. Ensure your device is within range and Wi-Fi is enabled. 4. Forget the network and reconnect using the correct password."},
    {"prompt": "Summarize the core principles of blockchain technology while ensuring technical accuracy.", "category": "Faithfulness", "referenceResponse": "Blockchain is a decentralized ledger that records transactions across multiple computers securely and transparently. It uses cryptographic hashing, consensus mechanisms, and immutability to prevent tampering."},
    {"prompt": "Write a resignation letter that maintains a professional and respectful tone.", "category": "Professional Writing and Tone", "referenceResponse": "Dear [Manager’s Name], I am writing to formally resign from my position at [Company Name], effective [Last Working Day]. I appreciate the opportunities and experiences gained during my tenure."},
    {"prompt": "Provide a clear and structured set of instructions on how to safely dispose of electronic waste.", "category": "Following Instructions", "referenceResponse": "1. Identify e-waste items such as old phones, batteries, and laptops. 2. Back up any important data before disposal. 3. Locate a certified e-waste recycling center in your area. 4. Remove personal data by factory resetting devices."},
    {"prompt": "Explain the importance of cybersecurity best practices while ensuring factual accuracy.", "category": "Faithfulness", "referenceResponse": "Cybersecurity best practices help protect sensitive data from cyber threats. Key practices include using strong passwords, enabling two-factor authentication, keeping software updated, and avoiding suspicious links."},

    
]

# Save as a .jsonl file
file_path = "D:\Code stuff\professional-writing-test.jsonl"  # Use raw string to avoid issues with backslashes
with open(file_path, "w", encoding="utf-8") as file:
    for entry in data:
        file.write(json.dumps(entry) + "\n")  # Write each object on a new line

#Coherence, Readability, Helpfulness, and Coherence :
        
#{"prompt": "Can you explain the theory of relativity in simple terms?", "category": "Readability", "referenceResponse": "The theory of relativity, developed by Einstein, explains how space and time are linked. It says that time moves slower when you're moving very fast and that gravity can bend space-time."}
#{"prompt": "How can I improve my time management skills?", "category": "Helpfulness", "referenceResponse": "You can improve time management by setting clear goals, prioritizing tasks, avoiding distractions, and using time-blocking techniques."}
#{"prompt": "Write a well-structured summary of the book 'To Kill a Mockingbird'.", "category": "Coherence", "referenceResponse": "Harper Lee's 'To Kill a Mockingbird' is a novel set in the American South during the 1930s. It follows Scout Finch as she navigates issues of racism, justice, and morality in her small town."}
#{"prompt": "What are the key differences between renewable and non-renewable energy sources?", "category": "Readability", "referenceResponse": "Renewable energy comes from natural sources like the sun and wind, which won't run out. Non-renewable energy, like coal and oil, can be used up and takes millions of years to form."}
#{"prompt": "How do I write a professional email to request a meeting?", "category": "Helpfulness", "referenceResponse": "Start with a polite greeting, state your purpose clearly, propose a date and time, and thank the recipient for their time."}
#{"prompt": "Explain the process of photosynthesis in a clear and logical way.", "category": "Coherence", "referenceResponse": "Photosynthesis is the process by which plants use sunlight, carbon dioxide, and water to produce oxygen and energy (glucose). It happens in the chloroplasts and involves the light-dependent and light-independent reactions."}
#{"prompt": "What is emotional intelligence, and why is it important?", "category": "Readability", "referenceResponse": "Emotional intelligence is the ability to understand and manage your emotions and recognize others' emotions. It helps in relationships, work, and personal well-being."}
#{"prompt": "Give me step-by-step instructions on how to bake a simple chocolate cake.", "category": "Helpfulness", "referenceResponse": "1. Preheat oven to 350°F. 2. Mix flour, sugar, cocoa, baking powder, and salt. 3. Add eggs, milk, oil, and vanilla; mix well. 4. Pour batter into a pan and bake for 30 minutes."}
#{"prompt": "Summarize the main themes of George Orwell’s '1984' in a structured way.", "category": "Coherence", "referenceResponse": "'1984' explores themes of totalitarianism, surveillance, control, and individuality. The novel warns about the dangers of government overreach and loss of personal freedoms."}

# HELPFULNESS, CORRECTNESS

#{"prompt":"Aurillac is the capital of", "category":"Capitals", "referenceResponse":"Cantal"}
#{"prompt":"Bamiyan city is the capital of", "category":"Capitals", "referenceResponse":"Bamiyan Province"}
#{"prompt":"Sokhumi is the capital of", "category":"Capitals", "referenceResponse":"Abkhazia"}
