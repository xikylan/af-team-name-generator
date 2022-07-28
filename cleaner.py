

with open('./terms.txt', 'r') as input:
  terms = [term.lower() for term in input]

  with open('./terms_clean.txt', 'w') as output:
    for term in set(terms):
      output.write(term)
