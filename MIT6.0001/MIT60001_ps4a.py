# Problem Set 4A

def get_permutations(sequence):
  '''
  Enumerate all permutations of a given string

  sequence (string): an arbitrary string to permute. Assume that it is a
  non-empty string.  
  '''
  if len(sequence) == 1:
    return sequence
  # Otherwise, hold one constnat and call self
  ret = []
  for (i, letter) in enumerate(sequence):
    arr_seq = list(sequence)
    del arr_seq[i]
    for substr in get_permutations(''.join(arr_seq)):
      ret.append(letter + substr)
  # only reason list(set) is needed is if original had repeated letters
  return list(set(ret))

if __name__ == '__main__':
  example_input = 'abc'
  print('Input:', example_input)
  print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
  print('Actual Output:', get_permutations(example_input))