import pymupdf, io, zlib, sys
from PIL import Image
src, out, MAXPX, Q = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
d=pymupdf.open(src); n=0; masks=set()
for x in range(1,d.xref_length()):
    if d.xref_get_key(x,'Subtype')[1]=='/Image' and d.xref_get_key(x,'SMask')[0]=='xref': masks.add(int(d.xref_get_key(x,'SMask')[1].split()[0]))
def pil(x):
    pm=pymupdf.Pixmap(d,x)
    if pm.alpha: pm=pymupdf.Pixmap(pm,0)
    if pm.n not in (1,3): pm=pymupdf.Pixmap(pymupdf.csRGB,pm)
    return Image.frombytes('L' if pm.n==1 else 'RGB',(pm.width,pm.height),pm.samples)
def put(x,I,jpeg):
    if jpeg:
        b=io.BytesIO(); I.save(b,'JPEG',quality=Q,optimize=True); data=b.getvalue(); f='/DCTDecode'
    else: data=zlib.compress(I.tobytes(),9); f='/FlateDecode'
    d.update_stream(x,data,compress=False)
    for k,v in (('Filter',f),('DecodeParms','null'),('Width',str(I.size[0])),('Height',str(I.size[1])),('BitsPerComponent','8'),('ColorSpace','/DeviceRGB' if I.mode=='RGB' else '/DeviceGray')): d.xref_set_key(x,k,v)
for x in range(1,d.xref_length()):
    if x in masks or d.xref_get_key(x,'Subtype')[1]!='/Image' or d.xref_get_key(x,'BitsPerComponent')[1]=='1': continue
    L=len(d.xref_stream_raw(x)); I=pil(x)
    if max(I.size)<=MAXPX and L<200_000: continue
    I.thumbnail((MAXPX,MAXPX)); put(x,I,True)
    sm=d.xref_get_key(x,'SMask')
    if sm[0]=='xref':
        mx=int(sm[1].split()[0]); put(mx,pil(mx).convert('L').resize(I.size,Image.LANCZOS),False)
    n+=1
d.save(out,garbage=4,deflate=True); print('recompressed',n)
