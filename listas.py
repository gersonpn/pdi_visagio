coordenadas_cidades = (
    ('São Paulo', -23.5505, -46.6333),
    ('Rio de Janeiro', -22.9068, -43.1729),
    ('Belo Horizonte', -19.9167, -43.9345),
    ('Curitiba', -25.4296, -49.2713),
    ('Porto Alegre', -30.0346, -51.2177)
)


estudantes = {
    '123': {'nome': 'Ana Silva', 'idade': 20, 'curso': 'Engenharia', 'nota_final': 88},
    '456': {'nome': 'João Santos', 'idade': 22, 'curso': 'Medicina', 'nota_final': 91},
    '789': {'nome': 'Marcos Oliveira', 'idade': 21, 'curso': 'Direito', 'nota_final': 85},
    '101': {'nome': 'Carla Souza', 'idade': 23, 'curso': 'Administração', 'nota_final': 92}
}


for aluno in estudantes.keys():
    print(estudantes)


produtos = [
    {'nome': 'Notebook', 'preco': 3500.00, 'quantidade': 10},
    {'nome': 'Smartphone', 'preco': 1800.00, 'quantidade': 25},
    {'nome': 'Tablet', 'preco': 1200.00, 'quantidade': 15},
    {'nome': 'Monitor', 'preco': 800.00, 'quantidade': 8}
]




pro = [[1, 2], [3, 4], [5, 6], [7, 10]]



print(pro[1][1])
print(pro[::2])
lista_aux = []
for n in pro:
  lista_aux.append(n[1])

print(lista_aux)



buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0),
    ('C', 4, 1), ('=', 4, 2),
    ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3)
]


def lista_intervalo(intervalo):
   n = buttons[::intervalo]
   return n

l = lista_intervalo(3)
print(l)
