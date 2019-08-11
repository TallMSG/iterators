import hashlib

def get_hash(path):
  with open(path, encoding='utf8') as file:
    for string in file:
      line_hash = hashlib.md5(string.encode("utf-8")).hexdigest()
      yield line_hash

if __name__ == '__main__':
    for el in get_hash('countries_wiki.txt'):
        print(el)