"""
Дана строка - "Это тестовая <start>строка для изучения<end> строковых операций". 
Программа должна вывести на экран текст из данной строки     
заключенный между тэгами <start> и <end>. 
Программа должна работать с любой другой строкой с подобными тэгами.
"""

KEY_START = "<start>"
KEY_END = "<end>"
TEMPLATE = "Это тестовая <start>строка для изучения<end> строковых операций"

start = TEMPLATE.find(KEY_START) + len(KEY_START)
end = TEMPLATE.find(KEY_END)
print(TEMPLATE[start:end])
