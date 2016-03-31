[![wercker status](https://app.wercker.com/status/1acfadc93e9737096c380604b0cc0e42/m/master "wercker status")](https://app.wercker.com/project/bykey/1acfadc93e9737096c380604b0cc0e42)

# 00keys

A website to showcase custom keycap designs.

## Articles and Article Types

There are three main content folders:
* `/articles/` - used for sub pages (not really used)
* `/keys/` - used for individual key entries
* `/gbs/` - used for group buys

A new folder has to be added for each entry and the content has to be a file named `index.md`.

### Keys

#### Code Name

There is a naming format for keys.
It shoudl be used for all identifying folders and files.
This is never seen on the website, it's just used inside of the website generation.

```
[design]-[base color]-[legend color]-[profile type]

example: v12-bfk-yy-sa1
example: mininuke-ra-wa-dsa
```

The image for the key will be found in the folder `\contents\singlekeys\`.

#### Frontmatter

There are some manditory fields to make the templates work.

```YAML
title: Mini Nuke
profile: SA Row 1
colorway: Special Fat Man
base: VV # Signiture Plastics color code
legend: YY # Signiture Plastics color code
author: 00keys # Always use 00keys
date: 2016-04-01 # Date added to website
code: mininuke-vv-yy-sa1 # The code name
id: 708 # 700 = Glowing One, SA1 # ID for  Custom sorting logic
tags: SA Row 1, Mini Nuke, The Megaton Vault Drop GB, Special Fat Man # Comma seperated list for tags
template: key.jade # Rendering template
```

#### Desgin Descriptions

There is a folder named `/keyinfo/` where you can put a markdown files with the design codename e.g. `mininuke.md`.
This will be added to each key page that uses that as the design part of it's code e.g. `mininuke-vv-yy-sa1`.

#### Color Descriptions

There is a folder named `/colorinfo/` where you can put a markdown files with the color codename e.g. `bfk-yy.md`.
This will be added to each key page that uses that as the design part of it's code e.g. `v87-bfk-yy-dsa`.


### GBs

#### Code Name

A GB needs an identifier wich can work as a file name e.g. `glowingone`.
This is never seen on the website, it's just used inside of the website generation.

#### Frontmatter

A GB has some complex front matter to allow the automatic generation of the GB page.

```YAML
title: The Megaton Vault Drop # The name seen on the website
author: 00keys # Always use 00keys
date: 2016-04-01 # Date added to website
gbtag: The Megaton Vault Drop GB # Match an entry used in the 'tags' of the keys
code: glowingone # The code name
offers: # A lis of objects with each 'kit' in the GB
    - img: sa1
      name: SA Row 1 Kit
      price: 40
      tagfilter: 
        - SA Row 1
    - img: sa3            # The section to locate the image '\contents\gbs\glowingone-sa3'
      name: SA Row 3 Kit  # The name of the kit which is seen on the website
      price: 40           # The price in USD
      tagfilter:          # A list of tags to filter content by
        - SA Row 3        # All content will match 'gbtag' and all tags in this list
    - img: dsa
      name: DSA Kit
      price: 40
      tagfilter: 
        - DSA
iclinks: # A list of objects with interest check links
    - name: geekhack.org Interst Check
      url: https://geekhack.org/index.php?topic=80552
    - name: /r/mechmarket Interst Check # The name seens on the website
      url: https://redd.it/4brqtu       # The URL that will be used
gblinks: # The same as iclinks, but for Group Buys
    - name: geekhack.org
      url: https://geekhack.org/index.php?topic=76885
template: groupbuy.jade # Rendering template
```

## Images

At the moment the only image type excpected in the templates is `.png`.


## Editing

This repository is linked to a wercker application that will automatically deploy any changes that are made.

This works for both edit mades in-browser viavia `github.com` and all pushes. If you need to be a contributor, you can be added to the white list so you can make instant edits.

### Local Install

This project uses [Wintersmith][wintersmith] which is a static site generator based on [Node.js][nodejs]. 
Automation is handled via [Grunt][grunt].

1. Set up Node.js and Node Package Manager on your machine(`npm`). Search the web for steps on that.
2. Clone this repository
    - `git clone git@github.com:nathanrosspowell/00keys.git` in the command line
    - or, use the "Save To Your Computer" button if you have GitHub Desktop installed (recommended step for Windows users)
3. Open a command promt inside the `00keys` director
    - GitHub Desktop users can use the "Open in Git Shell" option from the setting menu (cog icon)
4. Install all the dependencies
    - `npm install -g wintersmith grunt-cli; npm install` in the command promt
    - or, Windows users can use `.\windows_install.bat`
5. Launch the local server with `wintersmith preview`
6. Open a web browser and go to `localhost:8080/00keys`


[wintersmith]: http://wintersmith.io/
[nodejs]: https://nodejs.org/
[grunt]: http://gruntjs.com/
