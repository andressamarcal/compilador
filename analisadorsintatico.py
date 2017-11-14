import lexico

tabela_slr = [[   2,       99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   1,  99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   00,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,       4,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99,  3, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     12,   99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,      9,   99,   99, 99, 99,  99,  99,   5,   7,   99,   8,   99,   99,    6,         14,    99,    99],
[   99,      99,      17,     49,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 15,  16,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,    "r5",  99,  99,  99,   "r5",   "r5",     99,        99,  99,   99, "r5",  99, 99,   99,   99,    99,   "r5",   "r2",   99, 99, 99,  99,  99,   5,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     12,   99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,      9,   99,   99, 99, 99,  99,  99,  18,   7,   99,   8,   99,   99,    6,         14,    99,    99],
[   99,      99,      99,     12,   99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,      9,   99,   99, 99, 99,  99,  99,  57,   7,   99,   8,   99,   99,    6,         14,    99,    99],
[   99,      99,      99,     12,   99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  19,   7,   99,   8,   99,   99,    6,         14,    99,    99],
[   99,      99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,"r30",   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     20,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   00,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     23,   99,  99,  99,     99,     99,     22,        24,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   21,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  25,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  26, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     12,   99,  99,  99,     10,     11,     99,        99,  99,   99,   13,  99, 99,   99,   99,    30,     99,   99,   99, 99, 99,  99,  99,  99,  28,   99,  29,   99,   99,   55,         14,    99,    27],
[   99,      99,      99,   "r3",   99,  99,  99,   "r3",   "r3",     99,        99,  99,   99, "r3",  99, 99,   99,   99,    99,   "r3",   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      17,     49,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 31,  16,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,   "r5",   58,  99,  99,   "r5",   "r5",     99,        99,  99,   99, "r5",  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,   99,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,"r22",   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,  "r16",   99,  99,  99, "r16",  "r16",      99,        99,  99,   99, "r16", 99, 99,   99,   99,    99, "r16",    "r16",   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,  "r11",   32,  99,  99, "r11",  "r11",      99,        99,  99,   99, "r11", 99, 99,   99,   99,    99, "r11",    99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,   48,  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,"r13",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,"r15",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,"r14",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     35,  99,   99,  99,     99,     99,     99,        36,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   33,   34,   99,         99,    99,    99],
[   99,      99,      99,     35,  99,   99,  99,     99,     99,     99,        36,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   38,   99,         99,    37,    99],
[   99,      99,      99,  "r23",  99,   99,  99,  "r23",  "r23",     99,        99,  99,   99,"r23",  99, 99,   99,   99, "r23",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     12,  99,   99,  99,     10,     11,     99,        99,  99,   99,   99,  99, 99,   99,   99,    30,     99,   99,   99, 99, 99,  99,  99,  99,  28,   99,  29,   99,   99,   99,         99,    99,    39],
[   99,      99,      99,     12,  99,   99,  99,     10,     11,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  28,   99,  29,   99,   99,   99,         99,    99,    40],
[   99,      99,      99,  "r29",  99,   99,  99,  "r29",  "r29",     99,        99,  99,   99,"r29",  99, 99,   99,   99, "r29",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,   "r4",  99,   99,  99,   "r4",   "r4",     99,        99,  99,   99, "r4",  99, 99,   99,   99,    99,   "r4",   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,  "r11",  99,   99,  99,  "r11",  "r11",     99,        99,  99,   99,"r11",  99, 99,   99,   99, "r11",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,  41,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,"r19",   99,  99,     99,     99,     99,        99,  99,   42,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,"r20",  99,  99,     99,     99,     99,        99,  99,"r20",   99,  99,"r20", 99,"r20",    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,"r21",  99,  99,     99,     99,     99,        99,  99,"r21",   99,  99,"r21", 99,"r21",    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,  99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 43,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,  99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   44,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,   "r26", 99,   99,  99,  "r26",  "r26",     99,        99,  99,   99,"r26",  99, 99,   99,   99, "r26",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,   "r27", 99,   99,  99,  "r27",  "r27",     99,        99,  99,   99,   99,  99, 99,   99,   99, "r27",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,   "r17", 99,   99,  99,  "r17",  "r17",     99,        99,  99,   99,"r17",  99, 99,   99,   99, "r17",  "r17",   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99,"r18",  99,  99,     99,     99,     99,        45,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   45,   99,         99,    99,    99],
[   99,      99,      99,     99,  99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   46,   99,    99,      99,  99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     35,  99,   99,  99,     99,     99,     99,        36,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   47,   99,         99,    99,    99],
[   99,      99,      99,     99,"r18",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,   "r24", 99,   99,  99,  "r24",  "r24",     99,        99,  99,   99, "r24", 99, 99,   99,   99, "r24",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,     99, "r5",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, "r25",   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,   "r12", 99,   99,  99,   "r12",  "r12",    99,        99,  99,   99,"r12",  99, 99,   99,   99, "r12",  "r12",   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,      99, 99,   51,  52,     99,     99,     53,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  50,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,      99, 54,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,      99,"r7",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,      99,"r8",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,      99,"r9",  99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,    "r6",    "r6", 99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,      99, 99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    30,     99,   99,   99, 99, 99,  99,  99,  99,  99,   28,  29,   99,   99,   99,         99,    99,    56],
[   99,      99,      99,   "r28", 99,   99,  99,  "r28",   "r28",    99,        99,  99,   99,"r28",  99, 99,   99,   99, "r28",     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,      99, 99,   99,  99,     99,     99,     99,        99,  99,   99,   99,  99, 99,   99,   99,    99,     99,"r10",   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99],
[   99,      99,      99,    "r5", 99,   99,  99,   "r5",   "r5",     99,        99,  99,   99, "r5",  99, 99,   99,   99,    99,     99,   99,   99, 99, 99,  99,  99,  99,  99,   99,  99,   99,   99,   99,         99,    99,    99]]

gramatica = ["P'->1", "P->3", "V->2", "LV->2","LV->2", "D->3", "TIPO->1", "TIPO->1", "TIPO->1", "A->2", "ES->3", "ES->3", "ARG->1", "ARG->1", "ARG->1", "A->2", "CMD->4", "LD->3", "LD->1", "OPRD->1", "OPRD->1", "A->2", "COND->2", "CABECALHO->5", "EXP_R->3", "CORPO->2", "CORPO->2", "CORPO->2", "CORPO->1", "A->1"]
coluna = [ "inicio", "varinicio", "varfim", "id", "pt_v", "inteiro", "real", "leia", "escreva", "literal", "num", "rcb", "opm", "se", "ab_p", "fc_p", "entao", "opr","fimse", "fim", "$", "P", "V", "LV", "D", "TIPO", "A", "ES", "ARG", "CMD", "LD", "OPRD", "COND","CABECALHO","EXP_R", "CORPO"]
producoes = ["P'->P", "P->inicio V A", "V-> varinicio LV", "LV->D LV","LV-> varfim ;", "D-> id TIPO ;", "TIPO-> int", "TIPO->real", "TIPO-> literal", "A->ES A", "ES-> leia id ;", "ES-> escreva ARG ;", "ARG-> literal", "ARG-> num", "ARG->id", "A-> CMD A", "CMD-> id rcb LD ;", "LD-> OPRD opm OPRD", "LD-> OPRD", "OPRD-> id", "OPRD-> num", "A-> COND A", "COND-> CABECALHO CORPO", "CABECALHO-> se ( EXP_R ) entao", "EXP_R->OPRD opr OPRD", "CORPO-> ES CORPO", "CORPO-> CMD CORPO", "CORPO-> COND CORPO", "CORPO->fimse", "A->fim"]

def separa_reducao(reducao):
    a = reducao.replace("r", "")
    return int(a)

def __main__():
    stack = [0]
    fonte = open("texto.alg", "r")
    s = 0
    while(True):
        lexema = fonte.readline()
        if(lexema == ""):
            break
        a = 0
        a = lexico.__main__(lexema)
        i = 0
        while(i < len(a)):
            try:
                indice = coluna.index(a[i])
            except:
                print("error")
                break
            auxiliar = tabela_slr[s][indice]
            s = auxiliar
            if(str(auxiliar).isdigit() and auxiliar == 00):
                print("Aceita!!")
                break
            elif(str(auxiliar).isdigit() == True and auxiliar != 99):
                stack.append(coluna[indice])
                stack.append(auxiliar)
                i += 1
            else:
                aux2 = gramatica[separa_reducao(auxiliar)-1]
                aux2 = aux2.split("->")
                split_esq = aux2[0]
                split_dir = int(aux2[1]) * 2
                aux3 = 0
                print(producoes[separa_reducao(auxiliar) - 1])
                while(aux3 < split_dir):
                    stack.pop()
                    aux3 += 1
                stack.append(split_esq)
                indiceaux = int(coluna.index(stack[len(stack) - 1]))
                indiceaux2 = int(stack[len(stack) - 2])
                s = tabela_slr[indiceaux2][indiceaux]
                stack.append(s)
    fonte.close()


__main__()
