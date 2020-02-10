import time
import json
import io
from PIL import Image
def start(args, hkubeapi):
     image = Image.open('Sydney-Opera-House.jpg')
     print(image.format)
     print(image.mode)
     print(image.size)
     imgByteArr = io.BytesIO()
     image.save(imgByteArr, format=image.format)
     result = imgByteArr.getvalue()
  
     time.sleep(2)
     return  {"name":"python test",
              "version":"v3-branch1",
              "image.format":image.format,
              "image.mode":image.mode,
              "image.size":image.size,              
              "image":bytearray(result)
              }
    
     
