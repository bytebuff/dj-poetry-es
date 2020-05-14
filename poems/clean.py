import os
import json

def all_file_name(path):
    return os.listdir(path)

def extract_poem(file_name):
    if 'DS_Store' not in file_name:
        with open(file_name, 'r', encoding='utf-8') as fp:
            poems = fp.read()
            json_poems = json.loads(poems)
            for poem in json_poems:
                title = poem['title']
                author = poem['author']
                paragraphs = ''.join(poem['paragraphs'])
                yield title, author, paragraphs

def run():
    all_file_names = all_file_name('./poemsdata/json')
    for file_name in all_file_names:
        print('正在处理>>', file_name)
        poems = extract_poem(f'./poemsdata/json/{file_name}')
        for poem in poems:
            yield poem
            

if __name__ == "__main__":
    # all_file_name('../poemsdata/json')
    poems = extract_poem('../poemsdata/json/poet.song.5000.json')
    for poem in poems:
        print(poem)
    