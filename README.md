# Notas de Inferência Estatística Bayesiana

Livro Digital e material de estudo completo, rigoroso e aprofundado sobre **Inferência Estatística Bayesiana**, estruturado de acordo com o conteúdo programático oficial da disciplina.

**Autor:** Luca Ferreira Barboza

---

## 🌐 Acesso Online (Deploy no GitHub Pages)

O material está publicado e pode ser lido interativamente em qualquer dispositivo através do link:
👉 **[https://lucabarboza.github.io/notas-inferencia-estatistica/](https://lucabarboza.github.io/notas-inferencia-estatistica/)**

---

## 📥 Versão em PDF para Leitura Offline

O repositório inclui a versão completa diagramada para impressão e leitura em PDF:
📄 **[Notas_de_Inferencia_Estatistica.pdf](Notas_de_Inferencia_Estatistica.pdf)** (2.18 MB)

* Todas as demonstrações matemáticas abertas por padrão;
* Códigos em R e Python apresentados em sequência;
* Diagramação em páginas A4 com equações vetoriais de alta resolução renderizadas pelo MathJax.

---

## 📚 Estrutura dos 6 Módulos

1. **Fundamentos e Modelos de Probabilidade:**
   * Duelo de Paradigmas: Bayesiano vs. Frequentista (probabilidade como crença racional vs. frequência assintótica, interpretação de parâmetros e rejeição de contrafactuais).
   * Princípio da Verossimilhança, Teorema da Fatoração de Fisher-Neyman e o *Stopping Rule Principle*.
   * Fichas Técnicas dos Modelos Discretos: Bernoulli, Binomial, Poisson, Geométrica, Binomial Negativa (Pascal), Hipergeométrica e Multinomial.
   * Fichas Técnicas dos Modelos Contínuos: Uniforme, Exponencial, Gama, Qui-Quadrado, Beta, Normal Univariada/Multivariada, $t$ de Student e Dirichlet.

2. **Distribuições a Priori, a Posteriori e Preditivas:**
   * Formulação contínua e discreta do Teorema de Bayes e constante normalizadora (evidência marginal $p(x)$).
   * Prova analítica da atualização sequencial do conhecimento.
   * Distribuição Preditiva a Priori $p(x)$ e Preditiva a Posteriori $p(y \mid x)$ sob independência condicional.
   * Priori Não Informativa de Jeffreys: Informação de Fisher, regra formal e **demonstração analítica da invariância sob transformações monótonas 1-a-1 via Jacobiano**.
   * Prioris Hierárquicas (efeito *shrinkage*) e Misturas de Prioris.

3. **Famílias Conjugadas e a Família Exponencial:**
   * Conceito de fechamento por amostragem e estrutura canônica na Família Exponencial regular.
   * Deduções analíticas completas dos pares canônicos: Beta-Binomial (com preditiva Beta-Binomial), Gama-Poisson (com preditiva Binomial Negativa), Normal com variância conhecida (adição de precisões), Normal com média conhecida, Normal conjunta Normal-Gama e Dirichlet-Multinomial.
   * **Resolução Exata do Problema de Behrens-Fisher** para duas amostras com variâncias desiguais.

4. **Teoria da Decisão, Estimação e Testes de Hipóteses:**
   * Fundamentos da Teoria da Decisão: espaço de ações, funções de perda e risco a posteriori.
   * **Deduções formais dos três estimadores pontuais ótimos:** Média (perda quadrática), Mediana (perda absoluta via regra de Leibniz) e Moda/MAP (perda 0-1).
   * Intervalos de Credibilidade e **Demonstração do Teorema do Volume Mínimo da Região HPD**.
   * Testes de Hipóteses Bayesianos: Razões de chances (Odds), **Fator de Bayes ($B_{10}$)** com a escala de evidência de Harold Jeffreys, e síntese conceitual do teste **FBST** ($e$-value).

5. **Computação Bayesiana e Métodos Estocásticos:**
   * O dilema da integração em altas dimensões e a quebra de quadraturas determinísticas.
   * Monte Carlo Simples ($MCSE$), Amostragem por Importância e Reamostragem (Rejeição e SIR).
   * Cadeias de Markov e a condição de balanço detalhado.
   * **Algoritmo de Metropolis-Hastings com prova de reversibilidade**, Amostrador de Gibbs e RJMCMC.
   * Laboratório prático com scripts comparativos em **R e Python**.
   * Diagnósticos rigorosos de convergência: *Burn-in*, *Thinning*, Tamanho Amostral Efetivo ($ESS$) e estatística $\hat{R}$ de Gelman-Rubin.

6. **Modelos Lineares e ANOVA sob a Ótica Bayesiana:**
   * Regressão Linear Múltipla Normal: formulação matricial e priori conjugada Normal-Gama multivariada.
   * Análise sob Priori Não Informativa de Jeffreys: equivalência numérica com Mínimos Quadrados Ordinários (MQO) e ganho de interpretação probabilística direta.
   * ANOVA com 1 Fator de Classificação e **inferência exata sobre contrastes de tratamentos** ($\psi = \sum c_j \beta_j$).

---

## 🛠️ Tecnologias Utilizadas

* **HTML5 & CSS3:** Design system acadêmico responsivo com suporte nativo a Tema Claro e Escuro.
* **MathJax 3:** Motor de renderização matemática vetorial de alta precisão.
* **Python 3:** Scripts modulares de compilação em `builder/`.
* **GitHub Pages:** Hospedagem estática contínua e gratuita.
