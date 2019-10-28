import json
from difflib import get_close_matches

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
          # make suggestion and substitute word for suggestion if user wishes
          suggestion = close_matches[0]
          print("Word not found.\nDid you mean {}?".format(suggestion))
          prompt = input("Yes/No, or 'exit' to quit: ")
          if prompt == "Yes":
            word = suggestion
          elif prompt == "NO":
            print("The word you searched for does not exist!")
            return
          elif prompt == "exit":
            print("Quitting now...")
            return
          else:
            print("We did not understand your response. Please try again")
            word = input("Enter a word to search for: ")
        else:
          print("The word you searched for does not exist!")
          return
    else:
      print("You did not enter any value!")
      word = input("Enter a word to search for: ")

  definitions = json_data[word]
  # prettify output
  print()
  print("{}: ".format(word.capitalize()))
  for index, definition in enumerate(definitions):
    print('{}. {}'.format(index + 1, definition))
  print()

dictionary()