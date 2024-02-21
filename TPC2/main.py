import re
import sys

def main(argv: list[str]):
    filename = argv[1]
    try:
        file = open(filename)
    except:
        print("Ficheiro Inválido.")
        return 0

    content = file.read()

    # titulos
    for i in range(7,0,-1):
        content = re.sub(r"(?<!\S|#| )" + "".join("#" for _ in range(0,i)) + r" (.*?)\n", f"<h{i}>\\1</h{i}>\\n", content)

    # bold
    content = re.sub(r"\*\*(.*?)\*\*", "<b>\\1</b>", content)

    # italic
    content = re.sub(r"\*(.*?)\*", "<i>\\1</i>", content)

    # lists
    res = ""
    started_ul = False
    started_ol = False
    for line in content.split("\n"):
        if re.match(r"^[ ]*- (.*)$", line):
            if not started_ul:
                started_ul = True
                res += "<ul>\n"
            line = re.sub(r"^[ ]*- (.*)$", "\t<li>\\1</li>", line)
            res += line + "\n"
        elif re.match(r"^[ ]*[\d]+. (.*)$", line):
            if not started_ol:
                started_ol = True
                res += "<ol>\n"
            line = re.sub(r"^[ ]*[\d]+. (.*)$", "\t<li>\\1</li>", line)
            res += line + "\n"
        else:
            if started_ul:
                started_ul = False
                res += "</ul>\n"
            if started_ol:
                started_ol = False
                res += "</ol>\n"
            res += line + "\n"

    content = res

    # images
    content = re.sub(r"!\[(.*?)\]\((.*?)\)", "<img src='\\2' alt='\\1'>", content)
    
    # links
    content = re.sub(r"(?<!\!)\[(.+?)\]\((.+?)\)", "<a href='\\2'>\\1</a>", content)

    # paragraphs
    content = re.sub(r"\n\n", "\\n\\n<p></p>\\n\\n", content)

    file.close()
    res = open(filename.split(".")[0] + ".html", "w")
    res.write(content)
    res.close()

main(sys.argv)