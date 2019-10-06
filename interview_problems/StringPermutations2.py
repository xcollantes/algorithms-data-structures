"""Return all permutations of given string."""


def main():
  s = 'abc'
  print(permute(s))


def permute(s):
  out = []

  if len(s) == 1:
    out = [s]

  for i,letter in enumerate(s):

    for perm in permute(s[:i] + s[i + 1:]):
      out = out + [letter + perm]


  return out


if __name__=='__main__':
  main()
