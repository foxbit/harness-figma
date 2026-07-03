#!/usr/bin/env python3
import sys
import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def analyze_website(url):
    print(f"Analisando o site: {url}")
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 1. Extração de Cores (via inline styles e classes CSS comuns se possível, ou analisando o HTML)
        colors = set()
        # Procura por hex colors no HTML e CSS inline
        hex_pattern = re.compile(r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b')
        for match in hex_pattern.finditer(response.text):
            color = match.group(0).upper()
            if len(color) == 4: # expand short hex
                color = '#' + color[1]*2 + color[2]*2 + color[3]*2
            colors.add(color)
            
        # Filtra cores muito comuns como branco puro ou preto se houver muitas
        unique_colors = list(colors)[:10] # limit to top 10 for now
        
        # 2. Extração de Fontes
        fonts = set()
        # Procura por font-family no HTML
        font_family_pattern = re.compile(r'font-family\s*:\s*([^;\}]+)')
        for match in font_family_pattern.finditer(response.text):
            font_list = [f.strip().strip('"\'') for f in match.group(1).split(',')]
            for font in font_list:
                if font and font not in ['sans-serif', 'serif', 'monospace', 'inherit', 'initial']:
                    fonts.add(font)
                    
        # Também procura links do Google Fonts
        google_font_pattern = re.compile(r'fonts\.googleapis\.com/css2\?family=([^&"\' >]+)')
        for match in google_font_pattern.finditer(response.text):
            font_name = match.group(1).split(':')[0].replace('+', ' ')
            fonts.add(font_name)
            
        unique_fonts = list(fonts)[:5]
        
        # 3. Informações de Metadados
        title = soup.title.string.strip() if soup.title else ""
        description = ""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            description = meta_desc.get('content', '').strip()
            
        return {
            "success": True,
            "title": title,
            "description": description,
            "colors": unique_colors,
            "fonts": unique_fonts,
            "url": url
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def analyze_file(file_path):
    print(f"Analisando o arquivo: {file_path}")
    if not os.path.exists(file_path):
        return {"success": False, "error": "Arquivo não encontrado"}
        
    try:
        # Se for um arquivo de texto/markdown/html
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        colors = set()
        hex_pattern = re.compile(r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b')
        for match in hex_pattern.finditer(content):
            color = match.group(0).upper()
            if len(color) == 4:
                color = '#' + color[1]*2 + color[2]*2 + color[3]*2
            colors.add(color)
            
        fonts = set()
        font_pattern = re.compile(r'font-family\s*:\s*([^;\}]+)')
        for match in font_pattern.finditer(content):
            font_list = [f.strip().strip('"\'') for f in match.group(1).split(',')]
            for font in font_list:
                if font not in ['sans-serif', 'serif', 'monospace', 'inherit', 'initial']:
                    fonts.add(font)
                    
        return {
            "success": True,
            "colors": list(colors)[:10],
            "fonts": list(fonts)[:5],
            "file_path": file_path
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 analyze_brand.py <url_ou_caminho_arquivo>")
        sys.exit(1)
        
    target = sys.argv[1]
    if target.startswith(('http://', 'https://')) or '.' in target and '/' not in target:
        result = analyze_website(target)
    else:
        result = analyze_file(target)
        
    import json
    print(json.dumps(result, indent=2))
