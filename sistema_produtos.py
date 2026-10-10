
def cadastrar_produtos():
    produtos = []

    print("=== Cadastro de produtos ===")
    quantidade = int(input("Quantos produtos deseja cadastrar? "))

    while quantidade <= 0:
        print("Digite uma quantidade maior que zero.")
        quantidade = int(input("Quantos produtos deseja cadastrar? "))

    for indice in range(quantidade):
        print(f"\nProduto {indice + 1}")
        nome = input("Nome: ").strip()

        while not nome:
            print("O nome não pode ficar vazio.")
            nome = input("Nome: ").strip()

        while True:
            try:
                preco = float(input("Preço (use ponto ou vírgula): ").replace(",", "."))
                if preco < 0:
                    print("O preço não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("Preço inválido. Exemplo: 12.50")

        categoria = input("Categoria: ").strip()
        while not categoria:
            print("A categoria não pode ficar vazia.")
            categoria = input("Categoria: ").strip()

        # Cada produto é guardado como um dicionário dentro da lista.
        produtos.append({
            "nome": nome,
            "preco": preco,
            "categoria": categoria
        })

    return produtos


def mostrar_produtos(titulo, produtos):
    print(f"\n=== {titulo} ===")
    if not produtos:
        print("Nenhum produto encontrado.")
        return

    for produto in produtos:
        print(
            f"Produto: {produto['nome']} | "
            f"Preço: € {produto['preco']:.2f} | "
            f"Categoria: {produto['categoria']}"
        )


def main():
    produtos = cadastrar_produtos()
    precos = [produto["preco"] for produto in produtos]

    # Filtragem por preço: mostra produtos acima e abaixo do valor informado.
    valor_filtro = float(
        input("\nDigite um valor para filtrar os preços (use ponto ou vírgula): ")
        .replace(",", ".")
    )
    acima = [produto for produto in produtos if produto["preco"] > valor_filtro]
    abaixo = [produto for produto in produtos if produto["preco"] < valor_filtro]

    mostrar_produtos(f"Produtos acima de € {valor_filtro:.2f}", acima)
    mostrar_produtos(f"Produtos abaixo de € {valor_filtro:.2f}", abaixo)

    # sort() modifica a lista original de produtos.
    produtos_crescente = produtos.copy()
    produtos_crescente.sort(key=lambda produto: produto["preco"])
    mostrar_produtos("Produtos por preço crescente (sort)", produtos_crescente)

    # sorted() cria uma nova lista, sem modificar a original.
    produtos_decrescente = sorted(
        produtos, key=lambda produto: produto["preco"], reverse=True
    )
    mostrar_produtos("Produtos por preço decrescente (sorted)", produtos_decrescente)

    # O set elimina categorias repetidas automaticamente.
    categorias_unicas = set(produto["categoria"] for produto in produtos)
    print("\n=== Categorias únicas ===")
    for categoria in sorted(categorias_unicas):
        print(f"- {categoria}")

    # A tupla guarda estatísticas em uma estrutura imutável.
    estatisticas = (min(precos), max(precos), sum(precos) / len(precos))
    menor_preco, maior_preco, media_precos = estatisticas

    print("\n=== Relatório final ===")
    print(f"Quantidade de produtos: {len(produtos)}")
    print(f"Menor preço: € {menor_preco:.2f}")
    print(f"Maior preço: € {maior_preco:.2f}")
    print(f"Média dos preços: € {media_precos:.2f}")
    print(f"Categorias encontradas: {len(categorias_unicas)}")
    print(f"Tupla de estatísticas: {estatisticas}")


if __name__ == "__main__":
    main()
