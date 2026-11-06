"""
Simplex passo a passo (maximização, restrições <=)
Uso:  python simplex.py
Edite os dados na seção "DADOS DO PROBLEMA" lá embaixo e rode.
Não precisa instalar nada (só Python 3).
Imprime TODOS os quadros, quem entra, quem sai, as razões e as contas de cada linha.
"""
from fractions import Fraction as F


def fmt(x):
    """Mostra fração e decimal (ex.: 80/3 (26,67))."""
    x = F(x)
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator} ({float(x):.2f})".replace(".", ",")


def imprimir_quadro(base, cols, T, z, titulo):
    print(f"\n=== {titulo} ===")
    larg = 14
    print("Base".ljust(6) + "".join(c.rjust(larg) for c in cols) + "b".rjust(larg))
    for nome, linha in zip(base, T):
        print(nome.ljust(6) + "".join(fmt(v).rjust(larg) for v in linha))
    print("Z".ljust(6) + "".join(fmt(v).rjust(larg) for v in z))


def simplex(c, A, b, nomes=None, minimizar=False):
    m, n = len(A), len(c)
    nomes = nomes or [f"x{j+1}" for j in range(n)]
    folgas = [f"f{i+1}" for i in range(m)]
    cols = nomes + folgas

    c_uso = [-v for v in c] if minimizar else list(c)
    if minimizar:
        print("Minimização: vamos maximizar (-Z) e trocar o sinal no final.")

    T = [[F(v) for v in A[i]] + [F(int(i == j)) for j in range(m)] + [F(b[i])] for i in range(m)]
    z = [F(-v) for v in c_uso] + [F(0)] * m + [F(0)]
    base = folgas[:]

    print("Linha Z começa com os coeficientes da função objetivo COM SINAL TROCADO.")
    imprimir_quadro(base, cols, T, z, "QUADRO INICIAL")

    it = 0
    while True:
        menor = min(z[:-1])
        if menor >= 0:
            break
        it += 1
        e = z[:-1].index(menor)
        print(f"\n--- ITERAÇÃO {it} ---")
        print(f"Mais negativo na linha Z: {fmt(menor)} -> ENTRA {cols[e]}")

        razoes = []
        for i in range(m):
            if T[i][e] > 0:
                r = T[i][-1] / T[i][e]
                razoes.append((r, i))
                print(f"  Razão {base[i]}: {fmt(T[i][-1])} ÷ [{fmt(T[i][e])}] = {fmt(r)}")
            else:
                print(f"  Razão {base[i]}: coeficiente {fmt(T[i][e])} <= 0 -> ignora")
        if not razoes:
            print("Nenhuma razão válida: SOLUÇÃO ILIMITADA (Z cresce sem limite).")
            return
        _, l = min(razoes)
        p = T[l][e]
        print(f"Menor razão -> SAI {base[l]}.  Pivô = {fmt(p)}")

        T[l] = [v / p for v in T[l]]
        print(f"  Nova linha {cols[e]} = linha {base[l]} / {fmt(p)}")
        for i in range(m):
            if i != l and T[i][e] != 0:
                k = T[i][e]
                print(f"  Nova {base[i]} = {base[i]} - ({fmt(k)}) x nova linha {cols[e]}")
                T[i] = [a - k * bb for a, bb in zip(T[i], T[l])]
        k = z[e]
        print(f"  Nova Z = Z - ({fmt(k)}) x nova linha {cols[e]}")
        z = [a - k * bb for a, bb in zip(z, T[l])]
        base[l] = cols[e]
        imprimir_quadro(base, cols, T, z, f"QUADRO APÓS ITERAÇÃO {it}")

    print("\nNão há negativos na linha Z -> SOLUÇÃO ÓTIMA.\n")
    valores = {col: F(0) for col in cols}
    for nome, linha in zip(base, T):
        valores[nome] = linha[-1]
    zval = -z[-1] if minimizar else z[-1]
    print("RESPOSTA:")
    for nome in nomes:
        print(f"  {nome} = {fmt(valores[nome])}")
    print(f"  Z = {fmt(zval)}")
    print("FOLGAS (sobra de cada recurso):")
    for i, f_ in enumerate(folgas):
        v = valores[f_]
        status = "SOBROU" if v > 0 else "usado por completo (recurso escasso)"
        preco = z[n + i]
        print(f"  {f_} = {fmt(v)}  -> {status}; preço-sombra = {fmt(preco)}")
    for j in range(n + m):
        if cols[j] not in base and z[j] == 0:
            print(f"Obs.: {cols[j]} está fora da base com 0 na linha Z -> existem SOLUÇÕES ÓTIMAS ALTERNATIVAS.")


def analisar_quadro(cols, base, T, z):
    """Para questões tipo 'leia este quadro'. T = linhas (sem a coluna Base), último valor = b."""
    cols_all = cols
    imprimir_quadro(base, cols_all, [[F(v) for v in l] for l in T], [F(v) for v in z], "QUADRO DADO")
    neg = [(F(v), j) for j, v in enumerate(z[:-1]) if F(v) < 0]
    if neg:
        print("\na) NÃO é ótima: há negativos na linha Z ->", ", ".join(f"{cols[j]}={fmt(v)}" for v, j in neg))
        v, e = min(neg)
        print(f"   Próxima a entrar: {cols[e]}")
        raz = [(F(T[i][-1]) / F(T[i][e]), i) for i in range(len(T)) if F(T[i][e]) > 0]
        for r, i in raz:
            print(f"   Razão {base[i]}: {fmt(T[i][-1])} ÷ [{fmt(T[i][e])}] = {fmt(r)}")
        if raz:
            print(f"   Sairia: {base[min(raz)[1]]}")
    else:
        print("\na) É ótima: nenhum negativo na linha Z.")
    print(f"b) Z = {fmt(z[-1])}")
    print("c) Valores (na base = b da linha; fora da base = 0):")
    for c_ in cols:
        val = F(T[base.index(c_)][-1]) if c_ in base else F(0)
        print(f"   {c_} = {fmt(val)}")


if __name__ == "__main__":
    # ================= DADOS DO PROBLEMA =================
    # Max Z = 10x1 + 12x2 + 8x3 + 15x4   (Questão 2 da Avaliação II)
    c = [10, 12, 8, 15]
    A = [
        [1, 2, 1, 1],
        [2, 1, 2, 2],
        [3, 1, 4, 1],
    ]
    b = [100, 120, 90]
    simplex(c, A, b)

    # Para a cervejaria (Questão 1), troque por:
    # simplex([600, 500, 350, 400],
    #         [[6, 5, 4, 4], [3, 2, 1, 1], [2, 2, 1, 3]],
    #         [300, 120, 160],
    #         nomes=["IPA", "Stout", "Pilsen", "Weiss"])

    # Para LER um quadro pronto (Questão 3), descomente:
    # analisar_quadro(cols=["x1", "x2", "x3", "f1", "f2", "f3"],
    #                 base=["f1", "f2", "x2"],
    #                 T=[[0, 0, 1, 1, 0, -2, 40],
    #                    [-0.5, 0, 0.5, 0, 1, -1.5, 30],
    #                    [0.5, 1, 0.5, 0, 0, 0.5, 50]],
    #                 z=[-50, 0, -150, 0, 0, 250, 25000])
