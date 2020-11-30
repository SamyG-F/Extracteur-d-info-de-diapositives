from pptx import Presentation

root = Presentation()

slide_layout = root.slide_layouts[0]

slide1 = root.slides.add_slide(slide_layout)
slide1.shapes.title.text = 'première page'
slide1.placeholders[1].add_paragraph()
.text = 'ceci est en italique'
#slide1.placeholders[1].text.font.italic = True

slide2 = root.slides.add_slide(slide_layout)
slide2.shapes.title.text = 'deuxième page'
slide2.placeholders[1].text = 'ceci est en gras'
#slide2.placeholders[1].text.font.bold = True

slide3 = root.slides.add_slide(slide_layout)
slide3.shapes.title.text = 'troisième page'
slide3.placeholders[1].text = 'ceci est souligné'
#slide3.placeholders[1].text.font.underline = True

root.save('presentation_test1.pptx')