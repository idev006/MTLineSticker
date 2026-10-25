from PIL import Image
from pathlib import Path
from tempfile import TemporaryDirectory
from check_sticker_png import validate
with TemporaryDirectory() as temp:
    p=Path(temp)/'good.png'
    im=Image.new('RGBA',(592,512),(0,0,0,0))
    for x in range(100,492):
        for y in range(100,400):im.putpixel((x,y),(255,255,255,255))
    im.save(p)
    assert validate(p)['passed'],validate(p)
    im=Image.new('RGB',(592,512),'white');im.save(p)
    assert 'NOT_RGBA' in validate(p)['errors']
    im=Image.new('RGBA',(590,512),(0,0,0,0));im.save(p)
    assert 'FRAME_RATIO_INVALID' in validate(p)['errors']
print('B_PNG_TESTS_PASS: 3/3')
