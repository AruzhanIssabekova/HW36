import re

from bs4 import BeautifulSoup

#
# def Body(html_content):
#     p = '<p>(.*?)</p>'
#     r = re.findall(p, html_content, re.S )
#     return r
# with open('Astana.html', 'r', encoding='utf-8') as file:
#     c = file.read()
#     b_c = Body(c)
#     for line in b_c:
#         words = line.split()
#         print(*words)

#
#
# with open('Astana.html', 'r', encoding='utf-8') as file:
#     c = file.read()
#     s = BeautifulSoup(c,'html.parser')
#     for i in s.find_all('p'):
#         print(i.get_text())