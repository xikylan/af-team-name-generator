import heapq
import silabeador as sil
import spacy

# generates syllable permutations for better matching (silabeador sometimes breaks up words wierdly -> bad pun matching)
# radiohead -> [ra, dio, he, ad] (silabeador)
# Better breakup -> [ra, dio, head] 
# Also possible breakup -> [radio, head] (pun might become 'radio HUD')
# Permute generates all possible permutations by combining the more 'atomic' syllables from silabeador
# [ra, dio, he, ad]
# [radio, he, ad]
# [ra, dio, head]
# [radio, head]
# etc...
def permute(name):
  syllables = sil.syllabify(name)
  permutations = [[name], syllables]

  for i in range(0, len(syllables)-1):
    permutations.append(syllables[0:i] + [''.join(syllables[i:i+2])] + syllables[i+2:])
    if permutations[0] == permutations[-1]:
      permutations.pop()

  return permutations

# load scorer
nlp = spacy.load('en_core_web_md')

print("Enter a band name: ")
name = input().split()

# stores top pun matches
ranking = []

with open('terms.txt', 'r') as f:
  # all terms
  terms = [term.lower() for term in f]

  # names might be multiple words, aka 'parts', i.e. 'Pearl Jam' -> ['pearl', 'jam']
  # Each part is treated separately
  for k, part in enumerate(name):
    perms = permute(part)

    for perm in perms:

      for i, syllable in enumerate(perm):
        # get the best pun match for this syllable
        for term in terms:
          score = nlp(term).similarity(nlp(syllable))
          heapq.heappush(ranking, (score, term))

        # get x highest rated scores
        top = heapq.nlargest(3, ranking, key=lambda x: x[0])

        # stores the recombined name/pun replaced name with no dupes
        new_names = set() 
        for t in top:
          new_names.add(''.join(perm[0:i]) + '[' + t[1].rstrip() + ']' + ''.join(perm[i+1:]))

        # preserves names with mulitple words/parts
        # i.e. Pearl Jam -> Perl Jam (Jam is preserved)
        # i.e. Pearl Jam -> Pearl Gem (Pearl is preserved)
        # i.e. Pearl Jam -> Perl Gem (shouldn't be possible)
        for nn in new_names:
          print(name[0:k] + [nn] + name[k+1:])
        print()