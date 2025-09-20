#!/usr/bin/env python3
import os
import re

def add_logos_to_project_page(filepath):
    """Add ArXiv and GitHub logos to project page"""
    
    # Read the current file
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Define the new links section with logos
    new_links_section = '''        .links a {
            display: inline-block;
            margin-right: 15px;
            margin-bottom: 10px;
            padding: 10px 20px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .links a:hover {
            background: #0056b3;
        }
        
        .links a.secondary {
            background: #6c757d;
        }
        
        .links a.secondary:hover {
            background: #545b62;
        }
        
        .links a.github {
            background: #24292e;
        }
        
        .links a.github:hover {
            background: #1a1e22;
        }
        
        .links a.arxiv {
            background: #b31b1b;
        }
        
        .links a.arxiv:hover {
            background: #8b0000;
        }
        
        .logo {
            width: 16px;
            height: 16px;
            fill: currentColor;
        }'''
    
    # Replace the CSS section
    content = re.sub(
        r'\.links a \{[^}]+\}',
        new_links_section,
        content,
        flags=re.DOTALL
    )
    
    # Define the new links HTML with logos
    new_links_html = '''    <div class="links">
        <a href="../assets/emnlp2025.pdf" target="_blank" class="arxiv">
            <svg class="logo" viewBox="0 0 24 24">
                <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
            </svg>
            Paper PDF
        </a>
        <a href="#" target="_blank" class="github">
            <svg class="logo" viewBox="0 0 24 24">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            Code Repository
        </a>
        <a href="#" target="_blank">
            <svg class="logo" viewBox="0 0 24 24">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
            </svg>
            Dataset
        </a>
        <a href="https://scholar.google.com/citations?user=jgle1SAAAAAJ&hl=en" target="_blank" class="secondary">
            <svg class="logo" viewBox="0 0 24 24">
                <path d="M5.242 13.769L0 9.5 12 0l12 9.5-5.242 4.269C17.548 11.249 14.978 9.5 12 9.5s-5.548 1.749-6.758 4.269zM12 10a7 7 0 1 0 0 14 7 7 0 0 0 0-14z"/>
            </svg>
            Google Scholar
        </a>
    </div>'''
    
    # Replace the links section
    content = re.sub(
        r'<div class="links">.*?</div>',
        new_links_html,
        content,
        flags=re.DOTALL
    )
    
    # Write the updated content back
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Updated: {filepath}")

def main():
    # Update all project pages
    project_files = [
        'projects/project-emnlp2025-advanced-mechanistic-interpretability.html',
        'projects/project-blackboxnlp2024-probing-language-models-knowledge-source.html',
        'projects/project-alta2022-fine-tuning-parsing-distinction.html'
    ]
    
    for filepath in project_files:
        if os.path.exists(filepath):
            add_logos_to_project_page(filepath)
        else:
            print(f"File not found: {filepath}")

if __name__ == "__main__":
    main()
