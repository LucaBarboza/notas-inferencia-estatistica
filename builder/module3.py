# -*- coding: utf-8 -*-
"""
Módulo 3: Famílias Conjugadas
"""

def get_module3_html():
    return """
    <!-- ========================================== -->
    <!-- MÓDULO 3: FAMÍLIAS CONJUGADAS              -->
    <!-- ========================================== -->
    <section id="modulo3" class="module-chapter">
        <h1 class="module-title">
            <span class="module-num">Módulo 3</span>
            Famílias Conjugadas e a Família Exponencial
        </h1>

        <div class="callout callout-tip">
            <div class="callout-header">💡 Sinopse Conceitual</div>
            <p>Em inferência bayesiana, a integral no denominador do Teorema de Bayes pode ser analiticamente intratável para modelos arbitrários. No entanto, quando a distribuição a priori possui a mesma estrutura funcional do núcleo da verossimilhança, a distribuição a posteriori resultante pertence rigorosamente à mesma família paramétrica da priori. Essa propriedade matemática extraordinária é denominada <strong>fechamento por amostragem</strong> ou <strong>conjugação</strong>. Na Família Exponencial de distribuições, a conjugação surge de forma canônica, permitindo que toda a inferência seja reduzida a uma simples atualização algébrica de hiperparâmetros &mdash; onde o conhecimento prévio atua como "amostras virtuais adicionais".</p>
        </div>

        <h2>3.1 Definição Formal de Conjugação e Fechamento</h2>
        <div class="callout callout-def">
            <div class="callout-header">📘 Família de Distribuições Conjugada</div>
            <p>Seja $\\mathcal{P} = \\{p(\\theta \\mid \\boldsymbol{\\eta}) : \\boldsymbol{\\eta} \\in H\\}$ uma família de distribuições de probabilidade indexada pelo vetor de hiperparâmetros $\\boldsymbol{\\eta}$. Dizemos que $\\mathcal{P}$ é <strong>conjugada</strong> para um modelo amostral $p(x \\mid \\theta)$ se, para qualquer priori $p(\\theta) \\in \\mathcal{P}$ e qualquer amostra observada $x$, a distribuição a posteriori correspondente também pertencer a $\\mathcal{P}$:</p>
            $$p(\\theta) \\in \\mathcal{P} \\implies p(\\theta \\mid x) \\in \\mathcal{P}$$
        </div>

        <p>A conjugação proporciona três vantagens teóricas e práticas inestimáveis:</p>
        <ul>
            <li><strong>Tratabilidade Analítica:</strong> Dispensa métodos numéricos de integração para encontrar momentos, quantis e intervalos de credibilidade.</li>
            <li><strong>Interpretação Clara dos Hiperparâmetros:</strong> Os hiperparâmetros da priori podem ser interpretados intuitivamente como o tamanho de uma <em>amostra histórica</em> ou <em>pseudodados</em> acumulados no passado.</li>
            <li><strong>Média a Posteriori como Combinação Convexa:</strong> Em praticamente todos os pares conjugados, a média a posteriori pode ser expressa como uma média ponderada entre a média a priori e a média dos dados observados:
                $$\\hat{\\theta}_{\\text{Bayes}} = w \\, E[\\theta]_{\\text{priori}} + (1-w) \\, \\hat{\\theta}_{\\text{amostra}}, \\quad w \\in [0, 1]$$
            </li>
        </ul>

        <h2>3.2 Conjugação na Família Exponencial</h2>
        <p>A existência de famílias conjugadas naturais não é um acidente algébrico; ela é uma consequência direta do <strong>Teorema de Pitman-Koopman-Darmois</strong>, que estabelece que apenas distribuições pertencentes à Família Exponencial possuem estatísticas suficientes de dimensão fixa independentemente do tamanho da amostra $n$.</p>

        <div class="callout callout-thm">
            <div class="callout-header">⚙️ A Família Exponencial Regular a 1 Parâmetro</div>
            <p>Um modelo amostral pertence à Família Exponencial a um parâmetro se sua densidade puder ser expressa na forma:</p>
            $$p(x \\mid \\theta) = a(x) \\exp\\left\\{ u(x) \\phi(\\theta) - b(\\theta) \\right\\}$$
            <p>onde $u(x)$ é a estatística suficiente para $\\theta$, $\\phi(\\theta)$ é o parâmetro natural, e $b(\\theta)$ é a função cumulante logarítmica.</p>
        </div>

        <p>Para uma amostra aleatória independente de tamanho $n$, $x = (x_1, \\dots, x_n)$, a verossimilhança conjunta assume a forma:</p>
        $$p(x \\mid \\theta) = \\left[ \\prod_{i=1}^n a(x_i) \\right] \\exp\\left\\{ \\left[ \\sum_{i=1}^n u(x_i) \\right] \\phi(\\theta) - n \\, b(\\theta) \\right\\}$$
        
        <p>Aproveitando a estrutura funcional exata dessa verossimilhança, constrói-se a <strong>priori conjugada natural</strong> com hiperparâmetros $\\alpha$ e $\\beta$:</p>
        $$p(\\theta \\mid \\alpha, \\beta) = k(\\alpha, \\beta) \\exp\\left\\{ \\alpha \\, \\phi(\\theta) - \\beta \\, b(\\theta) \\right\\}$$
        <p>onde $k(\\alpha, \\beta)$ é a constante normalizadora que garante $\\int p(\\theta) d\\theta = 1$.</p>

        <details class="proof">
            <summary>🔍 Demonstração Matemática: Atualização e Preditiva na Família Exponencial</summary>
            <div class="proof-body">
                <p>Aplicando o Teorema de Bayes combinando a verossimilhança da amostra e a priori conjugada:</p>
                $$p(\\theta \\mid x) \\propto p(x \\mid \\theta) \\, p(\\theta) = \\left[ \\prod_{i=1}^n a(x_i) \\right] \\exp\\left\\{ \\left[ \\sum u(x_i) \\right] \\phi(\\theta) - n b(\\theta) \\right\\} \\times k(\\alpha, \\beta) \\exp\\left\\{ \\alpha \\phi(\\theta) - \\beta b(\\theta) \\right\\}$$
                <p>Somando os expoentes diretamente:</p>
                $$p(\\theta \\mid x) \\propto \\exp\\left\\{ \\left[ \\alpha + \\sum_{i=1}^n u(x_i) \\right] \\phi(\\theta) - [\\beta + n] \\, b(\\theta) \\right\\}$$
                <p>Notamos que esta expressão tem <strong>exatamente a mesma forma funcional da distribuição a priori</strong>, bastando substituir os hiperparâmetros originais pelos hiperparâmetros atualizados:</p>
                $$\\alpha^* = \\alpha + \\sum_{i=1}^n u(x_i), \\quad \\beta^* = \\beta + n$$
                <p>Portanto, a distribuição a posteriori normalizada é dada por:</p>
                $$p(\\theta \\mid x) = k\\left(\\alpha + \\sum u(x_i), \\, \\beta + n\\right) \\exp\\left\\{ \\left[ \\alpha + \\sum u(x_i) \\right] \\phi(\\theta) - [\\beta + n] \\, b(\\theta) \\right\\}$$
                <p>Além disso, a <strong>distribuição preditiva</strong> $p(x)$ para os dados é obtida de forma estritamente analítica como a razão das constantes normalizadoras:</p>
                $$p(x) = \\frac{p(x \\mid \\theta) p(\\theta)}{p(\\theta \\mid x)} = \\left[ \\prod_{i=1}^n a(x_i) \\right] \\frac{k(\\alpha, \\beta)}{k\\left(\\alpha + \\sum u(x_i), \\, \\beta + n\\right)}$$
            </div>
        </details>

        <h2 id="pares-conjugados">3.3 Os Grandes Pares Conjugados Canônicos</h2>

        <!-- Par 1: Beta-Binomial -->
        <h3>1. O Modelo Beta-Binomial</h3>
        <p>Seja $X \\sim \\text{Binomial}(n, \\theta)$ com $n$ conhecido e $\\theta \\in [0, 1]$. Adotamos uma priori conjugada $\\theta \\sim \\text{Beta}(\\alpha, \\beta)$:</p>
        $$l(\\theta; x) = \\binom{n}{x} \\theta^x (1-\\theta)^{n-x}, \\quad p(\\theta) = \\frac{1}{B(\\alpha, \\beta)} \\theta^{\\alpha-1} (1-\\theta)^{\\beta-1}$$
        <p>Multiplicando os termos no Teorema de Bayes:</p>
        $$p(\\theta \\mid x) \\propto \\theta^x (1-\\theta)^{n-x} \\cdot \\theta^{\\alpha-1} (1-\\theta)^{\\beta-1} = \\theta^{(\\alpha+x)-1} (1-\\theta)^{(\\beta + n - x)-1}$$
        <p>Reconhecemos imediatamente o núcleo de uma nova distribuição Beta com parâmetros atualizados:</p>
        $$\\theta \\mid x \\sim \\text{Beta}(\\alpha + x, \\, \\beta + n - x)$$

        <div class="callout callout-tip">
            <div class="callout-header">💡 Intuição dos Pseudodados</div>
            <p>A priori $\\text{Beta}(\\alpha, \\beta)$ equivale a iniciar o experimento tendo observado previamente $\\alpha - 1$ sucessos e $\\beta - 1$ fracassos virtuais. A média a posteriori é uma média ponderada pura:</p>
            $$E[\\theta \\mid x] = \\frac{\\alpha + x}{\\alpha + \\beta + n} = \\left( \\frac{\\alpha + \\beta}{\\alpha + \\beta + n} \\right) \\frac{\\alpha}{\\alpha + \\beta} + \\left( \\frac{n}{\\alpha + \\beta + n} \\right) \\frac{x}{n}$$
            <p>Quando $n \\to \\infty$, o peso da priori decai a zero e a média a posteriori converge assintoticamente para a proporção amostral clássica $\\hat{\\theta}_{\\text{MV}} = x/n$.</p>
        </div>

        <details class="proof">
            <summary>🔍 Demonstração Matemática: A Preditiva Beta-Binomial</summary>
            <div class="proof-body">
                <p>Desejamos calcular a probabilidade de observar $y$ sucessos em $m$ novos ensaios independentes, $Y \\sim \\text{Binomial}(m, \\theta)$:</p>
                $$p(y \\mid x) = \\int_0^1 p(y \\mid \\theta) \\, p(\\theta \\mid x) \\, d\\theta = \\int_0^1 \\binom{m}{y} \\theta^y (1-\\theta)^{m-y} \\frac{1}{B(\\alpha^*, \\beta^*)} \\theta^{\\alpha^*-1} (1-\\theta)^{\\beta^*-1} d\\theta$$
                <p>onde $\\alpha^* = \\alpha + x$ e $\\beta^* = \\beta + n - x$. Colocando as constantes para fora da integral:</p>
                $$p(y \\mid x) = \\binom{m}{y} \\frac{1}{B(\\alpha^*, \\beta^*)} \\int_0^1 \\theta^{(\\alpha^* + y) - 1} (1-\\theta)^{(\\beta^* + m - y) - 1} d\\theta$$
                <p>A integral no interior é exatamente a definição da função Beta $B(\\alpha^* + y, \\, \\beta^* + m - y)$. Portanto:</p>
                $$p(y \\mid x) = \\binom{m}{y} \\frac{B(\\alpha^* + y, \\, \\beta^* + m - y)}{B(\\alpha^*, \\beta^*)}$$
                <p>Esta é a <strong>distribuição Beta-Binomial</strong>. Se considerarmos uma única observação futura ($m = 1$), a probabilidade preditiva de sucesso é exatamente a média a posteriori: $P(Y = 1 \\mid x) = \\frac{\\alpha^*}{\\alpha^* + \\beta^*}$.</p>
            </div>
        </details>

        <!-- Par 2: Gama-Poisson -->
        <h3>2. O Modelo Gama-Poisson</h3>
        <p>Sejam $x_1, \\dots, x_n$ observações independentes de uma distribuição $\\text{Poisson}(\\lambda)$, com $t = \\sum_{i=1}^n x_i$. A verossimilhança conjunta é:</p>
        $$l(\\lambda; x) = \\left[ \\prod_{i=1}^n \\frac{1}{x_i!} \\right] e^{-n\\lambda} \\lambda^t \\propto e^{-n\\lambda} \\lambda^t$$
        <p>A priori conjugada é uma $\\text{Gama}(\\alpha, \\beta)$ com taxa $\\beta$ e forma $\\alpha$:</p>
        $$p(\\lambda) = \\frac{\\beta^\\alpha}{\\Gamma(\\alpha)} \\lambda^{\\alpha-1} e^{-\\beta \\lambda} \\propto \\lambda^{\\alpha-1} e^{-\\beta \\lambda}$$
        <p>Multiplicando na regra de Bayes:</p>
        $$p(\\lambda \\mid x) \\propto e^{-n\\lambda} \\lambda^t \\cdot \\lambda^{\\alpha-1} e^{-\\beta \\lambda} = \\lambda^{(\\alpha + t) - 1} e^{-(\\beta + n)\\lambda}$$
        <p>Concluímos diretamente que a distribuição a posteriori é:</p>
        $$\\lambda \\mid x \\sim \\text{Gama}(\\alpha + \\sum_{i=1}^n x_i, \\, \\beta + n)$$

        <details class="proof">
            <summary>🔍 Demonstração Matemática: A Preditiva Binomial Negativa</summary>
            <div class="proof-body">
                <p>Para uma nova contagem futura $Y \\sim \\text{Poisson}(\\lambda)$:</p>
                $$p(y \\mid x) = \\int_0^\\infty \\frac{e^{-\\lambda} \\lambda^y}{y!} \\frac{(\\beta^*)^{\\alpha^*}}{\\Gamma(\\alpha^*)} \\lambda^{\\alpha^*-1} e^{-\\beta^* \\lambda} d\\lambda$$
                <p>Agrupando os termos em $\\lambda$:</p>
                $$p(y \\mid x) = \\frac{(\\beta^*)^{\\alpha^*}}{y! \\, \\Gamma(\\alpha^*)} \\int_0^\\infty \\lambda^{(\\alpha^* + y) - 1} e^{-(\\beta^* + 1)\\lambda} d\\lambda$$
                <p>Pela integral da densidade Gama, $\\int_0^\\infty u^{k-1} e^{-c u} du = \\frac{\\Gamma(k)}{c^k}$. Aplicando com $k = \\alpha^* + y$ e $c = \\beta^* + 1$:</p>
                $$p(y \\mid x) = \\frac{(\\beta^*)^{\\alpha^*}}{y! \\, \\Gamma(\\alpha^*)} \\frac{\\Gamma(\\alpha^* + y)}{(\\beta^* + 1)^{\\alpha^* + y}} = \\frac{\\Gamma(\\alpha^* + y)}{y! \\, \\Gamma(\\alpha^*)} \\left( \\frac{\\beta^*}{\\beta^* + 1} \\right)^{\\alpha^*} \\left( \\frac{1}{\\beta^* + 1} \\right)^y$$
                <p>Reescrevendo em termos combinatórios para $\\alpha^*$ inteiro, temos precisamente a f.p. da <strong>Distribuição Binomial Negativa</strong>:</p>
                $$p(y \\mid x) = \\binom{\\alpha^* + y - 1}{y} \\left( \\frac{\\beta^*}{\\beta^* + 1} \\right)^{\\alpha^*} \\left( \\frac{1}{\\beta^* + 1} \\right)^y$$
            </div>
        </details>

        <!-- Par 3: Normal com Variância Conhecida -->
        <h3>3. Modelo Normal com Variância Conhecida (Conjugação de Precisões)</h3>
        <p>Seja $X_1, \\dots, X_n \\sim N(\\mu, \\sigma^2)$ com variância $\\sigma^2$ fixada e conhecida. É matematicamente mais elegante trabalhar com a <strong>precisão dos dados</strong> $\\tau = 1/\\sigma^2$. A verossimilhança em termos da média amostral $\\bar{x} = \\frac{1}{n}\\sum x_i$ é:</p>
        $$l(\\mu; x) \\propto \\exp\\left\\{ -\\frac{n\\tau}{2} (\\bar{x} - \\mu)^2 \\right\\}$$
        <p>Adotamos uma priori conjugada Normal para $\\mu$ com média inicial $\\mu_0$ e precisão inicial $\\tau_0 = 1/\\sigma_0^2$:</p>
        $$p(\\mu) \\propto \\exp\\left\\{ -\\frac{\\tau_0}{2} (\\mu - \\mu_0)^2 \\right\\}$$
        <p>Completando os quadrados no expoente da regra de Bayes:</p>
        $$p(\\mu \\mid x) \\propto \\exp\\left\\{ -\\frac{1}{2} \\left[ \\tau_0 (\\mu - \\mu_0)^2 + n\\tau (\\mu - \\bar{x})^2 \\right] \\right\\}$$
        <p>Desenvolvendo e reagrupando os termos quadráticos e lineares em $\\mu$, obtém-se:</p>
        $$\\mu \\mid x \\sim N(\\mu_1, \\, \\tau_1^{-1})$$
        <p>onde os parâmetros a posteriori satisfazem a seguinte regra aditiva de precisões:</p>
        $$\\tau_1 = \\tau_0 + n\\tau \\quad \\Longleftrightarrow \\quad \\frac{1}{\\sigma_1^2} = \\frac{1}{\\sigma_0^2} + \\frac{n}{\\sigma^2}$$
        $$\\mu_1 = \\frac{\\tau_0 \\mu_0 + n\\tau \\bar{x}}{\\tau_0 + n\\tau} = w \\, \\mu_0 + (1-w) \\, \\bar{x}, \\quad \\text{com } w = \\frac{\\tau_0}{\\tau_0 + n\\tau}$$

        <div class="callout callout-tip">
            <div class="callout-header">💡 A Elegância da Adição de Precisões</div>
            <p>Note como a incerteza se comporta: <strong>as precisões simplesmente se somam</strong>. Cada nova observação acrescenta uma quantidade de precisão igual a $\\tau = 1/\\sigma^2$ ao nosso estado de conhecimento. Se a priori for vaga ($\tau_0 \\to 0$), o peso $w \\to 0$, e a média a posteriori recai exatamente na média amostral $\\bar{x}$.</p>
        </div>

        <!-- Par 4: Normal com Média Conhecida e Variância Desconhecida -->
        <h3>4. Modelo Normal com Média Conhecida e Variância Desconhecida</h3>
        <p>Se $\\mu$ é conhecido e a precisão $\\phi = 1/\\sigma^2$ é desconhecida, a verossimilhança é:</p>
        $$l(\\phi; x) \\propto \\phi^{n/2} \\exp\\left\\{ -\\frac{\\phi}{2} \\sum_{i=1}^n (x_i - \\mu)^2 \\right\\}$$
        <p>Esta forma algébrica coincide exatamente com a densidade $\\text{Gama}(\\alpha, \\beta)$. Adotando uma priori $\\phi \\sim \\text{Gama}(\\alpha_0, \\beta_0)$:</p>
        $$\\phi \\mid x \\sim \\text{Gama}\\left( \\alpha_0 + \\frac{n}{2}, \\; \\beta_0 + \\frac{1}{2}\\sum_{i=1}^n (x_i - \\mu)^2 \\right)$$
        <p>Se expressarmos o modelo em termos da variância $\\sigma^2 = 1/\\phi$, a priori conjugada correspondente é a <strong>Inversa-Gama</strong>.</p>

        <!-- Par 5: Normal com Média e Variância Desconhecidas -->
        <h3>5. Modelo Normal com Ambos Desconhecidos: A Priori Conjunta Normal-Gama</h3>
        <p>Quando nem a média $\\mu$ nem a precisão $\\phi = \\sigma^{-2}$ são conhecidas, não podemos tratá-las como independentes a priori se quisermos conjugação estrita. A especificação conjugada padrão é a distribuição conjunta <strong>Normal-Gama</strong>:</p>
        $$\\mu \\mid \\phi \\sim N(\\mu_0, \\, (n_0 \\phi)^{-1}), \\quad \\phi \\sim \\text{Gama}(\\alpha_0, \\beta_0)$$
        <p>onde $n_0$ representa o número de observações virtuais associadas à média a priori. A densidade conjunta a priori é:</p>
        $$p(\\mu, \\phi) = p(\\mu \\mid \\phi) p(\\phi) \\propto \\phi^{1/2} \\exp\\left\\{ -\\frac{n_0 \\phi}{2}(\\mu - \\mu_0)^2 \\right\\} \\phi^{\\alpha_0-1} e^{-\\beta_0 \\phi}$$
        
        <p>Após observar a amostra $x_1, \\dots, x_n$ com média $\\bar{x}$ e soma de quadrados dos desvios $S = \\sum (x_i - \\bar{x})^2$, a distribuição a posteriori conjunta continua sendo Normal-Gama:</p>
        $$\\mu, \\phi \\mid x \\sim \\text{Normal-Gama}(\\mu_n, \\, n_n, \\, \\alpha_n, \\, \\beta_n)$$
        <p>com hiperparâmetros atualizados analiticamente por:</p>
        $$n_n = n_0 + n$$
        $$\\mu_n = \\frac{n_0 \\mu_0 + n \\bar{x}}{n_n}$$
        $$\\alpha_n = \\alpha_0 + \\frac{n}{2}$$
        $$\\beta_n = \\beta_0 + \\frac{1}{2}S + \\frac{n_0 n (\\bar{x} - \\mu_0)^2}{2 n_n}$$

        <div class="callout callout-thm">
            <div class="callout-header">⚙️ Marginais Analíticas: O Surgimento da $t$ de Student</div>
            <p>Integrando a precisão $\\phi$ na posteriori conjunta, obtém-se a <strong>distribuição a posteriori marginal da média $\\mu$</strong>, que é exatamente uma distribuição $t$ de Student:</p>
            $$\\mu \\mid x \\sim t_{2\\alpha_n}\\left( \\mu_n, \\; \\frac{\\beta_n}{\\alpha_n n_n} \\right)$$
            <p>E a marginal para a precisão é simplesmente:</p>
            $$\\phi \\mid x \\sim \\text{Gama}(\\alpha_n, \\beta_n)$$
        </div>

        <!-- O Caso de Duas Amostras e Behrens-Fisher -->
        <h3>6. O Caso de Duas Amostras e o Problema de Behrens-Fisher</h3>
        <p>Considere agora duas amostras normais independentes:</p>
        $$X_1, \\dots, X_{n_1} \\sim N(\\mu_1, \\sigma_1^2) \\quad \\text{e} \\quad Y_1, \\dots, Y_{n_2} \\sim N(\\mu_2, \\sigma_2^2)$$
        <p>O interesse principal reside na diferença entre as médias $\\delta = \\mu_1 - \\mu_2$.</p>
        <ul>
            <li><strong>Cenário Homocedástico ($\\sigma_1^2 = \\sigma_2^2 = \\sigma^2$):</strong> Adotando a priori de referência $p(\\mu_1, \\mu_2, \\sigma^2) \\propto 1/\\sigma^2$, a posteriori marginal da diferença segue exatamente uma distribuição $t$ de Student clássica com $n_1 + n_2 - 2$ graus de liberdade.</li>
            <li><strong>Cenário Heterocedástico ($\\sigma_1^2 \\neq \\sigma_2^2$ - O Problema de Behrens-Fisher):</strong> Na inferência clássica, a violação da igualdade de variâncias inviabiliza um teste $t$ exato, demandando aproximações assintóticas como a correção de Welch-Satterthwaite.</li>
        </ul>
        <p>Na inferência bayesiana, o problema de Behrens-Fisher é resolvido com absoluta naturalidade conceitual: as posteriores de $(\\mu_1, \\sigma_1^2)$ e $(\\mu_2, \\sigma_2^2)$ são calculadas de forma independente. A distribuição a posteriori marginal da diferença $\\delta = \\mu_1 - \\mu_2$ é a <strong>convolução exata de duas distribuições $t$ de Student independentes</strong>:</p>
        $$\\mu_1 \\mid x \\sim t_{n_1-1}\\left(\\bar{x}, \\frac{s_1^2}{n_1}\\right), \\quad \\mu_2 \\mid y \\sim t_{n_2-1}\\left(\\bar{y}, \\frac{s_2^2}{n_2}\\right)$$
        <p>Embora essa convolução não admita uma fórmula fechada simples em funções elementares (sendo conhecida como a <em>distribuição de Behrens-Fisher</em>), amostrar diretamente dessa distribuição no computador via simulação é imediato: basta sortear $N$ valores de $\\mu_1^{(i)}$, $N$ valores de $\\mu_2^{(i)}$ e subtraí-los $\\delta^{(i)} = \\mu_1^{(i)} - \\mu_2^{(i)}$, obtendo intervalos de credibilidade e probabilidades exatas sem qualquer aproximação ad-hoc!</p>

        <!-- Par 6: Dirichlet-Multinomial -->
        <h3>7. O Modelo Dirichlet-Multinomial</h3>
        <p>Para contagens multivariadas $\\mathbf{x} = (x_1, \\dots, x_k) \\sim \\text{Multinomial}(n, \\boldsymbol{\\theta})$, a verossimilhança é proporcional a $\\prod_{j=1}^k \\theta_j^{x_j}$. A priori conjugada no simplex unitário é $\\boldsymbol{\\theta} \\sim \\text{Dirichlet}(\\alpha_1, \\dots, \\alpha_k)$:</p>
        $$p(\\boldsymbol{\\theta}) \\propto \\prod_{j=1}^k \\theta_j^{\\alpha_j - 1}$$
        <p>Multiplicando na regra de Bayes, os expoentes se somam elemento a elemento:</p>
        $$p(\\boldsymbol{\\theta} \\mid \\mathbf{x}) \\propto \\prod_{j=1}^k \\theta_j^{(\\alpha_j + x_j) - 1} \\implies \\boldsymbol{\\theta} \\mid \\mathbf{x} \\sim \\text{Dirichlet}(\\alpha_1 + x_1, \\, \\dots, \\, \\alpha_k + x_k)$$
        <p>Os hiperparâmetros $\\alpha_j$ atuam como contagens prévias observadas para cada uma das $k$ categorias.</p>
    </section>
"""
