# House Rocket Project (Insights project)

<img src="https://github.com/FelipeCaetanoDS/useful_files/blob/5db87200884245173b720260c437c00f25b4397b/house%20rocket.png" alt="logo" style="zoom:100%;" />

Este é um projeto fictício. A empresa, o contexto e as perguntas de negócios não são reais. Este portfólio está seguindo as recomendações da Comunidade Data Science. 

​						                                  																																		*A logo criada é ficticia.* 

 
**:trophy: ​A [Aplicação](https://house-rocket-project.herokuapp.com/) desse projeto foi selecionado pela comunidade Streamlit como uma das 4 melhores aplicações na categoria finanças e negócios na [Weekly Roundup](https://discuss.streamlit.io/t/weekly-roundup-custom-theming-march-madness-recap-videos-and-more/11167) ! :trophy:**



# 1. Descrição 

*House Rocket* é uma empresa que trabalha com a compra e venda de imóveis. O Cientista de dados da empresa deverá ajudar a encontrar as melhores oportunidades de negócio, ou seja, maximizar a receita. A melhor estratégia para o negócio consiste em "comprar barato e vender caro". Os atributos das casas as tornam mais ou menos atraentes para o negócio, influenciando o seu preço, tanto na compra quanto na venda. As questões a serem respondidas são:

**1**. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?

**2.** Uma vez que as casas foram compradas, qual o melhor momento para vendê-las e qual seria o preço da venda?

 


# 2. Atributos 

Os dados para este projeto podem ser encontrados em: https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885 . Abaixo segue a definição para cada um dos 21 atributos:


|    Atributos    |                         Significado                          |
| :-------------: | :----------------------------------------------------------: |
|       id        |       Numeração única de identificação de cada imóvel        |
|      date       |                    Data da venda da casa                     |
|      price      |    Preço que a casa está sendo vendida pelo proprietário     |
|    bedrooms     |                      Número de quartos                       |
|    bathrooms    | Número de banheiros (0.5 = banheiro em um quarto, mas sem chuveiro) |
|   sqft_living   | Medida (em pés quadrado) do espaço interior dos apartamentos |
|    sqft_lot     |     Medida (em pés quadrado)quadrada do espaço terrestre     |
|     floors      |                 Número de andares do imóvel                  |
|   waterfront    | Variável que indica a presença ou não de vista para água (0 = não e 1 = sim) |
|      view       | Um índice de 0 a 4 que indica a qualidade da vista da propriedade. Varia de 0 a 4, onde: 0 = baixa  4 = alta |
|    condition    | Um índice de 1 a 5 que indica a condição da casa. Varia de 1 a 5, onde: 1 = baixo \|-\| 5 = alta |
|      grade      | Um índice de 1 a 13 que indica a construção e o design do edifício. Varia de 1 a 13, onde: 1-3 = baixo, 7 = médio e 11-13 = alta |
|  sqft_basement  | A metragem quadrada do espaço habitacional interior acima do nível do solo |
|    yr_built     |               Ano de construção de cada imóvel               |
|  yr_renovated   |                Ano de reforma de cada imóvel                 |
|     zipcode     |                         CEP da casa                          |
|       lat       |                           Latitude                           |
|      long       |                          Longitude                           |
| sqft_livining15 | Medida (em pés quadrado) do espaço interno de habitação para os 15 vizinhos mais próximo |
|   sqft_lot15    | Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo |



# 3. Premissas do Negócio

Quais premissas foram adotadas para este projeto:

- As seguintes premissas foram consideradas para esse projeto:
- Os valores iguais a zero em **yr_renovated** são casas que nunca foram reformadas.
- A coluna **price** significa o preço que a casa será comprada pela empresa House Rocket
- A localidade e a condição do imóvel foram características decisivas na compra ou não do imóvel
- A estação do ano e o tipo do imóvel foram as características decisivas para definir a compra, a venda e o preço de venda de cada imóvel.



# 4. Estratégia de solução

Quais foram as etapas para solucionar o problema de negócio:

1. Coleta de dados via Kaggle
2. Entendimento de negócio
3. Tratamento de dados 

- ​	Tranformação de variaveis 
- ​	Limpeza 
-   Criação de novas variáveis
- ​	Entendimento

4. Exploração de dados

- Elaboração e validação de hipóteses.
- Desenvolvimento de app interativo para análise personalizada.
[link para app no Streamlit](https://felipe-houserocketproject.streamlit.app/)

5. Responder as questões principais do negócio

6. Apurar o resultado financeiro para o negócio

7. Conclusão

# 5. Top Insights

Insights mais relevantes para o projeto:

Imóveis com terrenos maiores tem valor superior, independente do estado de conservação da construção.

**Falso**: Imóveis que ocupam terrenos menores e aqueles em condição regular de conservação tem os maiores preços.

Imóveis com vista para o mar são 20% mais caros do que aqueles que não tem essa vista.

**Falso**: O incremento de preço relacionado à vista para o mar é superior a 20%.

Imóveis com construções antigas são mais baratas do que imóveis construidos recentemente.  

**Falso**: A idade da construção das propriedades é uma variável que, isoladamente, não parece influenciar seu preço.



# 6. Tradução para o negócio

O as análises das hipóteses dizem sobre o negócio

| Hipótese                                                     | Resultado  | Tradução para negócio                                        |
| ------------------------------------------------------------ | ---------- | ------------------------------------------------------------ |
| **H1** -Imóveis com melhor vista tem preço maior | Verdadeira | Investir em que a qualidade da vista é melhor                      |
| **H2** - Imóveis em melhores condições tem uma diferença de preço 10% superior àqueles em condição imediatamente inferior | Falsa      | Investir em imóveis com estado de conservação regular       |
| **H3** - Quanto maior o terreno do imóvel, maior o preço, independente da condiçao de conservação do imóvel | Falsa | Investir em imóveis com terrenos menores                                |
| **H4** - Imóveis com vista para a água são 20% mais caros do que imóveis que não tem vista para a água | Falsa | Investir com vista para a água pois a diferença de preço é maior do que 20%  |
| **H5** - A adição de um banheiro extra encarece o imóvel em 5% por banheiro adicional | Falsa      | Investir em imóveis com mais banheiros pois o incremento de preço a cada banheiro adicional é superior a 5%                     |
| **H6** - No inverno o preço dos imóveis é mais barato do que no verão | Falsa      | Comprar imóveis no inverno                         |
| **H7** - Imóveis mais velhos são mais baratos do que imóveis mais novos   | Falsa      | Investir em imóveis independentemente da idade da sua construção                  |
| **H8** - Imóveis com reforma inferior a 10 anos são, em média, 15% mais caros do que imóveis não reformados ou com mais tempo desde a reforma | Falsa      | Investir em imóveis independentemente da existência de reforma                 |
| **H9** - A estação do ano tem impacto direto sobre o preço dos imóveis | Verdadeira      | Investir em imóveis do tipo 'house' e 'apartment' no inverno, e imóveis do tipo 'studio' no outono para vendê-los na primavera                  |

O desembolso total para compra dos imóveis selecionados foi de US$45.977.490,00

A receita total após a venda dos imóveis foi de US$49.066.810,13

O lucro após a venda de todos os imóveis comprados foi de **US$3.089.320,13**



# 7. Conclusão

O objetivo final desse projeto era responder a duas questões principais:

**1**. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?

**2** Uma vez que as casas foram compradas, qual o melhor momento para vendê-las e qual seria o preço da venda?

Os objetivos foram alcançados conforme o seguinte plano de negócios:

A) Para que fossem comprados, os imóveis deveriam atender aos seguintes critérios:

- A qualidade da vista deveria ser superior a 2;
- O estado de conservação deveria ser regular;
- O preço de compra deveria ser menor que a mediana dos preços da região em que o imóvel se encontra; e
- Imóveis do tipo 'house' e 'aparment' deveriam ser comprados no inverno, enquanto imóveis do tipo 'studio' deveriam ser comprados no outono.

**61 imóveis atenderam a esses critérios**

B) Para determinar o melhor momento e definir o preço pelo qual os imóveis seriam vendidos:

- Diferente da época de compra, para todos os tipos de imóveis, o melhor momento para venda, é aquele compreendido pela primavera, época em que os preços estão mais altos.
- O preço de venda dos imóveis foi determinado pela variação do preço médio entre as estações de compra dos imóveis e a estação em que os imóveis serão vendidos, variando de acordo com o tipo de imóvel:
**Tipo 'Apartment'** - Acréscimo de 3,7% sobre o preço de compra;
**Tipo 'House'** - Acréscimo de 8,2% sobre o preço de compra;
**Tipo 'Studio'** - Acréscimo de 11,1% sobre o preço de compra;

Essa estratégia trouxe um lucro equivalente a **6,72%** do capital investido em um intervalo máximo de 6 meses, considerando a compra no início do inverno e a venda no final da primavera. Em termos de comparação, a taxa de juros americana no ano de 2015 (época dos dados) era de 1,75% **ao ano**, ou seja, em seis meses foi possível auferir uma rentabilidade 3,8 vezes maior do que os títulos americanos oferecem em um ano. 

Como próximo passo, seria interessante  aprofundar a análise e diminuir o intervalo de compra e venda de trimestral (dada a duração das estações) para mensal, além de identificar quais imóveis deveriam passar por reformas visto que a variação de preço entre imóveis em más condições de conservação e imóvel em condição regular é superior a 30% e se o custo para revitalizar esses imóveis for inferior a esse percentual, torna-se uma nova estratégia para aumento da rentabilidade do negócio. 
