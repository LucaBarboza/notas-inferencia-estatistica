# -*- coding: utf-8 -*-
"""
Módulo 5: Computação Bayesiana e Métodos Aproximados (MCMC)
"""

def get_module5_html():
    return """
    <!-- ========================================== -->
    <!-- MÓDULO 5: COMPUTAÇÃO BAYESIANA E MCMC      -->
    <!-- ========================================== -->
    <section id="modulo5" class="module-chapter">
        <h1 class="module-title">
            <span class="module-num">Módulo 5</span>
            Computação Bayesiana e Métodos Estocásticos
        </h1>

        <div class="callout callout-tip">
            <div class="callout-header">💡 Sinopse Conceitual</div>
            <p>O Teorema de Bayes formula uma teoria inferencial unificada e elegante, mas sua aplicação em modelos realistas &mdash; multiparamétricos, hierárquicos ou não-lineares &mdash; enfrenta um obstáculo matemático intransponível: <strong>a constante de normalização e as marginais a posteriori envolvem integrais em dimensões elevadas sem solução analítica fechada</strong>. Métodos numéricos determinísticos (como Simpson ou quadraturas gaussianas) sucumbem à maldição da dimensionalidade. A revolução bayesiana contemporânea foi viabilizada pelo desenvolvimento de algoritmos estocásticos baseados em simulação: <em>Monte Carlo Simples</em>, <em>Amostragem por Importância</em> e, fundamentalmente, <strong>Monte Carlo via Cadeias de Markov (MCMC)</strong>, onde geramos trajetórias cujo comportamento de longo prazo converge para a distribuição a posteriori exata.</p>
        </div>

        <h2>5.1 O Desafio da Integração Numérica em Altas Dimensões</h2>
        <p>Praticamente todo objetivo na inferência bayesiana pode ser formalizado como o cálculo da esperança a posteriori de alguma função de interesse $g(\\boldsymbol{\\theta})$:</p>
        $$E[g(\\boldsymbol{\\theta}) \\mid x] = \\int_\\Theta g(\\boldsymbol{\\theta}) \\, p(\\boldsymbol{\\theta} \\mid x) \\, d\\boldsymbol{\\theta} = \\frac{\\int_\\Theta g(\\boldsymbol{\\theta}) \\, p(x \\mid \\boldsymbol{\\theta}) \\, p(\\boldsymbol{\\theta}) \\, d\\boldsymbol{\\theta}}{\\int_\\Theta p(x \\mid \\boldsymbol{\\theta}) \\, p(\\boldsymbol{\\theta}) \\, d\\boldsymbol{\\theta}}$$
        
        <p>Se o vetor $\\boldsymbol{\\theta}$ tem dimensão $d = 20$ e tentarmos usar uma regra de quadratura determinística simples dividindo cada eixo em apenas 10 pontos, precisaremos avaliar a verossimilhança em $10^{20}$ nós &mdash; o que exigiria séculos de processamento nos supercomputadores mais rápidos do planeta! É a célebre <strong>maldição da dimensionalidade</strong>.</p>

        <h2>5.2 Métodos de Monte Carlo sem Cadeias</h2>

        <h3>1. Monte Carlo Simples</h3>
        <p>Se tivermos um algoritmo capaz de gerar amostras independentes e identicamente distribuídas (i.i.d.) $\\boldsymbol{\\theta}^{(1)}, \\dots, \\boldsymbol{\\theta}^{(N)}$ diretamente da posteriori $p(\\boldsymbol{\\theta} \\mid x)$, a esperança teórica é aproximada pela média amostral empírica:</p>
        $$\\bar{g}_N = \\frac{1}{N} \\sum_{i=1}^N g(\\boldsymbol{\\theta}^{(i)})$$
        
        <p>Pela <strong>Lei Forte dos Grandes Números</strong>, $\\bar{g}_N \\xrightarrow{\\text{q.c.}} E[g(\\boldsymbol{\\theta}) \\mid x]$ conforme $N \\to \\infty$. Além disso, pelo <strong>Teorema Central do Limite</strong>, o <em>Erro Padrão de Monte Carlo</em> decresce a uma taxa estritamente universal de ordem $O(1/\\sqrt{N})$, <strong>independentemente da dimensão $d$ do espaço!</strong></p>
        $$MCSE = \\frac{s_g}{\\sqrt{N}}, \\quad \\text{onde } s_g^2 = \\frac{1}{N-1} \\sum_{i=1}^N (g(\\boldsymbol{\\theta}^{(i)}) - \\bar{g}_N)^2$$

        <h3>2. Amostragem por Importância (Importance Sampling)</h3>
        <p>Quando não é viável amostrar diretamente de $p(\\theta \\mid x)$, introduz-se uma <strong>densidade instrumental ou auxiliar</strong> $q(\\theta)$ cujo suporte contenha o de $p(\\theta \\mid x)$ e da qual sabemos gerar amostras facilmente. Reescrevemos a integral como:</p>
        $$E[g(\\theta) \\mid x] = \\int g(\\theta) \\frac{p(\\theta \\mid x)}{q(\\theta)} q(\\theta) d\\theta = E_q[g(\\theta) w(\\theta)]$$
        <p>onde $w(\\theta) = \\frac{p(\\theta \\mid x)}{q(\\theta)}$ é denominado <strong>peso de importância</strong>. Se a constante normalizadora de $p(\\theta \\mid x)$ for desconhecida ($p(\\theta \\mid x) = \\frac{q^*(\\theta)}{k}$), utilizamos os pesos normalizados:</p>
        $$\\hat{I}_{IS} = \\sum_{i=1}^N W_i \\, g(\\theta^{(i)}), \\quad \\text{com } W_i = \\frac{w(\\theta^{(i)})}{\\sum_{j=1}^N w(\\theta^{(j)})}$$

        <h3>3. Métodos de Reamostragem: Rejeição e SIR</h3>
        <ul>
            <li><strong>Método da Rejeição:</strong> Encontra-se uma constante $M > 0$ tal que a proposta majora o núcleo: $M q(\\theta) \\ge p(x \\mid \\theta) p(\\theta)$ para todo $\\theta$. Gera-se $\\theta^* \\sim q(\\theta)$ e $u \\sim U(0,1)$; aceita-se $\\theta^*$ se $u \\le \\frac{p(x \\mid \\theta^*) p(\\theta^*)}{M q(\\theta^*)}$. A taxa média de aceitação é $1/M$. Em altas dimensões, $M$ torna-se astronomicamente grande e a aceitação colapsa para zero.</li>
            <li><strong>Reamostragem Ponderada (Sampling-Importance-Resampling / SIR):</strong> Em vez de rejeitar pontos um a um, gera-se uma amostra preliminar de tamanho $M$ de $q(\\theta)$, calculam-se os pesos normalizados $W_i$ e, no terceiro passo, reamostram-se $N < M$ valores com probabilidades proporcionais a $W_i$. É a base do filtro de partículas e do bootstrap bayesiano.</li>
        </ul>

        <h2>5.3 Monte Carlo via Cadeias de Markov (MCMC)</h2>
        <p>Para contornar as falhas dos métodos anteriores em dimensões moderadas e altas, o MCMC constrói uma <strong>cadeia de Markov ergódica</strong> cujo espaço de estados é $\\Theta$ e cuja <strong>distribuição estacionária invariante</strong> coincide exatamente com a distribuição a posteriori alvo $\\pi(\\theta) = p(\\theta \\mid x)$.</p>

        <div class="callout callout-thm">
            <div class="callout-header">⚙️ A Condição de Balanço Detalhado</div>
            <p>Seja $T(\\theta \\to \\theta')$ a densidade de transição de mover do estado $\\theta$ para $\\theta'$. A distribuição $\\pi(\\theta)$ é garantidamente a distribuição estacionária da cadeia se a transição satisfizer a condição de <strong>balanço detalhado</strong> (reversibilidade microscópica):</p>
            $$\\pi(\\theta) \\, T(\\theta \\to \\theta') = \\pi(\\theta') \\, T(\\theta' \\to \\theta) \\quad \\forall \\, \\theta, \\theta' \\in \\Theta$$
        </div>

        <h3>1. O Algoritmo de Metropolis-Hastings</h3>
        <p>O algoritmo proposto por Nicholas Metropolis (1953) e generalizado por W. K. Hastings (1970) divide a transição em duas etapas: um mecanismo de <strong>proposta</strong> $q(\\theta' \\mid \\theta)$ seguido de uma decisão probabilística de <strong>aceitação</strong> com probabilidade $\\alpha(\\theta, \\theta')$.</p>

        <div class="callout callout-def">
            <div class="callout-header">📘 Algoritmo de Metropolis-Hastings</div>
            <p>Estando no estado atual $\\theta^{(t)}$ na iteração $t$:</p>
            <ol>
                <li>Gere um candidato $\\theta'$ a partir da distribuição proposta $q(\\theta' \\mid \\theta^{(t)})$.</li>
                <li>Calcule a <strong>razão de aceitação de Metropolis-Hastings</strong>:
                    $$\\alpha(\\theta^{(t)}, \\theta') = \\min\\left( 1, \\; \\frac{\\pi(\\theta') \\, q(\\theta^{(t)} \\mid \\theta')}{\\pi(\\theta^{(t)}) \\, q(\\theta' \\mid \\theta^{(t)})} \\right) = \\min\\left( 1, \\; \\frac{p(x \\mid \\theta') \\, p(\\theta') \\, q(\\theta^{(t)} \\mid \\theta')}{p(x \\mid \\theta^{(t)}) \\, p(\\theta^{(t)}) \\, q(\\theta' \\mid \\theta^{(t)})} \\right)$$
                </li>
                <li>Gere $u \\sim U(0, 1)$. Se $u \\le \\alpha(\\theta^{(t)}, \\theta')$, <strong>aceite</strong> e faça $\\theta^{(t+1)} = \\theta'$. Caso contrário, <strong>rejeite</strong> e repita o estado anterior: $\\theta^{(t+1)} = \\theta^{(t)}$.</li>
            </ol>
        </div>

        <details class="proof">
            <summary>🔍 Demonstração Matemática: O Metropolis-Hastings Satisfaz o Balanço Detalhado</summary>
            <div class="proof-body">
                <p>Para $\\theta \\neq \\theta'$, a densidade de transição efetiva é $T(\\theta \\to \\theta') = q(\\theta' \\mid \\theta) \\, \\alpha(\\theta, \\theta')$.</p>
                <p>Desejamos provar que $\\pi(\\theta) q(\\theta' \\mid \\theta) \\alpha(\\theta, \\theta') = \\pi(\\theta') q(\\theta \\mid \\theta') \\alpha(\\theta', \\theta)$.</p>
                <ol>
                    <li>Sem perda de generalidade, suponha que a razão seja menor ou igual a 1, isto é:
                        $$\\frac{\\pi(\\theta') q(\\theta \\mid \\theta')}{\\pi(\\theta) q(\\theta' \\mid \\theta)} \\le 1$$
                    </li>
                    <li>Neste caso, pela definição do mínimo:
                        $$\\alpha(\\theta, \\theta') = \\frac{\\pi(\\theta') q(\\theta \\mid \\theta')}{\\pi(\\theta) q(\\theta' \\mid \\theta)}$$
                    </li>
                    <li>Por simetria, na direção inversa a razão será maior ou igual a 1, logo:
                        $$\\alpha(\\theta', \\theta) = 1$$
                    </li>
                    <li>Avaliando o lado esquerdo do balanço detalhado:
                        $$\\pi(\\theta) T(\\theta \\to \\theta') = \\pi(\\theta) q(\\theta' \\mid \\theta) \\left[ \\frac{\\pi(\\theta') q(\\theta \\mid \\theta')}{\\pi(\\theta) q(\\theta' \\mid \\theta)} \\right] = \\pi(\\theta') q(\\theta \\mid \\theta')$$
                    </li>
                    <li>Avaliando o lado direito:
                        $$\\pi(\\theta') T(\\theta' \\to \\theta) = \\pi(\\theta') q(\\theta \\mid \\theta') \\alpha(\\theta', \\theta) = \\pi(\\theta') q(\\theta \\mid \\theta') \\cdot 1 = \\pi(\\theta') q(\\theta \\mid \\theta')$$
                    </li>
                </ol>
                <p><strong>Conclusão:</strong> Os dois lados são identicamente iguais. Portanto, o balanço detalhado é rigorosamente satisfeito, o que garante matematicamente que a distribuição estacionária da cadeia é a distribuição a posteriori alvo $\\pi(\\theta)$.</p>
            </div>
        </details>

        <h3>2. O Amostrador de Gibbs</h3>
        <p>Proposto por Geman & Geman (1984) e introduzido na estatística por Gelfand & Smith (1990), o <strong>Amostrador de Gibbs</strong> é um caso particular extraordinário de Metropolis-Hastings aplicável quando o vetor de parâmetros é multidimensional $\\boldsymbol{\\theta} = (\\theta_1, \\dots, \\theta_d)'$ e conhecemos a forma analítica das <strong>distribuições condicionais completas (*full conditionals*)</strong>:</p>
        $$\\pi(\\theta_j \\mid \\boldsymbol{\\theta}_{-j}, x) = p(\\theta_j \\mid \\theta_1, \\dots, \\theta_{j-1}, \\theta_{j+1}, \\dots, \\theta_d, x)$$
        
        <p>Em cada iteração $t+1$, atualiza-se uma coordenada por vez utilizando os valores mais recentes disponíveis:</p>
        $$\\theta_1^{(t+1)} \\sim \\pi(\\theta_1 \\mid \\theta_2^{(t)}, \\theta_3^{(t)}, \\dots, \\theta_d^{(t)}, x)$$
        $$\\theta_2^{(t+1)} \\sim \\pi(\\theta_2 \\mid \\theta_1^{(t+1)}, \\theta_3^{(t)}, \\dots, \\theta_d^{(t)}, x)$$
        $$\\vdots$$
        $$\\theta_d^{(t+1)} \\sim \\pi(\\theta_d \\mid \\theta_1^{(t+1)}, \\theta_2^{(t+1)}, \\dots, \\theta_{d-1}^{(t+1)}, x)$$
        
        <p>Como a distribuição proposta é exatamente a condicional completa, ao substituir na fórmula de Metropolis-Hastings verifica-se que <strong>a probabilidade de aceitação $\\alpha$ é identicamente igual a 100%</strong>: todo candidato gerado no Amostrador de Gibbs é aceito automaticamente!</p>

        <h3>3. MCMC de Dimensão Variável: Reversible Jump MCMC (RJMCMC)</h3>
        <p>Em problemas de seleção e comparação de modelos concorrentes $\\mathcal{M}_1, \\dots, \\mathcal{M}_K$, cada modelo pode ter um número diferente de parâmetros (por exemplo, comparar uma regressão com 2 preditores contra uma com 5 preditores). Peter Green (1995) formulou o <strong>RJMCMC</strong> para permitir que a cadeia salte entre subespaços de dimensões desiguais.</p>
        <p>Para saltar de um modelo de dimensão menor $n_k$ para um maior $n_{k'}$, gera-se um vetor de variáveis auxiliares $u \\sim q(u)$ com dimensão $n_{k'} - n_k$, e define-se uma bijeção determinística diferenciável $\\theta' = g(\\theta, u)$. A razão de aceitação incorpora o <strong>determinante Jacobiano</strong> da transformação para garantir a reversibilidade:</p>
        $$\\alpha = \\min\\left(1, \\; \\frac{\\pi(k', \\theta') \\, r_{k', k}}{\\pi(k, \\theta) \\, r_{k, k'} \\, q(u)} \\left| \\det \\frac{\\partial g(\\theta, u)}{\\partial(\\theta, u)} \\right| \\right)$$

        <h2 id="lab-mcmc">5.4 Laboratório Prático: Implementações em R e Python</h2>
        <p>Abaixo apresentamos snippets comparativos autocontidos para rodar e visualizar o funcionamento dos algoritmos de simulação.</p>

        <h3>Exemplo 1: Metropolis-Hastings para uma Distribuição Bimodal</h3>
        <div class="code-tabs" id="code-tabs-mh">
            <div class="tab-nav">
                <button class="tab-btn active" data-tab="r" onclick="switchTab('code-tabs-mh', 'r')">R Script</button>
                <button class="tab-btn" data-tab="py" onclick="switchTab('code-tabs-mh', 'py')">Python (NumPy / Matplotlib)</button>
            </div>
            <div class="tab-pane active" data-lang-pane="r" data-lang="Código em R">
<pre><code># Metropolis-Hastings para Mistura Bimodal em R
set.seed(42)
target_log_density &lt;- function(theta) {
  # Alvo: Mistura de 2 Normais 0.3*N(-3, 1) + 0.7*N(3, 1)
  log(0.3 * dnorm(theta, -3, 1) + 0.7 * dnorm(theta, 3, 1))
}

N &lt;- 10000
chain &lt;- numeric(N)
chain[1] &lt;- 0  # Ponto inicial
sigma_prop &lt;- 1.5
accepted &lt;- 0

for (t in 1:(N - 1)) {
  current &lt;- chain[t]
  candidate &lt;- rnorm(1, mean = current, sd = sigma_prop)
  
  log_alpha &lt;- target_log_density(candidate) - target_log_density(current)
  if (log(runif(1)) &lt; log_alpha) {
    chain[t + 1] &lt;- candidate
    accepted &lt;- accepted + 1
  } else {
    chain[t + 1] &lt;- current
  }
}

cat("Taxa de Aceitação:", round(accepted / N, 3), "\\n")
par(mfrow = c(1, 2))
plot(chain[1:1000], type = "l", col = "#2563eb", main = "Traceplot (1000 iter)", ylab = expression(theta))
hist(chain[2000:N], breaks = 40, prob = TRUE, col = "#e0f2fe", border = "#0369a1", main = "Posteriori Estimada")
curve(0.3 * dnorm(x, -3, 1) + 0.7 * dnorm(x, 3, 1), add = TRUE, col = "#ea580c", lwd = 2)</code></pre>
            </div>
            <div class="tab-pane" data-lang-pane="py" data-lang="Código em Python">
<pre><code># Metropolis-Hastings para Mistura Bimodal em Python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def target_density(theta):
    # Alvo: 0.3*N(-3, 1) + 0.7*N(3, 1)
    p1 = 0.3 * np.exp(-0.5 * (theta + 3)**2) / np.sqrt(2 * np.pi)
    p2 = 0.7 * np.exp(-0.5 * (theta - 3)**2) / np.sqrt(2 * np.pi)
    return p1 + p2

N = 10000
chain = np.zeros(N)
sigma_prop = 1.5
accepted = 0

for t in range(N - 1):
    current = chain[t]
    candidate = np.random.normal(current, sigma_prop)
    
    alpha = target_density(candidate) / target_density(current)
    if np.random.uniform(0, 1) &lt; alpha:
        chain[t + 1] = candidate
        accepted += 1
    else:
        chain[t + 1] = current

print(f"Taxa de Aceitação: {accepted / N:.3f}")

# Visualização
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.plot(chain[:1000], color='#2563eb', lw=0.8)
ax1.set_title("Traceplot (Primeiras 1000 iterações)")
ax2.hist(chain[2000:], bins=40, density=True, color='#bae6fd', edgecolor='#0284c7')
x = np.linspace(-7, 7, 200)
ax2.plot(x, target_density(x), color='#ea580c', lw=2, label="Densidade Exata")
ax2.set_title("Histograma da Cadeia vs Alvo Teórico")
ax2.legend()
plt.tight_layout()
plt.show()</code></pre>
            </div>
        </div>

        <h3>Exemplo 2: Amostrador de Gibbs para Normal Bivariada</h3>
        <div class="code-tabs" id="code-tabs-gibbs">
            <div class="tab-nav">
                <button class="tab-btn active" data-tab="r" onclick="switchTab('code-tabs-gibbs', 'r')">R Script</button>
                <button class="tab-btn" data-tab="py" onclick="switchTab('code-tabs-gibbs', 'py')">Python</button>
            </div>
            <div class="tab-pane active" data-lang-pane="r" data-lang="Código em R">
<pre><code># Amostrador de Gibbs para Normal Bivariada Correlacionada em R
# Alvo: (X, Y) ~ N_2(0, [1, rho; rho, 1])
# Condicionais: X|Y ~ N(rho*Y, 1 - rho^2) e Y|X ~ N(rho*X, 1 - rho^2)
set.seed(42)
rho &lt;- 0.8
N &lt;- 5000
cond_sd &lt;- sqrt(1 - rho^2)

chain_x &lt;- numeric(N)
chain_y &lt;- numeric(N)
chain_x[1] &lt;- -4
chain_y[1] &lt;- 4

for (t in 1:(N - 1)) {
  # 1. Atualizar X dado o Y mais recente
  chain_x[t + 1] &lt;- rnorm(1, mean = rho * chain_y[t], sd = cond_sd)
  # 2. Atualizar Y dado o X recém-gerado
  chain_y[t + 1] &lt;- rnorm(1, mean = rho * chain_x[t + 1], sd = cond_sd)
}

plot(chain_x[100:1000], chain_y[100:1000], pch = 16, cex = 0.5, col = rgb(0.1, 0.4, 0.9, 0.4),
     main = "Amostras Conjuntas de Gibbs (rho = 0.8)", xlab = expression(theta[1]), ylab = expression(theta[2]))</code></pre>
            </div>
            <div class="tab-pane" data-lang-pane="py" data-lang="Código em Python">
<pre><code># Amostrador de Gibbs para Normal Bivariada em Python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
rho = 0.8
N = 5000
cond_sd = np.sqrt(1 - rho**2)

x = np.zeros(N)
y = np.zeros(N)
x[0], y[0] = -4.0, 4.0

for t in range(N - 1):
    # 1. Atualiza X condicionado no Y atual
    x[t + 1] = np.random.normal(rho * y[t], cond_sd)
    # 2. Atualiza Y condicionado no X atualizado
    y[t + 1] = np.random.normal(rho * x[t + 1], cond_sd)

plt.figure(figsize=(6, 6))
plt.scatter(x[200:], y[200:], alpha=0.3, s=8, color='#0284c7')
plt.title(f"Amostras do Amostrador de Gibbs (ρ = {rho})")
plt.xlabel("θ₁")
plt.ylabel("θ₂")
plt.grid(True, alpha=0.3)
plt.show()</code></pre>
            </div>
        </div>

        <h2>5.5 Diagnósticos Rigorosos de Convergência</h2>
        <p>Como o MCMC produz amostras correlacionadas geradas de forma sequencial, é mandatório realizar diagnósticos formais antes de confiar nas estimativas:</p>

        <div class="callout callout-def">
            <div class="callout-header">📘 1. Período de Aquecimento (Burn-in)</div>
            <p>O ponto de partida arbitrário $\\theta^{(0)}$ pode estar em uma região de probabilidade baixíssima. O <strong>burn-in</strong> consiste em descartar as primeiras $B$ iterações da cadeia (comumente 10% a 50%) para assegurar que a amostragem seja coletada apenas após a cadeia ter atingido sua distribuição de equilíbrio estacionária.</p>
        </div>

        <div class="callout callout-def">
            <div class="callout-header">📘 2. Autocorrelação, Desbaste (Thinning) e Tamanho Efetivo ($ESS$)</div>
            <p>Devido à natureza da cadeia, $\\theta^{(t)}$ e $\\theta^{(t+k)}$ possuem autocorrelação positiva $\\rho_k$. O <strong>Tamanho Amostral Efetivo ($ESS$)</strong> quantifica quantas observações verdadeiramente independentes a cadeia correlacionada equivale:</p>
            $$ESS = \\frac{N}{1 + 2 \\sum_{k=1}^\\infty \\rho_k}$$
            <p>Se o $ESS$ for muito inferior a $N$, recomenda-se aplicar <strong>desbaste (*thinning*)</strong>, guardando apenas a cada $k$-ésima observação (ex: guardar de 5 em 5 passos) para economizar memória e reduzir a dependência serial.</p>
        </div>

        <div class="callout callout-thm">
            <div class="callout-header">⚙️ 3. Fator de Redução de Escala Potencial de Gelman-Rubin ($\\hat{R}$)</div>
            <p>O diagnóstico padrão-ouro consiste em inicializar $M \\ge 3$ cadeias independentes a partir de pontos amplamente dispersos no espaço e comparar a <strong>variância intra-cadeia ($W$)</strong> com a <strong>variância entre-cadeias ($B$)</strong>:</p>
            $$W = \\frac{1}{M} \\sum_{m=1}^M s_m^2, \\quad \\frac{B}{N} = \\frac{1}{M-1} \\sum_{m=1}^M (\\bar{\\theta}_m - \\bar{\\bar{\\theta}})^2$$
            <p>A variância marginal estimada combinada é $\\widehat{\\Var}(\\theta) = \\frac{N-1}{N} W + \\frac{1}{N} B$. O índice de Gelman-Rubin é dado por:</p>
            $$\\hat{R} = \\sqrt{ \\frac{\\widehat{\\Var}(\\theta)}{W} }$$
            <p><strong>Critério de Parada:</strong> Se $\\hat{R} \\approx 1.0$ (universalmente aceito se $\\hat{R} < 1.05$), todas as cadeias convergiram para a mesma região estacionária e estão bem misturadas. Se $\\hat{R} > 1.1$, as cadeias ainda estão explorando regiões distintas e as simulações devem ser continuadas.</p>
        </div>
    </section>
"""
