#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/8/22 16:22


def init():
    try:
        import Image
    except ImportError:
        from PIL import Image
    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/3.05.02/bin/tesseract'

    # Simple image to string
    print(pytesseract.image_to_string(Image.open('/Users/jtusta/Pictures/QQ20180822-164248.png')))


if __name__ == '__main__':
    init()
