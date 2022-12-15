import numpy as np
matrix  = np.array([[3, 12, 1, 10, 3],[11, 12, 7, 7, 6],[12, 5, 7, 4, 8],[7, 8, 4, 0, 8],[9, 5, 3, 7, 1]])
q=[0.0, 0.0, 0.0, 0.4, 0.6]
p=[0.0, 0.8, 0.2, 0.0, 0.0]
answer = {}

lower_price = max([min(x) for x in matrix])
upper_price = min([max(x) for x in np.rot90(matrix)])
if lower_price==upper_price:print("седловая точка есть", f"ответ v={lower_price}")
else:
  buff=0
  for i,pin in zip(matrix,p):
    buff+=pin*sum([x*y for x,y in zip(i,q)])
  answer["H(P,Q)"]=buff
  for k, i  in enumerate(np.rot90(matrix),1):
    answer["H(P,B{})".format(k)]=sum([x*y for x,y in zip(i,p)])
for i in [(x,y) for x,y in answer.items()]:
  print("Ответ выйгрыш игрока А в ситуации {0[0]} = {0[1]}".format(i))