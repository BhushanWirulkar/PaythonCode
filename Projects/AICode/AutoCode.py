import docx

# String variable
name = "Alice"
print("Name:", name)

# Integer variable
age = 30
print("Age:", age)

# Float variable
height = 5.7
print("Height:", height)

# Boolean variable
is_student = True
print("Is student:", is_student)



doc = docx.Document('C:\\Bhushan\\RESUME_20Sep2025.docx')
for para in doc.paragraphs:
    print(para.text)