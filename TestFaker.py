from faker import Faker
fake = Faker()

nombre = fake.name()

direccion = fake.address()

texto = fake.text()

print("Nombre:")
print(nombre)

print("Dirección:")
print(direccion)

print("Texto:")
print(texto)

# Imprime 10 nombres
print("Se van a imprimir 10 nombres")
contador = 1
for _ in range(10):
  print(str(contador) + " - " + fake.name())
  contador=contador+1
print("Se termina de imprimir 10 nombres")
