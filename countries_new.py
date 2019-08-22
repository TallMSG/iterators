import json
import wikipedia


class Coutries:
  def __init__(self, path):
    self.path = path
    with open(path, encoding="utf-8") as file:
      self.data = json.load(file)
    self.counter = 0

  def __iter__(self):
    return self

  def __next__(self):
    self.counter += 1
    if self.counter < 2:
      countries_list = []
      for item in self.data:
        country_name_dict = item['name']['common']
        countries_list.append(country_name_dict)
        wiki_url = []
        for i in countries_list:
          try:
            a = wikipedia.page(i).url
          except wikipedia.exceptions.DisambiguationError as e:
            a = wikipedia.page(e.options[0]).url
          wiki_url.append(a)
      countries_url = dict(zip(countries_list, wiki_url))
      return countries_url
    else:
      raise StopIteration

def countries_wiki(inp, out):
  for item in Coutries(inp):
    dicty = item
  with open(out,'w', encoding="utf-8") as output:
    for k, v in dicty.items():
      output.write('{} - {}\n'.format(k, v))


if __name__ == '__main__':
  countries_wiki('countries.json', 'countries_wiki_new.txt')










    