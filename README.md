Refer to [@Schwenger for the original version](https://github.com/Schwenger/CSKey)


To work with the layout files the software [ukelele](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ukelele) is used.

# Setup

run 

    python3 install.py

to install the Keyboard Layout with its icon.


# Icons

Icons have to be named "`CSLayout.icns`" and are installed using the `install.py`

Below you will find two ways to create such icns files.

## Apple-icons

use 

    curl https://raw.githubusercontent.com/phible/scripts/master/apple-kbd-dat-icon-extract.py -o a.py;mkdir icons;python a.py -o icons
    
to extract apple flag-icons into new `icons` directory


## Manual

icns creation by [@retifrav](https://github.com/retifrav/python-scripts/blob/master/generate-iconset/generate-iconset.py)

    python3 generate_iconset.py source_images/CSLayout_example.png

to create apple icns file that supports variety of sizes/resolutions
