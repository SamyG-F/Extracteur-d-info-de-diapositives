from pptx import Presentation
import json
#from json import loads
from json import dumps

#print(prs.slides[0].shapes[0].text_frame.paragraphs[0].runs[0].text)
def parse_presentation(p):
    rv = {}
    if p.core_properties.title:
        if p.core_properties.title.strip() != '': rv['title'] = p.core_properties.title
    if p.core_properties.subject:
        if p.core_properties.subject.strip() != '': rv['subject'] = p.core_properties.subject
    if p.core_properties.keywords:
        if p.core_properties.keywords.strip() != '': rv['keywords'] = p.core_properties.keywords
    if p.core_properties.created:
        if p.core_properties.created != None: rv['created'] = str(p.core_properties.created)
    if p.core_properties.modified:
        if p.core_properties.modified != None: rv['modified'] = str(p.core_properties.modified)
    if p.core_properties.author:
        if p.core_properties.author.strip() != '': rv['author'] = p.core_properties.author
    rv['length'] = len(p.slides)
    rv['format'] = 'pptx'
    slides = []
    for i in range(len(p.slides)):
        s = p.slides[i]
        slide = {}
        slide['page'] = str(i+1)
        if s.shapes.title != None:
            slide['header'] = str(s.shapes.title.text)
        else:
            slide['header'] = ''
        paragraphs = []
        for shape in s.shapes:
            #paragraphs = []
            if shape.is_placeholder and shape.has_text_frame:
                phf = shape.placeholder_format
                #print('shape.placeholder_format idx=%d, type=%s' % (phf.idx, phf.type))
                type_paragraph = str(phf.type)
                #print(str(phf.type))
                for parag in shape.text_frame.paragraphs:
                    for run in parag.runs:
                        paragraph = {}
                        paragraph['text'] = run.text
                        paragraph['type'] = type_paragraph
                        if run.font.name != None: paragraph['font'] = run.font.name
                        if run.font.bold != None: paragraph['bold'] = run.font.bold
                        if run.font.italic != None: paragraph['italic'] = run.font.italic
                        if run.font.underline != None: paragraph['underline'] = run.font.underline
                        if run.font.size != None: paragraph['size'] = run.font.size    
                        if run.hyperlink.address != None: paragraph['href'] = run.hyperlink.address     #text_runs.append(run.text)
                        if run.font.color.type != None:
                            if run.font.color != None:                                     paragraph['color'] = str(run.font.color.rgb)
                        paragraphs.append(paragraph)
        slide['paragraphs'] = paragraphs
        slides.append(slide)
    rv['slides'] = slides
    return rv

prs = Presentation('../data/CM1_React.pptx')
p = parse_presentation(prs)
with open('test_Samy.txt', 'w', encoding='utf8') as json_file:
    json.dump(p, json_file, ensure_ascii=False, indent=2)