#question 1
#א. ההבדל  שראם יש אליו גישה מהירה, זמנית וקטנה יותר. הקבוע איטי יותר, קבוע וגדול יותר.
#ב. ssd, hdd, usb
#ג.לסגור קובץ
#ד. r זה לקריאה, w לכתיבתו (מחדש) ו a להוסיף לסוף הקובץ

#question 2
with open("example.txt", "w") as example:
    example.write("Hello, World!")

#question 3
def read_50_notes(file_name:str):
    with open(file_name, "r") as file:
        return file.read(50)
#question 4
def write_sentence(file_name: str, sentence: str):
    try:
        with open(file_name, "w") as file:
            file.write(sentence)
            return True
    except:
        return False
print(write_sentence("text.txt", "ha ha ha"))
print(write_sentence("hhhhhhh/pop", "hi hi hi"))

