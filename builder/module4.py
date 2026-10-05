# -*- coding: utf-8 -*-
"""
Módulo 4: Estimação, Teoria da Decisão e Testes de Hipóteses
"""

def get_module4_html():
    return """
    <!-- ========================================== -->
    <!-- MÓDULO 4: DECISÃO, ESTIMAÇÃO E HIPÓTESES   -->
    <!-- ========================================== -->
    <section id="modulo4" class="module-chapter">
        <h1 class="module-title">
            <span class="module-num">Módulo 4</span>
            Teoria da Decisão, Estimação e Testes de Hipóteses
        </h1>

        <div class="callout callout-tip">
            <div class="callout-header">💡 Sinopse Conceitual</div>
            <p>A distribuição a posteriori $p(\\theta \\mid x)$ contém toda a informação probabilística existente sobre o parâmetro. No entanto, o mundo real exige ações concretas: fixar a dosagem de um fármaco, precificar um seguro ou decidir se aprovamos ou rejeitamos uma teoria científica. A <strong>Teoria da Decisão Estatística</strong> formaliza essa ponte entre crença e ação. Ao ponderarmos as consequências dos erros através de uma <em>função de perda</em>, derivamos de forma unificada os estimadores pontuais ótimos (média, mediana e moda). Na inferência intervalar, as regiões de Maior Densidade a Posteriori (HPD) garantem os menores intervalos possíveis com credibilidade fixada. Por fim, a comparação de teorias e hipóteses atinge sua forma mais expressiva através do <strong>Fator de Bayes</strong> e das razões de chances.</p>
        </div>

        <h2>4.1 Fundamentos da Teoria da Decisão Estatística</h2>
        <p>Um problema formal de decisão estatística é especificado pela quádrupla $(\\Theta, \\Omega, \\mathcal{A}, L)$:</p>
        <ul>
            <li><strong>Espaço de Estados da Natureza $\\Theta$:</strong> O conjunto de todos os valores possíveis do parâmetro desconhecido $\\theta$.</li>
            <li><strong>Espaço Amostral $\\Omega$:</strong> O conjunto de todos os dados observáveis $x$.</li>
            <li><strong>Espaço de Ações $\\mathcal{A}$:</strong> O conjunto de decisões ou estimativas possíveis $a \\in \\mathcal{A}$ que o estatístico pode adotar.</li>
            <li><strong>Função de Perda $L(\\theta, a)$:</strong> Uma função não-negativa $L: \\Theta \\times \\mathcal{A} \\to \\mathbb{R}^+$ que quantifica o prejuízo ou custo incorrido ao tomar a ação $a$ quando o verdadeiro estado da natureza é $\\theta$.</li>
        </ul>

        <h3>Risco Frequentista versus Risco a Posteriori</h3>
        <p>A divergência entre as escolas reflete-se na forma como a incerteza é integrada:</p>
        <ul>
            <li><strong>Risco Frequentista $R(\\theta, \\delta)$:</strong> É a perda média calculada integrando sobre o espaço amostral $\\Omega$, mantendo o parâmetro $\\theta$ congelado como uma constante hipotética:
                $$R(\\theta, \\delta) = E_{X \\mid \\theta}[L(\\theta, \\delta(X))] = \\int_\\Omega L(\\theta, \\delta(x)) \\, p(x \\mid \\theta) \\, dx$$
                Como depende de $\\theta$, não existe, em geral, uma regra de decisão que minimize $R(\\theta, \\delta)$ simultaneamente para todos os valores de $\\theta$.
            </li>
            <li><strong>Risco a Posteriori $\\rho(a, x)$ (Perda Esperada a Posteriori):</strong> É a perda média calculada integrando sobre o espaço de parâmetros $\\Theta$, <strong>mantendo os dados observados $x$ estritamente fixados</strong>:
                $$\\rho(a, x) = E_{\\theta \\mid x}[L(\\theta, a)] = \\int_\\Theta L(\\theta, a) \\, p(\\theta \\mid x) \\, d\\theta$$
            </li>
        </ul>

        <div class="callout callout-def">
            <div class="callout-header">📘 Regra de Decisão de Bayes</div>
            <p>O <strong>Estimador de Bayes</strong> $\\hat{\\delta}(x)$ é a ação $a^* \\in \\mathcal{A}$ que minimiza o risco a posteriori para a amostra observada:</p>
            $$\\hat{\\delta}_{\\text{Bayes}}(x) = \\arg\\min_{a \\in \\mathcal{A}} \\rho(a, x) = \\arg\\min_{a \\in \\mathcal{A}} \\int_\\Theta L(\\theta, a) \\, p(\\theta \\mid x) \\, d\\theta$$
        </div>

        <h2>4.2 Dedução dos Estimadores Pontuais Canônicos</h2>
        <p>A beleza da teoria da decisão reside em demonstrar que os estimadores de tendência central clássicos (média, mediana e moda) não são escolhas arbitrárias; cada um é a <strong>solução ótima exata</strong> para uma geometria de penalização específica.</p>

        <div class="table-responsive">
            <table class="academic-table">
                <thead>
                    <tr>
                        <th>Função de Perda $L(\\theta, a)$</th>
                        <th>Natureza da Penalização</th>
                        <th>Estimador de Bayes Ótimo $\\hat{\\theta}_{\\text{Bayes}}$</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Quadrática:</strong> $(a - \\theta)^2$</td>
                        <td>Penaliza erros proporcionalmente ao quadrado da distância; erros grandes são severamente punidos.</td>
                        <td><strong>Média a Posteriori:</strong> $\\hat{\\theta} = E[\\theta \\mid x]$</td>
                    </tr>
                    <tr>
                        <td><strong>Linear Absoluta:</strong> $|a - \\theta|$</td>
                        <td>Penaliza o erro linearmente; robusta a caudas pesadas e valores extremos.</td>
                        <td><strong>Mediana a Posteriori:</strong> $\\hat{\\theta} = \\text{Mediana}(\\theta \\mid x)$</td>
                    </tr>
                    <tr>
                        <td><strong>Zero-Um (0-1):</strong> $I(|a - \\theta| > \\epsilon)$</td>
                        <td>Não penaliza pequenos desvios $\\le \\epsilon$ e atribui perda máxima a qualquer erro maior.</td>
                        <td><strong>Moda a Posteriori (MAP / EMVG):</strong> $\\hat{\\theta} = \\arg\\max_\\theta p(\\theta \\mid x)$</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <details class="proof">
            <summary>🔍 Demonstração Matemática: Minimização Rigorosa das 3 Funções de Perda</summary>
            <div class="proof-body">
                <h4>1. Perda Quadrática $\\implies$ Média a Posteriori</h4>
                <p>O risco a posteriori é $\\rho(a, x) = \\int (a - \\theta)^2 p(\\theta \\mid x) d\\theta$. Derivando em relação a $a$ sob o sinal da integral:</p>
                $$\\frac{d}{da} \\rho(a, x) = \\frac{d}{da} \\int_\\Theta (a^2 - 2a\\theta + \\theta^2) p(\\theta \\mid x) d\\theta = 2a \\int_\\Theta p(\\theta \\mid x) d\\theta - 2 \\int_\\Theta \\theta p(\\theta \\mid x) d\\theta$$
                <p>Como $\\int p(\\theta \\mid x) d\\theta = 1$, igualando a zero:</p>
                $$2a(1) - 2 E[\\theta \\mid x] = 0 \\implies a^* = E[\\theta \\mid x]$$
                <p>Como $\\frac{d^2}{da^2}\\rho(a, x) = 2 > 0$, trata-se de um mínimo global estrito.</p>

                <hr style="margin: 15px 0; border: none; border-top: 1px dashed #ccc;">

                <h4>2. Perda Linear Absoluta $\\implies$ Mediana a Posteriori</h4>
                <p>O risco é $\\rho(a, x) = \\int_{-\\infty}^\\infty |a - \\theta| p(\\theta \\mid x) d\\theta$. Decompondo a integral no ponto de corte $a$:</p>
                $$\\rho(a, x) = \\int_{-\\infty}^a (a - \\theta) p(\\theta \\mid x) d\\theta + \\int_a^\\infty (\\theta - a) p(\\theta \\mid x) d\\theta$$
                <p>Aplicando a <strong>Regra de Leibniz para diferenciação de integrais com limites variáveis</strong> $\\frac{d}{da}\\int_{u(a)}^{v(a)} f(t, a)dt = f(v(a), a)v'(a) - f(u(a), a)u'(a) + \\int_{u(a)}^{v(a)} \\frac{\\partial f}{\\partial a} dt$:</p>
                $$\\frac{d}{da} \\rho(a, x) = \\left[ (a-a)p(a\\mid x) + \\int_{-\\infty}^a 1 \\cdot p(\\theta\\mid x)d\\theta \\right] - \\left[ (a-a)p(a\\mid x) + \\int_a^\\infty 1 \\cdot p(\\theta\\mid x)d\\theta \\right]$$
                $$\\frac{d}{da} \\rho(a, x) = P(\\theta \\le a \\mid x) - P(\\theta > a \\mid x) = P(\\theta \\le a \\mid x) - [1 - P(\\theta \\le a \\mid x)] = 2P(\\theta \\le a \\mid x) - 1$$
                <p>Igualando a zero:</p>
                $$2P(\\theta \\le a^* \\mid x) - 1 = 0 \\implies P(\\theta \\le a^* \\mid x) = \\frac{1}{2}$$
                <p>Portanto, $a^*$ é precisamente a <strong>mediana da distribuição a posteriori</strong>.</p>

                <hr style="margin: 15px 0; border: none; border-top: 1px dashed #ccc;">

                <h4>3. Perda Zero-Um no Limite $\\implies$ Moda a Posteriori (MAP)</h4>
                <p>Defina $L_\\epsilon(\\theta, a) = 0$ se $|\\theta - a| \\le \\epsilon$ e $1$ se $|\\theta - a| > \\epsilon$. O risco a posteriori é:</p>
                $$\\rho(a, x) = \\int_{|\\theta - a| > \\epsilon} p(\\theta \\mid x) d\\theta = 1 - \\int_{a-\\epsilon}^{a+\\epsilon} p(\\theta \\mid x) d\\theta$$
                <p>Minimizar o risco $\\rho(a, x)$ equivale a maximizar $\\int_{a-\\epsilon}^{a+\\epsilon} p(\\theta \\mid x) d\\theta$. Pelo Teorema do Valor Médio para integrais, quando $\\epsilon \\to 0$:</p>
                $$\\frac{1}{2\\epsilon} \\int_{a-\\epsilon}^{a+\\epsilon} p(\\theta \\mid x) d\\theta \\xrightarrow{\\epsilon \\to 0} p(a \\mid x)$$
                <p>Portanto, no limite, o estimador ótimo é o ponto que maximiza diretamente a densidade a posteriori:</p>
                $$\\hat{\\theta}_{\\text{MAP}} = \\arg\\max_a p(a \\mid x)$$
            </div>
        </details>

        <h2>4.3 Estimação por Intervalos: Regiões de Credibilidade e HPD</h2>
        <p>A abordagem bayesiana para inferência intervalar não sofre da ambiguidade contraintuitiva dos intervalos de confiança clássicos.</p>

        <div class="callout callout-def">
            <div class="callout-header">📘 Intervalo de Credibilidade de $100(1-\\alpha)\\%$</div>
            <p>Dizemos que um subconjunto $C \\subset \\Theta$ é uma <strong>região de credibilidade</strong> de nível $1-\\alpha$ para $\\theta$ se a probabilidade a posteriori de que $\\theta$ pertença a $C$ satisfaz:</p>
            $$P(\\theta \\in C \\mid x) = \\int_C p(\\theta \\mid x) \\, d\\theta \\ge 1 - \\alpha$$
        </div>

        <h3>1. Intervalos de Caudas Iguais (Equi-tailed)</h3>
        <p>Para um parâmetro unidimensional, a forma mais imediata de construir o intervalo $[\\theta_L, \\theta_U]$ é deixar uma probabilidade de $\\alpha/2$ em cada uma das caudas:</p>
        $$P(\\theta < \\theta_L \\mid x) = \\frac{\\alpha}{2} \\quad \\text{e} \\quad P(\\theta > \\theta_U \\mid x) = \\frac{\\alpha}{2}$$
        <p>Os limites são simplesmente os quantis $q_{\\alpha/2}$ e $q_{1-\\alpha/2}$ da posteriori. Sua principal vantagem é a <strong>invariância sob transformações monótonas</strong>: o intervalo para $\\phi = g(\\theta)$ é diretamente $[g(\\theta_L), g(\\theta_U)]$.</p>

        <h3>2. Região de Maior Densidade a Posteriori (HPD / MDP)</h3>
        <p>Em distribuições assimétricas ou multimodais, os intervalos de caudas iguais podem incluir pontos com densidade baixíssima e excluir pontos com densidade alta. Para solucionar isso, formulamos os intervalos <strong>HPD (Highest Posterior Density)</strong>.</p>

        <div class="callout callout-def">
            <div class="callout-header">📘 Região HPD (Highest Posterior Density)</div>
            <p>Uma região $C \\subset \\Theta$ é dita uma <strong>região HPD</strong> de credibilidade $1-\\alpha$ se:</p>
            $$C = \\{ \\theta \\in \\Theta : p(\\theta \\mid x) \\ge k_\\alpha \\}$$
            <p>onde $k_\\alpha$ é a maior constante positiva tal que $P(\\theta \\in C \\mid x) = 1-\\alpha$.</p>
        </div>

        <details class="proof">
            <summary>🔍 Demonstração Matemática: Teorema do Volume Mínimo da Região HPD</summary>
            <div class="proof-body">
                <p><strong>Teorema:</strong> Entre todas as regiões de credibilidade $A \\subset \\Theta$ tais que $P(\\theta \\in A \\mid x) \\ge 1-\\alpha$, a região HPD $C = \\{\\theta: p(\\theta\\mid x) \\ge k\\}$ possui o <strong>menor volume (medida de Lebesgue) possível</strong>.</p>
                <p><strong>Prova:</strong></p>
                <p>Seja $A$ qualquer outra região satisfazendo $\\int_A p(\\theta \\mid x) d\\theta \\ge 1-\\alpha = \\int_C p(\\theta \\mid x) d\\theta$. Desejamos provar que $\\text{Vol}(C) \\le \\text{Vol}(A)$, ou equivalentemente $\\int_C 1 d\\theta \\le \\int_A 1 d\\theta$.</p>
                <ol>
                    <li>Decomponha as regiões em termos de suas interseções e complementares:
                        $$\\int_C p(\\theta \\mid x) d\\theta = \\int_{C \\cap A} p(\\theta \\mid x) d\\theta + \\int_{C \\setminus A} p(\\theta \\mid x) d\\theta$$
                        $$\\int_A p(\\theta \\mid x) d\\theta = \\int_{C \\cap A} p(\\theta \\mid x) d\\theta + \\int_{A \\setminus C} p(\\theta \\mid x) d\\theta$$
                    </li>
                    <li>Como $\\int_C p(\\theta \\mid x) d\\theta \\le \\int_A p(\\theta \\mid x) d\\theta$, subtraindo o termo comum $\\int_{C \\cap A}$:
                        $$\\int_{C \\setminus A} p(\\theta \\mid x) d\\theta \\le \\int_{A \\setminus C} p(\\theta \\mid x) d\\theta$$
                    </li>
                    <li>Pela definição da região HPD, para qualquer ponto $\\theta_1 \\in C \\setminus A$, temos $p(\\theta_1 \\mid x) \\ge k$. Logo:
                        $$\\int_{C \\setminus A} p(\\theta \\mid x) d\\theta \\ge k \\int_{C \\setminus A} 1 \\, d\\theta = k \\, \\text{Vol}(C \\setminus A)$$
                    </li>
                    <li>Por outro lado, para qualquer ponto $\\theta_2 \\in A \\setminus C$ (fora de $C$), temos $p(\\theta_2 \\mid x) < k$. Logo:
                        $$\\int_{A \\setminus C} p(\\theta \\mid x) d\\theta \\le k \\int_{A \\setminus C} 1 \\, d\\theta = k \\, \\text{Vol}(A \\setminus C)$$
                    </li>
                    <li>Combinando as três desigualdades:
                        $$k \\, \\text{Vol}(C \\setminus A) \\le \\int_{C \\setminus A} p(\\theta \\mid x) d\\theta \\le \\int_{A \\setminus C} p(\\theta \\mid x) d\\theta \\le k \\, \\text{Vol}(A \\setminus C)$$
                    </li>
                    <li>Como $k > 0$, dividindo por $k$: $\\text{Vol}(C \\setminus A) \\le \\text{Vol}(A \\setminus C)$. Somando $\\text{Vol}(C \\cap A)$ em ambos os lados:
                        $$\\text{Vol}(C) \\le \\text{Vol}(A)$$
                    </li>
                </ol>
                <p><strong>Conclusão:</strong> A região HPD é garantidamente a mais compacta e informativa possível para qualquer nível de credibilidade fixado.</p>
            </div>
        </details>

        <h2 id="fator-bayes">4.4 Testes de Hipóteses Bayesianos e o Fator de Bayes</h2>
        <p>Diferente da inferência clássica de Neyman-Pearson &mdash; que é assimétrica e só permite "rejeitar" ou "não rejeitar" a hipótese nula sem jamais atribuir probabilidade direta a ela &mdash;, a abordagem bayesiana trata o teste de hipóteses como uma comparação probabilística simétrica entre modelos concorrentes.</p>

        <h3>Razões de Chances (Odds) e Fator de Bayes</h3>
        <p>Considere duas hipóteses concorrentes, $H_0: \\theta \\in \\Theta_0$ e $H_1: \\theta \\in \\Theta_1$. Antes de coletar os dados, atribuímos probabilidades a priori $P(H_0)$ e $P(H_1)$. A <strong>razão de chances a priori</strong> (*prior odds*) é:</p>
        $$O(H_1, H_0) = \\frac{P(H_1)}{P(H_0)}$$
        <p>Após observar os dados $x$, calculamos as probabilidades a posteriori $P(H_0 \\mid x)$ e $P(H_1 \\mid x)$. A <strong>razão de chances a posteriori</strong> (*posterior odds*) é:</p>
        $$O(H_1, H_0 \\mid x) = \\frac{P(H_1 \\mid x)}{P(H_0 \\mid x)}$$

        <div class="callout callout-def">
            <div class="callout-header">📘 O Fator de Bayes ($B_{10}$)</div>
            <p>O <strong>Fator de Bayes</strong> $B_{10}(x)$ é a razão pela qual os dados observados alteram as chances relativas em favor de $H_1$ em detrimento de $H_0$:</p>
            $$\\text{Odds a Posteriori} = \\text{Fator de Bayes} \\times \\text{Odds a Priori} \\quad \\Longleftrightarrow \\quad B_{10}(x) = \\frac{O(H_1, H_0 \\mid x)}{O(H_1, H_0)} = \\frac{P(H_1 \\mid x) / P(H_0 \\mid x)}{P(H_1) / P(H_0)}$$
            <p>Pelo Teorema de Bayes, o Fator de Bayes coincide rigorosamente com a <strong>razão entre as verossimilhanças marginais preditivas</strong> dos dois modelos:</p>
            $$B_{10}(x) = \\frac{p(x \\mid H_1)}{p(x \\mid H_0)} = \\frac{\\int_{\\Theta_1} p(x \\mid \\theta) \\, p(\\theta \\mid H_1) \\, d\\theta}{\\int_{\\Theta_0} p(x \\mid \\theta) \\, p(\\theta \\mid H_0) \\, d\\theta}$$
        </div>

        <p>Se $B_{10} > 1$, os dados fornecem suporte para $H_1$; se $B_{10} < 1$, os dados favorecem $H_0$. Note a simetria perfeita: $B_{01} = 1 / B_{10}$.</p>

        <h3>Escala de Evidência de Harold Jeffreys</h3>
        <p>Para interpretar a magnitude do Fator de Bayes na prática científica, utiliza-se universalmente a escala calibrada proposta por Harold Jeffreys:</p>

        <div class="table-responsive">
            <table class="academic-table">
                <thead>
                    <tr>
                        <th>$B_{10}$ (Razão de Evidência)</th>
                        <th>$2 \\ln B_{10}$ (Escala em Decibéis)</th>
                        <th>Grau de Evidência em Favor de $H_1$ sobre $H_0$</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>$1$ a $3.2$</td>
                        <td>$0$ a $2.3$</td>
                        <td>Evidência anedótica (quase não vale a pena mencionar)</td>
                    </tr>
                    <tr>
                        <td>$3.2$ a $10$</td>
                        <td>$2.3$ a $4.6$</td>
                        <td>Evidência <strong>substancial / moderada</strong></td>
                    </tr>
                    <tr>
                        <td>$10$ a $100$</td>
                        <td>$4.6$ a $9.2$</td>
                        <td>Evidência <strong>forte</strong></td>
                    </tr>
                    <tr>
                        <td>$> 100$</td>
                        <td>$> 9.2$</td>
                        <td>Evidência <strong>decisiva</strong></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <h3>Síntese Conceitual: O Teste FBST (Full Bayesian Significance Test)</h3>
        <p>Quando nos deparamos com uma <strong>hipótese nula pontual precisa</strong> em um espaço contínuo (por exemplo, testar se a diferença de tratamentos é exatamente nula: $H_0: \\theta = 0$), o cálculo tradicional do Fator de Bayes exige atribuir uma probabilidade positiva concentrada pontual $P(\\theta = 0) > 0$ (uma massa de Dirac), o que viola a continuidade natural da distribuição a priori e dá origem ao famoso <em>Paradoxo de Lindley-Jeffreys</em>.</p>

        <div class="callout callout-tip">
            <div class="callout-header">💡 O FBST e a Medida de Evidência ($e$-value)</div>
            <p>Criado pelos estatísticos brasileiros <strong>Carlos Alberto de Bragança Pereira</strong> e <strong>Julio Michael Stern</strong> (1999), o <strong>Full Bayesian Significance Test (FBST)</strong> resolve esse impasse de forma estritamente bayesiana, sem distorcer o espaço com massas pontuais artificiais:</p>
            <ol>
                <li>Trabalha-se com a distribuição a posteriori contínua original $p(\\theta \\mid x)$.</li>
                <li>Identifica-se a máxima densidade alcançada sobre a variedade da hipótese nula: $m^* = \\sup_{\\theta \\in \\Theta_0} p(\\theta \\mid x)$.</li>
                <li>Define-se o <em>conjunto tangencial</em> $T = \\{ \\theta \\in \\Theta : p(\\theta \\mid x) > m^* \\}$, que contém todos os pontos do espaço paramétrico cuja plausibilidade a posteriori é <strong>estritamente maior</strong> que qualquer ponto sob $H_0$.</li>
                <li>A evidência contra $H_0$ é calculada integrando a posteriori sobre esse conjunto: $Ev(H_0) = \\int_T p(\\theta \\mid x) d\\theta$. O <strong>$e$-value</strong> em favor de $H_0$ é simplesmente $e^* = 1 - Ev(H_0)$.</li>
            </ol>
            <p>Se o $e$-value for muito pequeno, significa que quase toda a massa de probabilidade a posteriori reside em regiões mais plausíveis do que a hipótese nula, justificando a rejeição de $H_0$ sob uma interpretação geométrica pura da distribuição a posteriori.</p>
        </div>
    </section>
"""
