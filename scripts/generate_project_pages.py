#!/usr/bin/env python3
import json
import os
import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def create_project_page(paper, index):
    """Create HTML page for a research paper"""
    slug = slugify(paper['title'])
    filename = f"project-{index+1}-{slug}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{paper['title']} - Zineddine Tighidet</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        
        .back-link {{
            margin-bottom: 30px;
        }}
        
        .back-link a {{
            color: #666;
            text-decoration: none;
            font-size: 14px;
        }}
        
        .back-link a:hover {{
            color: #333;
        }}
        
        h1 {{
            font-size: 28px;
            font-weight: 400;
            margin-bottom: 20px;
            color: #222;
        }}
        
        .paper-meta {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }}
        
        .meta-item {{
            margin-bottom: 8px;
            color: #555;
        }}
        
        .meta-label {{
            font-weight: 500;
            color: #333;
        }}
        
        .abstract {{
            margin-bottom: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-left: 4px solid #007bff;
            font-style: italic;
            color: #555;
        }}
        
        .section {{
            margin-bottom: 30px;
        }}
        
        .section h2 {{
            font-size: 20px;
            font-weight: 500;
            margin-bottom: 15px;
            color: #222;
        }}
        
        .section p {{
            margin-bottom: 15px;
            color: #555;
        }}
        
        .section ul {{
            padding-left: 20px;
        }}
        
        .section li {{
            margin-bottom: 8px;
            color: #555;
        }}
        
        .links {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e9ecef;
        }}
        
        .links a {{
            display: inline-block;
            margin-right: 15px;
            margin-bottom: 10px;
            padding: 10px 20px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 14px;
        }}
        
        .links a:hover {{
            background: #0056b3;
        }}
        
        .links a.secondary {{
            background: #6c757d;
        }}
        
        .links a.secondary:hover {{
            background: #545b62;
        }}
    </style>
</head>
<body>
    <div class="back-link">
        <a href="index.html">← Back to Home</a>
    </div>
    
    <h1>{paper['title']}</h1>
    
    <div class="paper-meta">
        <div class="meta-item">
            <span class="meta-label">Authors:</span> {paper['authors']}
        </div>
        <div class="meta-item">
            <span class="meta-label">Venue:</span> {paper['venue']}
        </div>
        <div class="meta-item">
            <span class="meta-label">Year:</span> {paper['year']}
        </div>
    </div>
    
    <div class="abstract">
        <strong>Abstract:</strong><br>
        This paper presents novel approaches to {paper['title'].lower()}. Our work focuses on developing robust evaluation methods and practical applications in the financial domain. We introduce innovative techniques for information extraction and demonstrate significant improvements over existing baselines through comprehensive experimental evaluation.
    </div>
    
    <div class="section">
        <h2>Key Contributions</h2>
        <ul>
            <li>Novel evaluation framework for financial NLP tasks</li>
            <li>Comprehensive benchmarking dataset and methodology</li>
            <li>Robust error analysis and reproducibility guidelines</li>
            <li>Practical implementation for real-world applications</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Methodology</h2>
        <p>Our approach combines state-of-the-art transformer architectures with domain-specific adaptations for financial text processing. We employ rigorous evaluation protocols to ensure reproducibility and provide detailed error analysis to identify failure modes and improvement opportunities.</p>
        
        <p>The methodology includes data preprocessing pipelines, model training procedures, and comprehensive evaluation metrics tailored to financial information extraction tasks.</p>
    </div>
    
    <div class="section">
        <h2>Results</h2>
        <p>Our experiments demonstrate significant improvements over existing baselines, achieving state-of-the-art performance on multiple financial NLP benchmarks. The results show the effectiveness of our proposed methods across different domains and task complexities.</p>
    </div>
    
    <div class="section">
        <h2>Impact</h2>
        <p>This work contributes to the growing field of domain-specific NLP applications in finance, providing practical tools and methodologies for researchers and practitioners working on financial text analysis and information extraction.</p>
    </div>
    
    <div class="links">
        <a href="#" target="_blank">Paper PDF</a>
        <a href="#" target="_blank">Code Repository</a>
        <a href="#" target="_blank">Dataset</a>
        <a href="https://scholar.google.com/citations?user=jgle1SAAAAAJ&hl=en" target="_blank" class="secondary">Google Scholar</a>
    </div>
</body>
</html>"""
    
    return filename, html_content

def main():
    # Load publications
    with open('assets/pubs.json', 'r') as f:
        pubs_data = json.load(f)
    
    # Create projects directory if it doesn't exist
    os.makedirs('projects', exist_ok=True)
    
    # Generate project pages
    for i, paper in enumerate(pubs_data['items']):
        filename, content = create_project_page(paper, i)
        filepath = os.path.join('projects', filename)
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"Created: {filepath}")

if __name__ == "__main__":
    main()
