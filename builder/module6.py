# -*- coding: utf-8 -*-
"""
Módulo 6: Modelos Lineares e ANOVA sob a Ótica Bayesiana
"""

def get_module6_html():
    return """
    <!-- ========================================== -->
    <!-- MÓDULO 6: MODELOS LINEARES E ANOVA         -->
    <!-- ========================================== -->
    <section id="modulo6" class="module-chapter">
        <h1 class="module-title">
            <span class="module-num">Módulo 6</span>
            Modelos Lineares e ANOVA Bayesiana
        </h1>

        <div class="callout callout-tip">
            <div class="callout-header">💡 Sinopse Conceitual</div>
            <p>O Modelo Linear Normal constitui a viga-mestra da modelagem estatística aplicada.</p>
            <p>Na inferência bayesiana, a formulação matricial generaliza a estrutura conjugada Normal-Gama para dimensões arbitrárias com notável concisão.</p>
            <p>Sob a priori de referência de Jeffreys, os estimadores pontuais coincidem numericamente com os Mínimos Quadrados Ordinários (MQO).</p>
            <p>Contudo, a interpretação bayesiana supera as limitações frequentistas: dispomos da distribuição de probabilidade exata dos efeitos, permitindo testar <strong>contrastes lineares em ANOVA</strong> de forma direta, sem a necessidade de correções artificiais para testes múltiplos.</p>
        </div>

        <h2>6.1 O Modelo de Regressão Linear Múltipla Normal</h2>
        <p>Considere $n$ observações de uma variável resposta contínua $y_i$ associadas a $k$ variáveis explicativas $\\mathbf{x}_i = (x_{i1}, \\dots, x_{ik})'$. Na notação matricial padrão:</p>
        $$\\mathbf{y} = \\mathbf{X} \\boldsymbol{\\beta} + \\boldsymbol{\\epsilon}, \\quad \\boldsymbol{\\epsilon} \\sim N_n(\\mathbf{0}, \\; \\phi^{-1} \\mathbf{I}_n)$$
        <p>onde:</p>
        <ul>
            <li>$\\mathbf{y} \\in \\mathbb{R}^{n \\times 1}$ é o vetor de respostas observadas;</li>
            <li>$\\mathbf{X} \\in \\mathbb{R}^{n \\times k}$ é a matriz de planejamento ou delineamento (posto completo $k < n$);</li>
            <li>$\\boldsymbol{\\beta} = (\\beta_1, \\dots, \\beta_k)' \\in \\mathbb{R}^{k \\times 1}$ é o vetor de coeficientes de regressão;</li>
            <li>$\\phi = \\sigma^{-2} > 0$ é a precisão dos erros aleatórios gaussianos.</li>
        </ul>

        <h3>A Função de Verossimilhança Matricial</h3>
        <p>Como os erros são i.i.d. normais, a verossimilhança conjunta para $(\\boldsymbol{\\beta}, \\phi)$ é:</p>
        $$l(\\boldsymbol{\\beta}, \\phi; \\mathbf{y}) = (2\\pi)^{-n/2} \\phi^{n/2} \\exp\\left\\{ -\\frac{\\phi}{2} (\\mathbf{y} - \\mathbf{X}\\boldsymbol{\\beta})'(\\mathbf{y} - \\mathbf{X}\\boldsymbol{\\beta}) \\right\\}$$
        
        <p>Definindo o estimador clássico de Mínimos Quadrados Ordinários $\\hat{\\boldsymbol{\\beta}} = (\\mathbf{X}'\\mathbf{X})^{-1} \\mathbf{X}'\\mathbf{y}$ e a soma de quadrados dos resíduos $S = (\\mathbf{y} - \\mathbf{X}\\hat{\\boldsymbol{\\beta}})'(\\mathbf{y} - \\mathbf{X}\\hat{\\boldsymbol{\\beta}})$, decompomos a forma quadrática em dois termos ortogonais:</p>
        $$(\\mathbf{y} - \\mathbf{X}\\boldsymbol{\\beta})'(\\mathbf{y} - \\mathbf{X}\\boldsymbol{\\beta}) = S + (\\boldsymbol{\\beta} - \\hat{\\boldsymbol{\\beta}})' (\\mathbf{X}'\\mathbf{X}) (\\boldsymbol{\\beta} - \\hat{\\boldsymbol{\\beta}})$$
        <p>Portanto, a verossimilhança separa-se naturalmente em:</p>
        $$l(\\boldsymbol{\\beta}, \\phi; \\mathbf{y}) \\propto \\phi^{n/2} \\exp\\left\\{ -\\frac{\\phi}{2} \\left[ S + (\\boldsymbol{\\beta} - \\hat{\\boldsymbol{\\beta}})'(\\mathbf{X}'\\mathbf{X})(\\boldsymbol{\\beta} - \\hat{\\boldsymbol{\\beta}}) \\right] \\right\\}$$

        <h2>6.2 Análise sob Priori Não Informativa de Jeffreys</h2>
        <p>Quando não há conhecimento prévio substancial sobre os efeitos das covariáveis ou a precisão, adota-se a <strong>priori de referência de Jeffreys</strong> para parâmetros de locação e escala multivariados:</p>
        $$p(\\boldsymbol{\\beta}, \\phi) \\propto \\frac{1}{\\phi} \\quad \\Longleftrightarrow \\quad p(\\boldsymbol{\\beta}, \\sigma^2) \\propto \\frac{1}{\\sigma^2}$$

        <div class="callout callout-thm">
            <div class="callout-header">⚙️ Posteriori Conjunta e Marginais sob Priori de Referência</div>
            <p>Multiplicando a verossimilhança pela priori de Jeffreys no Teorema de Bayes, obtemos:</p>
            <ol>
                <li><strong>Posteriori Condicional de $\\boldsymbol{\\beta}$ dada a precisão $\\phi$:</strong>
                    $$\\boldsymbol{\\beta} \\mid \\phi, \\mathbf{y} \\sim N_k\\left( \\hat{\\boldsymbol{\\beta}}, \\; [\\phi (\\mathbf{X}'\\mathbf{X})]^{-1} \\right)$$
                </li>
                <li><strong>Posteriori Marginal da Precisão $\\phi$:</strong>
                    $$\\phi \\mid \\mathbf{y} \\sim \\text{Gama}\\left( \\frac{n - k}{2}, \\; \\frac{S}{2} \\right) \\quad \\Longleftrightarrow \\quad \\frac{S}{\\sigma^2} \\mid \\mathbf{y} \\sim \\chi^2_{n-k}$$
                </li>
                <li><strong>Posteriori Marginal dos Coeficientes $\\boldsymbol{\\beta}$:</strong>
                    Integrando $\\phi$ analiticamente, a distribuição marginal de $\\boldsymbol{\\beta}$ é uma <strong>$t$ de Student multivariada</strong> com $n-k$ graus de liberdade:
                    $$\\boldsymbol{\\beta} \\mid \\mathbf{y} \\sim t_{n-k}\\left( \\hat{\\boldsymbol{\\beta}}, \\; s^2 (\\mathbf{X}'\\mathbf{X})^{-1} \\right)$$
                    onde $s^2 = \\frac{S}{n-k}$ é a variância residual amostral não viesada.
                </li>
            </ol>
        </div>

        <div class="callout callout-tip">
            <div class="callout-header">💡 Equivalência Numérica vs Diferença Conceitual</div>
            <p>Sob a priori de Jeffreys, a média a posteriori $\\hat{\\boldsymbol{\\beta}}_{\\text{Bayes}} = \\hat{\\boldsymbol{\\beta}}$ coincide <strong>numericamente</strong> com a estimativa pontual de Mínimos Quadrados e com os limites dos intervalos de confiança clássicos. No entanto, o significado epistemológico é diametralmente oposto:</p>
            <ul>
                <li>O estatístico frequentista precisa dizer: <em>"O parâmetro $\\boldsymbol{\\beta}$ é uma constante fixa; se repetíssemos o experimento infinitas vezes, 95% dos intervalos aleatórios conteriam esse valor."</em></li>
                <li>O estatístico bayesiano afirma diretamente: <em>"Condicionado aos dados observados, existe uma probabilidade real de 95% de que o efeito $\\beta_j$ esteja contido no intervalo de credibilidade calculado."</em></li>
            </ul>
        </div>

        <h2>6.3 Análise de Variância (ANOVA) com 1 Fator de Classificação</h2>
        <p>A Análise de Variância com um fator de classificação destina-se a comparar as médias de uma variável resposta contínua entre $p$ grupos ou tratamentos independentes. Sob a ótica bayesiana, a ANOVA é expressa diretamente como um caso especial do modelo linear geral.</p>

        <h3>O Modelo em Médias de Grupos</h3>
        <p>Para a $i$-ésima observação no $j$-ésimo grupo ($j = 1, \\dots, p$ e $i = 1, \\dots, n_j$), com tamanho total $n = \\sum_{j=1}^p n_j$:</p>
        $$y_{ij} = \\beta_j + \\epsilon_{ij}, \\quad \\epsilon_{ij} \\sim N(0, \\sigma^2)$$
        <p>onde $\\beta_j$ representa a média populacional verdadeira do $j$-ésimo tratamento e $\\sigma^2$ é a variância comum intra-grupos (homocedasticidade).</p>

        <h3>A Estrutura da Matriz de Delineamento</h3>
        <p>A matriz de projeto $\\mathbf{X} \\in \\mathbb{R}^{n \\times p}$ é composta por colunas indicadoras em blocos:</p>
        $$\\mathbf{X} = \\begin{bmatrix} 
        \\mathbf{1}_{n_1} & \\mathbf{0} & \\cdots & \\mathbf{0} \\\\
        \\mathbf{0} & \\mathbf{1}_{n_2} & \\cdots & \\mathbf{0} \\\\
        \\vdots & \\vdots & \\ddots & \\vdots \\\\
        \\mathbf{0} & \\mathbf{0} & \\cdots & \\mathbf{1}_{n_p}
        \\end{bmatrix}$$
        
        <p>A matriz de covariância cruzada $\\mathbf{X}'\\mathbf{X}$ resulta em uma <strong>matriz diagonal pura</strong> cujos elementos da diagonal principal são os respectivos tamanhos amostrais dos grupos:</p>
        $$\\mathbf{X}'\\mathbf{X} = \\begin{bmatrix}
        n_1 & 0 & \\cdots & 0 \\\\
        0 & n_2 & \\cdots & 0 \\\\
        \\vdots & \\vdots & \\ddots & \\vdots \\\\
        0 & 0 & \\cdots & n_p
        \\end{bmatrix} = \\text{diag}(n_1, n_2, \\dots, n_p)$$
        
        <p>Por ser diagonal, sua inversa é trivialmente $(\\mathbf{X}'\\mathbf{X})^{-1} = \\text{diag}\\left(\\frac{1}{n_1}, \\dots, \\frac{1}{n_p}\\right)$, e o vetor de estimadores MQO é o vetor das médias amostrais observadas em cada grupo:</p>
        $$\\hat{\\boldsymbol{\\beta}} = (\\mathbf{X}'\\mathbf{X})^{-1} \\mathbf{X}'\\mathbf{y} = (\\bar{y}_1, \\bar{y}_2, \\dots, \\bar{y}_p)'$$

        <h3>Distribuição a Posteriori dos Efeitos de Tratamento</h3>
        <p>Adotando a priori de referência $p(\\boldsymbol{\\beta}, \\sigma^2) \\propto 1/\\sigma^2$, a distribuição a posteriori conjunta dos parâmetros condicionada à variância residual é uma Normal multivariada com matriz de covariância diagonal:</p>
        $$\\beta_j \\mid \\sigma^2, \\mathbf{y} \\sim N\\left( \\bar{y}_j, \\; \\frac{\\sigma^2}{n_j} \\right) \\quad \\text{independentes entre si}$$
        <p>E a marginal para cada média de grupo é uma $t$ de Student univariada com $n - p$ graus de liberdade:</p>
        $$\\beta_j \\mid \\mathbf{y} \\sim t_{n-p}\\left( \\bar{y}_j, \\; \\frac{s^2}{n_j} \\right), \\quad \\text{onde } s^2 = \\frac{\\sum_{j=1}^p \\sum_{i=1}^{n_j} (y_{ij} - \\bar{y}_j)^2}{n - p}$$

        <h2>6.4 Inferência Exata sobre Contrastes</h2>
        <p>Na prática experimental, raramente estamos interessados apenas em testar a hipótese global genérica de que "todos os grupos são iguais". O verdadeiro interesse científico quase sempre reside em <strong>contrastes específicos</strong> entre tratamentos.</p>

        <div class="callout callout-def">
            <div class="callout-header">📘 Contraste Linear</div>
            <p>Um <strong>contraste linear</strong> entre as médias dos tratamentos é qualquer combinação linear $\\psi = \\sum_{j=1}^p c_j \\beta_j = \\mathbf{c}'\\boldsymbol{\\beta}$ cujos coeficientes satisfazem a restrição de soma zero:</p>
            $$\\sum_{j=1}^p c_j = 0$$
        </div>

        <p>Exemplos comuns de contrastes:</p>
        <ul>
            <li><strong>Comparação Simples entre dois tratamentos:</strong> $\\psi = \\beta_1 - \\beta_2$ (com $\\mathbf{c} = (1, -1, 0, \\dots, 0)'$).</li>
            <li><strong>Controle versus Média dos Novos Tratamentos:</strong> $\\psi = \\beta_1 - \\frac{\\beta_2 + \\beta_3}{2}$ (com $\\mathbf{c} = (1, -0.5, -0.5)'$).</li>
        </ul>

        <div class="callout callout-thm">
            <div class="callout-header">⚙️ Distribuição Exata de um Contraste a Posteriori</div>
            <p>Como $\\boldsymbol{\\beta} \\mid \\mathbf{y} \\sim t_{n-p}(\\hat{\\boldsymbol{\\beta}}, s^2 (\\mathbf{X}'\\mathbf{X})^{-1})$, qualquer combinação linear $\\psi = \\mathbf{c}'\\boldsymbol{\\beta}$ tem distribuição $t$ de Student univariada exata:</p>
            $$\\psi \\mid \\mathbf{y} \\sim t_{n-p}\\left( \\hat{\\psi}, \\; s^2 \\sum_{j=1}^p \\frac{c_j^2}{n_j} \\right), \\quad \\text{com } \\hat{\\psi} = \\sum_{j=1}^p c_j \\bar{y}_j$$
        </div>

        <div class="callout callout-tip">
            <div class="callout-header">💡 O Fim das "Correções para Múltiplas Comparações"</div>
            <p>Na ANOVA frequentista clássica, testar múltiplos contrastes inflaciona a taxa de erro do tipo I, forçando o pesquisador a recorrer a penalizações artificiais (como os métodos de Bonferroni, Tukey HSD ou Scheffé). Na abordagem bayesiana:</p>
            <ul>
                <li>Não existe "inflação de erro tipo I" porque não se calculam taxas de erro em infinitas repetições hipotéticas.</li>
                <li>A distribuição a posteriori conjunta $p(\\boldsymbol{\\beta} \\mid \\mathbf{y})$ é <strong>uma só e já contém toda a correlação e incerteza global</strong> do experimento.</li>
                <li>Podemos calcular diretamente a probabilidade de qualquer afirmação científica substantiva, como:
                    $$P(\\beta_1 > \\beta_2 \\mid \\mathbf{y}) = P(\\beta_1 - \\beta_2 > 0 \\mid \\mathbf{y}) = \\int_0^\\infty p(\\psi \\mid \\mathbf{y}) \\, d\\psi$$
                </li>
            </ul>
            <p>Se essa probabilidade for, por exemplo, 0.985, concluímos imediatamente que há 98.5% de certeza de que o tratamento 1 é superior ao tratamento 2 &mdash; uma resposta transparente, intuitiva e epistemologicamente inatacável.</p>
        </div>
    </section>
"""
