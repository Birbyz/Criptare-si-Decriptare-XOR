import sys

#python encrypt parolamea2021 input.txt output
parola,finput,foutput=sys.argv[1:] 

def encriptare(text, parola):
    cheie = parola
    for i in range(len(text)):
        text = (text[:i] + chr(ord(text[i]) ^ ord(cheie[i % len(cheie)])) + text[i + 1:])
    return text

fin = open(finput,"r")
text = fin.read()
fin.close()

text = encriptare(text, parola)
fout = open(foutput,"wb")
fout.write(bytes(text,"utf-8"))
fout.close()

