arqui = open('/home/mateus/Área de Trabalho/Rotinas/julho','w')
arqui.write(
    'Rotina:\n'        
             '                      [Duolingo] - [Leitura]   -   [Commit]  -  [codewars]  - [Alongar-se]\n')
for i in range(31):
    arqui.write(f'{i+1} de Julho de 2021        []          []             []            []             []\n')
arqui.close()    