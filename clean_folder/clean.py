from pathlib import Path
import sys
import os
import shutil


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґА\
                            БВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЄІЇҐ"

TRANSLATION = ["a", "b", "v", "g", "d", "e", "e", "j", "z", "i",
               "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "'", "y", "'", "e",
               "yu", "ya", "e", "i", "ji", "g"]

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(p):

    name = p.name.translate(TRANS)
    for n in name:
        if not n.isalpha() and not n.isdecimal():
            name = name.replace(n, "_")
    norm = ''       
    try:
        norm = os.rename(p, os.path.join(p.parent, name))
    except:
        pass
    return norm   

images_end = ('JPEG', 'PNG', 'JPG', 'SVG')
video_end = ('AVI', 'MP4', 'MOV', 'MKV')
documents_end = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
audio_end = ('MP3', 'OGG', 'WAV', 'AMR')
archives_end = ('ZIP', 'GZ', 'TAR')

path = Path(sys.argv[1])

def fold_sort(path):

    if not os.path.exists('images'):
        os.mkdir('images')
    else:
        pass
    if not os.path.exists('video'):
        os.mkdir('video')
    else:
        pass
    if not os.path.exists('documents'):
        os.mkdir('documents')
    else:
        pass
    if not os.path.exists('audio'):
        os.mkdir('audio')
    else:
        pass
    if not os.path.exists('archives'):
        os.mkdir('archives')
    else:
        pass
    for p in path.iterdir():

        normalize(p)

        file_name_split = p.name.split('.')
        file_end_up = ''
        if len(file_name_split) > 1:
            file_end_up = file_name_split[-1].upper()

        if p.is_dir():
            if len(os.listdir(p)) > 0:
                fold_sort(p)
            else:
                try:
                    os.removedirs(p)
                except:
                    pass
        elif file_end_up in images_end:
            try:
                shutil.move(p, 'images')
            except:
                pass
        elif file_end_up in video_end:
            try:
                shutil.move(p, 'video')
            except:
                pass
        elif file_end_up in documents_end:
            try:
                shutil.move(p, 'documents')
            except:
                pass
        elif file_end_up in audio_end:
            try:
                shutil.move(p, 'audio')
            except:
                pass
        elif file_end_up in archives_end:
            ln = len(".ZIP")
            arc_name = p.name[:-ln]
            try:
                shutil.unpack_archive(p, os.path.join('archives', arc_name))
            except:
                pass

  
if __name__ == '__main__':

    fold_sort(path)