import json

def dictionary():
  source = open("data.json")
  json_data = json.load(source)

  word = input("Enter a word to search for: ")
  
  # handle no inputs
  while not word or word == '':
    print("You did not enter any value!")
    word = input("Enter a word to search for: ")

  # handle words not in dict
  if not word in json_data:
    print("The word you searched for does not exist!")
    return

  definitions = json_data[word]
  for index, definition in enumerate(definitions):
    print('{}. {}'.format(index + 1, definition))

dictionary()