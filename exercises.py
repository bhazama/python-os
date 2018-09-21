#1. Open the filenames.txt file with read-only access with the open() function

file_object = open("filenames.txt","r+")
print(file_object)
#file_object.close()
#2. Print the name of the file and if it is open or closed using the .name and .closed properties

print(file_object.name)
print(file_object.closed)
#3. Use a for loop to read all lines of filenames.txt into a list variable
#file_object = open("filenames.txt", "r")

reader_list = []
for lines in file_object:
    reader_list.append(lines)
#4. Print out all the lines from the file from your variable

print(reader_list)
#5. Close the filenames.txt file and print if the file is open or closed

file_object.close()
print(file_object.closed)
#6. Create a file using the open() function called secrets.txt

file_next = open("secrets.txt","w")
print(file_next)
#7. Write your own secrets to the file with the write() function
file_next.write("WHAT IS GOING ON")

#8. Close the secrets.txt file using the close() method. DON'T FORGET!
file_next.close()

#9. Print out the contents of the text file in your terminal to prove it worked
read_file = open("secrets.txt", "r")
print(read_file.read())
#10. Open your secrets.txt file in append mode and write some more super secret info
file_new_object = open("secrets.txt", "a")
file_new_object.write("\nADD MORE THINGZZ!!!!")

#11. Close the secrets.txt file again using the close() function
file_object.close()
#12. Rename the secrets.txt and make it a "hidden" file named .supersecret.txt using the os.rename() function
import os
os.rename("secrets.txt", ".supersecret.txt")
#13. See if you can see the file in your file explorer

#14. Create a list variable named file_names that contains a list of filenames
file_names = ["hello.txt ", "there.txt ", "friend.txt"]
#15. Use the writelines() function to append the filenames to the filenames.txt file
file_reopen = open("filenames.txt", "a+")
file_reopen.writelines(file_names)
file_reopen.close()
#16. Delete the initial secrets.txt file now that you have a super secret hidden version

#17. BOSS LEVEL: Use the input() function to accept user input of a filename to create and create that file.
def create_file():
    file_name = input("Name a File: ") + ".txt"
    print(file_name)
    created_file = open(file_name, "w+")
    created_file.close()

create_file()
