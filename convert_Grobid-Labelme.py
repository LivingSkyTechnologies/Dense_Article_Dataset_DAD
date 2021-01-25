#!/usr/bin/env python
# coding: utf-8

# In[1]:


# change working dirA
import os
import glob
os.chdir("..")
import os.path
import json
from PIL import Image


# In[5]:


def convert_labelme(input_json_path, output_labelmepath):
    for jsonname in os.listdir(input_json_path):
        if jsonname.endswith(".json"):
            json_path = os.path.join(input_json_path, jsonname)
            jsonname_noExtension = (os.path.splitext(jsonname)[0]) # extract jsonfile names without the extention
            json_outpath = os.path.join(output_labelmepath, jsonname_noExtension) # create labelme json output path with json names 
            dataset = json.load(open(json_path))
            labelme_data = {}
            for data in dataset.values():
                raw_coordinates = data["coordinates"]
                for coords in raw_coordinates.split(";"):
                    if len(coords.split(",")) != 5:
                        continue
                    page, x, y, w, h = coords.split(",")
                    page_name = jsonname_noExtension + "-" + str(page) + ".jpg"
                    page_name = os.path.join(output_labelmepath, jsonname_noExtension, page_name)
                    page_name = page_name if os.path.exists(page_name) else os.path.join(output_labelmepath, jsonname_noExtension, jsonname_noExtension + "-0" + str(page) + ".jpg") 
                    if page_name not in labelme_data:
                        labelme_data[page_name] = []
                    labelme_data[page_name].append((float(x), float(y), float(w), float(h)))
                for page_name, coords in labelme_data.items():
                    page_name_path = os.path.join (json_outpath, page_name)
                    width, height = Image.open(page_name_path).size
                    labelme_template = {"version": "4.2.10",
                                        "flags": {},
                                        "shapes": [],
                                        "imagePath": page_name,
                                        "imageData": None,
                                        "imageHeight": height, 
                                        "imageWidth": width}
                    for coord in coords:
                        x, y, w, h = coord
                        labelme_template["shapes"].append({"label": "citation",
                                                           "points": [
                                                           [
                                                             x*2.776,
                                                             y*2.776
                                                           ],
                                                           [
                                                             x*2.776 + w*2.776,
                                                             y*2.776 + h*2.776
                                                           ]
                                                          ],
                                                           "group_id": None,
                                                           "shape_type": "rectangle",
                                                           "flags": {},
                                                           })
                    page_nameNoExtension = (os.path.splitext(page_name)[0])
                    page_namewithpath = os.path.join(json_outpath,page_nameNoExtension + ".json") # set the final output dir
                    with open(page_namewithpath, 'w') as f:
                        json.dump(labelme_template, f, indent=2)

