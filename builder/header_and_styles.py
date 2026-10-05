# -*- coding: utf-8 -*-
"""
Módulo de Cabeçalho, Estilos CSS, Configurações do MathJax e JavaScript.
"""

def get_head_and_styles():
    return """<!DOCTYPE html>
<html lang="pt-BR" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Luca Ferreira Barboza">
    <title>Notas de Inferência Estatística Bayesiana</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400;1,8..60,600&display=swap" rel="stylesheet">
    
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
                given: "\\\\,\\\\vert\\\\,"
            }
        },
        options: {
            skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
        },
        chtml: {
            displayAlign: 'center'
        }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <style>
        :root {
            /* Tema Claro (Padrão) */
            --bg-canvas: #f8fafc;
            --bg-surface: #ffffff;
            --bg-sidebar: #0f172a;
            --text-sidebar: #cbd5e1;
            --text-sidebar-active: #38bdf8;
            --text-primary: #1e293b;
            --text-secondary: #475569;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
            --border-light: #f1f5f9;
            --accent-primary: #2563eb;
            --accent-hover: #1d4ed8;
            --accent-soft: #eff6ff;
            --code-bg: #1e293b;
            --code-text: #f8fafc;
            
            /* Callout colors */
            --callout-def-border: #0284c7;
            --callout-def-bg: #f0f9ff;
            --callout-thm-border: #7c3aed;
            --callout-thm-bg: #f5f3ff;
            --callout-tip-border: #059669;
            --callout-tip-bg: #ecfdf5;
            --callout-warn-border: #ea580c;
            --callout-warn-bg: #fff7ed;
            
            --sidebar-width: 290px;
            --header-height: 60px;
        }

        [data-theme="dark"] {
            --bg-canvas: #090d16;
            --bg-surface: #111827;
            --bg-sidebar: #050811;
            --text-sidebar: #94a3b8;
            --text-sidebar-active: #38bdf8;
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --border-color: #1f2937;
            --border-light: #182234;
            --accent-primary: #38bdf8;
            --accent-hover: #0284c7;
            --accent-soft: #082f49;
            --code-bg: #030712;
            --code-text: #e2e8f0;
            
            --callout-def-border: #38bdf8;
            --callout-def-bg: #082f4940;
            --callout-thm-border: #a78bfa;
            --callout-thm-bg: #2e106540;
            --callout-tip-border: #34d399;
            --callout-tip-bg: #064e3b40;
            --callout-warn-border: #fb923c;
            --callout-warn-bg: #43140740;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Source Serif 4', Georgia, serif;
            font-size: 17.5px;
            line-height: 1.85;
            color: var(--text-primary);
            background-color: var(--bg-canvas);
            display: flex;
            min-height: 100vh;
        }

        /* SIDEBAR NAVEGAÇÃO */
        .sidebar {
            width: var(--sidebar-width);
            background-color: var(--bg-sidebar);
            color: var(--text-sidebar);
            position: fixed;
            top: 0;
            left: 0;
            bottom: 0;
            overflow-y: auto;
            padding: 25px 18px;
            display: flex;
            flex-direction: column;
            gap: 18px;
            z-index: 100;
            box-shadow: 2px 0 10px rgba(0,0,0,0.15);
        }

        .sidebar-brand {
            font-family: 'Inter', sans-serif;
            font-size: 1.05rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.35;
            border-bottom: 1px solid #1e293b;
            padding-bottom: 14px;
        }

        .sidebar-brand small {
            display: block;
            font-size: 0.75rem;
            font-weight: 400;
            color: #94a3b8;
            margin-top: 4px;
        }

        .sidebar-actions {
            display: flex;
            gap: 8px;
        }

        .btn-ui {
            font-family: 'Inter', sans-serif;
            font-size: 0.8rem;
            font-weight: 600;
            padding: 8px 12px;
            border-radius: 6px;
            border: 1px solid #334155;
            background: #1e293b;
            color: #e2e8f0;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            transition: all 0.2s ease;
            text-decoration: none;
            flex: 1;
        }

        .btn-ui:hover {
            background: #334155;
            color: #38bdf8;
            border-color: #475569;
        }

        .sidebar-nav {
            font-family: 'Inter', sans-serif;
            font-size: 0.85rem;
            display: flex;
            flex-direction: column;
            gap: 6px;
            flex: 1;
        }

        .nav-category {
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #64748b;
            margin: 16px 0 4px 0;
            padding-left: 8px;
        }

        .nav-link {
            display: block;
            padding: 7px 10px;
            border-radius: 6px;
            color: var(--text-sidebar);
            text-decoration: none;
            line-height: 1.4;
            transition: all 0.15s ease;
        }

        .nav-link:hover {
            background: rgba(255,255,255,0.06);
            color: #ffffff;
            transform: translateX(3px);
        }

        .nav-link.active {
            background: rgba(56, 189, 248, 0.12);
            color: var(--text-sidebar-active);
            font-weight: 600;
        }

        /* CONTEÚDO PRINCIPAL */
        .main-wrapper {
            margin-left: var(--sidebar-width);
            flex: 1;
            padding: 50px 60px 100px 60px;
            max-width: 1040px;
        }

        /* CABEÇALHO DO DOCUMENTO */
        .doc-header {
            margin-bottom: 50px;
            padding-bottom: 30px;
            border-bottom: 2px solid var(--border-color);
        }

        .doc-title {
            font-family: 'Inter', sans-serif;
            font-size: 2.7rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            color: var(--text-primary);
            line-height: 1.15;
            margin-bottom: 12px;
        }

        .doc-meta {
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            color: var(--text-muted);
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            align-items: center;
        }

        .doc-meta span {
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }

        .badge-academic {
            background: var(--accent-soft);
            color: var(--accent-primary);
            font-size: 0.78rem;
            font-weight: 600;
            padding: 3px 9px;
            border-radius: 9999px;
            border: 1px solid rgba(37, 99, 235, 0.2);
        }

        /* TIPOGRAFIA E SEÇÕES */
        .module-chapter {
            margin-top: 60px;
            padding-top: 20px;
        }

        h1.module-title {
            font-family: 'Inter', sans-serif;
            font-size: 2.05rem;
            font-weight: 700;
            color: var(--text-primary);
            margin: 45px 0 20px 0;
            padding-bottom: 12px;
            border-bottom: 1.5px solid var(--border-color);
            display: flex;
            align-items: baseline;
            gap: 12px;
        }

        h1.module-title .module-num {
            color: var(--accent-primary);
            font-size: 1.25rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        h2 {
            font-family: 'Inter', sans-serif;
            font-size: 1.45rem;
            font-weight: 600;
            color: var(--text-primary);
            margin: 38px 0 16px 0;
        }

        h3 {
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--text-primary);
            margin: 28px 0 12px 0;
        }

        p {
            margin-bottom: 1.25rem;
            text-align: justify;
        }

        ul, ol {
            margin: 0 0 1.5rem 1.6rem;
        }

        li {
            margin-bottom: 0.45rem;
        }

        strong {
            color: var(--text-primary);
            font-weight: 600;
        }

        /* BOXES SEMÂNTICOS */
        .callout {
            border-radius: 8px;
            padding: 18px 22px;
            margin: 25px 0;
            position: relative;
            background-color: var(--bg-surface);
            border-left: 5px solid;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .callout-header {
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 8px;
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
            margin: 24px 0;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            background: var(--bg-surface);
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
            transition: all 0.2s ease;
        }

        details.proof[open] {
            border-color: var(--accent-primary);
        }

        details.proof summary {
            font-family: 'Inter', sans-serif;
            font-size: 0.92rem;
            font-weight: 600;
            color: var(--text-primary);
            padding: 12px 18px;
            cursor: pointer;
            background-color: var(--border-light);
            display: flex;
            align-items: center;
            gap: 10px;
            user-select: none;
            transition: background 0.15s ease;
        }

        details.proof summary:hover {
            background-color: var(--accent-soft);
            color: var(--accent-primary);
        }

        details.proof summary::marker {
            color: var(--accent-primary);
        }

        .proof-body {
            padding: 20px 24px;
            border-top: 1px solid var(--border-color);
            background: var(--bg-surface);
        }

        /* CARDS DE DISTRIBUIÇÃO */
        .dist-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 22px 24px;
            margin: 24px 0 32px 0;
            box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        }

        .dist-card-header {
            font-family: 'Inter', sans-serif;
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 14px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
        }

        .dist-card-header h4 {
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .dist-badge {
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            padding: 2px 8px;
            border-radius: 4px;
        }

        .badge-discrete { background: #e0f2fe; color: #0369a1; }
        .badge-continuous { background: #fef3c7; color: #92400e; }

        .dist-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 14px;
            font-family: 'Inter', sans-serif;
            font-size: 0.88rem;
            background: var(--border-light);
            padding: 14px 18px;
            border-radius: 6px;
            margin-bottom: 16px;
        }

        .dist-grid-item span.label {
            display: block;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            color: var(--text-muted);
            margin-bottom: 3px;
        }

        .dist-role {
            font-size: 0.95rem;
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px dashed var(--border-color);
        }

        /* TABELAS COMPARATIVAS */
        .table-responsive {
            overflow-x: auto;
            margin: 25px 0;
        }

        table.academic-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Inter', sans-serif;
            font-size: 0.88rem;
            background: var(--bg-surface);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        }

        table.academic-table th {
            background: #1e293b;
            color: #ffffff;
            font-weight: 600;
            text-align: left;
            padding: 12px 16px;
        }

        table.academic-table td {
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
            vertical-align: top;
        }

        table.academic-table tr:hover td {
            background-color: var(--accent-soft);
        }

        /* ABAS INTERATIVAS DE CÓDIGO */
        .code-tabs {
            margin: 25px 0;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background: var(--code-bg);
        }

        .tab-nav {
            display: flex;
            background: #0f172a;
            border-bottom: 1px solid #334155;
            padding: 4px 8px 0 8px;
        }

        .tab-btn {
            font-family: 'Inter', sans-serif;
            font-size: 0.82rem;
            font-weight: 600;
            padding: 8px 16px;
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
            padding: 18px 20px;
            overflow-x: auto;
        }

        .tab-pane.active {
            display: block;
        }

        pre code {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.84rem;
            line-height: 1.6;
            color: var(--code-text);
            background: transparent;
        }

        p code, li code {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.88em;
            background: var(--border-light);
            color: var(--accent-primary);
            padding: 2px 6px;
            border-radius: 4px;
            border: 1px solid var(--border-color);
        }

        /* RODAPÉ ACADÊMICO */
        .academic-footer {
            margin-top: 80px;
            padding-top: 30px;
            border-top: 1px solid var(--border-color);
            font-family: 'Inter', sans-serif;
            font-size: 0.85rem;
            color: var(--text-muted);
            text-align: center;
        }

        /* REGRAS ESPECÍFICAS DE IMPRESSÃO / PDF (@media print) */
        @media print {
            body {
                background: #ffffff !important;
                color: #000000 !important;
                font-size: 11pt !important;
                line-height: 1.5 !important;
                display: block !important;
            }

            .sidebar, 
            .sidebar-actions, 
            .tab-nav, 
            .theme-toggle-btn, 
            .print-btn,
            .badge-academic {
                display: none !important;
            }

            .main-wrapper {
                margin-left: 0 !important;
                padding: 0 !important;
                max-width: 100% !important;
            }

            /* Forçar abertura de todas as demonstrações recolhíveis */
            details.proof {
                display: block !important;
                border: 1px solid #cccccc !important;
                page-break-inside: avoid;
                margin: 15pt 0 !important;
            }

            details.proof summary {
                background: #f1f1f1 !important;
                color: #000000 !important;
                font-weight: bold !important;
                display: block !important;
                border-bottom: 1px solid #cccccc;
            }

            .proof-body {
                display: block !important;
                padding: 10pt !important;
            }

            /* Exibir ambos os códigos R e Python em sequência */
            .code-tabs {
                border: 1px solid #cccccc !important;
                background: #f8f9fa !important;
            }

            .tab-pane {
                display: block !important;
                padding: 10pt !important;
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

            /* Quebras de página controladas por módulo */
            .module-chapter {
                break-before: page !important;
                page-break-before: always !important;
            }

            .callout {
                border-left-width: 4px !important;
                box-shadow: none !important;
                page-break-inside: avoid;
            }

            a {
                color: #000000 !important;
                text-decoration: none !important;
            }
        }
    </style>
</head>
<body>
"""

def get_sidebar_html():
    return """
    <!-- SIDEBAR DE NAVEGAÇÃO ACADÊMICA -->
    <aside class="sidebar">
        <div class="sidebar-brand">
            Notas de Inferência
            <small>Inferência Estatística Bayesiana</small>
        </div>

        <div class="sidebar-actions">
            <button class="btn-ui" onclick="window.print()" title="Salvar em PDF ou Imprimir">
                <span>📥</span> PDF
            </button>
            <button class="btn-ui" id="themeToggleBtn" onclick="toggleTheme()" title="Alternar Modo Claro/Escuro">
                <span id="themeIcon">🌙</span> Tema
            </button>
        </div>

        <nav class="sidebar-nav">
            <div class="nav-category">Programa da Disciplina</div>
            <a href="#modulo1" class="nav-link">1. Fundamentos & Modelos</a>
            <a href="#modulo2" class="nav-link">2. Priori, Posteriori & Preditiva</a>
            <a href="#modulo3" class="nav-link">3. Famílias Conjugadas</a>
            <a href="#modulo4" class="nav-link">4. Decisão, Estimação & Hipóteses</a>
            <a href="#modulo5" class="nav-link">5. Computação Bayesiana (MCMC)</a>
            <a href="#modulo6" class="nav-link">6. Modelos Lineares & ANOVA</a>
            
            <div class="nav-category">Acesso Rápido</div>
            <a href="#catalogo-discretas" class="nav-link">→ Modelos Discretos</a>
            <a href="#catalogo-continuas" class="nav-link">→ Modelos Contínuos</a>
            <a href="#priori-jeffreys" class="nav-link">→ Regra de Jeffreys</a>
            <a href="#pares-conjugados" class="nav-link">→ Pares Conjugados</a>
            <a href="#fator-bayes" class="nav-link">→ Fator de Bayes</a>
            <a href="#lab-mcmc" class="nav-link">→ Laboratório MCMC (R & Py)</a>
        </nav>
    </aside>

    <main class="main-wrapper">
        <header class="doc-header">
            <div class="badge-academic">Livro Digital Acadêmico</div>
            <h1 class="doc-title">Notas de Inferência Estatística Bayesiana</h1>
            <div class="doc-meta">
                <span><strong>Autor:</strong> Luca Ferreira Barboza</span>
                <span>•</span>
                <span><strong>Disciplina:</strong> Inferência Estatística</span>
                <span>•</span>
                <span><strong>Formato:</strong> Interativo com Suporte a PDF</span>
            </div>
        </header>
"""

def get_footer_and_scripts():
    return """
        <footer class="academic-footer">
            <p><strong>Notas de Aula de Inferência Estatística Bayesiana</strong></p>
            <p>Elaborado por Luca Ferreira Barboza • Baseado no programa oficial da disciplina.</p>
            <p><small>Material diagramado com suporte a fórmulas matemáticas vetoriais (MathJax 3) e visualização de código lado a lado.</small></p>
        </footer>
    </main>

    <script>
        // Alternador de Tema Claro / Escuro
        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        }

        function updateThemeIcon(theme) {
            const icon = document.getElementById('themeIcon');
            if (icon) {
                icon.textContent = theme === 'dark' ? '☀️' : '🌙';
            }
        }

        // Carregar tema salvo
        (function() {
            const savedTheme = localStorage.getItem('theme') || 'light';
            document.documentElement.setAttribute('data-theme', savedTheme);
            updateThemeIcon(savedTheme);
        })();

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

        // Destaque de Link Ativo na Sidebar ao Rolar a Página
        window.addEventListener('DOMContentLoaded', () => {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const id = entry.target.getAttribute('id');
                        document.querySelectorAll('.sidebar-nav .nav-link').forEach(link => {
                            if (link.getAttribute('href') === `#${id}`) {
                                link.classList.add('active');
                            } else if (link.getAttribute('href').startsWith('#modulo')) {
                                link.classList.remove('active');
                            }
                        });
                    }
                });
            }, { rootMargin: '-20% 0px -70% 0px' });

            document.querySelectorAll('section[id]').forEach(section => {
                observer.observe(section);
            });
        });
    </script>
</body>
</html>
"""
