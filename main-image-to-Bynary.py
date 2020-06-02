import time
import json
import io
import os
from PIL import Image
def start(args, hkubeapi):
     image = Image.open('Sydney-Opera-House.jpg')
     print(image.format)
     print(image.mode)
     print(image.size)
     imgByteArr = io.BytesIO()
     image.save(imgByteArr, format=image.format)
     result = imgByteArr.getvalue()
     EnvironmentVariables = os.getenv('FOO','Foo does not exist')
     time.sleep(3)
     return  {"name":"python test",
              "EnvironmentVariables":EnvironmentVariables,
              "version":"v3",
              "image.format":image.format,
              "image.mode":image.mode,
              "image.size":image.size,              
              "image":bytearray(result)
              }
    
     
