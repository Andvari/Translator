mkdir /usr/share/pyshared/Translator
cp src/Translator.py /usr/share/pyshared/Translator/Translator.py
cp src/images/icon.png /usr/share/pyshared/Translator/images/icon.png
cp translator.desktop /usr/share/applications/translator.desktop
ln -s -T /usr/share/pyshared/Translator/Translator.py /usr/bin/Translator
