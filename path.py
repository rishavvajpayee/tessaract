ppath = '/home/ctp/Desktop/poppler/Library/bin'
pdpath = '/home/ctp/Desktop/pdf-parser/parser/NMR_PDF/746485-1.pdf'

from pdf2image import convert_from_path
pages = convert_from_path(pdf_path=pdpath,poppler_path=ppath)

import os
save = pdpath.split("/")[-1].split(".")[0]

save_path = f"/home/ctp/Desktop/tessaract/test/{save}.jpeg"
print(save)

c = 1

for page in pages:
    img_name = f"img-{c}.jpeg"
    page.save(os.path.join(save_path,img_name),"JPEG")
    c+=1