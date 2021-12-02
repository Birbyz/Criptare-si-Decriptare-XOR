import sys

#python decrypt output parolamea2021 input_recuperat.txt
finput,parola,foutput=sys.argv[1:] 

def decriptare(text, parola):
    cheie = parola
    for i in range(len(text)):
        text = (text[:i] + chr(ord(text[i]) ^ ord(cheie[i % len(cheie)])) + text[i + 1:])
    return text

fin = open(finput,"rb")
text = fin.read()
text = text.decode("utf-8")
fin.close()

text = decriptare(text, parola)
fout = open(foutput,"w")
fout.write(text)
fout.close()

