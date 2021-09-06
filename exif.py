import os
from PIL import Image, ExifTags

#img = Image.open("hiragana-chart.jpeg")
#img_exif = img.getexif()
#print(type(img_exif))
# <class 'PIL.Image.Exif'>

directory = os.getcwd()

## Idea
## if argv is null, then default to current dir, otherwise, allow a named file with -f
## or a named directory with -d

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".jpg") or filename.endswith(".jpeg"):
          print(os.path.join(directory, filename))
          img = Image.open(filename)
          img_exif = img.getexif()

          if img_exif is None:
               print('Sorry, image has no exif data.')
          else:
    	       for key, val in img_exif.items():
                    if key in ExifTags.TAGS and (str(ExifTags.TAGS[key]) == 'GPSInfo'):
                         print(f'{ExifTags.TAGS[key]}:{val}')
          continue
     else:
          continue

