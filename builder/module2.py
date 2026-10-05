# -*- coding: utf-8 -*-
"""
Módulo 2: Distribuições a Priori e a Posteriori (Teorema de Bayes e Preditiva)
"""

def get_module2_html():
    return """
    <!-- ========================================== -->
    <!-- MÓDULO 2: PRIORI, POSTERIORI E PREDITIVA   -->
    <!-- ========================================== -->
    <section id="modulo2" class="module-chapter">
        <h1 class="module-title">
            <span class="module-num">Módulo 2</span>
            Distribuições a Priori, a Posteriori e Preditivas
        </h1>

        <div class="callout callout-tip">
            <div class="callout-header">💡 Sinopse Conceitual</div>
            <p>O coração operacional da inferência bayesiana é o processo contínuo de aprendizado via atualização de evidências. A distribuição a priori $p(\\theta)$ sintetiza nosso conhecimento ou incerteza inicial antes de olhar para a amostra. Uma vez observados os dados $x$, a função de verossimilhança $l(\\theta; x) = p(x \\mid \\theta)$ atua como um operador multiplicativo de transmissão de informação. Por meio do Teorema de Bayes, combinamos ambas as fontes na distribuição a posteriori $p(\\theta \\mid x)$. Quando não dispomos de opiniões sólidas a priori, recorremos à teoria das prioris objetivas de Harold Jeffreys, que garante coerência matemática independentemente da escala de parametrização adotada.</p>
        </div>

        <h2>2.1 O Teorema de Bayes e a Mecânica do Aprendizado</h2>
        <p>A expressão matemática da atualização bayesiana decorre diretamente da definição axiomática de probabilidade condicional de Kolmogorov. Para um espaço contínuo de parâmetros $\\Theta$ e dados $x$:</p>

        <div class="callout callout-def">
            <div class="callout-header">📘 Teorema de Bayes (Formulação Contínua)</div>
            $$p(\\theta \\mid x) = \\frac{p(x, \\theta)}{p(x)} = \\frac{p(x \\mid \\theta) \\, p(\\theta)}{\\int_\\Theta p(x \\mid \\theta) \\, p(\\theta) \\, d\\theta}$$
        </div>

        <p>Esta equação divide-se em quatro pilares estruturais:</p>
        <ol>
            <li><strong>Distribuição a Priori $p(\\theta)$:</strong> Representa a incerteza probabilística sobre o vetor de parâmetros $\\theta$ antes da observação da amostra atual.</li>
            <li><strong>Verossimilhança $l(\\theta; x) = p(x \\mid \\theta)$:</strong> A probabilidade/densidade com que o modelo proposto geraria os dados observados $x$ para cada valor possível de $\\theta$.</li>
            <li><strong>Constante Normalizadora (Evidência Marginal dos Dados) $p(x)$:</strong>
                $$p(x) = \\int_\\Theta p(x \\mid \\theta) \\, p(\\theta) \\, d\\theta = E_\\theta[p(x \\mid \\theta)]$$
                Trata-se de uma média ponderada da verossimilhança ponderada pela distribuição a priori. Ela não depende de $\\theta$, atuando estritamente como um fator de escala para assegurar que a integral da posteriori sobre todo o espaço $\\Theta$ seja unitária: $\\int_\\Theta p(\\theta \\mid x) d\\theta = 1$.
            </li>
            <li><strong>Distribuição a Posteriori $p(\\theta \\mid x)$:</strong> A distribuição de probabilidade atualizada sobre $\\theta$, condicionada aos dados efetivamente observados. Resume todo o conhecimento disponível após o experimento.</li>
        </ol>

        <h3>A Forma Proporcional</h3>
        <p>Como a evidência $p(x)$ é uma constante fixada após a coleta dos dados e não envolve o parâmetro $\\theta$, a relação bayesiana é frequentemente expressa na forma proporcional:</p>
        $$p(\\theta \\mid x) \\propto p(x \\mid \\theta) \\, p(\\theta) \\quad \\Longleftrightarrow \\quad \\text{Posteriori} \\propto \\text{Verossimilhança} \\times \\text{Priori}$$
        
        <p>Em muitas deduções analíticas, basta trabalhar com o <em>núcleo</em> da posteriori (a expressão funcional em termos de $\\theta$, descartando fatores puramente multiplicativos em $x$) e reconhecer a qual família de distribuição conhecida esse núcleo pertence para deduzir sua constante normalizadora sem necessidade de resolver integrais complexas.</p>

        <h3>Atualização Sequencial do Conhecimento</h3>
        <p>Uma das propriedades mais elegantes do método bayesiano é que ele é um <strong>mecanismo natural de aprendizado iterativo</strong>: o que hoje é nossa posteriori torna-se automaticamente a priori para a próxima coleta de dados.</p>

        <details class="proof">
            <summary>🔍 Demonstração Matemática: Coerência da Atualização Sequencial</summary>
            <div class="proof-body">
                <p>Suponha que os dados sejam coletados em dois lotes independentes condicionados a $\\theta$: $x = (x_1, x_2)$, com $p(x_1, x_2 \\mid \\theta) = p(x_1 \\mid \\theta) p(x_2 \\mid \\theta)$.</p>
                <p><strong>Cenário A (Processamento em Lote Único):</strong></p>
                $$p(\\theta \\mid x_1, x_2) \\propto p(x_1, x_2 \\mid \\theta) p(\\theta) = p(x_1 \\mid \\theta) p(x_2 \\mid \\theta) p(\\theta)$$
                <p><strong>Cenário B (Processamento Sequencial):</strong></p>
                <ol>
                    <li>Após observar $x_1$, atualizamos a priori $p(\\theta)$ para a primeira posteriori:
                        $$p(\\theta \\mid x_1) = \\frac{p(x_1 \\mid \\theta) p(\\theta)}{p(x_1)}$$
                    </li>
                    <li>Ao coletar $x_2$, adotamos $p(\\theta \\mid x_1)$ como nossa nova priori. A nova posteriori resultante é:
                        $$p(\\theta \\mid x_1, x_2) = \\frac{p(x_2 \\mid \\theta) \\, p(\\theta \\mid x_1)}{p(x_2 \\mid x_1)} = \\frac{p(x_2 \\mid \\theta) \\left[ \\frac{p(x_1 \\mid \\theta) p(\\theta)}{p(x_1)} \\right]}{p(x_2 \\mid x_1)}$$
                    </li>
                    <li>Lembrando que pela regra do produto $p(x_1) p(x_2 \\mid x_1) = p(x_1, x_2)$, substituímos no denominador:
                        $$p(\\theta \\mid x_1, x_2) = \\frac{p(x_1 \\mid \\theta) p(x_2 \\mid \\theta) p(\\theta)}{p(x_1, x_2)}$$
                    </li>
                </ol>
                <p><strong>Conclusão:</strong> Os dois procedimentos produzem matematicamente a mesmíssima distribuição a posteriori final. Aprender em lote ou dado a dado preserva a integridade epistêmica global.</p>
            </div>
        </details>

        <h2>2.2 Distribuições Preditivas</h2>
        <p>Na ciência empírica, parâmetros $\\theta$ costumam ser constructos teóricos inobserváveis (uma taxa de falha intrínseca, a média populacional de glicose, a probabilidade subjacente de chuva). O que nós efetivamente observamos no mundo real são <strong>novas realizações amostrais</strong> $Y$. A inferência bayesiana trata previsões integrando sobre a incerteza do parâmetro.</p>

        <h3>1. Distribuição Preditiva a Priori</h3>
        <p>A <strong>distribuição preditiva a priori</strong> $p(x)$ descreve que tipo de dados devemos esperar observar antes de coletar qualquer amostra, considerando apenas o conhecimento inicial modelado na priori:</p>
        $$p(x) = \\int_\\Theta p(x \\mid \\theta) \\, p(\\theta) \\, d\\theta = E_\\theta[p(X \\mid \\theta)]$$
        <p>Ela coincide exatamente com a constante normalizadora do Teorema de Bayes e é amplamente utilizada na <em>checagem preditiva a priori</em> (para checar se as crenças iniciais geram dados fisicamente razoáveis) e no cálculo de evidências para o Fator de Bayes.</p>

        <h3>2. Distribuição Preditiva a Posteriori</h3>
        <p>Considere agora que já observamos os dados $x$ e desejamos prever uma nova observação futura $Y$. Sob a premissa de <strong>independência condicional</strong> (isto é, conhecendo o parâmetro verdadeiro $\\theta$, os dados futuros $Y$ são independentes dos dados passados $X$, ou seja, $Y \\perp X \\mid \\theta$), a <strong>distribuição preditiva a posteriori</strong> $p(y \\mid x)$ é obtida integrando a densidade do novo dado ponderada pela posteriori de $\\theta$:</p>

        <div class="callout callout-def">
            <div class="callout-header">📘 Distribuição Preditiva a Posteriori</div>
            $$p(y \\mid x) = \\int_\\Theta p(y, \\theta \\mid x) \\, d\\theta = \\int_\\Theta p(y \\mid \\theta, x) \\, p(\\theta \\mid x) \\, d\\theta = \\int_\\Theta p(y \\mid \\theta) \\, p(\\theta \\mid x) \\, d\\theta$$
            $$p(y \\mid x) = E_{\\theta \\mid x}[p(Y \\mid \\theta)]$$
        </div>

        <p>Esta fórmula possui um significado estatístico profundo: a previsão bayesiana para $Y$ <strong>não é calculada simplesmente plugando um estimador pontual</strong> $\\hat{\\theta}$ em $p(y \\mid \\hat{\\theta})$ (o que subestimaria drasticamente a incerteza do sistema). Ela propaga adequadamente tanto a variabilidade aleatória inerente do processo gerador $p(y \\mid \\theta)$ quanto a incerteza epistêmica remanescente sobre o parâmetro $p(\\theta \\mid x)$.</p>

        <h2>2.3 Classificação e Estrutura das Prioris</h2>

        <h3>1. Prioris Próprias versus Impróprias</h3>
        <ul>
            <li><strong>Priori Própria:</strong> É uma função densidade de probabilidade legítima, cuja integral sobre todo o suporte $\\Theta$ converge rigorosamente para 1:
                $$\\int_\\Theta p(\\theta) \\, d\\theta = 1$$
            </li>
            <li><strong>Priori Imprópria:</strong> Uma função não negativa cuja integral sobre o suporte diverge ($+\\infty$):
                $$\\int_\\Theta p(\\theta) \\, d\\theta = \\infty$$
                Exemplo: $p(\\theta) = c > 0$ para todo $\\theta \\in (-\\infty, \\infty)$.
            </li>
        </ul>

        <div class="callout callout-warn">
            <div class="callout-header">⚠️ Cuidado Obrigatório com Prioris Impróprias</div>
            <p>O uso de uma priori imprópria $p(\\theta)$ <strong>só é estatisticamente aceitável</strong> se a integral da verossimilhança combinada for finita, isto é:</p>
            $$p(x) = \\int_\\Theta p(x \\mid \\theta) \\, p(\\theta) \\, d\\theta < \\infty$$
            <p>Se essa integral convergir, a posteriori resultante $p(\\theta \\mid x) = \\frac{p(x \\mid \\theta) p(\\theta)}{p(x)}$ será uma <strong>distribuição de probabilidade própria e válida</strong>. Se divergir, a inferência será completamente inválida e colapsará.</p>
        </div>

        <h3>2. Grau de Informatividade: Informativas, Vagas e Objetivas</h3>
        <ul>
            <li><strong>Prioris Informativas:</strong> Expressam conhecimento substancial prévio sobre $\\theta$, seja advindo de estudos clínicos anteriores, literatura consolidada ou elicitação de especialistas. Possuem variância pequena e hiperparâmetros firmemente ancorados.</li>
            <li><strong>Prioris Moderadamente Informativas (ou Regularizadoras):</strong> Concentram massa de probabilidade em ordens de grandeza fisicamente plausíveis, evitando que o modelo explore valores absurdos, mas sem dominar a influência dos dados reais.</li>
            <li><strong>Prioris Não Informativas (Vagas / de Referência):</strong> Têm o propósito de permitir que a evidência amostral domine completamente a inferência ("deixar os dados falarem por si mesmos"). Possuem grande dispersão (ex: $N(0, 10^4)$).</li>
        </ul>

        <h3>A Priori Uniforme de Bayes-Laplace e o Problema da Reparametrização</h3>
        <p>A primeira tentativa intuitiva de expressar completa ignorância sobre um parâmetro contínuo $\\theta$ foi proposta por Thomas Bayes e Pierre-Simon Laplace através do <em>Princípio da Razão Insuficiente</em>: se não há motivo para favorecer nenhum valor, atribui-se densidade constante uniforme:</p>
        $$p(\\theta) \\propto c$$
        
        <p>Embora pareça uma escolha neutra, ela sofre de um grave calcanhar de Aquiles: a <strong>falta de invariância sob transformações monótonas</strong>. Se um pesquisador modela a probabilidade de cara $\\theta \\sim U(0,1)$, um segundo pesquisador interessado nas <em>odds</em> $\\phi = \\frac{\\theta}{1-\\theta}$ (ou no logit) descobrirá, aplicando o teorema de transformação de variáveis, que sua priori implícita para $\\phi$ é:</p>
        $$p(\\phi) = p(\\theta(\\phi)) \\left| \\frac{d\\theta}{d\\phi} \\right| = 1 \\cdot \\frac{1}{(1+\\phi)^2}$$
        <p>Isto é, o segundo pesquisador não está mais atribuindo uma priori uniforme a $\\phi$, mas sim uma distribuição estritamente enviesada em direção a valores pequenos. A "ignorância" não se preservou na mudança de coordenadas!</p>

        <h2 id="priori-jeffreys">2.4 A Priori Não Informativa de Jeffreys</h2>
        <p>Para solucionar de forma definitiva o problema da dependência de parametrização, o geofísico e estatístico britânico <strong>Sir Harold Jeffreys</strong> (1961) formulou uma regra objetiva fundamentada na geometria da informação da verossimilhança.</p>

        <div class="callout callout-def">
            <div class="callout-header">📘 A Priori de Jeffreys</div>
            <p>Seja $I(\\theta)$ a <strong>Informação de Fisher esperada</strong> para o parâmetro escalar $\\theta$, definida por:</p>
            $$I(\\theta) = - E_{X \\mid \\theta}\\left[ \\frac{\\partial^2 \\log p(X \\mid \\theta)}{\\partial \\theta^2} \\right] = E_{X \\mid \\theta}\\left[ \\left( \\frac{\\partial \\log p(X \\mid \\theta)}{\\partial \\theta} \\right)^2 \\right]$$
            <p>A <strong>distribuição a priori de Jeffreys</strong> para $\\theta$ é definida como sendo proporcional à raiz quadrada da Informação de Fisher:</p>
            $$p(\\theta) \\propto \\sqrt{I(\\theta)}$$
            <p>No caso de um vetor de parâmetros $\\boldsymbol{\\theta} = (\\theta_1, \\dots, \\theta_p)'$, a priori é proporcional à raiz quadrada do determinante da Matriz de Informação de Fisher:</p>
            $$p(\\boldsymbol{\\theta}) \\propto \\sqrt{\\det \\mathbf{I}(\\boldsymbol{\\theta})}$$
        </div>

        <details class="proof">
            <summary>🔍 Demonstração Matemática: Invariância de Jeffreys sob Reparametrização 1-a-1</summary>
            <div class="proof-body">
                <p>Considere uma transformação bijetora monótona diferenciável $\\phi = g(\\theta)$. Pela regra da cadeia para derivadas de log-verossimilhança:</p>
                $$\\frac{\\partial \\log p(x \\mid \\phi)}{\\partial \\phi} = \\frac{\\partial \\log p(x \\mid \\theta)}{\\partial \\theta} \\frac{d\\theta}{d\\phi}$$
                <p>Elevando ao quadrado e aplicando a esperança com relação aos dados $X$:</p>
                $$I(\\phi) = E\\left[ \\left(\\frac{\\partial \\log p(x \\mid \\phi)}{\\partial \\phi}\\right)^2 \\right] = E\\left[ \\left(\\frac{\\partial \\log p(x \\mid \\theta)}{\\partial \\theta}\\right)^2 \\right] \\left( \\frac{d\\theta}{d\\phi} \\right)^2 = I(\\theta) \\left( \\frac{d\\theta}{d\\phi} \\right)^2$$
                <p>Extraindo a raiz quadrada em ambos os lados:</p>
                $$\\sqrt{I(\\phi)} = \\sqrt{I(\\theta)} \\left| \\frac{d\\theta}{d\\phi} \\right|$$
                <p>Se adotarmos a regra de Jeffreys para $\\phi$, temos $p_\\phi(\\phi) \\propto \\sqrt{I(\\phi)}$. Substituindo a relação acima:</p>
                $$p_\\phi(\\phi) \\propto \\sqrt{I(\\theta)} \\left| \\frac{d\\theta}{d\\phi} \\right| = p_\\theta(\\theta) \\left| \\frac{d\\theta}{d\\phi} \\right|$$
                <p><strong>Conclusão:</strong> Esta é exatamente a fórmula da transformação de variáveis para densidades de probabilidade! Portanto, a priori de Jeffreys calculada diretamente sobre $\\phi$ é formalmente idêntica à priori calculada sobre $\\theta$ transformada para $\\phi$. O método é estritamente <strong>invariante</strong>.</p>
            </div>
        </details>

        <h3>Exemplos Canônicos da Priori de Jeffreys</h3>
        <ol>
            <li><strong>Parâmetro de Locação:</strong> Seja $p(x \\mid \\theta) = f(x - \\theta)$. Como a densidade depende de $x$ e $\\theta$ apenas através da diferença, a derivada segunda de $\\log f(x-\\theta)$ não depende de $\\theta$. Logo, $I(\\theta) = c$ (constante), resultando em:
                $$p(\\theta) \\propto 1 \\quad \\text{(Uniforme imprópria na reta real)}$$
            </li>
            <li><strong>Parâmetro de Escala:</strong> Seja $p(x \\mid \\sigma) = \\frac{1}{\\sigma} f\\left(\\frac{x}{\\sigma}\\right)$. É fácil demonstrar que a informação de Fisher decresce quadraticamente com a dispersão: $I(\\sigma) \\propto \\frac{1}{\\sigma^2}$. Aplicando a raiz quadrada:
                $$p(\\sigma) \\propto \\sqrt{\\frac{1}{\\sigma^2}} = \\frac{1}{\\sigma} \\quad \\Longleftrightarrow \\quad p(\\log \\sigma) \\propto 1$$
            </li>
            <li><strong>Modelo Bernoulli / Binomial:</strong> Para $p(x \\mid \\theta) = \\theta^x (1-\\theta)^{1-x}$, temos:
                $$\\log p(x \\mid \\theta) = x \\log \\theta + (1-x)\\log(1-\\theta) \\implies \\frac{\\partial^2 \\log p}{\\partial \\theta^2} = -\\frac{x}{\\theta^2} - \\frac{1-x}{(1-\\theta)^2}$$
                Como $E[X] = \\theta$, aplicando a esperança negativa:
                $$I(\\theta) = \\frac{\\theta}{\\theta^2} + \\frac{1-\\theta}{(1-\\theta)^2} = \\frac{1}{\\theta(1-\\theta)}$$
                Portanto, a priori de Jeffreys é:
                $$p(\\theta) \\propto [\\theta(1-\\theta)]^{-1/2} = \\theta^{-1/2}(1-\\theta)^{-1/2} \\equiv \\text{Beta}\\left(\\frac{1}{2}, \\frac{1}{2}\\right)$$
            </li>
            <li><strong>Modelo de Poisson:</strong> Para $p(x \\mid \\lambda) = \\frac{e^{-\\lambda} \\lambda^x}{x!}$, a informação de Fisher é $I(\\lambda) = \\frac{1}{\\lambda}$. Logo:
                $$p(\\lambda) \\propto \\lambda^{-1/2}$$
            </li>
        </ol>

        <div class="callout callout-tip">
            <div class="callout-header">💡 Priori de Jeffreys Independente para o Modelo Normal</div>
            <p>Se aplicarmos a regra multivariada direta de Jeffreys para a Normal com $(\\mu, \\sigma^2)$ simultaneamente desconhecidos, obtém-se $p(\\mu, \\sigma^2) \\propto \\sigma^{-3}$, o que pode causar inconsistências em certas dimensões. Harold Jeffreys propôs aplicar a regra separadamente para locação e escala ($p(\\mu) \\propto 1$ e $p(\\sigma^2) \\propto 1/\\sigma^2$), assumindo independência a priori:</p>
            $$p(\\mu, \\sigma^2) \\propto \\frac{1}{\\sigma^2} \\quad \\Longleftrightarrow \\quad p(\\mu, \\phi) \\propto \\frac{1}{\\phi}$$
            <p>Esta é a <strong>priori de referência padrão</strong> para o modelo normal, que conduz exatamente às clássicas distribuições $t$ de Student a posteriori.</p>
        </div>

        <h2>2.5 Estruturas Avançadas de Priori</h2>

        <h3>1. Prioris Hierárquicas</h3>
        <p>Muitas vezes, a atribuição de valores numéricos rígidos aos hiperparâmetros de uma priori parece arbitrária. A modelagem hierárquica resolve esse dilema introduzindo múltiplos estágios de incerteza:</p>
        $$y_i \\mid \\theta_i \\sim p(y_i \\mid \\theta_i) \\quad \\text{(Estágio 1: Modelo Amostral dos Grupos)}$$
        $$\\theta_i \\mid \\boldsymbol{\\phi} \\sim p(\\theta_i \\mid \\boldsymbol{\\phi}) \\quad \\text{(Estágio 2: Priori Populacional)}$$
        $$\\boldsymbol{\\phi} \\sim p(\\boldsymbol{\\phi}) \\quad \\text{(Estágio 3: Hiperpriori sobre os Hiperparâmetros)}$$
        
        <p>Essa arquitetura gera o fenômeno bayesiano fundamental conhecido como <strong>encolhimento (*shrinkage*)</strong> e <strong>empréstimo de força estatística (*borrowing strength*)</strong>: grupos com poucas observações têm suas estimativas "puxadas" em direção à média global da população, enquanto grupos com muitos dados mantêm suas estimativas fiéis aos dados locais.</p>

        <h3>2. Misturas de Prioris</h3>
        <p>Quando a incerteza inicial é multimodal (por exemplo, quando dois especialistas discordam radicalmente sobre a taxa de sucesso de uma droga), uma única distribuição unimodal é inadequada. Define-se então uma <strong>mistura finita de prioris</strong>:</p>
        $$p(\\theta) = \\sum_{k=1}^K w_k \\, p_k(\\theta), \\quad \\text{com } w_k > 0 \\text{ e } \\sum_{k=1}^K w_k = 1$$
        
        <p>Ao observar os dados $x$, a distribuição a posteriori também é uma mistura das posteriores individuais geradas por cada componente:</p>
        $$p(\\theta \\mid x) = \\sum_{k=1}^K w_k^* \\, p_k(\\theta \\mid x)$$
        <p>onde os novos pesos atualizados $w_k^*$ são diretamente proporcionais à evidência marginal que cada componente forneceu para os dados observados: $w_k^* \\propto w_k \\, p_k(x)$. Assim, o próprio Teorema de Bayes se encarrega de selecionar e amplificar os especialistas cujas crenças foram mais compatíveis com a realidade observada!</p>
    </section>
"""
