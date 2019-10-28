import json
from difflib import get_close_matches
from close_matches import handle_close_matches

def dictionary():
  source = open("data.json")
  json_data = json.load(source)

  word = input("Enter a word to search for: ")
  word = word.lower()
  
  # handle no inputs
  while not word or word not in json_data:
    # handle words not in dict
    if word:
      if not word in json_data:
        close_matches = get_close_matches(word, json_data.keys(), cutoff=0.8)
        if close_matches:
          word = handle_close_matches(word, close_matches)
        else:
          print("The word you searched for does not exist!")
          return
    else:
      print("You did not enter any value!")
      word = input("Enter a word to search for: ")

  definitions = json_data[word]
  # prettify output
  print()
  print("{}: {} {}:".format(word.capitalize(), len(definitions), "definition" if len(definitions)== 1 else "definitions"))
  for index, definition in enumerate(definitions):
    if len(definitions) == 1:
      print(definition)
    else:
      print('{}. {}'.format(index + 1, definition))
  print()

dictionary()