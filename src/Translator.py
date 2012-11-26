#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Nov 26, 2012

@author: nemo
'''

import os
import gtk
import httplib
import re
import pynotify

cb = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)
term = cb.wait_for_text().encode('utf-8')

term = term.replace("\n", "")
term = term.lstrip()
term = term.strip()

term_to_google = term.replace(" ", "%20")

conn = httplib.HTTPConnection("translate.google.com")
conn.request("GET","/translate_a/t?client=t&text=" + term_to_google + "&hl=en&tl=ru&ie=UTF-8&oe=UTF-8")
res = conn.getresponse()
data = res.read()

terms = re.compile('"(.*?)"').findall(data)

pynotify.init("Null")
n = pynotify.Notification (term, terms[0], "Null")
n.show()

os._exit(True)