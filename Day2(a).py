#reading from a file
with open ("drax.txt", "r") as file_object:
    file_contents = file_object()
    print(file_contents)


#writing to a file
with open ("drax.txt", "w") as file_object:
    file_object.write("n this is another")



#appending or update to file
with open ("drax.txt", "a") as file_object:
    file_object.write("\n this is another")