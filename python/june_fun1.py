#!/usr/bin/env python 

import PIL.Image,PIL.ImageDraw

tw = 200
th = 300

out = PIL.Image.new("RGB",(tw*4,th*4))

for i in range(1,17):
    fn = "{0:03}.jpg.png".format(i)
    im = PIL.Image.open(fn)
    rim = im.resize((tw,th),PIL.Image.BILINEAR)
    t = i-1
    x = (t%4)*tw
    y = int(t/4)*th
    out.paste(rim,(x,y))
    del im
    del rim

out.save("out.png")
