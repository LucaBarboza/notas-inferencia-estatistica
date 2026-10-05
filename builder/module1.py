# -*- coding: utf-8 -*-
"""
Módulo 1: Fundamentos e Distribuições de Probabilidade
"""

def get_module1_html():
    return """
    <!-- ========================================== -->
    <!-- MÓDULO 1: FUNDAMENTOS E DISTRIBUIÇÕES      -->
    <!-- ========================================== -->
    <section id="modulo1" class="module-chapter">
        <h1 class="module-title">
            <span class="module-num">Módulo 1</span>
            Fundamentos e Modelos de Probabilidade
        </h1>

        <div class="callout callout-tip">
            <div class="callout-header">💡 Sinopse Conceitual</div>
            <p>A inferência estatística dedica-se a responder: <em>o que podemos aprender sobre o mundo a partir de observações empíricas incompletas?</em> O paradigma bayesiano estabelece que qualquer quantidade desconhecida &mdash; sejam parâmetros latentes $\\theta$, estados não observados da natureza ou previsões futuras &mdash; deve ser tratada como uma variável aleatória governada pelas leis da probabilidade. Os modelos probabilísticos discretos e contínuos funcionam como as lentes que traduzem tanto o processo gerador de dados (a verossimilhança $p(x \\mid \\theta)$) quanto o conhecimento inicial acumulado antes da coleta da amostra.</p>
        </div>

        <h2>1.1 Paradigma Bayesiano versus Paradigma Frequentista</h2>
        <p>A grande bifurcação da inferência estatística não reside em desacordos de cálculo, mas sim na <strong>concepção epistemológica da incerteza e da probabilidade</strong>. Compreender essa distinção é indispensável para evitar equívocos graves de interpretação em testes e intervalos.</p>

        <div class="table-responsive">
            <table class="academic-table">
                <thead>
                    <tr>
                        <th>Critério</th>
                        <th>Abordagem Frequentista (Clássica)</th>
                        <th>Abordagem Bayesiana</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Conceito de Probabilidade</strong></td>
                        <td>Frequência relativa de ocorrência de um evento em um número infinito de repetições hipotéticas e idênticas do experimento.</td>
                        <td>Grau de crença racional ou estado epistêmico de incerteza do pesquisador, condicionado à informação disponível.</td>
                    </tr>
                    <tr>
                        <td><strong>Natureza do Parâmetro $\\theta$</strong></td>
                        <td>Uma <strong>constante fixa desconhecida</strong> no universo. Faz sentido dizer que $\\theta = 0.5$, mas não que $P(\\theta > 0.5) = 0.8$.</td>
                        <td>Uma <strong>variável aleatória</strong> dotada de uma distribuição de probabilidade que quantifica nossa incerteza sobre ele.</td>
                    </tr>
                    <tr>
                        <td><strong>Papel dos Dados $x$</strong></td>
                        <td>Uma realização entre infinitos pontos amostrais possíveis no espaço amostral $\\Omega$. Avaliam-se procedimentos baseando-se no comportamento médio em repetições.</td>
                        <td>A <strong>única evidência física real e concreta</strong> observada ($x_{\\text{obs}}$). Toda a inferência deve condicionar estritamente aos dados reais.</td>
                    </tr>
                    <tr>
                        <td><strong>Uso de Contrafactuais</strong></td>
                        <td>Sim. Métricas como o $p$-valor integram probabilidades de dados que <em>jamais ocorreram</em> mas que seriam "mais extremos que o observado".</td>
                        <td>Não. Uma vez realizada a amostra, resultados alternativos que poderiam ter ocorrido em universos paralelos são irrelevantes.</td>
                    </tr>
                    <tr>
                        <td><strong>Incorporação de Conhecimento Prévio</strong></td>
                        <td>Indireta ou informal (via desenho amostral ou restrições ad-hoc de parâmetros).</td>
                        <td>Formal e axiomática: através da <strong>distribuição a priori</strong> $p(\\theta)$ integrada via Teorema de Bayes.</td>
                    </tr>
                    <tr>
                        <td><strong>Interpretação do Intervalo</strong></td>
                        <td><em>"Se repetirmos este ensaio 100 vezes, 95% dos intervalos construídos conterão o verdadeiro parâmetro fixo."</em> (O parâmetro não tem probabilidade de estar lá).</td>
                        <td><em>"A probabilidade a posteriori de que o parâmetro $\\theta$ pertença ao intervalo $[a, b]$, dado os dados observados, é de 95%."</em></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="callout callout-warn">
            <div class="callout-header">⚠️ A Falácia da Transposição do Condicional</div>
            <p>Na inferência clássica, o valor-$p$ calcula a probabilidade dos dados sob a hipótese nula: $P(\\text{Dados tão ou mais extremos} \\mid H_0)$. No entanto, a pergunta genuína que qualquer cientista faz é exatamente a inversa: <em>"Dada a evidência observada, qual a probabilidade de a hipótese ser verdadeira?"</em>, ou seja, $P(H_0 \\mid \\text{Dados})$. Inverter essas probabilidades sem considerar a probabilidade a priori de $H_0$ é um erro probabilístico análogo a confundir $P(\\text{febre} \\mid \\text{gripe})$ com $P(\\text{gripe} \\mid \\text{febre})$.</p>
        </div>

        <h2>1.2 Princípio da Verossimilhança e Suficiência</h2>

        <h3>A Função de Verossimilhança</h3>
        <p>Dado um modelo probabilístico $p(x \\mid \\theta)$, a <strong>função de verossimilhança</strong> $l(\\theta; x)$ representa a densidade conjunta ou probabilidade avaliada no ponto amostral observado $x$, considerada estritamente como função do parâmetro desconhecido $\theta$:</p>
        $$l(\\theta; x) = p(x \\mid \\theta), \\quad \\theta \\in \\Theta$$
        
        <p>É vital lembrar que $l(\\theta; x)$ <strong>não é uma densidade de probabilidade em $\\theta$</strong>. Em geral, a integral de $l(\\theta; x)$ em relação a $\theta$ não é igual a 1 (e pode até ser infinita). A verossimilhança apenas estabelece uma plausibilidade relativa: se $l(\\theta_1; x) > l(\\theta_2; x)$, os dados observados tornam o parâmetro $\theta_1$ mais plausível que $\theta_2$.</p>

        <div class="callout callout-def">
            <div class="callout-header">📘 Princípio da Verossimilhança (Likelihood Principle)</div>
            <p>Se dois experimentos independentes envolvendo o mesmo parâmetro de interesse $\\theta$ geram funções de verossimilhança que são proporcionais para os dados efetivamente coletados, isto é:</p>
            $$l_1(\\theta; x_1) = c(x_1, x_2) \\, l_2(\\theta; x_2) \\quad \\forall \\, \\theta \\in \\Theta$$
            <p>onde a constante $c(x_1, x_2) > 0$ não depende de $\theta$, então <strong>toda e qualquer conclusão inferencial sobre $\\theta$ deve ser estritamente idêntica</strong> nos dois experimentos.</p>
        </div>

        <h3>A Regra de Parada (Stopping Rule Principle)</h3>
        <p>Uma consequência notável do Princípio da Verossimilhança é que a <strong>intenção do experimentador ao coletar os dados não deve alterar a inferência</strong>. Considere o exemplo clássico:</p>
        <ul>
            <li><strong>Pesquisador A (Modelo Binomial):</strong> Decide de antemão lançar uma moeda $n = 12$ vezes. Observa $x = 3$ caras e 9 coroas.
                $$p_A(x=3 \\mid \\theta) = \\binom{12}{3} \\theta^3 (1-\\theta)^9 = 220 \\, \\theta^3 (1-\\theta)^9$$
            </li>
            <li><strong>Pesquisador B (Modelo Binomial Negativo):</strong> Decide lançar a moeda até obter $r = 3$ caras. Acontece que a 3ª cara surgiu exatamente no 12º lançamento ($y = 9$ coroas antes da 3ª cara):
                $$p_B(y=9 \\mid \\theta) = \\binom{9 + 3 - 1}{3 - 1} \\theta^3 (1-\\theta)^9 = \\binom{11}{2} \\theta^3 (1-\\theta)^9 = 55 \\, \\theta^3 (1-\\theta)^9$$
            </li>
        </ul>
        <p>Note que as duas verossimilhanças são proporcionais:</p>
        $$l_A(\\theta) = \\frac{220}{55} l_B(\\theta) = 4 \\, l_B(\\theta) \\propto \\theta^3 (1-\\theta)^9$$
        <p>Para o estatístico bayesiano, o Teorema de Bayes cancela o fator multiplicativo 4 na constante de normalização, resultando em <strong>distribuições a posteriori absolutamente idênticas</strong>. Para o estatístico frequentista, contudo, o cálculo do valor-$p$ para a hipótese $H_0: \\theta = 0.5$ envolve somar caudas de distribuições diferentes, gerando $p$-valores distintos ($p \\approx 0.073$ para a Binomial e $p \\approx 0.032$ para a Binomial Negativa), o que levaria a conclusões científicas opostas para o mesmíssimo conjunto de dados!</p>

        <h3>Estatísticas Suficientes e Fatoração de Fisher-Neyman</h3>
        <div class="callout callout-thm">
            <div class="callout-header">⚙️ Critério de Fatoração de Fisher-Neyman</div>
            <p>Uma estatística $T(X)$ é dita <strong>suficiente</strong> para o parâmetro $\\theta$ se e somente se a densidade conjunta $p(x \\mid \\theta)$ puder ser decomposta no produto de duas funções:</p>
            $$p(x \\mid \\theta) = g(T(x), \\theta) \\cdot h(x)$$
            <p>onde $h(x)$ depende unicamente dos dados amostrais (livre de $\\theta$) e $g(T(x), \\theta)$ depende de $x$ apenas através da estatística $T(x)$.</p>
        </div>
        <p>No prisma bayesiano, a suficiência é imediata: se $T(x)$ é suficiente, o núcleo da verossimilhança é inteiramente capturado por $g(T(x), \\theta)$, o que implica que $p(\\theta \\mid x) = p(\\theta \\mid T(x))$. Ou seja, conhecer $T(x)$ basta para atingir o estado de conhecimento a posteriori perfeito sobre $\\theta$.</p>

        <h2 id="catalogo-discretas">1.3 Catálogo Estruturado de Modelos Discretos</h2>
        <p>Apresentamos a seguir os principais modelos de probabilidade discretos, com suas parametrizações formais, intuição prática e papel na inferência bayesiana.</p>

        <!-- Bernoulli -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>1. Distribuição de Bernoulli</h4>
                <span class="dist-badge badge-discrete">Discreta</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\theta \\in [0, 1]$ (probabilidade de sucesso)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in \\{0, 1\\}$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = \\theta$, $\\Var(X) = \\theta(1-\\theta)$</div>
                <div class="dist-grid-density">
                    <span class="label">Função de Probabilidade (F.P.)</span>
                    <div class="formula">$$p(x \\mid \\theta) = \\theta^x (1-\\theta)^{1-x}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Modelagem de um único ensaio com resultado binário (sucesso/fracasso, doente/sadio, sim/não).</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> É o bloco atômico da verossimilhança para ensaios binários. Seu conjugado natural para $\\theta$ é a distribuição Beta.</div>
        </div>

        <!-- Binomial -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>2. Distribuição Binomial</h4>
                <span class="dist-badge badge-discrete">Discreta</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $n \\in \\mathbb{N}$ (fixado), $\\theta \\in [0, 1]$</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in \\{0, 1, \\dots, n\\}$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = n\\theta$, $\\Var(X) = n\\theta(1-\\theta)$</div>
                <div class="dist-grid-density">
                    <span class="label">Função de Probabilidade (F.P.)</span>
                    <div class="formula">$$p(x \\mid \\theta) = \\binom{n}{x} \\theta^x (1-\\theta)^{n-x}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Contagem do total de sucessos em $n$ ensaios de Bernoulli independentes com probabilidade constante $\\theta$.</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Forma o par conjugado clássico <strong>Beta-Binomial</strong>. A estatística suficiente para uma amostra de Bernoullis é a soma $T(x) = \\sum x_i \\sim \\text{Binomial}(n, \\theta)$.</div>
        </div>

        <!-- Poisson -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>3. Distribuição de Poisson</h4>
                <span class="dist-badge badge-discrete">Discreta</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\lambda > 0$ (taxa média de ocorrência)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in \\{0, 1, 2, \\dots\\}$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = \\lambda$, $\\Var(X) = \\lambda$ (equidispersão)</div>
                <div class="dist-grid-density">
                    <span class="label">Função de Probabilidade (F.P.)</span>
                    <div class="formula">$$p(x \\mid \\lambda) = \\frac{e^{-\\lambda} \\lambda^x}{x!}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Contagem de eventos raros que ocorrem em um intervalo contínuo de tempo ou espaço sob taxa constante.</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Forma o par conjugado <strong>Gama-Poisson</strong>. A estatística suficiente para uma amostra $x_1, \\dots, x_n$ é $T(x) = \\sum_{i=1}^n x_i$.</div>
        </div>

        <!-- Geométrica -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>4. Distribuição Geométrica</h4>
                <span class="dist-badge badge-discrete">Discreta</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\theta \\in (0, 1]$ (probabilidade de sucesso)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in \\{0, 1, 2, \\dots\\}$ (fracassos até o 1º sucesso)</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = \\frac{1-\\theta}{\\theta}$, $\\Var(X) = \\frac{1-\\theta}{\\theta^2}$</div>
                <div class="dist-grid-density">
                    <span class="label">Função de Probabilidade (F.P.)</span>
                    <div class="formula">$$p(x \\mid \\theta) = \\theta (1-\\theta)^x$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Modelagem do tempo de espera até o primeiro sucesso em ensaios de Bernoulli independentes. Possui a propriedade discreta de perda de memória.</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Como a verossimilhança é proporcional a $\\theta^n (1-\\theta)^{\\sum x_i}$, a priori conjugada para $\\theta$ também é a distribuição Beta.</div>
        </div>

        <!-- Binomial Negativa (Pascal) -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>5. Distribuição Binomial Negativa (Pascal)</h4>
                <span class="dist-badge badge-discrete">Discreta</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $r > 0$ (sucessos almejados), $\\theta \\in (0, 1]$</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in \\{0, 1, 2, \\dots\\}$ (fracassos até obter $r$ sucessos)</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = \\frac{r(1-\\theta)}{\\theta}$, $\\Var(X) = \\frac{r(1-\\theta)}{\\theta^2} > E[X]$</div>
                <div class="dist-grid-density">
                    <span class="label">Função de Probabilidade (F.P.)</span>
                    <div class="formula">$$p(x \\mid \\theta) = \\binom{x+r-1}{x} \\theta^r (1-\\theta)^x$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Generalização da Geométrica para $r$ sucessos, ou para modelar contagens com <em>superdispersão</em> (onde a variância excede a média, violando a Poisson).</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Surge naturalmente como a <strong>distribuição preditiva</strong> do modelo conjugado Gama-Poisson.</div>
        </div>

        <!-- Hipergeométrica -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>6. Distribuição Hipergeométrica</h4>
                <span class="dist-badge badge-discrete">Discreta</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $N$ (população), $K$ (sucessos na pop.), $n$ (amostra)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in \\{\\max(0, n-(N-K)), \\dots, \\min(n, K)\\}$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = n\\frac{K}{N}$, $\\Var(X) = n\\frac{K}{N}\\left(1-\\frac{K}{N}\\right)\\left(\\frac{N-n}{N-1}\\right)$</div>
                <div class="dist-grid-density">
                    <span class="label">Função de Probabilidade (F.P.)</span>
                    <div class="formula">$$p(x) = \\frac{\\binom{K}{x}\\binom{N-K}{n-x}}{\\binom{N}{n}}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Amostragem <strong>sem reposição</strong> em populações finitas. O termo $\\frac{N-n}{N-1}$ atua como o fator de correção de população finita.</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Utilizada na estimação de tamanhos populacionais desconhecidos $N$ (problema de captura-recaptura) ou de itens defeituosos $K$.</div>
        </div>

        <!-- Multinomial -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>7. Distribuição Multinomial</h4>
                <span class="dist-badge badge-discrete">Discreta</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $n$ (ensaios), $\\boldsymbol{\\theta} = (\\theta_1, \\dots, \\theta_k)$ com $\\sum \\theta_j = 1$</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $\\mathbf{x} = (x_1, \\dots, x_k) \\in \\mathbb{N}^k$ com $\\sum x_j = n$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X_j] = n\\theta_j$, $\\Var(X_j) = n\\theta_j(1-\\theta_j)$</div>
                <div class="dist-grid-density">
                    <span class="label">Função de Probabilidade (F.P.)</span>
                    <div class="formula">$$p(\\mathbf{x} \\mid \\boldsymbol{\\theta}) = \\frac{n!}{x_1! \\dots x_k!} \\prod_{j=1}^k \\theta_j^{x_j}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Generalização da Binomial para ensaios independentes com mais de dois desfechos possíveis mutuamente exclusivos (dados categóricos multivariados).</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Forma o par conjugado multivariado canônico <strong>Dirichlet-Multinomial</strong>.</div>
        </div>

        <h2 id="catalogo-continuas">1.4 Catálogo Estruturado de Modelos Contínuos</h2>
        <p>Abaixo detalhamos as principais famílias contínuas que atuam tanto como modelos amostrais quanto como prioris conjugadas fundamentais.</p>

        <!-- Uniforme -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>1. Distribuição Uniforme Contínua</h4>
                <span class="dist-badge badge-continuous">Contínua</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $a, b \\in \\mathbb{R}$ com $a < b$</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in [a, b]$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = \\frac{a+b}{2}$, $\\Var(X) = \\frac{(b-a)^2}{12}$</div>
                <div class="dist-grid-density">
                    <span class="label">Função Densidade de Probabilidade (F.D.P.)</span>
                    <div class="formula">$$f(x) = \\frac{1}{b-a}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Quando uma variável contínua está estritamente restrita a um intervalo finito e não há nenhuma preferência por qualquer sub-região.</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Base da clássica <em>priori uniforme de Bayes-Laplace</em> para parâmetros limitados (ex: $\\theta \\sim U(0, 1)$).</div>
        </div>

        <!-- Exponencial -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>2. Distribuição Exponencial</h4>
                <span class="dist-badge badge-continuous">Contínua</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\lambda > 0$ (taxa)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in [0, \\infty)$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = \\frac{1}{\\lambda}$, $\\Var(X) = \\frac{1}{\\lambda^2}$</div>
                <div class="dist-grid-density">
                    <span class="label">Função Densidade de Probabilidade (F.D.P.)</span>
                    <div class="formula">$$f(x \\mid \\lambda) = \\lambda e^{-\\lambda x}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Modelagem de intervalos de tempo contínuos entre ocorrências de eventos de Poisson. Possui a propriedade única de <em>perda de memória contínua</em>: $P(X > s + t \\mid X > s) = P(X > t)$.</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Caso particular de $\\text{Gama}(1, \\lambda)$. Sua priori conjugada para o parâmetro de taxa $\\lambda$ é a distribuição Gama.</div>
        </div>

        <!-- Gama -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>3. Distribuição Gama</h4>
                <span class="dist-badge badge-continuous">Contínua</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\alpha > 0$ (forma), $\\beta > 0$ (taxa)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in (0, \\infty)$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = \\frac{alpha}{\\beta}$, $\\Var(X) = \\frac{\\alpha}{\\beta^2}$</div>
                <div class="dist-grid-density">
                    <span class="label">Função Densidade de Probabilidade (F.D.P.)</span>
                    <div class="formula">$$f(x \\mid \\alpha, \\beta) = \\frac{\\beta^\\alpha}{\\Gamma(\\alpha)} x^{\\alpha-1} e^{-\\beta x}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Variáveis positivas contínuas com assimetria à direita (tempos de sobrevivência, custos, precipitação pluviométrica).</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Peça-chave da inferência bayesiana! Atua como a <strong>priori conjugada padrão para parâmetros de taxa da Poisson</strong> e para a <strong>precisão $\\phi = 1/\\sigma^2$ da distribuição Normal</strong>.</div>
        </div>

        <!-- Qui-Quadrado -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>4. Distribuição Qui-Quadrado ($\\chi^2$)</h4>
                <span class="dist-badge badge-continuous">Contínua</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\nu > 0$ (graus de liberdade)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in (0, \\infty)$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = \\nu$, $\\Var(X) = 2\\nu$</div>
                <div class="dist-grid-density">
                    <span class="label">Função Densidade de Probabilidade (F.D.P.)</span>
                    <div class="formula">$$f(x) = \\frac{1}{2^{\\nu/2} \\Gamma(\\nu/2)} x^{(\\nu/2)-1} e^{-x/2}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Soma dos quadrados de $\\nu$ variáveis normais padrão independentes ($X = \\sum_{i=1}^\\nu Z_i^2$).</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> É o caso especial $\\text{Gama}(\\alpha = \\nu/2, \\beta = 1/2)$, fundamental nas distribuições a posteriori de variâncias sob prioris não informativas.</div>
        </div>

        <!-- Beta -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>5. Distribuição Beta</h4>
                <span class="dist-badge badge-continuous">Contínua</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\alpha > 0, \\beta > 0$ (hiperparâmetros de forma)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $\\theta \\in (0, 1)$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[\\theta] = \\frac{\\alpha}{\\alpha+\\beta}$, $\\Var(\\theta) = \\frac{\\alpha\\beta}{(\\alpha+\\beta)^2(\\alpha+\\beta+1)}$</div>
                <div class="dist-grid-density">
                    <span class="label">Função Densidade de Probabilidade (F.D.P.)</span>
                    <div class="formula">$$f(\\theta) = \\frac{1}{B(\\alpha, \\beta)} \\theta^{\\alpha-1} (1-\\theta)^{\\beta-1}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Modelagem flexível de probabilidades, proporções ou taxas contidas no intervalo $(0,1)$. Dependendo de $\\alpha$ e $\\beta$, adquire forma de U, uniforme, sino simétrico ou assimétrico.</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> A <strong>priori conjugada canônica para probabilidades de sucesso</strong> em modelos Bernoulli e Binomial.</div>
        </div>

        <!-- Normal Univariada -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>6. Distribuição Normal (Gaussiana) Univariada</h4>
                <span class="dist-badge badge-continuous">Contínua</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\mu \\in \\mathbb{R}$ (média), $\\sigma^2 > 0$ ou $\\tau = 1/\\sigma^2$ (precisão)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in (-\\infty, \\infty)$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = \\mu$, $\\Var(X) = \\sigma^2 = \\tau^{-1}$</div>
                <div class="dist-grid-density">
                    <span class="label">Função Densidade de Probabilidade (F.D.P.)</span>
                    <div class="formula">$$f(x \\mid \\mu, \\tau) = \\sqrt{\\frac{\\tau}{2\\pi}} \\exp\\left\\{ -\\frac{\\tau}{2}(x - \\mu)^2 \\right\\}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Fenômenos biológicos, físicos e erros de medição resultantes da soma de múltiplos efeitos infinitesimais (Teorema Central do Limite).</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Conjugada com relação à média quando a variância é conhecida. A parametrização por precisão $\\tau$ simplifica enormemente a álgebra bayesiana.</div>
        </div>

        <!-- Normal Multivariada -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>7. Distribuição Normal Multivariada</h4>
                <span class="dist-badge badge-continuous">Contínua</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\boldsymbol{\\mu} \\in \\mathbb{R}^p$ (média), $\\boldsymbol{\\Sigma} \\in \\mathbb{R}^{p \\times p}$ (covariância)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $\\mathbf{x} \\in \\mathbb{R}^p$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[\\mathbf{X}] = \\boldsymbol{\\mu}$, $\\Cov(\\mathbf{X}) = \\boldsymbol{\\Sigma}$</div>
                <div class="dist-grid-density">
                    <span class="label">Função Densidade de Probabilidade (F.D.P.)</span>
                    <div class="formula">$$f(\\mathbf{x}) = (2\\pi)^{-p/2} |\\boldsymbol{\\Sigma}|^{-1/2} \\exp\\left\\{ -\\frac{1}{2}(\\mathbf{x}-\\boldsymbol{\\mu})'\\boldsymbol{\\Sigma}^{-1}(\\mathbf{x}-\\boldsymbol{\\mu}) \\right\\}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Modelagem conjunta de vetores correlacionados contínuos.</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Base teórica da regressão linear múltipla bayesiana e processos gaussianos. Atua como priori conjugada para os coeficientes de regressão $\\boldsymbol{\\beta}$.</div>
        </div>

        <!-- t de Student -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>8. Distribuição $t$ de Student</h4>
                <span class="dist-badge badge-continuous">Contínua</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\nu > 0$ (graus de lib.), $\\mu \\in \\mathbb{R}$ (locação), $\\sigma^2 > 0$ (escala)</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $x \\in (-\\infty, \\infty)$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[X] = \\mu$ (se $\\nu > 1$), $\\Var(X) = \\sigma^2 \\frac{\\nu}{\\nu-2}$ (se $\\nu > 2$)</div>
                <div class="dist-grid-density">
                    <span class="label">Função Densidade de Probabilidade (F.D.P.)</span>
                    <div class="formula">$$f(x) = \\frac{\\Gamma((\\nu+1)/2)}{\\Gamma(\\nu/2)\\sqrt{\\pi \\nu} \\sigma} \\left[ 1 + \\frac{1}{\\nu}\\left(\\frac{x-\\mu}{\\sigma}\\right)^2 \\right]^{-(\\nu+1)/2}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> Amostras pequenas de populações normais com variância desconhecida, ou quando se deseja modelagem robusta a valores discrepantes (<em>outliers</em>) devido às caudas pesadas.</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Surge analiticamente como a <strong>distribuição a posteriori marginal da média $\\mu$</strong> quando a variância $\\sigma^2$ é integrada (marginalizada) a partir da Normal-Gama.</div>
        </div>

        <!-- Dirichlet -->
        <div class="dist-card">
            <div class="dist-card-header">
                <h4>9. Distribuição Dirichlet</h4>
                <span class="dist-badge badge-continuous">Contínua</span>
            </div>
            <div class="dist-grid">
                <div class="dist-grid-item"><span class="label">Parâmetros</span> $\\boldsymbol{\\alpha} = (\\alpha_1, \\dots, \\alpha_k)$ com $\\alpha_j > 0$; $\\alpha_0 = \\sum \\alpha_j$</div>
                <div class="dist-grid-item"><span class="label">Suporte</span> $\\boldsymbol{\\theta} \\in \\Delta_k = \\{\\boldsymbol{\\theta} \\in (0,1)^k : \\sum_{j=1}^k \\theta_j = 1\\}$</div>
                <div class="dist-grid-item"><span class="label">Momentos</span> $E[\\theta_j] = \\frac{\\alpha_j}{\\alpha_0}$, $\\Var(\\theta_j) = \\frac{\\alpha_j(\\alpha_0-\\alpha_j)}{\\alpha_0^2(\\alpha_0+1)}$</div>
                <div class="dist-grid-density">
                    <span class="label">Função Densidade de Probabilidade (F.D.P.)</span>
                    <div class="formula">$$f(\\boldsymbol{\\theta}) = \\frac{\\Gamma(\\alpha_0)}{\\prod_{j=1}^k \\Gamma(\\alpha_j)} \\prod_{j=1}^k \\theta_j^{\\alpha_j-1}$$</div>
                </div>
            </div>
            <p><strong>Quando usar:</strong> É a generalização multivariada da Beta. Modela vetores de probabilidades categóricas que somam exatamente 1 (ex: proporções de votos entre $k$ candidatos).</p>
            <div class="dist-role"><strong>Papel Bayesiano:</strong> Priori conjugada para a distribuição Multinomial e base dos processos não-paramétricos de Dirichlet.</div>
        </div>
    </section>
"""
