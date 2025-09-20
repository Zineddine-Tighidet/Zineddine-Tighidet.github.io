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
    
    # Define research descriptions based on the actual papers
    descriptions = {
        0: {
            "abstract": "This paper investigates how language models handle different sources of knowledge, particularly focusing on the interplay between parametric and contextual knowledge. We develop probing techniques to understand when models rely on their training data versus contextual information, with implications for mitigating hallucinations in language models.",
            "contributions": [
                "Novel probing methodology for knowledge source attribution",
                "Analysis of parametric vs contextual knowledge conflicts",
                "Framework for understanding model knowledge behavior",
                "Insights for hallucination mitigation strategies"
            ],
            "methodology": "We employ mechanistic interpretability techniques combined with controlled probing experiments to analyze how language models process and integrate different knowledge sources. Our approach includes systematic evaluation of model responses under various knowledge conflict scenarios.",
            "impact": "This work contributes to mechanistic interpretability research by providing insights into how language models handle knowledge conflicts, with direct applications to reducing hallucinations and improving model reliability."
        },
        1: {
            "abstract": "This work presents a joint approach for dimensionality reduction and classification, combining these traditionally separate tasks into a unified framework. The method demonstrates improved performance by leveraging the interplay between feature reduction and classification objectives.",
            "contributions": [
                "Joint dimensionality reduction and classification framework",
                "Novel optimization approach for combined objectives",
                "Empirical validation on multiple datasets",
                "Theoretical analysis of joint optimization benefits"
            ],
            "methodology": "We develop a unified optimization framework that simultaneously learns dimensionality reduction transformations and classification boundaries. The approach uses joint loss functions that balance reconstruction quality with classification performance.",
            "impact": "This research advances machine learning methodology by showing how joint optimization can improve both dimensionality reduction and classification performance, with applications across various domains."
        },
        2: {
            "abstract": "This paper addresses a subtle parsing distinction in English grammar, specifically the postnominal 'that' in noun complement clauses versus relative clauses. We develop a probabilistic decision tree approach to fine-tune models on this challenging linguistic distinction.",
            "contributions": [
                "Probabilistic decision tree for subtle parsing distinctions",
                "Fine-tuning methodology for grammatical nuances",
                "Analysis of postnominal 'that' parsing challenges",
                "Evaluation framework for grammatical parsing tasks"
            ],
            "methodology": "We employ probabilistic decision trees combined with fine-tuning techniques to address the challenging distinction between noun complement clauses and relative clauses. The approach includes careful annotation and evaluation protocols.",
            "impact": "This work contributes to computational linguistics by developing methods for handling subtle grammatical distinctions, with implications for improving parsing accuracy and linguistic understanding in NLP systems."
        }
    }
    
    desc = descriptions.get(index, descriptions[0])
    
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
        {desc['abstract']}
    </div>
    
    <div class="section">
        <h2>Key Contributions</h2>
        <ul>
            {''.join([f'<li>{cont}</li>' for cont in desc['contributions']])}
        </ul>
    </div>
    
    <div class="section">
        <h2>Methodology</h2>
        <p>{desc['methodology']}</p>
    </div>
    
    <div class="section">
        <h2>Impact</h2>
        <p>{desc['impact']}</p>
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
