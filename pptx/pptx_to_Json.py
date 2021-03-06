# https://docs.python.org/3.8/library/json.html
import json
from json import loads # from text to object
from json import dumps # from object to text

from pptx import Presentation

prs = Presentation('../data/CM1_React.pptx')

def parse_pptx_presentation (presentation):
    # Parsing a pptx presentation and return a json object
    # slides > paragraph > run
    #https://python-pptx.readthedocs.io/en/latest/api/presentation.html#pptx.presentation.Presentation
    prs = dict()

    if presentation.core_properties.title:
        if presentation.core_properties.title.strip() != '': prs['title'] = presentation.core_properties.title
    if presentation.core_properties.subject:
        if presentation.core_properties.subject.strip() != '': prs['subject'] = presentation.core_properties.subject
    if presentation.core_properties.keywords:
        if presentation.core_properties.keywords.strip() != '': prs['keywords'] = presentation.core_properties.keywords
    if presentation.core_properties.created:
        if presentation.core_properties.created != None: prs['created'] = str(presentation.core_properties.created)
    if presentation.core_properties.modified:
        if presentation.core_properties.modified != None: prs['modified'] = str(presentation.core_properties.modified)
    if presentation.core_properties.author:
        if presentation.core_properties.author.strip() != '': prs['author'] = presentation.core_properties.author
    prs['length'] = len(presentation.slides)
    prs['format'] = 'pptx'
    slides = []
    for i in range(0, len(presentation.slides)):
        #https://python-pptx.readthedocs.io/en/latest/api/slides.html#pptx.slide.Slide
        s = presentation.slides[i]
        slide = dict()
        # alternative: s.slide_id ; unique identifier whatever the position
        slide['page'] = str(i+1)
        if s.shapes.title != None:
            slide['header'] = str(s.shapes.title.text)
        else:
            slide['header'] = ''
        
        text_frames = []
        for shape in s.shapes:
            #print (shape)
            frame = dict()
            if shape.is_placeholder:
                #print('shape.is_placeholder')
                phf = shape.placeholder_format
                #print('shape.placeholder_format idx=%d, type=%s' % (phf.idx, phf.type))
                frame['type'] = str(phf.type)
                #print ("Presentation.slides[].placeholders[{}]={}".format(s.placeholders[phf.idx].text))
                #text_frame = shape.text_frame
            if shape.has_text_frame:
                    paragraphs = []
                    for paragraph in shape.text_frame.paragraphs:
                        runs = []
                        for run in paragraph.runs:
                            feats = dict()
                            feats['text'] = run.text
                            if run.font.name != None: feats['font'] = run.font.name
                            if run.font.bold != None: feats['bold'] = run.font.bold
                            if run.font.italic != None: feats['italic'] = run.font.italic
                            if run.font.underline != None: feats['underline'] = run.font.underline
                            if run.font.size != None: feats['size'] = run.font.size    
                            if run.hyperlink.address != None: feats['href'] = run.hyperlink.address     #text_runs.append(run.text)
                            if run.font.color.type != None:
                                if run.font.color != None: 
                                    feats['color'] = str(run.font.color.rgb)
                            runs.append(feats)
                        paragraphs.append(runs)
                    frame['paragraphs'] = paragraphs
                    text_frames.append(frame)
                # Debug:
            #print ('Debug: frame=', frame)
        slide['frames'] = text_frames
        slides.append(slide)
        # Debug:
        #print ('Debug: slide=', slide)
    prs['slides'] = slides

    return prs
p = parse_pptx_presentation(prs)
with open('test.txt', 'w', encoding='utf8') as json_file:
    json.dump(p, json_file, ensure_ascii=False, indent=2)
