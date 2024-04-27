string_0 = "A Computer Science portal for geeks"
print(string_0)
print(type(string_0))


# Variables

first_name ="     JoHn"
last_name = "    DoE"

# create full Name

# full_name =(first_name +" " + last_name)

# print (full_name)


first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()

full_name =first_name +" " + last_name
print(full_name)


# check if its an email 

email="john@mail.com"
print(email.count("@") == 1)


# split it break up a string according to a criteria
st = "This is my book"

print(type(st.split(" ")))


# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces

st2="The Dog Breed is German Shepherd"
st2a=st2.split(" ")[2:5]
print(st2a)

st3="Defeats for the Clinton forces, this was her moment of triumph"
st3a=st3.split(" ")[3 :5]
print(st3a)


# Split the below sentence using a semicolon i.e ; And display length of the result. 
# “The lazy dog; ran so fast; it hit the wall.” 

st4="The lazy dog; ran so fast; it hit the wall"
st4a=st4.split(";")
print(len(st4a))

# Having the string r = '["E","W","C"]' #Manipulate it to display EWC

ra = '["E","W","C"]'
rstg="".join(map(str,ra))
print(rstg)

name="JOHN DEO"
print(name[2: : 1])