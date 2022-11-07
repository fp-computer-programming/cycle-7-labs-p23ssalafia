#Author: Sean Salafia 11/7/22


#Make a list defined by a variabel and print it

list_of_colors = ["red", "orange", "yellow", "green"] 
print (list_of_colors)

#Extend the list by using the extend method to add to the list. Print list.
list_of_colors.extend (["blue", "indigo", "violet"])
print (list_of_colors)

#Add sky blue to the end of the list by appending and printing.
list_of_colors.append ("sky blue")
print (list_of_colors)

#Add magenta to the 3rd index position
list_of_colors.insert (3,"magneta")
print (list_of_colors)

#Copy the list of colors
copy_of_list_of_colors = list_of_colors[:]
print (list_of_colors)
print (copy_of_list_of_colors)

#Remove one element from the copy of the list
copy_of_list_of_colors.remove ("red")
print(copy_of_list_of_colors)