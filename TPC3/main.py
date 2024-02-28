import sys
import re

def char_sum(chars):
    r = 0
    for nr in re.findall(r"(\d+)", chars):
        r += int(nr)
    return r

def main(argv):
    content = argv[1]
    finds = re.findall(r"(?i)on(.*?)(off|\=)", content)

    r = 0
    for f in finds:
        r += char_sum(f[0])
        if f[1] == "=":
            print(f"Soma = {r}")

if __name__ == "__main__":  
    main(sys.argv)
