# 📘 Simplex: roteiro de prova (Otimização do Processo Decisório)

> **Como usar este repositório na prova**
> 1. **Roteiro rápido** → [seção 1](#1-roteiro-rápido-checklist)
> 2. **Problema em texto (tipo cervejaria)** → [seção 2](#2-modelagem-transformar-texto-em-ppl)
> 3. **"Resolva pelo Simplex"** → [seção 3](#3-método-simplex-passo-a-passo)
> 4. **"Leia este quadro"** → [seção 4](#4-como-ler-um-quadro-simplex-interpretação)
> 5. **Exemplos resolvidos completos** → [seção 6](#6-exemplos-resolvidos-avaliação-ii)
> 6. **Script que resolve e mostra as contas** → [`simplex.py`](simplex.py) ([seção 7](#7-script-simplexpy))
> 7. **Simplex no Excel (automático + fórmulas para arrastar)** → [seção 8](#8-simplex-no-excel) · planilha [`Modelo_Simplex_Automatico.xlsx`](Modelo_Simplex_Automatico.xlsx)

---

## 1. Roteiro rápido (checklist)

- [ ] Defini as variáveis (x₁, x₂… = quanto produzir de cada coisa)
- [ ] Escrevi **Max Z = …** (lucro por unidade × variável)
- [ ] Escrevi uma restrição **≤** por recurso (consumo por unidade × variável ≤ disponível)
- [ ] Coloquei **x ≥ 0**
- [ ] Adicionei uma folga **f** por restrição (≤ vira =)
- [ ] Montei o quadro: linha **Z com sinais TROCADOS**
- [ ] **Entra:** o mais negativo da linha Z
- [ ] **Sai:** menor razão **b ÷ coluna pivô** (só divisores **positivos**)
- [ ] Linha pivô ÷ pivô
- [ ] Demais linhas: **nova = antiga − (nº dela na coluna pivô) × linha pivô nova**
- [ ] Repeti até **não ter negativo na linha Z**
- [ ] Li a resposta: base = b da linha, fora da base = 0, Z = canto inferior direito
- [ ] **Conferi** substituindo nas restrições e na função objetivo

---

## 2. Modelagem (transformar texto em PPL)

**Modelo para preencher:**

```
Variáveis:  x1 = quantidade de ____ , x2 = quantidade de ____ , ...

Max Z = (lucro1)x1 + (lucro2)x2 + ...

Sujeito a:
  Recurso A:  (gasto de A por x1)x1 + (gasto de A por x2)x2 + ... ≤ (total de A)
  Recurso B:  ...                                               ≤ (total de B)
  x1, x2, ... ≥ 0
```

**Dica:** quando há uma tabela, cada **linha** vira uma restrição e cada **coluna** vira uma variável.
O "Total disponível" é o lado direito (b).

**Atenção:** se o texto e a tabela tiverem números diferentes, escreva qual usou (ex.: cervejaria: 150 h no texto e 160 h na tabela).

---

## 3. Método Simplex passo a passo

### Passo 0: forma padrão
Cada restrição `≤` ganha uma folga:
`x1 + 2x2 ≤ 100` → `x1 + 2x2 + f1 = 100`

A função objetivo passa tudo para a esquerda:
`Z = 10x1 + 12x2` → `Z − 10x1 − 12x2 = 0` → **na linha Z entram −10 e −12**

### Passo 1: quadro inicial
| Base | x₁ | x₂ | … | f₁ | f₂ | f₃ | b |
|---|---|---|---|---|---|---|---|
| f₁ | coef. | coef. | … | 1 | 0 | 0 | total 1 |
| f₂ | coef. | coef. | … | 0 | 1 | 0 | total 2 |
| f₃ | coef. | coef. | … | 0 | 0 | 1 | total 3 |
| Z | −c₁ | −c₂ | … | 0 | 0 | 0 | 0 |

No início, **as folgas estão na base** e todos os x valem 0.

### Passo 2: quem ENTRA (coluna pivô)
O número **mais negativo da linha Z**. Em caso de empate, escolha qualquer um.

### Passo 3: quem SAI (linha pivô)
Para cada linha: **razão = b ÷ (número da coluna pivô)**
- Só calcule se o número da coluna pivô for **positivo** (> 0). Se for zero ou negativo, ignore a linha.
- A **menor razão** sai.
- **Pivô** = número no cruzamento da coluna pivô com a linha pivô.
- Se **nenhuma** razão for válida → **solução ilimitada**.

### Passo 4: pivotar
1. **Linha pivô nova = linha pivô ÷ pivô** (o pivô vira 1). Troque o nome na Base pela variável que entrou.
2. **Cada outra linha (incluindo Z):**
   **Linha nova = linha antiga − (k) × linha pivô nova**,
   onde **k** é o número que essa linha tinha na coluna pivô.
   → A coluna pivô fica com 1 no pivô e 0 no resto.

> Cuidado com o sinal: se k é negativo (ex.: −15 na linha Z), "− (−15) × linha" = **+15 × linha**.

### Passo 5: parar?
- **Ainda há negativo na linha Z?** → volte ao Passo 2.
- **Nenhum negativo?** → **ÓTIMO.**

### Passo 6: ler a resposta
- Variável **na base** = valor do **b** da sua linha
- Variável **fora da base** = **0**
- **Z** = canto inferior direito

---

## 4. Como ler um quadro Simplex (interpretação)

| Pergunta | Como responder |
|---|---|
| **É ótimo?** | **Sim**, se não houver nenhum negativo na linha Z (maximização). **Não**, se houver: "ainda há coeficientes negativos na linha Z (x₁ = −50, x₃ = −150), então Z ainda pode aumentar." |
| **Valor de Z?** | Canto inferior direito (coluna b, linha Z). |
| **Valor das variáveis?** | Na base: o b da linha. Fora da base: 0. |
| **Sobrou recurso?** | Olhe as folgas: **f na base com b > 0** → sobrou essa quantidade. **f fora da base** → f = 0 → recurso usado **por completo** (escasso/gargalo). |
| **Próxima a entrar?** | O mais negativo da linha Z. |
| **Próxima a sair?** | Menor razão b ÷ coluna (só positivos). |
| **Preço-sombra (valor de uma unidade a mais de recurso)?** | Número da coluna da folga **na linha Z** do quadro **ótimo**. Ex.: f₁ = 3 → mais 1 unidade do recurso 1 aumenta Z em 3. |
| **Soluções alternativas?** | No quadro ótimo, uma variável **fora da base com 0 na linha Z** → existem outras soluções com o mesmo Z. |
| **Solução ilimitada?** | A coluna que deve entrar não tem nenhum número positivo → não há razão válida. |

**Frase pronta para "não é ótimo":**
> "Não, pois ainda existem coeficientes negativos na linha Z (__ e __). Em um problema de maximização, isso indica que a função objetivo ainda pode ser melhorada. A próxima variável a entrar seria __ (a mais negativa)."

**Frase pronta para "é ótimo":**
> "Sim, pois todos os coeficientes da linha Z são maiores ou iguais a zero, então nenhuma variável pode entrar na base e aumentar Z."

---

## 5. Erros comuns ⚠️

- Esquecer de **trocar o sinal** da função objetivo na linha Z.
- Calcular razão com divisor **zero ou negativo** (não pode, ignore essa linha).
- Esquecer de atualizar a **linha Z** no pivoteamento.
- Escolher quem sai pelo **maior** b em vez da **menor razão**.
- Arredondar decimais no meio das contas. **Use frações** (1/3, 2/3…).
- Esquecer de trocar o nome da variável na coluna **Base**.
- **Minimização:** multiplique a função objetivo por −1 (Min Z = Max −Z), resolva normalmente e troque o sinal de Z no final.

---

## 6. Exemplos resolvidos (Avaliação II)

### Questão 2: Simplex direto

**Max Z = 10x₁ + 12x₂ + 8x₃ + 15x₄**
s.a. x₁ + 2x₂ + x₃ + x₄ ≤ 100 · 2x₁ + x₂ + 2x₃ + 2x₄ ≤ 120 · 3x₁ + x₂ + 4x₃ + x₄ ≤ 90

**Quadro inicial**

| Base | x₁ | x₂ | x₃ | x₄ | f₁ | f₂ | f₃ | b |
|---|---|---|---|---|---|---|---|---|
| f₁ | 1 | 2 | 1 | 1 | 1 | 0 | 0 | 100 |
| f₂ | 2 | 1 | 2 | 2 | 0 | 1 | 0 | 120 |
| f₃ | 3 | 1 | 4 | 1 | 0 | 0 | 1 | 90 |
| Z | −10 | −12 | −8 | **−15** | 0 | 0 | 0 | 0 |

**Iteração 1:** entra **x₄** (−15)
Razões: f₁ = 100/1 = 100 · f₂ = 120/2 = **60** · f₃ = 90/1 = 90 → **sai f₂**, pivô = 2

- x₄ (nova) = f₂ ÷ 2 → `1 | 1/2 | 1 | 1 | 0 | 1/2 | 0 | 60`
- f₁ = f₁ − 1 × x₄ → `0 | 3/2 | 0 | 0 | 1 | −1/2 | 0 | 40`
- f₃ = f₃ − 1 × x₄ → `2 | 1/2 | 3 | 0 | 0 | −1/2 | 1 | 30`
- Z = Z + 15 × x₄ → `5 | −9/2 | 7 | 0 | 0 | 15/2 | 0 | 900`

| Base | x₁ | x₂ | x₃ | x₄ | f₁ | f₂ | f₃ | b |
|---|---|---|---|---|---|---|---|---|
| f₁ | 0 | 3/2 | 0 | 0 | 1 | −1/2 | 0 | 40 |
| x₄ | 1 | 1/2 | 1 | 1 | 0 | 1/2 | 0 | 60 |
| f₃ | 2 | 1/2 | 3 | 0 | 0 | −1/2 | 1 | 30 |
| Z | 5 | **−9/2** | 7 | 0 | 0 | 15/2 | 0 | 900 |

**Iteração 2:** entra **x₂** (−9/2)
Razões: f₁ = 40 ÷ 3/2 = **80/3 ≈ 26,67** · x₄ = 60 ÷ 1/2 = 120 · f₃ = 30 ÷ 1/2 = 60 → **sai f₁**, pivô = 3/2

- x₂ (nova) = f₁ ÷ 3/2 → `0 | 1 | 0 | 0 | 2/3 | −1/3 | 0 | 80/3`
- x₄ = x₄ − 1/2 × x₂ → `1 | 0 | 1 | 1 | −1/3 | 2/3 | 0 | 140/3`
- f₃ = f₃ − 1/2 × x₂ → `2 | 0 | 3 | 0 | −1/3 | −1/3 | 1 | 50/3`
- Z = Z + 9/2 × x₂ → `5 | 0 | 7 | 0 | 3 | 6 | 0 | 1020`

| Base | x₁ | x₂ | x₃ | x₄ | f₁ | f₂ | f₃ | b |
|---|---|---|---|---|---|---|---|---|
| x₂ | 0 | 1 | 0 | 0 | 2/3 | −1/3 | 0 | 80/3 |
| x₄ | 1 | 0 | 1 | 1 | −1/3 | 2/3 | 0 | 140/3 |
| f₃ | 2 | 0 | 3 | 0 | −1/3 | −1/3 | 1 | 50/3 |
| Z | 5 | 0 | 7 | 0 | 3 | 6 | 0 | **1020** |

Sem negativos na linha Z → **ÓTIMO**

✅ **x₁ = 0 · x₂ = 80/3 ≈ 26,67 · x₃ = 0 · x₄ = 140/3 ≈ 46,67 · Z = 1020**
Folgas: f₁ = 0, f₂ = 0 (usados por completo) · f₃ = 50/3 ≈ 16,67 (sobra)

*Conferência:* 12·80/3 + 15·140/3 = 320 + 700 = 1020 ✓ · R1: 160/3 + 140/3 = 100 ✓ · R2: 80/3 + 280/3 = 120 ✓

---

### Questão 1: Cervejaria "Mestre Malte" (modelagem + Simplex)

**Variáveis:** x₁ = lotes de IPA, x₂ = Stout, x₃ = Pilsen, x₄ = Weiss

**Max Z = 600x₁ + 500x₂ + 350x₃ + 400x₄**
- Fermentação: 6x₁ + 5x₂ + 4x₃ + 4x₄ ≤ 300
- Lúpulo: 3x₁ + 2x₂ + x₃ + x₄ ≤ 120
- Mão de obra: 2x₁ + 2x₂ + x₃ + 3x₄ ≤ 160 *(o texto diz 150; a resposta é a mesma)*
- x₁, x₂, x₃, x₄ ≥ 0

**Quadro inicial**

| Base | x₁ | x₂ | x₃ | x₄ | f₁ | f₂ | f₃ | b |
|---|---|---|---|---|---|---|---|---|
| f₁ | 6 | 5 | 4 | 4 | 1 | 0 | 0 | 300 |
| f₂ | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 120 |
| f₃ | 2 | 2 | 1 | 3 | 0 | 0 | 1 | 160 |
| Z | **−600** | −500 | −350 | −400 | 0 | 0 | 0 | 0 |

**Iteração 1:** entra **x₁** (−600) · razões 300/6 = 50 · 120/3 = **40** · 160/2 = 80 → **sai f₂**, pivô 3

| Base | x₁ | x₂ | x₃ | x₄ | f₁ | f₂ | f₃ | b |
|---|---|---|---|---|---|---|---|---|
| f₁ | 0 | 1 | 2 | 2 | 1 | −2 | 0 | 60 |
| x₁ | 1 | 2/3 | 1/3 | 1/3 | 0 | 1/3 | 0 | 40 |
| f₃ | 0 | 2/3 | 1/3 | 7/3 | 0 | −2/3 | 1 | 80 |
| Z | 0 | −100 | −150 | **−200** | 0 | 200 | 0 | 24000 |

**Iteração 2:** entra **x₄** (−200) · razões f₁: 60/2 = **30** · x₁: 40 ÷ 1/3 = 120 · f₃: 80 ÷ 7/3 ≈ 34,3 → **sai f₁**, pivô 2

| Base | x₁ | x₂ | x₃ | x₄ | f₁ | f₂ | f₃ | b |
|---|---|---|---|---|---|---|---|---|
| x₄ | 0 | 1/2 | 1 | 1 | 1/2 | −1 | 0 | 30 |
| x₁ | 1 | 1/2 | 0 | 0 | −1/6 | 2/3 | 0 | 30 |
| f₃ | 0 | −1/2 | −2 | 0 | −7/6 | 5/3 | 1 | 10 |
| Z | 0 | 0 | 50 | 0 | 100 | 0 | 0 | **30000** |

✅ **30 lotes de IPA + 30 lotes de Weiss (0 Stout, 0 Pilsen). Lucro máximo = R$ 30.000/semana**
- Fermentação: 6·30 + 4·30 = 300 → usada toda
- Lúpulo: 3·30 + 1·30 = 120 → usado todo
- Mão de obra: 2·30 + 3·30 = 150 → sobram 10 h (de 160)

*Obs.:* x₂ (Stout) está fora da base com 0 na linha Z → existem **soluções ótimas alternativas** com o mesmo lucro.

---

### Questão 3: Leitura de quadro

| Base | x1 | x2 | x3 | f1 | f2 | f3 | b |
|---|---|---|---|---|---|---|---|
| f1 | 0 | 0 | 1 | 1 | 0 | −2 | 40 |
| f2 | −0,5 | 0 | 0,5 | 0 | 1 | −1,5 | 30 |
| x2 | 0,5 | 1 | 0,5 | 0 | 0 | 0,5 | 50 |
| Z | −50 | 0 | −150 | 0 | 0 | 250 | 25000 |

**a)** **Não é ótimo.** Ainda há coeficientes negativos na linha Z (x₁ = −50 e x₃ = −150), então Z ainda pode aumentar. A próxima a entrar seria **x₃** (−150). Razões: f₁ = 40/1 = **40**, f₂ = 30/0,5 = 60, x₂ = 50/0,5 = 100 → sairia **f₁**.

**b)** **Z = 25.000**

**c)** **x₁ = 0, x₂ = 50, x₃ = 0** (x₂ está na base com b = 50; x₁ e x₃ estão fora da base)

**d)** **Sim.** f₁ = 40 (sobraram 40 do recurso 1) e f₂ = 30 (sobraram 30 do recurso 2). **f₃ = 0**: o recurso 3 foi usado por completo (f₃ está fora da base).

---

## 7. Script `simplex.py`

Resolve **qualquer** problema de maximização com restrições ≤ e **imprime todas as contas**: quem entra, as razões, quem sai, o pivô, a operação feita em cada linha e todos os quadros, em **fração e decimal**.

**Como rodar (se for permitido):**
- No computador: `python simplex.py`
- No GitHub: botão verde **Code → Codespaces → Create codespace** → no terminal: `python simplex.py`
- Ou copie o código num Python online e rode.

**Como trocar o problema:** edite no final do arquivo:

```python
c = [10, 12, 8, 15]          # lucros da função objetivo
A = [[1, 2, 1, 1],           # coeficientes de cada restrição (uma lista por linha)
     [2, 1, 2, 2],
     [3, 1, 4, 1]]
b = [100, 120, 90]           # lado direito (totais disponíveis)
simplex(c, A, b)
```

- Minimização: `simplex(c, A, b, minimizar=True)`
- Nomes próprios: `simplex(c, A, b, nomes=["IPA", "Stout", "Pilsen", "Weiss"])`
- **Ler um quadro pronto** (tipo Questão 3): use `analisar_quadro(...)` (há um exemplo comentado no fim do arquivo).

---

## 8. Simplex no Excel

### A) Planilha automática: [`Modelo_Simplex_Automatico.xlsx`](Modelo_Simplex_Automatico.xlsx)

1. Clique no arquivo aqui no GitHub e depois no botão **Download raw file** (ícone ⬇ à direita).
2. Abra no Excel. Se aparecer "Habilitar edição", clique.
3. Preencha **só as células amarelas**:
   - **D2:** `MAX` ou `MIN`
   - **Linha "Lucro/custo (c)":** coeficientes da função objetivo (sinal normal, **sem** trocar)
   - **Restrições 1 a 4:** coeficientes e o **b** (coluna K)
   - Variável ou restrição que não existir no problema: **deixe 0**
4. Leia a **RESPOSTA FINAL** no topo (x, folgas f e Z).
5. Logo abaixo ficam **todos os quadros** (Quadro 0, 1, 2…). Embaixo de cada um, uma linha mostra **Status**, **Entra** (coluna), **Sai** (linha) e **Pivô**, para você copiar o passo a passo na prova.

> Ela vem preenchida com a Questão 2 (Z = 1020). Para a cervejaria, troque os dados e o resultado tem que dar Z = 30000.
> Aceita até 5 variáveis e 4 restrições "≤". Se aparecer "continua" no último quadro, o problema precisa de mais de 5 iterações.

### B) Fazendo à mão com fórmulas (do jeito das listas): o truque do `$`

Use o mesmo layout das listas: quadro inicial nas linhas 1 a 5 e o próximo quadro logo abaixo.
Exemplo (cervejaria, iteração 1): **entra x1 (coluna B)**, **sai f2 (linha 3)**, pivô = **B3 = 3**, e o quadro novo começa na linha 8.

| O quê | Fórmula (na coluna B) | Depois |
|---|---|---|
| **Razão** | `=I2/B2` (b ÷ coluna que entra) | arraste **para baixo** |
| **Linha pivô nova** (linha 10) | `=B3/$B$3` | arraste **para a direita** até o b |
| **Outra linha** (ex.: linha 9, vinda da 2) | `=B2-$B2*B$10` | arraste **para a direita** até o b |
| **Linha Z** (linha 12, vinda da 5) | `=B5-$B5*B$10` | arraste **para a direita** até o b |

Como ler `=B2-$B2*B$10`: **linha antiga − (número dela na coluna pivô) × linha pivô nova**.
- `$B2`: o `$` antes do B **trava a coluna pivô**.
- `B$10`: o `$` antes do 10 **trava a linha pivô nova**.
- A mesma fórmula serve para a linha Z (não precisa se preocupar com o sinal: −(−600) vira +600 sozinho).

**No próximo quadro**, troque B pela nova coluna pivô e 10 pela nova linha pivô.
Exemplo (cervejaria, iteração 2): entra x4 (coluna E), a linha pivô nova é a 16 (`=B9/$E$9`), e a linha do x1 (linha 17, vinda da 10) fica `=B10-$E10*B$16`.
