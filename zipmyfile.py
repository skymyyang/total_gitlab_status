#!/usr/bin/env python
# coding=utf-8
import os
import zipfile



def zip_dist(startdir, outFullName):
    z = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),
                    os.path.join(fpath, filename))
    z.close()