#coding: utf8

import csv
with open('index.csv', newline='', encoding='utf-8-sig') as csvfile:
    csvdb = csv.DictReader(csvfile)
    for lines in csvdb:
        if lines["chinese_title"]:
            page_name=lines["picid"]+".html"
            print(page_name)
            file=open("pages/"+page_name, "w+")
            file.write("<!DOCTYPE html>\r\n<html>\r\n<head>\r\n<meta charset=\"UTF-8\">\r\n</head>\r\n<body>\r\n")
            if (lines["episode"].isnumeric()) == True:
                file.write("<h3>" + lines["episode"] + ". " + lines["chinese_title"] + "</h3>\r\n")
            else:
                file.write("<h3>" + lines["chinese_title"] + "</h3>\r\n")
            if int(lines["picid"]) == 1:
                file.write("")
            elif int(lines["picid"]) == 121:
                file.write("<p><a href=\"../pages/" + str(int(lines["picid"])-1) + ".html\">上一章</a>")
            else:
                file.write("<p><a href=\"../pages/" + str(int(lines["picid"])-1) + ".html\">上一章</a>・")
            if int(lines["picid"]) == 121:
                file.write("</p>")
            else:
                file.write("<a href=\"../pages/" + str(int(lines["picid"])+1) + ".html\">下一章</a>・<a href=\"https://srgrafo.com/comic/" + lines["picid"] + "\">原版链接</a></p>")
            if lines["music"]:
                file.write("<p><a href=\"" + lines["music"] + "\">建议配乐</a></p>")
            file.write("<img src=\"../img/" + lines["picid"] + ".png" "\">")
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

            file2=open("index.html", "w+")
                file2.write()
