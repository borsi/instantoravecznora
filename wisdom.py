import re
import bottle
import string
import random

word_lists = {}

def init():
    global word_lists
    word_lists["fonev"] = load_textlist("assets/data/fonev.txt")
    word_lists["fonevbol"] = load_textlist("assets/data/fonevbol.txt")
    word_lists["foneve"] = load_textlist("assets/data/foneve.txt")
    word_lists["fonevvel"] = load_textlist("assets/data/fonevvel.txt")
    word_lists["ige_alanyi_e3"] = load_textlist("assets/data/ige_alanyi_e3.txt")
    word_lists["ige_targyas_e3"] = load_textlist("assets/data/ige_targyas_e3.txt")
    word_lists["jelzo"] = load_textlist("assets/data/jelzo.txt")
    word_lists["legjelzo"] = load_textlist("assets/data/legjelzo.txt")
    word_lists["ige_felszolito_e2"] = load_textlist("assets/data/ige_felszolito_e2.txt")
    word_lists["ige_felszolito_e3"] = load_textlist("assets/data/ige_felszolito_e3.txt")
    word_lists["szerkezet"] = load_textlist("assets/data/szerkezet.txt")
    bottle.TEMPLATE_PATH.insert(0, "./assets/tpl")

def generate():
    global word_lists
    skeleton = random.choice(word_lists["szerkezet"]).split(' ')
    result = ""

    for word in skeleton:
        rgx = re.compile(r"\{(.+?)\}")
        match = re.search(rgx, word)
        if match and len(match.groups()) == 1:
            result += re.sub(rgx, random.choice(word_lists[match.group(1)]), word)
        else:
            result += word
        result += ' '

    return result[0].upper() + result[1:]

def load_textlist(file_name):
    return [line.strip() for line in open(file_name, "r")]
