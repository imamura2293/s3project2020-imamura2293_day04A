class Member:
    def __init__(self, first_name: str, family_name: str):
        self.first_name = first_name
        self.family_name = family_name


bob = Member(first_name="bob", family_name="Martin")

print(bob.first_name)
print(bob.family_name)

# what type of bob
print(type(bob))
print(type("hello"))
print(type(345))




tom = Member(first_name="tom", family_name="Ford")

print(type(tom))
print(tom.first_name)
print(tom.family_name)
