# -*- coding: utf-8 -*-
"""
Script Principal de Construção do Livro Digital de Inferência Estatística Bayesiana.
Monta os módulos e gera os arquivos finais notas_inferencia_estatistica.html e index.html.
"""

import sys
import os

# Adiciona o diretório builder ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from header_and_styles import get_head_and_styles, get_sidebar_html, get_footer_and_scripts
from module1 import get_module1_html
from module2 import get_module2_html
from module3 import get_module3_html
from module4 import get_module4_html
from module5 import get_module5_html
from module6 import get_module6_html

def build_full_html():
    parts = [
        get_head_and_styles(),
        get_sidebar_html(),
        get_module1_html(),
        get_module2_html(),
        get_module3_html(),
        get_module4_html(),
        get_module5_html(),
        get_module6_html(),
        get_footer_and_scripts()
    ]
    return "".join(parts)

def main():
    base_dir = os.path.dirname(current_dir)
    target_main = os.path.join(base_dir, "notas_inferencia_estatistica.html")
    target_index = os.path.join(base_dir, "index.html")

    print("[*] Montando HTML completo dos 6 módulos...")
    full_html = build_full_html()

    print(f"[*] Gravando arquivo principal: {target_main}")
    with open(target_main, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"[*] Gravando cópia index: {target_index}")
    with open(target_index, "w", encoding="utf-8") as f:
        f.write(full_html)

    file_size_kb = len(full_html.encode("utf-8")) / 1024
    print(f"[OK] Construção concluída com sucesso! Tamanho final: {file_size_kb:.1f} KB")

if __name__ == "__main__":
    main()
