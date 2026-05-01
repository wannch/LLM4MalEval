from pathlib import Path
from PIL import Image

def make_thumbnails(src_dir, size=(200, 200), out_dir="thumbnails"):
    src = Path(src_dir)
    out = src / out_dir
    out.mkdir(exist_ok=True)
    for p in src.iterdir():
        if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".bmp"}:
            with Image.open(p) as im:
                im.thumbnail(size)
                dest = out / p.name
                im.save(dest)
                print("Saved:", dest)