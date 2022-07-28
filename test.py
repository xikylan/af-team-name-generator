import heapq
import silabeador as sil
import spacy
from pyphonetics import RefinedSoundex
from sys import argv


def permute(name):
  syllables = sil.syllabify(name)
  permutations = [[name], syllables]

  for i in range(0, len(syllables)):
    permutations.append(syllables[0:i] + [''.join(syllables[i:i+2])] + syllables[i+2:])
    if permutations[0] == permutations[-1]:
      permutations.pop()

  return permutations


def score_lev(str1, str2):
  rs = RefinedSoundex()
  return rs.distance(str1, str2)


def score_spacy(str1, str2):
  return nlp(str1).similarity(nlp(str2))


def compute(name, method, top_n, count):
  if count == 2:
    return

  ranking = []

  with open('terms.txt', 'r') as f:
    terms = [term.lower() for term in f]

    for k, part in enumerate(name):
      perms = permute(part)

      for perm in perms:

        for i, syllable in enumerate(perm):

          for term in terms:

            if method == 'spacy':
              score = score_spacy(term, syllable)
            elif method == 'lev':
              score = score_lev(term, syllable)

            heapq.heappush(ranking, (score, term))

          # get x highest rated scores
          if method == 'spacy':
            top = heapq.nlargest(top_n, ranking, key=lambda x: x[0])
          elif method == 'lev':
            top = heapq.nsmallest(top_n, ranking, key=lambda x: x[0])

          # stores the recombined name/pun replaced name with no dupes
          new_names = set() 
          for t in top:
            new_names.add((t[0], ''.join(perm[0:i]) + t[1].rstrip() + ''.join(perm[i+1:])))

          # preserves names with mulitple words/parts
          # i.e. Pearl Jam -> Perl Jam (Jam is preserved)
          # i.e. Pearl Jam -> Pearl Gem (Pearl is preserved)
          # i.e. Pearl Jam -> Perl Gem (shouldn't be possible)
          printables = []
          for nn in new_names:
            print('score: ', nn[0])
            printable_name = name[0:k] + [nn[1]] + name[k+1:]
            printables.append(' '.join(printable_name))

            compute(printable_name, method, top_n, count + 1)

          print(printables)


if __name__ == "__main__":
  scorer, top_n, recurse = argv[1], int(argv[2]), argv[3]

  band_name = input("Enter input: ").split()

  if recurse.lower() == 'yes':
    compute(name=band_name, method=scorer, top_n=top_n, count=0)
  else:
    compute(name=band_name, method=scorer, top_n=top_n, count=1)
