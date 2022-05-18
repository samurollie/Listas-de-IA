# Lista 1 de IA

## Aluno: Samuel Lucas Vieira Lins Barbosa

1. Problema dos missionários e canibais

   O problema de missionários e canibais é normalmente enunciado como a seguir.  Três missionários e três canibais estão em um lado de um rio, juntamente com  um barco que pode levar uma ou duas pessoas. Descubra um meio de fazer  todos atravessarem o rio, sem deixar que um grupo de missionários de um lado  fique em número menor que o número de canibais nesse mesmo lado do rio.  Esse problema é famoso em IA porque foi assunto do primeiro artigo que  abordou a formulação de problemas a partir de um ponto de vista analítico  (Amarel, 1968). 

    * Formule o problema precisamente, fazendo apenas as especificações  necessárias para assegurar uma solução válida. Faça um diagrama do espaço  de estados completo
    
    **Formulação do Problema:**  
      Estado Inicial: Os 3 missionários e os 3 canibais do lado esquerdo do rio
      Estado Final: Os 3 missionários e os 3 canibais do lado direito do rio

    * Implemente e resolva o problema de forma ótima, utilizando um algoritmo de  busca apropriado. É uma boa ideia verificar a existência de estados repetidos? 

    * Por que você imagina que as pessoas têm dificuldades para resolver esse  quebra-cabeça, considerando que o espaço de estados é tão simples? 

2. Considere as sentenças de 1 a 16, tomadas como verdadeiras. Usando tais  sentenças, prove Q a partir delas e usando as regras de inferência: MP, MT, SH,  SD e introdução do &. Formule o problema precisamente, fazendo apenas as especificações necessárias para assegurar uma solução válida. Faça um  diagrama do espaço de estados completo. Implemente e resolva o problema,  utilizando: a) algoritmo de busca em profundidade; b) algoritmo de busca em  largura; c) algum algoritmo heurístico que você julgue apropriado ao caso, por  exemplo: A* , subida de encosta (hill-climbing).

    1. (K & L & M) → I  
    2. (I & L & J) → Q  
    3. (C & D & E) → B  
    4. (A & B ) → Q  
    5. (L & N & O & P) → Q  
    6. (C & H) → R  
    7. (R & J & M) → S  
    8. (F & H) → B  
    9. G → F  
    10. A  
    11. C  
    12. D  
    13. E  
    14. G  
    15. H  
    16. K  
    
   Operadores ou Regras de Inferência: 
MP: Modus Ponens: P → Q , P produz Q 
MT: Modus Tollens: P → Q , ~Q produz ~P 
SH: Silogismo Hipotético: P → Q , Q → R produz P → R  
SD: Silogismo Disjuntivo: P ∨ Q , ~P produz Q 
Introdução do &: P, Q produz P & Q

3. Considere a base de conhecimento (regras e fatos) abaixo, aplicar os três algoritmos estudados e determine a sequência de disparo das regras. Mostre o  funcionamento de um engenho de inferência, realizando cada uma das duas  estratégias de encadeamento de regras vistas em sala de aula: (i) encadeamento  para frente (com busca em largura) e (ii) encadeamento para trás (com busca  em profundidade), respondendo à pergunta Q = Sim, mostrando os respectivos  grafos de busca que representam as soluções. Mostre um passo a passo da  execução da solução no grafo, ressaltando o que foi produzido a cada passo.  

   R1: SE K = sim & L = sim & M = sim ENTÃO I = sim  
R2: SE I = sim & L = sim & J = sim ENTÃO Q = sim  
R3: SE C = sim & D = sim & E = sim ENTÃO B = sim  
R4: SE A = sim & B = sim ENTÃO Q = sim  
R5: SE L = sim & N = sim & O = sim & P = sim ENTÃO Q = sim  R6: SE C = sim & H = sim ENTÃO R = sim  
R7: SE R = sim & J = sim & M = sim ENTÃO S = sim  
R8: SE F = sim & H = sim ENTÃO B = sim  
R9: SE G = sim ENTÃO F = sim  
Base de fatos (inicial) = {A=sim, C=sim, D=sim, E=sim, G=sim, H=sim,  K=sim}  
Pergunta: Q = sim ??  

4. Defina com suas próprias palavras os seguintes termos: estado, espaço de  estados, árvore de busca, nó de busca, objetivo, ação, modelo de transição e  fator de ramificação. Ilustre suas definições com a ajuda de um exemplo. 


5. O problema do caixeiro viajante  

   Um caixeiro viajante precisa visitar 10 cidades do interior de Pernambuco. Ele  pede a um agente de busca que determine uma rota para sua visita tal que cada  cidade só seja visitada uma única vez, e ele percorra o menor espaço possível (em Km). O agente de busca tem um mapa do estado, e, portanto, sabe as  distâncias entre as cidades.  
Formule e implemente este problema em termos de estado inicial, estado final,  operadores e função de avaliação para Busca por melhora iterativas com Hill Climbing.  
O operador considerado para gerar os filhos do estado corrente é permutar as  cidades da rota atual duas a duas, e verificar em seguida se o caminho está conectado (segundo a tabela abaixo, que representa o mapa da questão). A  cidade inicial deve ser mantida, uma vez que o caixeiro mora lá Jϑ A rota é fechada (ele volta à cidade de origem no final). 

   ![table](https://github.com/samurollie/Listas-de-IA/blob/main/Lista%201/img/unnamed.png)

   Obs.: Cada uma das 5 questões, vale de 0 a 2 pontos.
