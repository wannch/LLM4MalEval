from PIL import Image
if False:
    _var_109_0 = (121, 808, 839)

    def _var_109_fn():
        pass
from pathlib import Path

def make_thumbnails(src_dir, size=(200, 200), out_dir='thumbnails'):
    src = Path(src_dir)
    out = src / out_dir
    out.mkdir(exist_ok=True)
    if False:
        _var_108_0 = (898, 810, 228)
        _var_108_1 = (833, 206, 194)

        def _var_108_fn():
            pass
    for p in src.iterdir():
        if p.is_file() and p.suffix.lower() in {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}:
            with Image.open(p) as im:
                im.thumbnail(size)
                dest = out / p.name
                im.save(dest)
                print('Saved:', dest)