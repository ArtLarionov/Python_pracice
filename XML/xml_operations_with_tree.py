from xml.etree import ElementTree

tree = ElementTree.parse("xml_file_modified.xml")
root = tree.getroot()

# tree.write("xml_file_copy.xml")  -- создали новый файл-копию

# поступила информация, что Greg заработал дополнительные баллы в 1м модуле
greg = root[0]
# module1 = next(greg.iter("module1"))
# print(module1, module1.text)
# module1.text = str(float(module1.text) + 30)

# certificate = greg[2]         -- добавление данных
# certificate.set("type", "with distinction")

# description = ElementTree.Element("description")      -- добавление новых тегов в файл
# description.text = "Showed excellent skills during the course"
# greg.append(description)

# description = greg.find("description")  # удаление тегов
# greg.remove(description)

tree.write("xml_file_modified.xml")
