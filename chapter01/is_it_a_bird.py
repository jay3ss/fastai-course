from time import sleep

from duckduckgo_search import ddg_images
from fastai.vision.all import *
from fastcore.all import *
from fastdownload import download_url


def search_images(term: str, max_images: int = 30):
    print(f"Searching for '{term}'")
    return L(ddg_images(term, max_results=max_images)).itemgot("image")


urls = search_images("bird_photos", max_images=1)
print(urls[0])

dest = "bird.jpg"
download_url(urls[0], dest, show_progress=True)

# im = Image.open(dest)
# im.to_thumb(256, 256)

download_url(search_images("forest photos", max_images=1)[0], "forest.jpg", show_progress=False)
# Image.open("forest.jpg").to_thumb(256, 256)

searches = "forest", "bird"
path = Path("bird_or_not")

for o in searches:
    dest = (path / o)
    dest.mkdir(exist_ok=True, parents=True)
    download_images(dest, urls=search_images(f"{o} photo"))
    sleep(10) # pause between searches to avoid over-loading server
    download_images(dest, urls=search_images(f"{o} sun photo"))
    sleep(10)
    download_images(dest, urls=search_images(f"{o} shade photo"))
    sleep(10)
    resize_images(path/o, max_size=400, dest=path/o)


