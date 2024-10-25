# itens nao podem se repetir

materiais = {'ferro fundido','aluminio','aço','bronze'}

for i in materiais:
    print(i.upper())

materiais.add('plástico')
print(materiais)

materiais.remove('aço')
print(materiais)
