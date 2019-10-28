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
  print("Word not found.\nDid you mean {}?".format(suggestion))
  prompt = input("Yes/No, or 'exit' to quit: ")
  if prompt == "Yes".lower():
    word = suggestion
  elif prompt == "NO".lower():
    print("The word you searched for does not exist!")
    exit()
  elif prompt == "exit".lower():
    print("Quitting now...")
    exit()
  else:
    print("We did not understand your response. Please try again")
    word = input("Enter a word to search for: ")
  return word