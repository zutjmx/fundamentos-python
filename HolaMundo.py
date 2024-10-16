print('Hola mundo')
print('Usar el paquete Faker')
from faker import Factory
fake = Factory.create()
nombre = fake.name()
direccion = fake.address()
texto = fake.text()
print(nombre)
print(direccion)
print(texto)

print('Se imprimen 10 nombres de forma aleatoria:')
for _ in range(10):
  print(fake.name())
