#Args e Kwargs (*args - passa como tupla / **kwargs - passa como dicionário)

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Terça-Feira, 26 de setembro de 2023",
"Bonito é melhor que feio",
"Explícito é melhor que implícito",
"Simples é melhor que complexo",
"Complexo é melhor que complicado",
"Plano é melhor que aninhado",
"Esparso é melhor que denso",
"Legibilidade conta",
"Casos especiais não são especiais o bastante para quebrar as regras",
"Ainda que praticidade vença a pureza",
"Erros nunca devem passar silenciosamente",
"A menos que sejam explicitamente silenciados",
"Diante da ambiguidade, recuse a tentação de adivinhar",
"Deveria haver um — e preferencialmente só um — modo óbvio para fazer algo",
"Embora esse modo possa não ser óbvio a princípio, a menos que você seja holandês",
"Agora é melhor que nunca",
"Embora nunca normalmente seja melhor do que *já*",
"Se a implementação é difícil de explicar, é uma má ideia",
"Se a implementação é fácil de explicar, pode ser uma boa ideia",
"Namespaces são uma grande ideia — vamos fazer mais dessas!", autor = "Tim Peters", ano = 1999)