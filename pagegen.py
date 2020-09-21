#coding: utf8

import csv

file2=open("index.html", "w+")
indexfile = ["""<!DOCTYPE html>
<html>
    <head>
        <style type="text/css">
            body { font-size: 150%; text-align: center;}
        </style>
    </head>
    <body>
        <h1> Rimworld Tales 边缘世界物语 </h1>
        <span>汉化版</span>
        <p>
            原作者：<a href="https://srgrafo.com/">SrGrafo</a> ・<a href="https://srgrafo.com/home">漫画原作</a>・<a href="https://www.patreon.com/SrGrafo">赞助他</a>
        </p>
        <img src="img/cover.png">
        <h2>目录</h2>
"""]

with open('index.csv', newline='', encoding='utf-8-sig') as csvfile:
    csvdb = csv.DictReader(csvfile)
    for lines in csvdb:
        if lines["chinese_title"]:
            page_name=lines["picid"]+".html"
            print(page_name)
            file=open("pages/"+page_name, "w+")
            file.write("<!DOCTYPE html>\r\n<html>\r\n<head>\r\n<meta charset=\"UTF-8\">\r\n<style type=\"text/css\">\r\n body { font-size: 150%; text-align: center; }\r\n </style>\r\n</head>\r\n<body>\r\n")
            if (lines["episode"].isnumeric()) == True:
                file.write("<h3>" + lines["episode"] + ". " + lines["chinese_title"] + "</h3>\r\n")
                indexfile.append("<a href=\"pages/" + lines["picid"] + ".html\">" + lines["episode"] + "." + lines["chinese_title"] + "</a><br />\r\n")
            else:
                file.write("<h3>" + lines["chinese_title"] + "</h3>\r\n")
                indexfile.append("<a href=\"pages/" + lines["picid"] + ".html\">" + lines["chinese_title"] + "</a><br />\r\n")

            if int(lines["picid"]) == 1:
                file.write("")
            elif int(lines["picid"]) == 121:
                file.write("<p><a href=\"../pages/" + str(int(lines["picid"])-1) + ".html\">上一章</a>")
            else:
                file.write("<p><a href=\"../pages/" + str(int(lines["picid"])-1) + ".html\">上一章</a>・")

            if int(lines["picid"]) == 121:
                file.write("</p>")
            else:
                file.write("<a href=\"../pages/" + str(int(lines["picid"])+1) + ".html\">下一章</a>・<a href=\"https://srgrafo.com/comic/" + lines["picid"] + "\">原版链接</a>・<a href=\"../index.html\">回目录</a></p>")

            if lines["music"]:
                file.write("<p><a href=\"" + lines["music"] + "\">建议配乐</a></p>")

            file.write("<div><img src=\"../img/" + lines["picid"] + ".png" "\"></div>")

            if lines["comment"]:
                file.write("<p style=\"font-size: 80%; margin: 0 20% 0 20%; text-align: left;\">" + lines["comment"] + "</p>")

            if int(lines["picid"]) == 1:
                file.write("")
            elif int(lines["picid"]) == 121:
                file.write("<p><a href=\"../pages/" + str(int(lines["picid"])-1) + ".html\">上一章</a>")
            else:
                file.write("<p><a href=\"../pages/" + str(int(lines["picid"])-1) + ".html\">上一章</a>・")

            if int(lines["picid"]) == 121:
                file.write("</p>")
            else:
                file.write("<a href=\"../pages/" + str(int(lines["picid"])+1) + ".html\">下一章</a></p>")
            file.close()

indexfile.append("""	</body>
</hmtl>""")

indexhtml = ''.join(indexfile)
file2.write(indexhtml)
file2.close()
