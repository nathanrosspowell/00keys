gb_code = "junktown2"
gb_name = "Junktown II"
date = "2017-04-01"
base_id = 800
profiles = (
    ("sa1", "SA Row 1"),
    ("sa3", "SA Row 3"),
    ("dsa", "DSA"),
)
keys = (
    ("brotherhood", "Brotherhood Helmet"), 
    ("lucky38", "Lucky 38"),
    ("v21", "Vault 21"),
    ("mininuke", "Mini Nuke"),
)
colorways = (
    ("bfk", "yy", "Vault Jumpsuit"),
    ("silverabs", "nn", "Brotherhood of Steel"),
    ("polygreen", "wa", "Zetans"),
    ("polyred", "wa", "The Institute"),  
)


template = """---
title: {keyname}
profile: {profile}
colorway: {colorway}
base: {base_color}
legend: {legend_color}
author: 00keys
date: {date}
gb: {gb_code}
code: {keycode}-{base_color}-{legend_color}-{profile}
id: {id_code} # {base_id} = {gb_name}
tags: {profile_name}, {keyname}, {gb_name}, {colorway}
template: key.jade
---"""

key_name_template = "{keycode}-{base_color}-{legend_color}-{profile}"

placeholder_img = "missing"
img_ext = ".png"


def make_key(data):
    import os
    from shutil import copyfile
    root = os.path.dirname(os.path.abspath(__file__))
    key_dir = os.path.join(root, "keys")
    img_dir = os.path.join(root, "singlekeys")
    key_name = key_name_template.format(**data)
    new_key_dir = os.path.join(key_dir, key_name)
    placeholder = os.path.join(img_dir, placeholder_img + img_ext)
    new_img = os.path.join(img_dir, key_name + img_ext)
    #copyfile(placeholder, new_img)
    print("copy",placeholder, new_img)
    print(template.format(**data))
    print(new_key_dir)
    with 


if __name__ == "__main__":
    set_id = base_id
    for i, profile in enumerate(profiles):
        id_code = set_id
        for key in keys:
            for color in colorways:
                id_code += 1
                make_key({
                    "keyname" : key[1],
                    "profile" : profile[0],
                    "colorway" : color[2],
                    "base_color" : color[0],
                    "legend_color" : color[1],
                    "date" : date,
                    "gb_code" : gb_code,
                    "keycode" : key[0],
                    "id_code": id_code,
                    "base_id": set_id,
                    "profile_name": profile[1],
                    "gb_name" : gb_name,
                })
        set_id = base_id + ((i + 1) * 100)



