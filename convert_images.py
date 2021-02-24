import os, glob, shutil
import os.path
from PIL import Image

folder = 'uniform_images'
try:
  shutil.rmtree(folder)
except FileNotFoundError:
  pass
os.makedirs(folder)

for path in glob.glob('images/*'):
  im = Image.open(path)
  im.resize((256, 256), Image.LANCZOS).convert("RGB").save(os.path.join(folder, os.path.basename(path)) + ".png", "PNG")
