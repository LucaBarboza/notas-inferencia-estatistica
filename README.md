# Notas de Inferência Estatística Bayesiana

Material de estudo abrangente, analítico e estruturado sobre Inferência Estatística Bayesiana.

**Autor:** Luca Ferreira Barboza

---

## 🌐 Acesso Online (GitHub Pages)

Acesse a versão interativa online com renderização MathJax 3 e sumário navegável:
👉 **[https://lucabarboza.github.io/notas-inferencia-estatistica/](https://lucabarboza.github.io/notas-inferencia-estatistica/)**

---

## 📚 Conteúdo Programático Abordado

1. **Fundamentos e Distribuições de Probabilidade:**
   * Paradigma Bayesiano vs. Frequentista, Princípio da Verossimilhança e Birnbaum (1962).
   * Modelos Discretos: Bernoulli, Binomial, Poisson, Geométrica, Binomial Negativa (Pascal), Hipergeométrica e Multinomial.
   * Modelos Contínuos: Uniforme, Normal (univariada e multivariada), Gama, Beta, Exponencial, $t$ de Student e Dirichlet.

2. **Distribuições a Priori e a Posteriori (Teorema de Bayes e Preditiva):**
   * Formulação contínua e discreta, constante normalizadora e aprendizado sequencial.
   * Distribuição Preditiva a Priori $p(x)$ e Preditiva a Posteriori $p(y \mid x)$.
   * Classificação das prioris: Próprias vs. Impróprias, informativas, moderadamente informativas e vagas.
   * Priori de Jeffreys com prova de invariância, modelos de locação, escala, Binomial e Poisson.
   * Prioris Hierárquicas e Misturas de Prioris.

3. **Famílias Conjugadas:**
   * Fechamento por amostragem e estrutura na Família Exponencial.
   * Deduções analíticas completas para os principais pares conjugados (Beta-Binomial, Gama-Poisson, Normal-Normal, Normal com $\mu$ conhecido, Normal-Gama e Dirichlet-Multinomial).

4. **Estimação e Teoria da Decisão:**
   * Elementos formais da Teoria da Decisão, risco frequentista e risco a posteriori.
   * Deduções analíticas dos estimadores pontuais: Média (perda quadrática), Mediana (perda absoluta via Leibniz) e Moda/MAP (perda 0-1).
   * Intervalos de Credibilidade e Regiões HPD (comprimento mínimo).
   * Testes de Hipóteses Bayesianos, Fator de Bayes e teste FBST.

5. **Computação Bayesiana e Métodos Aproximados:**
   * Integração em alta dimensão e Monte Carlo simples (TLC, MCSE).
   * Amostragem por Importância (escolha ótima da densidade instrumental) e SIR.
   * Método da Rejeição com prova analítica.
   * MCMC, Cadeias de Markov, Balanço Detalhado e Algoritmo de Metropolis-Hastings.
   * Amostrador de Gibbs (prova de aceitação unitária).
   * Reversible Jump MCMC (RJMCMC) para seleção de modelos com Jacobiano de Green.
   * Diagnósticos de convergência: Burn-in, Thinning, ESS, Gelman-Rubin $\hat{R}$ e trace plots.

6. **Modelos Lineares e ANOVA:**
   * Regressão linear normal matricial com priori Normal-Gama multivariada e priori de Jeffreys.
   * Análise de Variância (ANOVA) com um fator de classificação e contrastes bayesianos.
