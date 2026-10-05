# -*- coding: utf-8 -*-
"""
Módulo de Cabeçalho, Estilos CSS de Livro Editorial, MathJax e JavaScript.
Configuração focada em estética de livro tradicional: página clara centralizada,
barra lateral fechada por padrão (gaveta off-canvas), entrelinha generosa e respiração visual.
"""

def get_head_and_styles():
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Luca Ferreira Barboza">
    <title>Notas de Inferência Estatística Bayesiana — Livro Digital</title>
    
    <!-- Google Fonts: Tipografia Editorial de Livro -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;0,8..60,700;1,8..60,400;1,8..60,600&display=swap" rel="stylesheet">
    
    <!-- Configuração Segura do MathJax 3 -->
    <script>
    window.MathJax = {
        tex: {
            inlineMath: [['\\\\(', '\\\\)'], ['$', '$']],
            displayMath: [['\\\\[', '\\\\]'], ['$$', '$$']],
            processEscapes: true,
            processEnvironments: true,
            tags: 'ams',
            macros: {
                Var: "\\\\operatorname{Var}",
                E: "\\\\operatorname{E}",
                Cov: "\\\\operatorname{Cov}",
                Beta: "\\\\operatorname{Beta}",
                Gama: "\\\\operatorname{Gama}",
                Dirichlet: "\\\\operatorname{Dirichlet}",
                argmax: "\\\\operatorname*{arg\\\\,max}",
                argmin: "\\\\operatorname*{arg\\\\,min}",
                given: "\\,\\vert\\,"
            }
        },
        options: {
            skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
        },
        chtml: {
            displayAlign: 'center',
            displayIndent: '0'
        }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <style>
        :root {
            /* Paleta Editorial de Livro Impresso (Papiro / Marfim / Tinta Profunda) */
            --bg-canvas: #fbfaf8;
            --bg-surface: #ffffff;
            --bg-surface-soft: #f7f5f1;
            --bg-drawer: #ffffff;
            
            --text-ink: #1c1917;         /* Tinta carvão profunda */
            --text-secondary: #44403c;   /* Texto secundário legível */
            --text-muted: #78716c;       /* Notas e referências */
            
            --border-paper: #e7e5e4;     /* Linha de caderno/papel */
            --border-subtle: #f0eeeb;    /* Divisórias suaves */
            
            --accent-book: #1e3a8a;      /* Azul clássico de encadernação */
            --accent-soft: #eff6ff;
            
            /* Destaques acadêmicos sutis */
            --callout-def-border: #0369a1;
            --callout-def-bg: #f8fafc;
            --callout-thm-border: #6d28d9;
            --callout-thm-bg: #faf5ff;
            --callout-tip-border: #047857;
            --callout-tip-bg: #f0fdf4;
            --callout-warn-border: #c2410c;
            --callout-warn-bg: #fffbeb;

            --code-bg: #1e293b;
            --code-text: #f8fafc;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
            background-color: var(--bg-canvas);
        }

        body {
            font-family: 'Source Serif 4', 'Newsreader', Georgia, serif;
            font-size: 19px;
            line-height: 2.15;           /* Entrelinha ampla e confortável de livro */
            color: var(--text-ink);
            background-color: var(--bg-canvas);
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        /* BARRA SUPERIOR DISCRETA (ESTILO LIVRO) */
        .book-topbar {
            position: sticky;
            top: 0;
            left: 0;
            right: 0;
            height: 58px;
            background: rgba(251, 250, 248, 0.94);
            backdrop-filter: blur(8px);
            border-bottom: 1px solid var(--border-paper);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 28px;
            z-index: 50;
        }

        .topbar-btn {
            font-family: 'Inter', sans-serif;
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--text-secondary);
            background: var(--bg-surface);
            border: 1px solid var(--border-paper);
            padding: 7px 14px;
            border-radius: 6px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 7px;
            transition: all 0.2s ease;
            box-shadow: 0 1px 2px rgba(0,0,0,0.03);
        }

        .topbar-btn:hover {
            color: var(--accent-book);
            border-color: #cbd5e1;
            background: #ffffff;
            transform: translateY(-1px);
        }

        .topbar-title {
            font-family: 'Inter', sans-serif;
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--text-muted);
            letter-spacing: 0.02em;
        }

        /* GAVETA LATERAL DO SUMÁRIO (FECHADA POR PADRÃO) */
        .sidebar-drawer {
            position: fixed;
            top: 0;
            left: 0;
            bottom: 0;
            width: 340px;
            max-width: 85vw;
            background-color: var(--bg-drawer);
            border-right: 1px solid var(--border-paper);
            box-shadow: 10px 0 30px rgba(0,0,0,0.08);
            transform: translateX(-100%);
            transition: transform 0.32s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 1000;
            display: flex;
            flex-direction: column;
            padding: 28px 24px;
            overflow-y: auto;
        }

        .sidebar-drawer.open {
            transform: translateX(0);
        }

        .drawer-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--border-paper);
            margin-bottom: 20px;
        }

        .drawer-title {
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-ink);
        }

        .drawer-close-btn {
            background: transparent;
            border: none;
            font-size: 1.4rem;
            color: var(--text-muted);
            cursor: pointer;
            padding: 4px 8px;
            line-height: 1;
            border-radius: 4px;
        }

        .drawer-close-btn:hover {
            color: var(--text-ink);
            background: var(--border-subtle);
        }

        .sidebar-backdrop {
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.3);
            backdrop-filter: blur(2px);
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
            z-index: 999;
        }

        .sidebar-backdrop.open {
            opacity: 1;
            pointer-events: auto;
        }

        .drawer-nav {
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .drawer-category {
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            margin: 20px 0 6px 4px;
        }

        .drawer-link {
            display: block;
            padding: 8px 12px;
            border-radius: 6px;
            color: var(--text-secondary);
            text-decoration: none;
            line-height: 1.45;
            transition: all 0.15s ease;
        }

        .drawer-link:hover {
            background: var(--bg-surface-soft);
            color: var(--accent-book);
            transform: translateX(4px);
        }

        /* CONTEÚDO PRINCIPAL (CENTRALIZADO COMO LIVRO) */
        .book-container {
            max-width: 830px;
            margin: 0 auto;
            padding: 60px 24px 140px 24px;
        }

        /* CABEÇALHO DO LIVRO */
        .book-frontmatter {
            text-align: center;
            margin-bottom: 70px;
            padding-bottom: 45px;
            border-bottom: 1px solid var(--border-paper);
        }

        .book-frontmatter .book-series {
            font-family: 'Inter', sans-serif;
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            color: var(--accent-book);
            margin-bottom: 16px;
        }

        .book-frontmatter h1 {
            font-family: 'Source Serif 4', Georgia, serif;
            font-size: 2.85rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            line-height: 1.25;
            color: var(--text-ink);
            margin-bottom: 22px;
        }

        .book-frontmatter .book-author {
            font-family: 'Inter', sans-serif;
            font-size: 1.05rem;
            color: var(--text-secondary);
            margin-bottom: 8px;
        }

        .book-frontmatter .book-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 0.88rem;
            color: var(--text-muted);
        }

        /* CAPÍTULOS E SEÇÕES */
        .module-chapter {
            margin-top: 85px;
            padding-top: 20px;
        }

        .chapter-header {
            margin-bottom: 35px;
            padding-bottom: 18px;
            border-bottom: 2px solid var(--text-ink);
        }

        .chapter-label {
            font-family: 'Inter', sans-serif;
            font-size: 0.85rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: var(--accent-book);
            margin-bottom: 8px;
            display: block;
        }

        h1.module-title {
            font-family: 'Source Serif 4', Georgia, serif;
            font-size: 2.25rem;
            font-weight: 700;
            line-height: 1.25;
            color: var(--text-ink);
            margin: 0;
        }

        h2 {
            font-family: 'Source Serif 4', Georgia, serif;
            font-size: 1.65rem;
            font-weight: 600;
            color: var(--text-ink);
            margin: 60px 0 24px 0;
            line-height: 1.35;
        }

        h3 {
            font-family: 'Inter', sans-serif;
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--text-ink);
            margin: 42px 0 18px 0;
            line-height: 1.4;
        }

        /* PARÁGRAFOS E ESPAÇAMENTO GENEROSO */
        p {
            margin-bottom: 2.1rem;      /* Mais quebra e respiro entre ideias */
            text-align: justify;
            text-justify: inter-word;
            hyphens: auto;
        }

        ul, ol {
            margin: 0 0 2.2rem 1.8rem;
        }

        li {
            margin-bottom: 0.9rem;
            line-height: 2.0;
        }

        strong {
            color: var(--text-ink);
            font-weight: 600;
        }

        /* EQUAÇÕES MATHJAX EM DESTAQUE */
        mjx-container[jax="CHTML"][display="true"] {
            margin: 2.4rem 0 !important;
            padding: 8px 0;
        }

        /* BOXES SEMÂNTICOS EDITORIAIS */
        .callout {
            border-radius: 8px;
            padding: 24px 28px;
            margin: 36px 0;
            background-color: var(--bg-surface);
            border-left: 5px solid;
            box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        }

        .callout-header {
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 14px;
        }

        .callout p:last-child {
            margin-bottom: 0;
        }

        .callout-def { border-left-color: var(--callout-def-border); background-color: var(--callout-def-bg); }
        .callout-def .callout-header { color: var(--callout-def-border); }

        .callout-thm { border-left-color: var(--callout-thm-border); background-color: var(--callout-thm-bg); }
        .callout-thm .callout-header { color: var(--callout-thm-border); }

        .callout-tip { border-left-color: var(--callout-tip-border); background-color: var(--callout-tip-bg); }
        .callout-tip .callout-header { color: var(--callout-tip-border); }

        .callout-warn { border-left-color: var(--callout-warn-border); background-color: var(--callout-warn-bg); }
        .callout-warn .callout-header { color: var(--callout-warn-border); }

        /* DEMONSTRAÇÕES MATEMÁTICAS RECOLHÍVEIS */
        details.proof {
            margin: 34px 0;
            border: 1px solid var(--border-paper);
            border-radius: 8px;
            background: var(--bg-surface);
            box-shadow: 0 1px 4px rgba(0,0,0,0.02);
            overflow: hidden;
        }

        details.proof[open] {
            border-color: #cbd5e1;
        }

        details.proof summary {
            font-family: 'Inter', sans-serif;
            font-size: 0.94rem;
            font-weight: 600;
            color: var(--text-ink);
            padding: 14px 22px;
            cursor: pointer;
            background-color: var(--bg-surface-soft);
            display: flex;
            align-items: center;
            gap: 10px;
            user-select: none;
            transition: background 0.15s ease;
        }

        details.proof summary:hover {
            background-color: var(--accent-soft);
            color: var(--accent-book);
        }

        .proof-body {
            padding: 26px 28px;
            border-top: 1px solid var(--border-paper);
            background: #ffffff;
        }

        /* CARDS DE DISTRIBUIÇÃO */
        .dist-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-paper);
            border-radius: 10px;
            padding: 28px 30px;
            margin: 38px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }

        .dist-card-header {
            font-family: 'Source Serif 4', Georgia, serif;
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 18px;
            border-bottom: 1px solid var(--border-paper);
            padding-bottom: 10px;
        }

        .dist-card-header h4 {
            font-size: 1.35rem;
            font-weight: 600;
            color: var(--text-ink);
        }

        .dist-badge {
            font-family: 'Inter', sans-serif;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            padding: 3px 9px;
            border-radius: 4px;
        }

        .badge-discrete { background: #e0f2fe; color: #0369a1; }
        .badge-continuous { background: #fef3c7; color: #92400e; }

        .dist-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            background: var(--bg-surface-soft);
            padding: 16px 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        @media (max-width: 768px) {
            .dist-grid {
                grid-template-columns: 1fr;
            }
        }

        .dist-grid-item span.label {
            display: block;
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: var(--text-muted);
            margin-bottom: 5px;
        }

        .dist-grid-density {
            grid-column: 1 / -1;
            background: #ffffff;
            border: 1px solid var(--border-paper);
            padding: 16px 22px;
            border-radius: 8px;
            margin-top: 6px;
        }

        .dist-grid-density span.label {
            display: block;
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: var(--text-muted);
            margin-bottom: 8px;
        }

        .dist-grid-density .formula {
            text-align: center;
            font-size: 1.1rem;
            overflow-x: auto;
            padding: 8px 0;
        }

        .dist-role {
            font-size: 0.98rem;
            margin-top: 14px;
            padding-top: 12px;
            border-top: 1px dashed var(--border-paper);
        }

        /* TABELAS COMPARATIVAS */
        .table-responsive {
            overflow-x: auto;
            margin: 35px 0;
        }

        table.academic-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            line-height: 1.6;
            background: var(--bg-surface);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 4px rgba(0,0,0,0.04);
            border: 1px solid var(--border-paper);
        }

        table.academic-table th {
            background: #292524;
            color: #ffffff;
            font-weight: 600;
            text-align: left;
            padding: 14px 18px;
        }

        table.academic-table td {
            padding: 14px 18px;
            border-bottom: 1px solid var(--border-paper);
            vertical-align: top;
        }

        table.academic-table tr:hover td {
            background-color: var(--bg-surface-soft);
        }

        /* ABAS DE CÓDIGO (R / PYTHON) */
        .code-tabs {
            margin: 35px 0;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #334155;
            background: var(--code-bg);
        }

        .tab-nav {
            display: flex;
            background: #0f172a;
            border-bottom: 1px solid #334155;
            padding: 4px 12px 0 12px;
        }

        .tab-btn {
            font-family: 'Inter', sans-serif;
            font-size: 0.84rem;
            font-weight: 600;
            padding: 9px 18px;
            border: none;
            background: transparent;
            color: #94a3b8;
            cursor: pointer;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            transition: all 0.15s ease;
        }

        .tab-btn:hover {
            color: #f1f5f9;
        }

        .tab-btn.active {
            background: var(--code-bg);
            color: #38bdf8;
            border-bottom: 2px solid #38bdf8;
        }

        .tab-pane {
            display: none;
            padding: 20px 24px;
            overflow-x: auto;
        }

        .tab-pane.active {
            display: block;
        }

        pre code {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            line-height: 1.65;
            color: var(--code-text);
        }

        p code, li code {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.88em;
            background: var(--bg-surface-soft);
            color: var(--accent-book);
            padding: 2px 6px;
            border-radius: 4px;
            border: 1px solid var(--border-paper);
        }

        /* RODAPÉ DO LIVRO */
        .book-colophon {
            margin-top: 110px;
            padding-top: 40px;
            border-top: 1px solid var(--border-paper);
            font-family: 'Inter', sans-serif;
            font-size: 0.88rem;
            color: var(--text-muted);
            text-align: center;
            line-height: 1.8;
        }

        /* REGRAS DE IMPRESSÃO / PDF (@media print) */
        @media print {
            body {
                background: #ffffff !important;
                color: #000000 !important;
                font-size: 11pt !important;
                line-height: 1.6 !important;
            }

            .book-topbar,
            .sidebar-drawer,
            .sidebar-backdrop,
            .tab-nav {
                display: none !important;
            }

            .book-container {
                max-width: 100% !important;
                padding: 0 !important;
            }

            details.proof {
                display: block !important;
                border: 1px solid #cccccc !important;
                page-break-inside: avoid;
                margin: 20pt 0 !important;
            }

            details.proof summary {
                background: #f5f5f5 !important;
                color: #000000 !important;
                font-weight: bold !important;
                display: block !important;
                border-bottom: 1px solid #cccccc;
            }

            .proof-body {
                display: block !important;
                padding: 12pt !important;
            }

            .code-tabs {
                border: 1px solid #cccccc !important;
                background: #fafafa !important;
            }

            .tab-pane {
                display: block !important;
                padding: 12pt !important;
                border-bottom: 1px dashed #cccccc;
            }

            .tab-pane::before {
                content: "=== " attr(data-lang) " ===";
                display: block;
                font-family: 'Inter', sans-serif;
                font-weight: bold;
                font-size: 9pt;
                color: #333333;
                margin-bottom: 6pt;
            }

            pre code {
                color: #111111 !important;
                font-size: 8.5pt !important;
            }

            .module-chapter {
                break-before: page !important;
                page-break-before: always !important;
            }

            .callout {
                border-left-width: 4px !important;
                page-break-inside: avoid;
            }
        }
    </style>
</head>
<body>
"""

def get_sidebar_html():
    return """
    <!-- BARRA SUPERIOR EDITORIAL (LIVRO DIGITAL) -->
    <header class="book-topbar">
        <button class="topbar-btn" onclick="toggleSidebar()" aria-label="Abrir Sumário">
            <span>☰</span> Sumário
        </button>
        <div class="topbar-title">Notas de Inferência Bayesiana</div>
        <button class="topbar-btn" onclick="window.print()" title="Salvar em PDF ou Imprimir">
            <span>📥</span> Baixar PDF
        </button>
    </header>

    <!-- FUNDO ESCURECIDO AO ABRIR GAVETA -->
    <div class="sidebar-backdrop" id="sidebarBackdrop" onclick="toggleSidebar()"></div>

    <!-- GAVETA LATERAL DO SUMÁRIO (FECHADA POR PADRÃO) -->
    <aside class="sidebar-drawer" id="sidebarDrawer">
        <div class="drawer-header">
            <div class="drawer-title">Sumário do Livro</div>
            <button class="drawer-close-btn" onclick="toggleSidebar()" aria-label="Fechar Sumário">✕</button>
        </div>

        <nav class="drawer-nav">
            <div class="drawer-category">Capítulos da Obra</div>
            <a href="#modulo1" class="drawer-link" onclick="toggleSidebar()">1. Fundamentos & Modelos</a>
            <a href="#modulo2" class="drawer-link" onclick="toggleSidebar()">2. Priori, Posteriori & Preditiva</a>
            <a href="#modulo3" class="drawer-link" onclick="toggleSidebar()">3. Famílias Conjugadas</a>
            <a href="#modulo4" class="drawer-link" onclick="toggleSidebar()">4. Decisão, Estimação & Hipóteses</a>
            <a href="#modulo5" class="drawer-link" onclick="toggleSidebar()">5. Computação Bayesiana (MCMC)</a>
            <a href="#modulo6" class="drawer-link" onclick="toggleSidebar()">6. Modelos Lineares & ANOVA</a>
            
            <div class="drawer-category">Tópicos e Laboratórios</div>
            <a href="#catalogo-discretas" class="drawer-link" onclick="toggleSidebar()">§ Modelos Discretos</a>
            <a href="#catalogo-continuas" class="drawer-link" onclick="toggleSidebar()">§ Modelos Contínuos</a>
            <a href="#priori-jeffreys" class="drawer-link" onclick="toggleSidebar()">§ A Priori de Jeffreys</a>
            <a href="#pares-conjugados" class="drawer-link" onclick="toggleSidebar()">§ Pares Conjugados</a>
            <a href="#fator-bayes" class="drawer-link" onclick="toggleSidebar()">§ Fator de Bayes & FBST</a>
            <a href="#lab-mcmc" class="drawer-link" onclick="toggleSidebar()">§ Laboratório MCMC (R & Python)</a>
        </nav>
    </aside>

    <div class="book-container">
        <!-- PÁGINA DE ROSTO DO LIVRO -->
        <div class="book-frontmatter">
            <div class="book-series">Tratado Acadêmico de Estatística</div>
            <h1>Notas de Inferência Estatística Bayesiana</h1>
            <div class="book-author">Luca Ferreira Barboza</div>
            <div class="book-subtitle">Uma Abordagem Epistêmica, Analítica e Computacional</div>
        </div>
"""

def get_footer_and_scripts():
    return """
        <footer class="book-colophon">
            <p><strong>Notas de Inferência Estatística Bayesiana</strong></p>
            <p>Obra compilada e formatada para leitura contínua com tipografia editorial.</p>
            <p><small>Autor: Luca Ferreira Barboza • Baseado no programa oficial da disciplina.</small></p>
        </footer>
    </div>

    <script>
        // Controle da Gaveta do Sumário (Abrir/Fechar)
        function toggleSidebar() {
            const drawer = document.getElementById('sidebarDrawer');
            const backdrop = document.getElementById('sidebarBackdrop');
            if (!drawer || !backdrop) return;
            
            const isOpen = drawer.classList.contains('open');
            drawer.classList.toggle('open', !isOpen);
            backdrop.classList.toggle('open', !isOpen);
            document.body.style.overflow = !isOpen ? 'hidden' : '';
        }

        // Alternador de Abas de Código (R / Python)
        function switchTab(containerId, lang) {
            const container = document.getElementById(containerId);
            if (!container) return;
            
            const btns = container.querySelectorAll('.tab-btn');
            const panes = container.querySelectorAll('.tab-pane');
            
            btns.forEach(btn => {
                btn.classList.toggle('active', btn.getAttribute('data-tab') === lang);
            });
            
            panes.forEach(pane => {
                pane.classList.toggle('active', pane.getAttribute('data-lang-pane') === lang);
            });
        }
    </script>
</body>
</html>
"""
