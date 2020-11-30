from pptx import Presentation

prs = Presentation('data/CM1_React.pptx')
# Parsing a presentation
# slides > paragraph > run
text_runs = []
for i in range(0, len(prs.slides)):
    s = prs.slides[i]
    print ("slide number="+str(i))
    print ("Presentation.slides[].slide_id     ="+str(s.slide_id))
    print ("Presentation.slides[].name         ="+s.name)
    print ("Presentation.slides[].shapes.title ="+str(s.shapes.title.text))
    for shape in s.shapes:
        if shape.is_placeholder:
            phf = shape.placeholder_format
            print('shape.placeholder_format idx=%d, type=%s' % (phf.idx, phf.type))
            #print ("Presentation.slides[].placeholders[{}]={}".format(s.placeholders[phf.idx].text))
            #text_frame = shape.text_frame
        if shape.has_text_frame:
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    text_runs.append(run.text)
                    print ("run.text  ="+run.text)
                    print ("font.name ="+str(run.font.name))
                    print ("is_bold   ="+str(run.font.bold))
                    print ("font      ="+str(run.font.italic))
                    print ("size      ="+str(run.font.size))
                    print ("underline ="+str(run.font.underline))
                    print ("color     ="+str(run.font.color)) # .rgb
                    print ("hyperlink.address="+str(run.hyperlink.address))
                print ('run....................')    
            print ('paragraph--------------------')
        print ('shape___________________________')
    print('slide====================\n')
    #placeholders = s.placeholders
    #print ("len(Presentation.slides[].placeholders)="+str(len(placeholders)))
    #for j in range (0, len(placeholders)):
    #    p = placeholders[j]
    #    print ("Presentation.slides[].placeholders[{}]={}".format(j, placeholders[j].text))
