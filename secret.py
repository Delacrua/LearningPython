def recoverSecret(triplets):
    secret = []
    for triplet in triplets:
        x = triplet[0]
        y = triplet[1]
        z = triplet[2]
        if x not in secret:
            secret.insert(0, x)
        if y not in secret:
            secret.insert(secret.index(x) + 1, y)
        else:
            secret.pop(secret.index(y))
            secret.insert(secret.index(x) + 1, y)
        if z not in secret:
            secret.insert(secret.index(y) + 1, z)
        else:
            secret.pop(secret.index(z))
            secret.insert(secret.index(y) + 1, z)

    return ''.join(secret)


triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))