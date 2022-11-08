#Author: Sean Salafia 11/8/22

#Print a line to clearly see where each runtime begins and ends
x = "________________________________________________________________________________"
print (x)


#make a list and set it equal to a variable
list_of_subjects = ["Algebra", "Programming" , "English"]
print(list_of_subjects)

#Add APUSH to the end of the list
list_of_subjects.append ("APUSH")
print (list_of_subjects)

#Return the index of the word "Algebra"
find_index = list_of_subjects.index ("Algebra")
print (find_index)

#Sort list of subjects alphabetically
list_of_subjects.sort ()
print (list_of_subjects)

#Copy the list
copy_list_of_subjects = list_of_subjects [:]
print (copy_list_of_subjects)

#Reverse the copied list
copy_list_of_subjects.reverse ()
print (copy_list_of_subjects)