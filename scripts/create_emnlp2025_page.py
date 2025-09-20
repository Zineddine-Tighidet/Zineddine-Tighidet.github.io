#!/usr/bin/env python3
import os

def create_emnlp2025_page():
    """Create project page for EMNLP 2025 paper"""
    filename = "project-emnlp2025-advanced-mechanistic-interpretability.html"
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Mechanistic Interpretability for Knowledge Processing - Zineddine Tighidet</title>
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
        <a href="../index.html">← Back to Home</a>
    </div>
    
    <h1>Advanced Mechanistic Interpretability for Knowledge Processing in Language Models</h1>
    
    <div class="paper-meta">
        <div class="meta-item">
            <span class="meta-label">Authors:</span> Zineddine Tighidet, et al.
        </div>
        <div class="meta-item">
            <span class="meta-label">Venue:</span> EMNLP 2025
        </div>
        <div class="meta-item">
            <span class="meta-label">Year:</span> 2025
        </div>
    </div>
    
    <div class="abstract">
        <strong>Abstract:</strong><br>
        This paper presents advanced mechanistic interpretability techniques for understanding how language models process and integrate knowledge. We develop novel methods to analyze the internal mechanisms of transformer architectures, focusing on knowledge source attribution and the resolution of conflicts between parametric and contextual information. Our approach provides deeper insights into model behavior and offers practical strategies for mitigating hallucinations through improved understanding of knowledge processing pathways.
    </div>
    
    <div class="section">
        <h2>Key Contributions</h2>
        <ul>
            <li>Novel mechanistic interpretability framework for knowledge processing analysis</li>
            <li>Advanced techniques for understanding parametric vs contextual knowledge integration</li>
            <li>Comprehensive analysis of attention mechanisms in knowledge attribution</li>
            <li>Practical methodologies for hallucination detection and mitigation</li>
            <li>Scalable approaches for analyzing large language models</li>
            <li>Empirical evaluation across multiple model architectures and knowledge domains</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Methodology</h2>
        <p>We employ state-of-the-art mechanistic interpretability techniques combined with controlled experiments to analyze knowledge processing in language models. Our methodology includes:</p>
        
        <ul>
            <li><strong>Knowledge Source Attribution:</strong> Developing probes to identify when models rely on parametric vs contextual knowledge</li>
            <li><strong>Attention Analysis:</strong> Examining attention patterns during knowledge integration processes</li>
            <li><strong>Activation Studies:</strong> Analyzing internal representations during knowledge conflicts</li>
            <li><strong>Intervention Experiments:</strong> Controlled studies to understand causal relationships</li>
        </ul>
        
        <p>The approach combines theoretical insights from mechanistic interpretability with practical evaluation methods to provide comprehensive understanding of model behavior.</p>
    </div>
    
    <div class="section">
        <h2>Key Findings</h2>
        <ul>
            <li>Language models exhibit distinct processing patterns for different knowledge sources</li>
            <li>Attention mechanisms play a crucial role in knowledge source attribution</li>
            <li>Models show systematic biases when faced with conflicting information</li>
            <li>Knowledge integration follows predictable pathways that can be analyzed and controlled</li>
            <li>Hallucination patterns correlate with specific attention and activation patterns</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Technical Innovation</h2>
        <p>This work introduces several technical innovations in mechanistic interpretability:</p>
        
        <ul>
            <li><strong>Multi-scale Analysis:</strong> Techniques for analyzing knowledge processing at different architectural levels</li>
            <li><strong>Dynamic Probing:</strong> Methods for probing model behavior during inference</li>
            <li><strong>Causal Intervention:</strong> Controlled experiments to establish causal relationships</li>
            <li><strong>Scalable Frameworks:</strong> Approaches that work across different model sizes and architectures</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Impact and Applications</h2>
        <p>This research has significant implications for the field of mechanistic interpretability and language model development:</p>
        
        <ul>
            <li><strong>Model Safety:</strong> Improved understanding of hallucination mechanisms enables better safety measures</li>
            <li><strong>Model Development:</strong> Insights can guide the design of more reliable language models</li>
            <li><strong>Evaluation Methods:</strong> New frameworks for evaluating model knowledge processing capabilities</li>
            <li><strong>Practical Applications:</strong> Techniques applicable to real-world deployment scenarios</li>
        </ul>
        
        <p>The findings contribute to the broader goal of developing more interpretable, reliable, and trustworthy language models.</p>
    </div>
    
    <div class="links">
        <a href="../assets/emnlp2025.pdf" target="_blank">Paper PDF</a>
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
    
    # Generate EMNLP 2025 project page
    filename, content = create_emnlp2025_page()
    filepath = os.path.join('projects', filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Created: {filepath}")

if __name__ == "__main__":
    main()
