
#Autor: Mariana Soeiro
#About: Exercicio 4 - Lista 4 (Python)

 #4. Given 2 strings, s1, and s2 [x]
 # return a new string made of the first, middle and last char each input string [x]
 
def appendMiddle(s1, s2):
   #middleIndex = int(len(s1) /2)
   print("Original Strings are", s1, s2)
   middleThree = s1[0]+ s1[int(len(s1) /2):int(len(s1) /2)+1] + s1[-1] + s2[0] + s2[int(len(s2) /2):int(len(s2) /2)+1] + s2[-1]
   print("After the new string are", middleThree)
appendMiddle("Mario", "Marcelo")



