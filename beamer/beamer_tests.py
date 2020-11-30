import re
import json
from json import loads # from text to object
from json import dumps # from object to text
from time import time

def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('temps passé = ', after - before)
        return rv
    return f


def applyRegexps(text, listRegExp):
    for element in listRegExp:
        print(element)
        left = element['left']
        right = element['right']
        r=re.compile(left)
        text=r.sub(right,text)
    return text

#take a beamer file
@timer
def search_properties(beamer_path):
    with open(beamer_path, 'r') as f:
        text = f.read()   
        p = re.search(r'^\\author\{(.*)\}.*$', text, re.M|re.I)
        if p:
            print('p.group() = ', p.group())
            print('p.group(1) = ', p.group(1))
        else:
            print('pas d\'auteur trouvé')



#param : path to a beamer file
#return a dictionary
@timer
def add_properties(beamer_path):
    pres = {}
    with open(beamer_path, 'r') as f:
        text = f.read()
        #add an author to the presentation definition
        p = re.search(r'^\\author\{(.*)\}.*$', text, re.M|re.I)
        if p: pres['author'] = p.group(1)
        p = re.search(r'^\\title\{(.*)\}.*$', text, re.M|re.I)
        if p: pres['title'] = p.group(1)
        p = re.search(r'^\\date\{(.*)\}.*$', text, re.M|re.I)
        if p: pres['modified'] = p.group(1)
        p = re.search(r'^\\subject\{(.*)\}.*$', text, re.M|re.I)
        if p: pres['subject'] = p.group(1)
        #\keywords is not a native LateX command, here we suppose that if keywords appear in the presentation,
        # it's in a custom command named 'keywords' (we found this style a common practice)
        p = re.search(r'^\\keywords\{(.*)\}.*$', text, re.M|re.I)
        if p: pres['keywords'] = p.group(1)
        p = re.findall(r'^\\begin\{(frame)\}.*$', text, re.M|re.I)
        if len(p) > 0:
            pres['length'] = len(p)
        pres['format'] = 'beamer'
    return pres

def add_content(pres, beamer_path):
    with open(beamer_path, 'r') as f:
        text = f.read().replace('\n', '')
        print(text)
        my_pattern = r'\\begin\{frame\}\{(.*)\}(.*)\\end\{frame\}.*'
        my_regex = re.compile(my_pattern, re.DOTALL|re.IGNORECASE)
        p = my_regex.findall(text)
        print('\n')
        print(min(p, key=len))
        print('\n')
        if len(p) > 0:
            print(p, len(p))
        pres['slides'] = []
        num_slide = 0
        for text in p:
            num_slide = num_slide + 1
            dic = {}
            dic['slide_number'] = num_slide
            dic['title'] = text[0]
            dic['content'] = text[1]
            pres['slides'].append(dic)
        print('\n')
    return pres 

def create_Json(pres, filename):
    with open(filename, 'w', encoding='utf8') as json_file:
        json.dump(pres, json_file, ensure_ascii=False, indent=2)
    

create_Json((add_content(add_properties('presentation_test1.beamer'), 'presentation_test1.beamer')), 'presentation_test1_beamer_Json')