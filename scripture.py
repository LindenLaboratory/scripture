def prompts(path):
    with open(path, 'r') as file: csv_reader = csv.reader(file);promptslst = [row[0] for row in csv_reader]
    return promptslst
import csv;from difflib import SequenceMatcher;promptslst = prompts("data.csv")
def evaluate(user_prompt, prompts):
    best_match,highest_similarity = None,0
    for prompt in prompts:
        similarity = SequenceMatcher(None, user_prompt, prompt).ratio()
        if similarity > highest_similarity: highest_similarity = similarity;best_match = prompt
    return best_match
def query(user_prompt):
    similar_prompt = evaluate(user_prompt, promptslst)
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == similar_prompt: return row[1]
    return "No answer found."
