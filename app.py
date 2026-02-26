import streamlit as st

st.title("Avaliação de Dons Espirituais")

st.markdown("### Esta afirmação tem sido a experiência da minha vida?")

st.markdown("""
0 - Nunca  
1 - Raramente  
2 - Às vezes  
3 - Frequentemente  
4 - Muito  
5 - Eu brilho nisso!
""")

perguntas = [
"1 - Tenho experimentado um desejo especial de transmitir mensagens vindas diretamente de Deus.",
"2 - Consigo comunicar uma visão do que é possível para alguém, encorajando-o a continuar na luta, apesar da derrota.",
"3 - Outros irmãos ficam animados e motivados a me seguir por meio da visão que compartilho com eles dos propósitos de Deus.",
"4 - Gosto de ajudar as pessoas fazendo pequenos serviços.",
"5 - Tenho tanta certeza de que Deus suprirá minhas necessidades que estou constantemente doando meu dinheiro de forma sacrificial.",
"6 - Tenho alegria em trabalhar com pessoas ignoradas ou desconhecidas da maioria.",
"7 - Aplico-me ao estudo da Palavra de Deus, dando atenção especial à pesquisa.",
"8 - Tenho facilidade para organizar ideias, pessoas, coisas e o tempo, visando um serviço mais efetivo e produtivo na obra do Senhor.",
"9 - Minha casa está sempre à disposição para quem precisar de uma cama ou um teto.",
"10 -Tenho ajudado os líderes da minha igreja para que eles tenham mais tempo para as coisas realmente importantes relacionadas ao chamado deles.",
"11 - Oro pelo menos uma hora por dia.",
"12 - Pessoas me dizem que transmito mensagens tão urgentes e apropriadas que só podem ter vindo diretamente de Deus.",
"13 - Deus me dá as palavras que pessoas indecisas, problemáticas e desencorajadas precisam ouvir.",
"14 - Fico à vontade quando me coloco à frente de um grupo para dar direção.",
"15 - Sinto-me muito à vontade realizando tarefas auxiliares (arrumar cadeiras, transportar objetos, manter a ordem, cozinhar, construir, reformar, secretariar reuniões, controlar o som, remeter cartas etc.).",
"16 - Tenho habilidade de administrar bem meu dinheiro para poder contribuir mais liberalmente para o serviço do Senhor.",
"17 - Gosto de visitar hospitais ou lares de pessoas necessitadas e sinto-me abençoado com isso.",
"18 - Sinto prazer em explicar a verdade de um texto bíblico.",
"19 - Tenho facilidade em fazer planos de ação para que, junto com outras pessoas, possamos atingir um objetivo específico.",
"20 - Gosto de ser responsável por atividades sociais da igreja.",
"21 - Pessoas me dizem que, por meio do meu auxílio, tornaram-se mais eficazes em suas tarefas ou ministérios.",
"22 - Quando recebo um pedido de oração, oro por isso durante alguns dias, pelo menos.",
"23 - Às vezes tenho a forte sensação de que sei exatamente o que Deus deseja dizer a alguém.",
"24 - Tenho facilidade em entender os problemas dos outros e apontar possíveis soluções.",
"25 - Gosto de começar novos trabalhos na igreja, mas prefiro que outra pessoa dê continuidade depois de um tempo.",
"26 - Já me disseram que pareço gostar de fazer trabalhos simples de rotina, e que os faço muito bem.",
"27 - Estou disposto a baixar meu padrão de vida para poder contribuir mais com o trabalho do Senhor.",
"28 - Falo carinhosamente e gosto de auxiliar pessoas necessitadas ou impossibilitadas de se ajudar.",
"29 - Tenho grande interesse em ver as verdades da Palavra de Deus apresentadas de forma clara, com explicação do significado das palavras.",
"30 - Gosto de trabalhar sob a coordenação de um líder para ajudar a realizar sua visão.",
"31 - Quando recebo visitas em minha casa, elas se sentem muito à vontade.",
"32 - Gosto de acompanhar um líder, poupando-lhe tempo ao servi-lo.",
"33 - Uma das minhas maneiras favoritas de passar o tempo é orando por outras pessoas.",
"34 - Tenho a sensação de que sei exatamente o que Deus quer que eu, ou outra pessoa, faça em uma situação específica.",
"35 - Aceito, sem muita dificuldade, os erros das pessoas, crendo que uma conversa pessoal é o melhor caminho.",
"36 - Tenho facilidade de interpretar os objetivos do meu grupo e pensar em estratégias para colocá-los em prática.",
"37 - Prefiro estar em atividade fazendo algo ao invés de apenas ouvir alguém falar.",
"38 - Meus registros mostram que tenho contribuído com mais de 10% da minha renda para o trabalho de Deus.",
"39 - Sinto-me realizado quando posso ajudar uma pessoa doente ou necessitada.",
"40 - Tenho facilidade em explicar a Bíblia.",
"41 - Tenho capacidade de elaborar planos eficientes para alcançar os objetivos do grupo.",
"42 - As pessoas frequentemente dizem que sou uma pessoa muito hospitaleira.",
"43 - Sinto-me contente servindo alguém pessoalmente, mesmo quando minha ajuda não é reconhecida.",
"44 - Alguém já me disse que uma oração minha trouxe respostas concretas em sua vida.",
"45 - Tenho facilidade em ouvir a voz de Deus.",
"46 - Quando alguém está em pecado, minha maior preocupação é ajudá-lo, e não criticá-lo.",
"47 - Quando lidero um grupo, ele cresce e apresenta resultados visíveis.",
"48 - Aceito com alegria tarefas simples, mesmo aquelas que qualquer pessoa poderia fazer.",
"49 - Quando surge uma necessidade financeira na igreja ou na vida de alguém, logo penso em contribuir com o que tenho.",
"50 - Quando vejo alguém doente ou com problemas, sinto grande compaixão.",
"51 - Alegro-me em descobrir verdades bíblicas para compartilhá-las com outros.",
"52 - Tenho experimentado alegria sendo responsável pelo sucesso de trabalhos especiais em minha igreja.",
"53 - Desejo que minha casa esteja sempre disponível para os servos de Deus.",
"54 - Tenho prazer em servir como auxiliar, realizando tarefas que atendam às necessidades de quem desejo ajudar.",
"55 - Persisto em oração até sentir que Deus respondeu."
]

respostas = {}

for i in range(len(perguntas)):
    pergunta_texto = f"{i+1}. {perguntas[i]}"
    respostas[i+1] = st.slider(pergunta_texto, 0, 5, 0)

mapa_resultados = {
    "Profecia (Pregação)": [1, 12, 23, 34, 45],
    "Exortação (Encorajamento)": [2, 13, 24, 35, 46],
    "Presidir (Liderança)": [3, 14, 25, 36, 47],
    "Serviço": [4, 15, 26, 37, 48],
    "Contribuição": [5, 16, 27, 38, 49],
    "Misericórdia": [6, 17, 28, 39, 50],
    "Ensino": [7, 18, 29, 40, 51],
    "Administração": [8, 19, 30, 41, 52],
    "Hospitalidade": [9, 20, 31, 42, 53],
    "Socorro / Ajuda": [10, 21, 32, 43, 54],
    "Intercessão": [11, 22, 33, 44, 55]
}

if st.button("Calcular Resultados"):
    st.subheader("Resultados")

    resultados = {}

    for nome, lista in mapa_resultados.items():
        soma = sum(respostas[num] for num in lista)
        resultados[nome] = soma

    resultados_ordenados = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

    for nome, valor in resultados_ordenados.items():

        if 0 <= valor <= 5:
            interpretacao = "Indica que você não tem esse dom; pode também indicar uma área que precisa de maior desenvolvimento espiritual."
        elif 6 <= valor <= 10:
            interpretacao = "Provavelmente você não tem esse dom, ou ele ainda não foi muito desenvolvido."
        elif 11 <= valor <= 15:
            interpretacao = "Há boa possibilidade de você ter esse dom."
        elif 16 <= valor <= 20:
            interpretacao = "É quase certo que você possui esse dom."
        else:
            interpretacao = "Indica um chamado muito especial nessa área."

        st.write(f"### {nome}: {valor} pontos")
        st.write(interpretacao)
        st.write("---")
