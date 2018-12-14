def replay(ask):
  print (eval (ask))

while(True):
  instrucao = input('digite uma operação matematica: ')
  
  try: 
    replay(instrucao)
  except:
    print('Instrução invalida') 
 
