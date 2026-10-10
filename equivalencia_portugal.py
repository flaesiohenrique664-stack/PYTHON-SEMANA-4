"""
ALGORITMO "SISTEMA_DE_PRODUTOS"

VAR
    N, I, J, CONT_CATEGORIAS: INTEIRO
    NOMES: VETOR[1..100] DE CARACTERE
    CATEGORIAS: VETOR[1..100] DE CARACTERE
    PRECOS: VETOR[1..100] DE REAL
    CATEGORIAS_UNICAS: VETOR[1..100] DE CARACTERE
    AUX_NOME, AUX_CATEGORIA: CARACTERE
    AUX_PRECO, VALOR_FILTRO, MENOR, MAIOR, SOMA, MEDIA: REAL
    TROCOU: LOGICO

INICIO
    ESCREVA("Quantidade de produtos (1 a 100): ")
    LEIA(N)

    ENQUANTO N < 1 OU N > 100 FACA
        ESCREVA("Digite uma quantidade entre 1 e 100: ")
        LEIA(N)
    FIMENQUANTO

    # CADASTRO: vetor de tamanho fixo preenchido por um laço PARA.
    PARA I DE 1 ATE N FACA
        ESCREVA("Nome do produto ", I, ": ")
        LEIA(NOMES[I])
        ESCREVA("Preço do produto ", I, ": ")
        LEIA(PRECOS[I])
        ESCREVA("Categoria do produto ", I, ": ")
        LEIA(CATEGORIAS[I])
    FIMPARA

    # FILTRAGEM: comparar cada preço com o valor informado.
    ESCREVA("Digite o valor para filtrar: ")
    LEIA(VALOR_FILTRO)

    ESCREVA("Produtos acima do valor:")
    PARA I DE 1 ATE N FACA
        SE PRECOS[I] > VALOR_FILTRO ENTAO
            ESCREVA(NOMES[I], " - ", PRECOS[I], " - ", CATEGORIAS[I])
        FIMSE
    FIMPARA

    ESCREVA("Produtos abaixo do valor:")
    PARA I DE 1 ATE N FACA
        SE PRECOS[I] < VALOR_FILTRO ENTAO
            ESCREVA(NOMES[I], " - ", PRECOS[I], " - ", CATEGORIAS[I])
        FIMSE
    FIMPARA

    # ORDENAÇÃO CRESCENTE: bubble sort, trocando nome, preço e categoria
    # juntos para que os dados do mesmo produto continuem associados.
    PARA I DE 1 ATE N - 1 FACA
        PARA J DE 1 ATE N - I FACA
            SE PRECOS[J] > PRECOS[J + 1] ENTAO
                AUX_PRECO <- PRECOS[J]
                PRECOS[J] <- PRECOS[J + 1]
                PRECOS[J + 1] <- AUX_PRECO

                AUX_NOME <- NOMES[J]
                NOMES[J] <- NOMES[J + 1]
                NOMES[J + 1] <- AUX_NOME

                AUX_CATEGORIA <- CATEGORIAS[J]
                CATEGORIAS[J] <- CATEGORIAS[J + 1]
                CATEGORIAS[J + 1] <- AUX_CATEGORIA
            FIMSE
        FIMPARA
    FIMPARA

    ESCREVA("Produtos ordenados por preço crescente:")
    PARA I DE 1 ATE N FACA
        ESCREVA(NOMES[I], " - ", PRECOS[I], " - ", CATEGORIAS[I])
    FIMPARA

    # ORDEM DECRESCENTE: repetir bubble sort, invertendo a comparação.
    PARA I DE 1 ATE N - 1 FACA
        PARA J DE 1 ATE N - I FACA
            SE PRECOS[J] < PRECOS[J + 1] ENTAO
                # Trocar PRECOS[J] com PRECOS[J+1].
                # Fazer a mesma troca para NOMES e CATEGORIAS.
                AUX_PRECO <- PRECOS[J]
                PRECOS[J] <- PRECOS[J + 1]
                PRECOS[J + 1] <- AUX_PRECO

                AUX_NOME <- NOMES[J]
                NOMES[J] <- NOMES[J + 1]
                NOMES[J + 1] <- AUX_NOME

                AUX_CATEGORIA <- CATEGORIAS[J]
                CATEGORIAS[J] <- CATEGORIAS[J + 1]
                CATEGORIAS[J + 1] <- AUX_CATEGORIA
            FIMSE
        FIMPARA
    FIMPARA

    ESCREVA("Produtos ordenados por preço decrescente:")
    PARA I DE 1 ATE N FACA
        ESCREVA(NOMES[I], " - ", PRECOS[I], " - ", CATEGORIAS[I])
    FIMPARA

    # CATEGORIAS ÚNICAS: simulação manual de um conjunto.
    # Cada nova categoria é comparada com as categorias já guardadas.
    CONT_CATEGORIAS <- 0
    PARA I DE 1 ATE N FACA
        J <- 1
        ENQUANTO J <= CONT_CATEGORIAS E
                 CATEGORIAS_UNICAS[J] <> CATEGORIAS[I] FACA
            J <- J + 1
        FIMENQUANTO

        SE J > CONT_CATEGORIAS ENTAO
            CONT_CATEGORIAS <- CONT_CATEGORIAS + 1
            CATEGORIAS_UNICAS[CONT_CATEGORIAS] <- CATEGORIAS[I]
        FIMSE
    FIMPARA

    ESCREVA("Categorias sem repetição:")
    PARA I DE 1 ATE CONT_CATEGORIAS FACA
        ESCREVA(CATEGORIAS_UNICAS[I])
    FIMPARA

    # ESTATÍSTICAS: menor, maior e média em uma estrutura equivalente
    # a uma tupla. No pseudocódigo, os três valores são guardados juntos.
    MENOR <- PRECOS[1]
    MAIOR <- PRECOS[1]
    SOMA <- 0

    PARA I DE 1 ATE N FACA
        SE PRECOS[I] < MENOR ENTAO
            MENOR <- PRECOS[I]
        FIMSE
        SE PRECOS[I] > MAIOR ENTAO
            MAIOR <- PRECOS[I]
        FIMSE
        SOMA <- SOMA + PRECOS[I]
    FIMPARA

    MEDIA <- SOMA / N

    # Equivalente conceitual da tupla: (MENOR, MAIOR, MEDIA).
    ESCREVA("Menor preço: ", MENOR)
    ESCREVA("Maior preço: ", MAIOR)
    ESCREVA("Média dos preços: ", MEDIA)

    # RELATÓRIO FINAL: exibir todos os resultados de forma organizada.
    ESCREVA("Total de produtos: ", N)
    ESCREVA("Total de categorias únicas: ", CONT_CATEGORIAS)
FIMALGORITMO
"""
