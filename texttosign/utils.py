import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

def load_folder_content(folder_path):
	folder_content = os.listdir(folder_path)
	return [item.replace(".gif", "") for item in folder_content]

def generate_prompt(text, word_list):
	return f"""Given a sentence, rephrase it using only words from a provided list. If the exact word is not present, substitute it with words that are almost the same, but only output words that are present in the list. Even conjunctions or nouns other than what present in the list is allowed. Only the words present in the below list. if even the substitute for a word can't be found, then ignore the word. The output should consist only the final sentence. Don't output any word which is not in the list. Always find the comparative closest substitute. Here is the sentence and the word list:
				Example Sentence: "The environment is very nice."
				Expected rephrase: "ENVIRONMENT VERY GOOD"
				Sentence to be converted : {text}
				Word list: {word_list}
			"""

def get_rephrased_text(prompt):
	client = OpenAI(api_key=OPEN_AI_API_KEY)
	completion = client.chat.completions.create(
		model="gpt-4",
		messages=[
			{"role": "user", "content": prompt},
		]
	)
	return completion.choices[0].message.content

def convert_to_sign_words(text, word_list):
	words = text.replace("\"", "").split(" ")
	sign_words = [word + ".gif" for word in words if word in word_list]
	return sign_words
