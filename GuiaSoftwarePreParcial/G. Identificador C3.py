nombre = input()
apellido = input()

nick = (nombre[:5] + apellido[0]).lower()
pin = (len(nombre) * 1000 + len(apellido)) % 10000
id = "C3-" + nick + "-" + str(pin)

print(f"Nick: {nick}")
print(f"Pin: {pin}")
print(f"ID: {id}")
