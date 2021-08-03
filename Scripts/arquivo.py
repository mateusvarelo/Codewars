arqui = open('/home/mateus/Área de Trabalho/Rotinas/Agosto.txt','w')
arqui.write(
    'Rotina:\n'        
             '                      [Duolingo] - [Leitura]   -   [Commit]  -  [codewars]  - [Alongar-se] - [Aerobico-Atividade]\n')
for i in range(31):
    arqui.write(f'{i+1} de Agosto de 2021        []          []             []            []             []         []\n')
arqui.close()    