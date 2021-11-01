import json
from utils import handle_no_input, handle_output

def dictionary():
  source = open("data.json")
  json_data = json.load(source)

  word = input("Enter a word to search for: ")
  word = word.lower()

  word = handle_no_input(word, json_data)
  definitions = json_data[word]

  handle_output(word, definitions)

dictionary()