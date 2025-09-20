#!/usr/bin/env python3
import json
import os
import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def create_blackboxnlp_page():
    """Create project page for BlackBoxNLP 2024 paper"""
    filename = "project-blackboxnlp2024-probing-language-models-knowledge-source.html"
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Probing Language Models on Their Knowledge Source - Zineddine Tighidet</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        .back-link {
            margin-bottom: 30px;
        }
        
        .back-link a {
            color: #666;
            text-decoration: none;
            font-size: 14px;
        }
        
        .back-link a:hover {
            color: #333;
        }
        
        h1 {
            font-size: 28px;
            font-weight: 400;
            margin-bottom: 20px;
            color: #222;
        }
        
        .paper-meta {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        
        .meta-item {
            margin-bottom: 8px;
            color: #555;
        }
        
        .meta-label {
            font-weight: 500;
            color: #333;
        }
        
        .abstract {
            margin-bottom: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-left: 4px solid #007bff;
            font-style: italic;
            color: #555;
        }
        
        .section {
            margin-bottom: 30px;
        }
        
        .section h2 {
            font-size: 20px;
            font-weight: 500;
            margin-bottom: 15px;
            color: #222;
        }
        
        .section p {
            margin-bottom: 15px;
            color: #555;
        }
        
        .section ul {
            padding-left: 20px;
        }
        
        .section li {
            margin-bottom: 8px;
            color: #555;
        }
        
        .links {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e9ecef;
        }
        
        .links a {
            display: inline-block;
            margin-right: 15px;
            margin-bottom: 10px;
            padding: 10px 20px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 14px;
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
    </style>
</head>
<body>
    <div class="back-link">
        <a href="index.html">← Back to Home</a>
    </div>
    
    <h1>Probing Language Models on Their Knowledge Source</h1>
    
    <div class="paper-meta">
        <div class="meta-item">
            <span class="meta-label">Authors:</span> Z Tighidet, A Mogini, J Mei, B Piwowarski, P Gallinari
        </div>
        <div class="meta-item">
            <span class="meta-label">Venue:</span> BlackBoxNLP@EMNLP2024
        </div>
        <div class="meta-item">
            <span class="meta-label">Year:</span> 2024
        </div>
    </div>
    
    <div class="abstract">
        <strong>Abstract:</strong><br>
        This paper investigates how language models handle different sources of knowledge, particularly focusing on the interplay between parametric and contextual knowledge. We develop probing techniques to understand when models rely on their training data versus contextual information, with implications for mitigating hallucinations in language models. Our approach combines mechanistic interpretability with controlled experiments to analyze knowledge source attribution in transformer architectures.
    </div>
    
    <div class="section">
        <h2>Key Contributions</h2>
        <ul>
            <li>Novel probing methodology for knowledge source attribution in language models</li>
            <li>Analysis of parametric vs contextual knowledge conflicts and their resolution</li>
            <li>Framework for understanding model knowledge behavior under different conditions</li>
            <li>Insights for hallucination mitigation strategies through knowledge source control</li>
            <li>Empirical evaluation on multiple model architectures and knowledge domains</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Methodology</h2>
        <p>We employ mechanistic interpretability techniques combined with controlled probing experiments to analyze how language models process and integrate different knowledge sources. Our approach includes systematic evaluation of model responses under various knowledge conflict scenarios, where parametric knowledge (from training) conflicts with contextual information.</p>
        
        <p>The methodology involves designing specific probes that can distinguish between different knowledge sources, using attention analysis and activation patterns to understand the internal mechanisms of knowledge processing. We evaluate our approach on multiple transformer architectures and knowledge domains to ensure generalizability.</p>
    </div>
    
    <div class="section">
        <h2>Key Findings</h2>
        <ul>
            <li>Language models show distinct patterns when processing parametric vs contextual knowledge</li>
            <li>Attention mechanisms play a crucial role in knowledge source attribution</li>
            <li>Models exhibit different behaviors when faced with conflicting knowledge sources</li>
            <li>Probing techniques can effectively identify knowledge source preferences</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Impact</h2>
        <p>This work contributes to mechanistic interpretability research by providing insights into how language models handle knowledge conflicts. The findings have direct applications to reducing hallucinations and improving model reliability, particularly in scenarios where models must balance different sources of information.</p>
        
        <p>The probing techniques developed in this work can be used by researchers and practitioners to better understand model behavior and develop more robust language models that can handle conflicting information more effectively.</p>
    </div>
    
    <div class="links">
        <a href="assets/blackboxnlp2024.pdf" target="_blank">Paper PDF</a>
        <a href="#" target="_blank">Code Repository</a>
        <a href="#" target="_blank">Dataset</a>
        <a href="https://scholar.google.com/citations?user=jgle1SAAAAAJ&hl=en" target="_blank" class="secondary">Google Scholar</a>
    </div>
</body>
</html>"""
    
    return filename, html_content

def create_alta2022_page():
    """Create project page for ALTA 2022 paper"""
    filename = "project-alta2022-fine-tuning-parsing-distinction.html"
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fine-tuning a Subtle Parsing Distinction Using a Probabilistic Decision Tree - Zineddine Tighidet</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        .back-link {
            margin-bottom: 30px;
        }
        
        .back-link a {
            color: #666;
            text-decoration: none;
            font-size: 14px;
        }
        
        .back-link a:hover {
            color: #333;
        }
        
        h1 {
            font-size: 28px;
            font-weight: 400;
            margin-bottom: 20px;
            color: #222;
        }
        
        .paper-meta {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        
        .meta-item {
            margin-bottom: 8px;
            color: #555;
        }
        
        .meta-label {
            font-weight: 500;
            color: #333;
        }
        
        .abstract {
            margin-bottom: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-left: 4px solid #007bff;
            font-style: italic;
            color: #555;
        }
        
        .section {
            margin-bottom: 30px;
        }
        
        .section h2 {
            font-size: 20px;
            font-weight: 500;
            margin-bottom: 15px;
            color: #222;
        }
        
        .section p {
            margin-bottom: 15px;
            color: #555;
        }
        
        .section ul {
            padding-left: 20px;
        }
        
        .section li {
            margin-bottom: 8px;
            color: #555;
        }
        
        .links {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e9ecef;
        }
        
        .links a {
            display: inline-block;
            margin-right: 15px;
            margin-bottom: 10px;
            padding: 10px 20px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 14px;
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
    </style>
</head>
<body>
    <div class="back-link">
        <a href="index.html">← Back to Home</a>
    </div>
    
    <h1>Fine-tuning a Subtle Parsing Distinction Using a Probabilistic Decision Tree: the Case of Postnominal "that" in Noun Complement Clauses vs. Relative Clauses</h1>
    
    <div class="paper-meta">
        <div class="meta-item">
            <span class="meta-label">Authors:</span> Z Tighidet, N Ballier
        </div>
        <div class="meta-item">
            <span class="meta-label">Venue:</span> ALTA2022
        </div>
        <div class="meta-item">
            <span class="meta-label">Year:</span> 2022
        </div>
    </div>
    
    <div class="abstract">
        <strong>Abstract:</strong><br>
        This paper addresses a subtle parsing distinction in English grammar, specifically the postnominal 'that' in noun complement clauses versus relative clauses. We develop a probabilistic decision tree approach to fine-tune models on this challenging linguistic distinction. The work demonstrates how machine learning techniques can be applied to handle nuanced grammatical phenomena that are difficult for traditional parsing approaches.
    </div>
    
    <div class="section">
        <h2>Key Contributions</h2>
        <ul>
            <li>Probabilistic decision tree approach for subtle parsing distinctions</li>
            <li>Fine-tuning methodology for grammatical nuances in English</li>
            <li>Analysis of postnominal 'that' parsing challenges</li>
            <li>Evaluation framework for grammatical parsing tasks</li>
            <li>Comparison with traditional parsing approaches</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Methodology</h2>
        <p>We employ probabilistic decision trees combined with fine-tuning techniques to address the challenging distinction between noun complement clauses and relative clauses. The approach includes careful annotation and evaluation protocols to ensure accurate classification of these subtle grammatical structures.</p>
        
        <p>The methodology involves creating a dataset of carefully annotated examples, training probabilistic decision trees on linguistic features, and fine-tuning the models to improve performance on this specific grammatical distinction. We evaluate the approach using standard parsing metrics and compare it with existing methods.</p>
    </div>
    
    <div class="section">
        <h2>Linguistic Challenge</h2>
        <p>The distinction between noun complement clauses and relative clauses with postnominal 'that' is particularly challenging because:</p>
        <ul>
            <li>Both structures use similar syntactic patterns</li>
            <li>Contextual cues are often subtle and require deep linguistic understanding</li>
            <li>Traditional rule-based approaches struggle with ambiguous cases</li>
            <li>Machine learning approaches need careful feature engineering</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Results</h2>
        <p>Our probabilistic decision tree approach achieves significant improvements over baseline methods in distinguishing between noun complement clauses and relative clauses. The fine-tuning process allows the model to learn subtle linguistic patterns that are difficult to capture with traditional approaches.</p>
    </div>
    
    <div class="section">
        <h2>Impact</h2>
        <p>This work contributes to computational linguistics by developing methods for handling subtle grammatical distinctions. The findings have implications for improving parsing accuracy and linguistic understanding in NLP systems, particularly for applications that require precise grammatical analysis.</p>
        
        <p>The probabilistic decision tree approach can be extended to other challenging grammatical phenomena, providing a framework for addressing similar linguistic challenges in different languages and contexts.</p>
    </div>
    
    <div class="links">
        <a href="assets/alta2022.pdf" target="_blank">Paper PDF</a>
        <a href="#" target="_blank">Code Repository</a>
        <a href="#" target="_blank">Dataset</a>
        <a href="https://scholar.google.com/citations?user=jgle1SAAAAAJ&hl=en" target="_blank" class="secondary">Google Scholar</a>
    </div>
</body>
</html>"""
    
    return filename, html_content

def main():
    # Create projects directory if it doesn't exist
    os.makedirs('projects', exist_ok=True)
    
    # Generate BlackBoxNLP 2024 project page
    filename1, content1 = create_blackboxnlp_page()
    filepath1 = os.path.join('projects', filename1)
    with open(filepath1, 'w') as f:
        f.write(content1)
    print(f"Created: {filepath1}")
    
    # Generate ALTA 2022 project page
    filename2, content2 = create_alta2022_page()
    filepath2 = os.path.join('projects', filename2)
    with open(filepath2, 'w') as f:
        f.write(content2)
    print(f"Created: {filepath2}")

if __name__ == "__main__":
    main()
