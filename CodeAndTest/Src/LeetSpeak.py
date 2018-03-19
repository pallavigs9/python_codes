leet_dict = {'A':'@','B':'8','C':'(','D':'D','E':'3','F':'F','G':'6','H':'#','I':'!','J':'J','K':'K','L':'1','M':'M','N':'N','O':'0','P':'P','Q':'Q','R':'R','S':'$','T':'7','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z':'2'}

def to_leet_speak(string):
    new_str = ''

    for i in string:
        new_str = new_str + leet_dict[i]
    return  new_str

print to_leet_speak("LEET")
print to_leet_speak("CODEWARS")