#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Nov 26, 2012

@author: nemo
'''

import gtk
import httplib
import pynotify
import os

SRC_LANG = 'en'
DST_LANG = 'ru'

term = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD).wait_for_text().encode('utf-8').replace("\n", "").lstrip().strip()

conn = httplib.HTTPConnection("translate.google.com")
conn.request("GET","/translate_a/t?client=t&text=" + term.replace(" ", "%20") + "&hl=" + SRC_LANG + "&tl=" + DST_LANG + "&ie=UTF-8&oe=UTF-8")
data = conn.getresponse().read()

transl = data[data.find('"') + 1 : ]
transl = transl[ : transl.find('"')]

pynotify.init("Null")
n = pynotify.Notification (term, transl, "Null")
n.show()

os.system("cvlc --play-and-exit 'http://translate.google.com/translate_tts?ie=UTF-8&q=" + term.replace(" ", "%20") + "&tl=" + SRC_LANG + "&total=1&idx=0&textlen=5'")
os.system("cvlc --play-and-exit 'http://translate.google.com/translate_tts?ie=UTF-8&q=" + transl + "&tl=" + DST_LANG + "&total=1&idx=0&textlen=5'")
