import string

naoTerminais = set(string.ascii_uppercase)
terminais = set(string.ascii_lowercase + "ε")

def validarLadoEsquerdo(lado, regra):
    if any(i not in naoTerminais.union(terminais) for i in lado):
        raise ValueError(f"Erro: Lado esquerdo da regra '{regra}' contém símbolo inválido.")
    if not any(i in naoTerminais for i in lado):
        raise ValueError(f"Erro: Lado esquerdo da regra '{regra}' deve conter pelo menos um símbolo não terminal (A-Z).")

def validarLadoDireito(lado, regra):
    if any(i not in naoTerminais.union(terminais) for i in lado):
        raise ValueError(f"Erro: Lado direito da regra '{regra}' contém símbolo inválido.")

def tipoGramatica(ladoEsquerdo, ladoDireito):
    tipoDeRegra = []
    tipo3Confirmacao = []

    for i in range(len(ladoEsquerdo)):
        esq = ladoEsquerdo[i]
        dir = ladoDireito[i]

        if len(esq) > len(dir):
            tipoDeRegra.append(0)
            continue

        if not (len(esq) == 1 and esq in naoTerminais):
            tipoDeRegra.append(1)
            continue

        if len(dir) > 2:
            tipoDeRegra.append(2)
            continue

        if len(dir) == 2 and dir[0] in terminais and dir[1] in naoTerminais:
            tipoDeRegra.append(3)
            tipo3Confirmacao.append('D')
            continue
        elif len(dir) == 2 and dir[0] in naoTerminais and dir[1] in terminais:
            tipoDeRegra.append(3)
            tipo3Confirmacao.append('E')
            continue
        elif len(dir) == 1 and dir[0] in terminais:
            tipoDeRegra.append(3)
            tipo3Confirmacao.append('T')
            continue
        else:
            tipoDeRegra.append(2)
            continue

    if 0 in tipoDeRegra:
        return "Gramática Irrestrita (Tipo 0)"
    elif 1 in tipoDeRegra:
        return "Gramática Sensível ao Contexto (Tipo 1)"
    elif 2 in tipoDeRegra:
        return "Gramática Livre de Contexto (Tipo 2)"
    else:
        tipos_unicos = set(tipo3Confirmacao)
        if 'D' in tipos_unicos and 'E' in tipos_unicos:
            return "Gramática Livre de Contexto (Tipo 2)"
        elif 'D' in tipos_unicos:
            return "Gramática Regular à Direita (Tipo 3)"
        elif 'E' in tipos_unicos:
            return "Gramática Regular à Esquerda (Tipo 3)"
        else:
            return "Gramática Regular Terminal Só (Tipo 3)"

def validar_gramatica(entrada):
    if not entrada:
        raise ValueError("Erro: Gramática vazia.")

    entrada = entrada.replace("\n", "")

    entrada = entrada.replace(" ", "")

    if not entrada.endswith('$'):
        raise ValueError("Erro: A gramática deve terminar com '$'")

    if not entrada.endswith('>$'):
        entrada = entrada[:-1]

    entrada = entrada.replace('$', 'ε')

    ladoEsquerdo = []
    ladoDireito = []

    separacaoRegras = entrada.split('-')

    for regra in separacaoRegras:
        parte = regra.split('>')
        if len(parte) == 2:
            esquerdo, direito = parte
            validarLadoEsquerdo(esquerdo, regra)
            validarLadoDireito(direito, regra)
            ladoEsquerdo.append(esquerdo)
            ladoDireito.append(direito)
        else:
            raise ValueError(f"Erro: Regra '{regra}' mal formada.")

    raiz = None
    for i in ladoEsquerdo[0]:
        if i in naoTerminais:
            raiz = i
            break

    if raiz is None:
        raise ValueError("Erro: O lado esquerdo da primeira regra deve conter pelo menos um símbolo não terminal.")

    tipo = tipoGramatica(ladoEsquerdo, ladoDireito)
    return ladoEsquerdo, ladoDireito, tipo, raiz

def pegar_nao_terminais(ladoEsquerdo, ladoDireito):
    usados = set()
    for lado in ladoEsquerdo + ladoDireito:
        for i in lado:
            if i in naoTerminais:
                usados.add(i)
    return usados

def pegar_terminais(ladoEsquerdo, ladoDireito):
    usados = set()
    for lado in ladoEsquerdo + ladoDireito:
        for i in lado:
            if i in terminais:
                usados.add(i)
    if '$' in usados:
        usados.remove('$')
    return usados

def ler_gramatica_arquivo():
    try:
        with open("gramatica.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        with open("gramatica.txt", "w") as f:
            f.write("S > aS - S>aaa - S>$")
    nome_arquivo = "gramatica.txt"
    
    try:
        with open(nome_arquivo, "r") as f:
            entrada = f.read().strip()
        print(f"Gramática lida do arquivo '{nome_arquivo}':\n{entrada}\n")
        return entrada
    except Exception as e:
        print(f"Erro ao abrir arquivo '{nome_arquivo}': {e}")
        return None

def regras(ladoEsquerdo, ladoDireito):
    lista_regras = []
    for i in range(len(ladoEsquerdo)):
        lista_regras.append(f"{ladoEsquerdo[i]} -> {''.join(ladoDireito[i])}")
    return lista_regras


def main():
    entrada = ler_gramatica_arquivo()
    if entrada is None:
        return

    try:
        ladoEsquerdo, ladoDireito, tipo, raiz = validar_gramatica(entrada)
        nao_terminais_usados = pegar_nao_terminais(ladoEsquerdo, ladoDireito)
        terminais_usados = pegar_terminais(ladoEsquerdo, ladoDireito)
        regrasP = regras(ladoEsquerdo, ladoDireito)
        print(f"\t {tipo}\n")
        print("G = (", nao_terminais_usados, ", ", terminais_usados, ",", regrasP, ",", raiz, ")\n")
    except ValueError as e:
        print(f"Erro: {e}")

main()
