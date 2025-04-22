class Biodata:
    def __init__(self, name, age, profession, address, phone, email):
        self.name = name
        self.age = age
        self.profession = profession
        self.address = address
        self.phone = phone
        self.email = email

    def display_biodata(self):
        biodata_text = f"""
        Biodata:
        Name: {self.name}
        Age: {self.age}
        Profession: {self.profession}
        Address: {self.address}
        Phone: {self.phone}
        Email: {self.email}
        """
        print(biodata_text)


# User input section
name = input("Enter your name: ")
age = input("Enter your age: ")
profession = input("Enter your profession: ")
address = input("Enter your address: ")
phone = input("Enter your phone number: ")
email = input("Enter your email address: ")

# Create Biodata object
my_biodata = Biodata(name, age, profession, address, phone, email)

# Display biodata
my_biodata.display_biodata()
