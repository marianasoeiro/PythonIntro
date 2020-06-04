#Autor: Mariana Soeiro
#About: Exercicio 2 - Lista 4 (Python)

# -  Given an input list
# -  Removes the element at index 4 and
# -  Add it to the 2nd position and also,
# -  The end of the list = [54, 44, 27, 79, 91, 41]

List = [54, 44, 27, 79, 91, 41]

print("Original list ", List)
element = List.pop(4)
print("List After removing element at index 4 ", List)

List.insert(2, element)
print("List after Adding element at index 2 ", List)

List.append(element)
print("List after Adding element at last ", List)
