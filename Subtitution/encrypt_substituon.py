OP=open('cipher.txt', 'r')
Cip=open('cipher.enc', 'w')
text=str(OP.read())
keys={
    'A':'B', 'B':'A', 'C':'D', 'D':'C', 'E':'F', 'F':'E', 'G':'H', 'H':'G',
    'I':'J', 'J':'I', 'K':'L', 'L':'K', 'M':'N', 'N':'M', 'O':'P', 'P':'O',
    'Q':'R', 'R':'Q', 'S':'T', 'T':'S', 'U':'V', 'V':'U', 'W':'X', 'X':'W',
    'Y':'Z', 'Z':'Y', 'a':'b', 'b':'a', 'c':'d', 'd':'c', 'e':'f', 'f':'e',
    'g':'h', 'h':'g', 'i':'j', 'j':'i', 'k':'l', 'l':'k', 'm':'n', 'n':'m',
    'o':'p', 'p':'o', 'q':'r', 'r':'q', 's':'t', 't':'s', 'u':'v', 'v':'u',
    'w':'x', 'x':'w', 'y':'z', 'z':'y', '0':'1', '1':'0', '2':'3', '3':'2',
    '4':'5', '5':'4', '6':'7', '7':'6', '8':'9', '9':'8', '{':'}', '}':'{',
    ' ':'_', '_':' ', ',':'.', '.':',', '(':')', ')':'(', '\n':'\n'
    }
crypt=""
for i in text:
    if i in keys:
        crypt+=keys[i]
Cip.write(crypt)
Cip.close()
