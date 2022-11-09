import os
import numpy as np
from natsort import natsorted

train_path = 'train'
dev_path = 'dev'

def folder2list(path, oufilename):
  f = open(oufilename, "a")
  f.writelines("rgb_path,video_id,label,protocol_4_1,protocol_4_2,protocol_4_3\n")
  for id_ in os.listdir(path):
    id_path = os.path.join(path, id_)
    for class_ in os.listdir(id_path):
      if class_ == "real":
        label_ = 1
      else:
        label_ = 0
      class_path = os.path.join(id_path, class_)
      for track_ in os.listdir(class_path):
        track_path  = os.path.join(class_path, track_)
        list_images = os.listdir(track_path)
        list_images = natsorted(list_images)
        for img_ in list_images:
          img_path = os.path.join(track_path, img_)
          f.writelines("{},{},{},True,False,False\n".format(img_path,track_,label_))
  f.close()
       
folder2list(train_path,"train_list.txt")
folder2list(dev_path,"dev_list.txt")
      
    
