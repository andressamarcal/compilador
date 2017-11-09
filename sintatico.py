import lexico

        #############inicio | varinicio | varfim | id |  ; | int | real | leia | escreva | literal | num | rcb | opm | se | ( | ) | entao | opr | fimse | fim |  $  | P  | V | LV | D | TIPO | A | ES | ARG | CMD | LD | OPRD | COND | CABECALHO| EXP_R |CORPO
tabela_slr = """0"""[   2,       99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   1,  99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
             """1"""[   99,      99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   00,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
             """2"""[   99,       4,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99,  3, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
             """3"""[   99,      99,      99,     12,   99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,      9,   99,   99, 99, 99,  99,  99,   5,   7,   99,   8,   99,   99,    6,         14,    99,    99],
             """4"""[   99,      99,      17,     49,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 15,  16,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],    
             """5"""[   99,      99,      99,    "r5",  99,  99,  99,   "r5",   "r5",     99,        99,  99,   99, "r5",  99, 99,   99,   99,    99,   "r5",   99,   99, 99, 99,  99,  99,   5,  99,   99,  99,   99,   99,   99,         99,    99,    99],
             """6"""[   99,      99,      99,     12,   99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,      9,   99,   99, 99, 99,  99,  99,  18,   7,   99,   8,   99,   99,    6,         14,    99,    99],
             """7"""[   99,      99,      99,     12,   99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,      9,   99,   99, 99, 99,  99,  99,  57,   7,   99,   8,   99,   99,    6,         14,    99,    99],
             """8"""[   99,      99,      99,     12,   99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  19,   7,   99,   8,   99,   99,    6,         14,    99,    99],
             """9"""[   99,      99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,"r30",   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """10"""[   99,      99,      99,     20,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   00,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """11"""[   99,      99,      99,     23,   99,  99,  99,     99,     99,     22,        24,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   21,  99,   99,   99,   99,         99,    99,    99],
            """12"""[   99,      99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  25,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """13"""[   99,      99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  26, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """14"""[   99,      99,      99,     12,   99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    30,     99,   99,   99, 99, 99,  99,  99,  99,  28,   99,  29,   99,   99,   55,         99,    99,    27],
            """15"""[   99,      99,      99,   "r3",   99,  99,  99,   "r3",   "r3",     99,        99,  99,   99, "r3",  99, 99,   99,   99,    99,   "r3",   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """16"""[   99,      99,      17,     49,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 31,  16,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """17"""[   99,      99,      99,   "r5",   58,  99,  99,   "r5",   "r5",     99,        99,  99,   99, "r5",  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """18"""[   99,      99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,"r22",   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """19"""[   99,      99,      99,  "r16",   99,  99,  99, "r16",  "r16",      99,        99,  99,   99, "r16", 99, 99,   99,   99,    99, "r16",    99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """20"""[   99,      99,      99,  "r11",   32,  99,  99, "r11",  "r11",      99,        99,  99,   99, "r11", 99, 99,   99,   99,    99, "r11",    99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """21"""[   99,      99,      99,     99,   48,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """22"""[   99,      99,      99,     99,"r13",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """23"""[   99,      99,      99,     99,"r15",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """24"""[   99,      99,      99,     99,"r14",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """25"""[   99,      99,      99,     35,  99,   99,  99,     99,     99,     99,        36,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   33,   34,   99,         99,    99,    99],
            """26"""[   99,      99,      99,     35,  99,   99,  99,     99,     99,     99,        36,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   38,   99,         99,    37,    99],
            """27"""[   99,      99,      99,  "r23",  99,   99,  99,  "r23",  "r23",     99,        99,  99,   99,"r23",  99, 99,   99,   99, "r23",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """28"""[   99,      99,      99,     12,  99,   99,  99,     10,     11,     99,        99,  99,   99,   99,  99, 99,   99,   99,    30,     99,   99,   99, 99, 99,  99,  99,  99,  28,   99,  29,   99,   99,   99,         99,    99,    39],
            """29"""[   99,      99,      99,     12,  99,   99,  99,     10,     11,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  28,   99,  29,   99,   99,   99,         99,    99,    40],
            """30"""[   99,      99,      99,  "r29",  99,   99,  99,  "r29",  "r29",     99,        99,  99,   99,"r29",  99, 99,   99,   99, "r29",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """31"""[   99,      99,      99,   "r4",  99,   99,  99,   "r4",   "r4",     99,        99,  99,   99, "r4",  99, 99,   99,   99,    99,   "r4",   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """32"""[   99,      99,      99,  "r11",  99,   99,  99,  "r11",  "r11",     99,        99,  99,   99,"r11",  99, 99,   99,   99, "r11",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """33"""[   99,      99,      99,     99,  41,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """34"""[   99,      99,      99,     99,  99,   99,  99,     99,     99,     99,        99,  99,   42,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """35"""[   99,      99,      99,     99,"r20",  99,  99,     99,     99,     99,        99,  99,"r20",   99,  99,"r20", 99,"r20",    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """36"""[   99,      99,      99,     99,"r21",  99,  99,     99,     99,     99,        99,  99,"r21",   99,  99,"r21", 99,"r21",    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """37"""[   99,      99,      99,     99,  99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 43,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """38"""[   99,      99,      99,     99,  99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   44,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """39"""[   99,      99,      99,   "r26", 99,   99,  99,  "r26",  "r26",     99,        99,  99,   99,"r26",  99, 99,   99,   99, "r26",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """40"""[   99,      99,      99,   "r27", 99,   99,  99,  "r27",  "r27",     99,        99,  99,   99,   99,  99, 99,   99,   99, "r27",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """41"""[   99,      99,      99,   "r17", 99,   99,  99,  "r17",  "r17",     99,        99,  99,   99,"r17",  99, 99,   99,   99, "r17",  "r17",   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """42"""[   99,      99,      99,     99,"r18",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   45,   99,         99,    99,    99],
            """43"""[   99,      99,      99,     99,  99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   46,   99,    99,      99,  99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """44"""[   99,      99,      99,     35,  99,   99,  99,     99,     99,     99,        26,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   47,   99,         99,    99,    99],
            """45"""[   99,      99,      99,     99,"r18",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """46"""[   99,      99,      99,   "r24", 99,   99,  99,  "r24",  "r24",     99,        99,  99,   99, "r24", 99, 99,   99,   99, "r24",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """47"""[   99,      99,      99,     99, "r5",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """48"""[   99,      99,      99,   "r12", 99,   99,  99,   "r12",  "r12",    99,        99,  99,   99,"r12",  99, 99,   99,   99, "r12",  "r12",   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """49"""[   99,      99,      99,      99, 99,   51,  52,     99,     99,     53,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  50,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """50"""[   99,      99,      99,      99, 54,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """51"""[   99,      99,      99,      99,"r7",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """52"""[   99,      99,      99,      99,"r8",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """53"""[   99,      99,      99,      99,"r9",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """54"""[   99,      99,    "r6",    "r6", 99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """55"""[   99,      99,      99,      99, 99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    30,     99,   99,   99, 99, 99,  99,  99,  99,  99,   28,  29,   99,   99,   99,         99,    99,    56],
            """56"""[   99,      99,      99,   "r28", 99,   99,  99,  "r28",   "r28",    99,        99,  99,   99,"r28",  99, 99,   99,   99, "r28",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """57"""[   99,      99,      99,      99, 99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,"r10",   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
            """58"""[   99,      99,      99,    "r5", 99,   99,  99,   "r5",   "r5",     99,        99,  99,   99, "r5",  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],

  

# Relacionar colunas com nome:
###IDEIA:
#tabela_slr[s].[a], relacionar a parte direita da igualdade com o número da coluna.
#Exemplo: tabela_slr[3].[inicio], procura no vetor qual o número de "inicio", e retorna, daí ficaria:
# tabela_slr[3].[0], sendo "0" o número da coluna do inicio pra fazer a busca na tabela. 



gramatica = ["P'->1", "P->3", "V->2", "LV->2","LV->2", "D->3", "TIPO->1", "TIPO->1", "TIPO->1", "A->2", "ES->3", "ES->3", "ARG->1", "ARG->1", "ARG->1", "A->2", "CMD->4", "LD->3", "LD->1", "OPRD->1", "OPRD->1", "A->2", "COND->2", "CABECALHO->5", "EXP_R->3", "CORPO->2", "CORPO->2", "CORPO->2", "CORPO->1", "A->1"]
coluna = [ "inicio", "varinicio", "varfim", "id", "pt_v", "Inteiro", "real", "leia", "escreva", "literal", "num", "rcb", "opm", "se", "ab_p", "fc_p", "entao", "opr","fimse", "fim", "$", "P", "V", "LV", "D", "TIPO", "A", "ES", "ARG", "CMD", "LD", "OPRD", "COND","CABECALHO","EXP_R", "CORPO"]
producoes = ["P'->P", "P->inicio V A", "V-> varinicio LV", "LV->D LV","LV-> varfim ;", "D-> id TIPO ;", "TIPO-> int", "TIPO->real", "TIPO-> literal", "A->ES A", "ES-> leia id ;", "ES-> escreva ARG ;", "ARG-> literal", "ARG-> num", "ARG->id", "A-> CMD A", "CMD-> id rcb LD ;", "LD-> OPRD opm OPRD", "LD-> OPRD", "OPRD-> id", "OPRD-> num", "A-> COND A", "COND-> CABECALHO CORPO", "CABECALHO-> se ( EXP_R ) entao", "EXP_R->OPRD opr OPRD", "CORPO-> ES CORPO", "CORPO-> CMD CORPO", "CORPO-> COND CORPO", "CORPO->fimse", "A->fim"]


Algoritmo SLR
s = estado no topo da pilha

lexema = 0;
while(true)

  a = lexema #                     vamos supor que recebeu "inicio"
  Procurar "a" no TXT do T1 #     encontrou lá (lexema = "inicio", token = "inicio")
  a = split pra pegar só o token # a = "inicio" 
  procurar "a" no vetor coluna[] # procurou, encontrou "início" na posição coluna[0]
  a = 0
  lexema = lexema + 1

  auxiliar = [s][a] 
  # Caso 1: shift 
  se auxiliar == número && != 99
        empilha coluna[a] # vai empilhar o token, no caso "inicio"
        empilha auxiliar

  Senão, se auxiliar != número
  # Caso 2: reduce, nesse caso auxiliar vai ter um "r" seguido de número
        aux2 = procura no vetor gramatica[] a posição do número seguido do "r" - 1
        split_esq = parte antes de "->", uma letra, ex: LD
        split_dir = parte depois do "->", um número ex: 3

        desempilha( 2 * split_dir)
        empilha(split_esq)
        imprime produção correspondente ao numero seguido do "r", que vai estar no vetor producoes
        s = [topo_pilha] [topo_pilha-1]
        
 Fim While
        

 
######## algoritmo parcialmente implementado
stack = [0]
i = 0

while(1):
    ip = entrada[i] 
    if(tabela_slr[s][a].isdigit() == True and tabela_slr[s,a] != 99):
        stack.append(entrada[i])
        stack.append(tabela_slr[s][a])
    elif(tabela_slr[s][a].isdigit() != True):
        for p in range(2*len(dirprod)): #dirprod = parte direita da producao
            stack.pop() #da pop nas 2 * tamanho de Beta entradas da pilha
        stack.append(stack[len(stack)]) #append no número do estado
        stack.append(tabela_slr[stack[len(stack)]][esqprod]) #esqprod = parte esquerda da producao
        print(prod) #printa a producao na tela
    elif(tabela_slr[s][a] == 00):
        return 0
    else:
        raise Exception("Erro!")

        # adicionar (+1) para achar o índice certo



