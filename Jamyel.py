count = 0
while (count<9):
    print "The Count is: %d " % count + "." ,
    count = count +1
    if (count %3 == 0):
        print
print "hallelujah!"
print "We're done! Goodbye! (:"


while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

   ## Note that while count == has two, not one equals signs

   ---
for row in reader:
    count += 1
    if count == 0:
        row[0] = name
        print row[0] # Name (ex. Stan Marsh)
        print "----------------"
    elif count == 1:
        row[1] = dob
        print row[1] # DOB
        print "----------------"
    elif count == 2:
        row[2] = descript
        print row[2] # Descriptive saying (ex. Respect My Authoritah!)
        print "----------------"
    elif count == 3:
        row[3] = phrase
        print row[3] # Catch Phrase (ex. Mooom!)
        print "----------------"
    elif count == 4:
        row[4] = personality
        print row[4] # Personality (ex. Jewish)
        print "----------------"
    elif count == 5:
        row[5] = character
        print row[5] # Characteristic (ex. Politically incorrect)
        print "----------------"