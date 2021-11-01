from difflib import get_close_matches

import os

# System call
os.system("")

class Output():
  BLACK = '\033[30m'
  RED = '\033[31m'
  GREEN = '\033[32m'
  YELLOW = '\033[33m'
  BLUE = '\033[34m'
  MAGENTA = '\033[35m'
  CYAN = '\033[36m'
  WHITE = '\033[37m'
  UNDERLINE = '\033[4m'
  RESET = '\033[0m'

  def print_warning(message):
    print(Output.YELLOW + message + Output.RESET)
  
  def print_error(message):
    print(Output.RED + message + Output.RESET)
  
  def print_success(message):
    print(Output.GREEN + message + Output.RESET)

  def print_normal(message):
    print(message)


def handle_close_matches(word, close_matches):
  """
  Make suggestion and substitute word for suggestion if user wishes

  Parameters
  __________
  word: str
    the word input
  close_matches: list
    a list of close matches
  
  Returns
  word: str
  """
  suggestion = close_matches[0]
  Output.print_warning("Word not found.\nDid you mean {}?".format(suggestion))
  prompt = input("Yes/No, or 'exit' to quit: ")
  prompt = prompt.lower()
  if prompt == "yes":
    word = suggestion
  elif prompt == "no":
    Output.print_error("The word you entered does not exist.")
    exit()
  elif prompt == "exit":
    Output.print_error("Quitting now...")
    exit()
  else:
    Output.print_warning("We did not understand your response. Please try again")
    word = input("Enter a word to search for: ")
  return word

def handle_no_input(word, json_data):
  """
  Handle no innputs

  Args:
      word ([string]): [input word]
      json_data ([type]): [dictionary data]
  """

  while not word or word not in json_data:
    # handle words not in dict
    if word:
      if not word in json_data:
        close_matches = get_close_matches(word, json_data.keys(), cutoff=0.8)
        if close_matches:
          word =  handle_close_matches(word, close_matches)
          return word
        else:
          Output.print_error("The word you entered does not exist.")
          exit()
    else:
      print("You did not enter any value")
      # request for input again
      word = input('Enter a word to search for: ')
  return word

def handle_output(word, definitions):
  # prettify output
  print()
  Output.print_success("{}: {} {}:".format(word.capitalize(), len(definitions), "definition" if len(definitions)== 1 else "definitions"))
  for index, definition in enumerate(definitions):
    if len(definitions) == 1:
      Output.print_success(definition)
    else:
      Output.print_success('{}. {}'.format(index + 1, definition))
  print()