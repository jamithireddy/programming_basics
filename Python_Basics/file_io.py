# file name and access mode ( if we are opening it for reading / writing / appending)

# Mode w opens an existing file. If any data is present, it deletes that data and writes on it. If file not present, it creates it.
fh = open("example.txt", "w")

for i in range(1, 25):
    fh.write("You are realiading Line %d \n" % i)
fh.close()
# we shall get an error if we try and write anythiong after cl;osing the file
