# -*- coding: utf-8 -*-
"""
Script para ventilar parágrafos em todos os 6 módulos usando substituição direta de strings.
"""

import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def refactor_module1():
    path = os.path.join(current_dir, "module1.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_p = "<p>A inferência estatística dedica-se a responder: <em>o que podemos aprender sobre o mundo a partir de observações empíricas incompletas?</em> O paradigma bayesiano estabelece que qualquer quantidade desconhecida &mdash; sejam parâmetros latentes $\\theta$, estados não observados da natureza ou previsões futuras &mdash; deve ser tratada como uma variável aleatória governada pelas leis da probabilidade. Os modelos probabilísticos discretos e contínuos funcionam como as lentes que traduzem tanto o processo gerador de dados (a verossimilhança $p(x \\mid \\theta)$) quanto o conhecimento inicial acumulado antes da coleta da amostra.</p>"
    new_p = """<p>A inferência estatística dedica-se a responder: <em>o que podemos aprender sobre o mundo a partir de observações empíricas incompletas?</em></p>
            <p>O paradigma bayesiano estabelece que qualquer quantidade desconhecida &mdash; sejam parâmetros latentes $\\theta$, estados não observados da natureza ou previsões futuras &mdash; deve ser tratada como uma variável aleatória governada pelas leis da probabilidade.</p>
            <p>Os modelos probabilísticos discretos e contínuos funcionam como as lentes que traduzem tanto o processo gerador de dados (a verossimilhança $p(x \\mid \\theta)$) quanto o conhecimento inicial acumulado antes da coleta da amostra.</p>"""
    content = content.replace(old_p, new_p)

    old_l = "<p>É vital lembrar que $l(\\theta; x)$ <strong>não é uma densidade de probabilidade em $\\theta$</strong>. Em geral, a integral de $l(\\theta; x)$ em relação a $\\theta$ não é igual a 1 (e pode até ser infinita). A verossimilhança apenas estabelece uma plausibilidade relativa: se $l(\\theta_1; x) > l(\\theta_2; x)$, os dados observados tornam o parâmetro $\\theta_1$ mais plausível que $\\theta_2$.</p>"
    new_l = """<p>É vital lembrar que $l(\\theta; x)$ <strong>não é uma densidade de probabilidade em $\\theta$</strong>.</p>
        <p>Em geral, a integral de $l(\\theta; x)$ em relação a $\\theta$ não é igual a 1 (e pode até divergir para o infinito).</p>
        <p>A verossimilhança apenas estabelece uma plausibilidade relativa entre valores concorrentes: se $l(\\theta_1; x) > l(\\theta_2; x)$, os dados observados tornam o parâmetro $\\theta_1$ mais plausível que $\\theta_2$.</p>"""
    content = content.replace(old_l, new_l)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Módulo 1 ventilado.")

def refactor_module2():
    path = os.path.join(current_dir, "module2.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_p = "<p>O coração operacional da inferência bayesiana é o processo contínuo de aprendizado via atualização de evidências. A distribuição a priori $p(\\theta)$ sintetiza nosso conhecimento ou incerteza inicial antes de olhar para a amostra. Uma vez observados os dados $x$, a função de verossimilhança $l(\\theta; x) = p(x \\mid \\theta)$ atua como um operador multiplicativo de transmissão de informação. Por meio do Teorema de Bayes, combinamos ambas as fontes na distribuição a posteriori $p(\\theta \\mid x)$. Quando não dispomos de opiniões sólidas a priori, recorremos à teoria das prioris objetivas de Harold Jeffreys, que garante coerência matemática independentemente da escala de parametrização adotada.</p>"
    new_p = """<p>O coração operacional da inferência bayesiana é o processo contínuo de aprendizado através da experiência.</p>
            <p>A distribuição a priori $p(\\theta)$ sintetiza nosso conhecimento ou incerteza inicial antes de examinar a amostra empírica.</p>
            <p>Uma vez observados os dados $x$, a função de verossimilhança $l(\\theta; x) = p(x \\mid \\theta)$ atua como um canal multiplicativo de transmissão de informação.</p>
            <p>Por meio do Teorema de Bayes, combinamos ambas as fontes na distribuição a posteriori $p(\\theta \\mid x)$. Quando não dispomos de opiniões sólidas a priori, recorremos às prioris objetivas de Harold Jeffreys, que garantem coerência matemática sob qualquer reparametrização.</p>"""
    content = content.replace(old_p, new_p)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Módulo 2 ventilado.")

def refactor_module3():
    path = os.path.join(current_dir, "module3.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_p = "<p>Em inferência bayesiana, a integral no denominador do Teorema de Bayes pode ser analiticamente intratável para modelos arbitrários. No entanto, quando a distribuição a priori possui a mesma estrutura funcional do núcleo da verossimilhança, a distribuição a posteriori resultante pertence rigorosamente à mesma família paramétrica da priori. Essa propriedade matemática extraordinária é denominada <strong>fechamento por amostragem</strong> ou <strong>conjugação</strong>. Na Família Exponencial de distribuições, a conjugação surge de forma canônica, permitindo que toda a inferência seja reduzida a uma simples atualização algébrica de hiperparâmetros &mdash; onde o conhecimento prévio atua como \"amostras virtuais adicionais\".</p>"
    new_p = """<p>Em inferência bayesiana, a constante normalizadora no denominador do Teorema de Bayes pode ser analiticamente intratável para modelos genéricos.</p>
            <p>No entanto, quando a distribuição a priori possui a mesma estrutura algébrica do núcleo da verossimilhança, a posteriori resultante pertence rigorosamente à mesma família funcional da priori.</p>
            <p>Essa propriedade é denominada <strong>fechamento por amostragem</strong> ou <strong>conjugação</strong>.</p>
            <p>Na Família Exponencial, a conjugação surge de forma canônica e elegante. Toda a inferência é reduzida a uma simples atualização de hiperparâmetros &mdash; onde o conhecimento a priori atua intuitivamente como <em>amostras virtuais adicionais</em>.</p>"""
    content = content.replace(old_p, new_p)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Módulo 3 ventilado.")

def refactor_module4():
    path = os.path.join(current_dir, "module4.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_p = "<p>A distribuição a posteriori $p(\\theta \\mid x)$ contém toda a informação probabilística existente sobre o parâmetro. No entanto, o mundo real exige ações concretas: fixar a dosagem de um fármaco, precificar um seguro ou decidir se aprovamos ou rejeitamos uma teoria científica. A <strong>Teoria da Decisão Estatística</strong> formaliza essa ponte entre crença e ação. Ao ponderarmos as consequências dos erros através de uma <em>função de perda</em>, derivamos de forma unificada os estimadores pontuais ótimos (média, mediana e moda). Na inferência intervalar, as regiões de Maior Densidade a Posteriori (HPD) garantem os menores intervalos possíveis com credibilidade fixada. Por fim, a comparação de teorias e hipóteses atinge sua forma mais expressiva através do <strong>Fator de Bayes</strong> e das razões de chances.</p>"
    new_p = """<p>A distribuição a posteriori $p(\\theta \\mid x)$ resume toda a informação probabilística sobre o parâmetro à luz dos dados observados.</p>
            <p>No entanto, a prática científica exige decisões concretas: estipular a dosagem de um fármaco, precificar uma apólice ou escolher entre teorias concorrentes.</p>
            <p>A <strong>Teoria da Decisão Estatística</strong> formaliza essa ponte entre crença e ação. Ao mensurarmos o custo dos erros através de uma <em>função de perda</em>, derivamos de forma unificada os estimadores pontuais ótimos (média, mediana e moda).</p>
            <p>Na inferência intervalar, as regiões de <strong>Maior Densidade a Posteriori (HPD)</strong> garantem os intervalos de menor comprimento possível para qualquer nível de credibilidade fixado.</p>
            <p>Por fim, a comparação direta entre hipóteses científicas atinge sua forma mais expressiva através do <strong>Fator de Bayes</strong> e das razões de chances.</p>"""
    content = content.replace(old_p, new_p)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Módulo 4 ventilado.")

def refactor_module5():
    path = os.path.join(current_dir, "module5.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_p = "<p>O Teorema de Bayes formula uma teoria inferencial unificada e elegante, mas sua aplicação em modelos realistas &mdash; multiparamétricos, hierárquicos ou não-lineares &mdash; enfrenta um obstáculo matemático intransponível: <strong>a constante de normalização e as marginais a posteriori envolvem integrais em dimensões elevadas sem solução analítica fechada</strong>. Métodos numéricos determinísticos (como Simpson ou quadraturas gaussianas) sucumbem à maldição da dimensionalidade. A revolução bayesiana contemporânea foi viabilizada pelo desenvolvimento de algoritmos estocásticos baseados em simulação: <em>Monte Carlo Simples</em>, <em>Amostragem por Importância</em> e, fundamentalmente, <strong>Monte Carlo via Cadeias de Markov (MCMC)</strong>, onde geramos trajetórias cujo comportamento de longo prazo converge para a distribuição a posteriori exata.</p>"
    new_p = """<p>O Teorema de Bayes estabelece uma teoria inferencial unificada e elegante.</p>
            <p>No entanto, sua aplicação em modelos complexos e realistas enfrenta uma barreira matemática: <strong>a constante de normalização e as distribuições marginais exigem integrais em dimensões elevadas sem solução analítica fechada</strong>.</p>
            <p>Métodos numéricos determinísticos sucumbem rapidamente à maldição da dimensionalidade.</p>
            <p>A moderna revolução bayesiana foi impulsionada por algoritmos de simulação estocástica: <em>Monte Carlo Simples</em>, <em>Amostragem por Importância</em> e, sobretudo, <strong>Monte Carlo via Cadeias de Markov (MCMC)</strong> &mdash; onde simulamos trajetórias cuja distribuição de equilíbrio estacionária é exatamente a posteriori desejada.</p>"""
    content = content.replace(old_p, new_p)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Módulo 5 ventilado.")

def refactor_module6():
    path = os.path.join(current_dir, "module6.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_p = "<p>O Modelo Linear Normal é a espinha dorsal da análise estatística aplicada. Na inferência bayesiana, a formulação matricial generaliza harmoniosamente a estrutura Normal-Gama para dimensões arbitrárias. Sob uma especificação de priori não informativa de referência (priori de Jeffreys), as estimativas pontuais coincidem numericamente de forma exata com o estimador de Mínimos Quadrados Ordinários (MQO) da inferência clássica. Contudo, a interpretação atinge um patamar superior: em vez de invocar teoremas assintóticos ou inventar correções ad-hoc para testes múltiplos, o estatístico bayesiano dispõe da distribuição a posteriori exata dos coeficientes, permitindo testar contrastes entre tratamentos em ANOVA diretamente como probabilidades de hipóteses substantivas.</p>"
    new_p = """<p>O Modelo Linear Normal constitui a viga-mestra da modelagem estatística aplicada.</p>
            <p>Na inferência bayesiana, a formulação matricial generaliza a estrutura conjugada Normal-Gama para dimensões arbitrárias com notável concisão.</p>
            <p>Sob a priori de referência de Jeffreys, os estimadores pontuais coincidem numericamente com os Mínimos Quadrados Ordinários (MQO).</p>
            <p>Contudo, a interpretação bayesiana supera as limitações frequentistas: dispomos da distribuição de probabilidade exata dos efeitos, permitindo testar <strong>contrastes lineares em ANOVA</strong> de forma direta, sem a necessidade de correções artificiais para testes múltiplos.</p>"""
    content = content.replace(old_p, new_p)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Módulo 6 ventilado.")

if __name__ == "__main__":
    refactor_module1()
    refactor_module2()
    refactor_module3()
    refactor_module4()
    refactor_module5()
    refactor_module6()
