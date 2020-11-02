class User:
    def __init__(self, first_name: str, family_name: str):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self) -> str:
        return self.first.name + " " + self.family_name


ken = User(first_name="ken", family_name="Tanaka")

print(ken.first_name)
print(ken.family_name)

print(type(ken))

print(ken.first_name + " " + ken.family_name)

print(ken.full_name())
