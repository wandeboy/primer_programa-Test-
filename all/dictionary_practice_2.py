

colors = {'red': 'rojo', 'rojo':'red',
          'blue': 'azul', 'azul': 'blue',
          'yellow': 'amarillo', 'amarillo': 'yellow',
          'green': 'verde', 'verde': 'green',
          'pink': 'rosa', 'rosa': 'pink',
          'purple': 'morado', 'morado': 'purple',
          'orange': 'naranja', 'naranja': 'orange',
          'white': 'blanco', 'blanco': 'white',
          'black': 'negro', 'negro': 'black',
          'gray': 'gris', 'gris': 'gray',
          'brown': 'cafe', 'cafe': 'brown',
          'silver': 'platiado', 'platiado': 'silver',
          'golden': 'dorado', 'dorado': 'golden',
          'violet': 'violeta', 'violeta': 'violet'}

print('what language you know?')
print('¿Que lenguaje conoces?')
language = ''

while not (language == 'ESP' or language == 'ENG'):
    language = input('[ESP] or [ENG]: ').upper()

if language == 'ESP':
    color = ''
    while color != 's' and color != 'salir':
        color = input('Cual color quieres traducir? ["S" para Salir]: ').lower()
        if color in colors:
            print(colors[color])


elif language == 'ENG':
    color = ''
    while color != 'e' and color != 'exit':
        color = input('which color do you want translate? ["E" for Exit]: ').lower()
        print(colors[color])
        if color in colors:
            print(colors[color])


