from flask import Flask, request, jsonify, render_template_string
import requests
import json
import os
from datetime import datetime

app = Flask(__name__)

# HTML template with SEO optimization
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PromptNest - FREE AI Prompt Generator | 1000+ Best ChatGPT, Midjourney & Claude Prompts 2025</title>
    <meta name="description" content="Get the best AI prompts instantly! 1000+ FREE prompts for ChatGPT, Midjourney, Claude & DALL-E. Generate viral content, stunning art & professional copy in seconds. Used by 50,000+ creators daily!">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }
        .glass { backdrop-filter: blur(16px); background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }
        .prompt-card { transition: all 0.3s ease; }
        .prompt-card:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.2); }
    </style>
</head>
<body>
    <div class="min-h-screen py-8">
        <div class="container mx-auto px-4">
            <div class="text-center mb-12">
                <h1 class="text-4xl md:text-6xl font-bold text-white mb-4">
                    <i class="fas fa-magic text-yellow-400 mr-4"></i>PromptNest
                </h1>
                <p class="text-xl text-white/90 max-w-3xl mx-auto">
                    Generate platform-specific AI prompts instantly. Free, powerful, and optimized for ChatGPT, Midjourney, Claude & DALL-E.
                </p>
            </div>

            <div class="max-w-4xl mx-auto mb-12">
                <div class="glass rounded-2xl p-8 shadow-2xl">
                    <h2 class="text-2xl font-bold text-white mb-6 text-center">
                        <i class="fas fa-robot text-cyan-400 mr-3"></i>AI Prompt Generator
                    </h2>
                    
                    <div class="glass rounded-lg p-4 mb-6">
                        <p class="text-white/90 text-sm font-medium mb-2">How to use:</p>
                        <div class="text-white/80 text-sm space-y-1">
                            <p>• "Create prompt for <strong class="text-cyan-300">ChatGPT</strong> to write professional emails"</p>
                            <p>• "Generate <strong class="text-purple-300">Midjourney</strong> prompt for realistic portraits"</p>
                            <p>• "Make <strong class="text-orange-300">Claude</strong> prompt for data analysis"</p>
                        </div>
                    </div>
                    
                    <form id="promptForm" class="space-y-4">
                        <div class="flex flex-col md:flex-row gap-4">
                            <input type="text" id="promptInput" 
                                placeholder="e.g., 'Create ChatGPT prompt for writing emails'"
                                class="flex-1 px-6 py-4 bg-white/20 backdrop-blur-sm border border-white/30 rounded-xl text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-cyan-400"
                                required>
                            <button type="submit"
                                class="px-8 py-4 bg-gradient-to-r from-cyan-500 to-purple-500 hover:from-cyan-600 hover:to-purple-600 text-white font-semibold rounded-xl transition-all duration-300 transform hover:scale-105 shadow-lg">
                                <i class="fas fa-magic mr-2"></i>Generate Prompts
                            </button>
                        </div>
                    </form>
                    
                    <div id="loading" class="hidden text-center py-8">
                        <i class="fas fa-spinner fa-spin text-4xl text-cyan-400 mb-4"></i>
                        <p class="text-white">Generating your perfect prompts...</p>
                    </div>
                    
                    <div id="results" class="hidden mt-8 space-y-6"></div>
                </div>
            </div>

            <div class="max-w-4xl mx-auto">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="glass rounded-xl p-6 text-center">
                        <i class="fas fa-lightbulb text-4xl text-yellow-400 mb-4"></i>
                        <h3 class="text-2xl font-bold text-white mb-2">1000+</h3>
                        <p class="text-white/80">Free AI Prompts</p>
                    </div>
                    <div class="glass rounded-xl p-6 text-center">
                        <i class="fas fa-users text-4xl text-green-400 mb-4"></i>
                        <h3 class="text-2xl font-bold text-white mb-2">50,000+</h3>
                        <p class="text-white/80">Daily Users</p>
                    </div>
                    <div class="glass rounded-xl p-6 text-center">
                        <i class="fas fa-star text-4xl text-orange-400 mb-4"></i>
                        <h3 class="text-2xl font-bold text-white mb-2">4.9/5</h3>
                        <p class="text-white/80">User Rating</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('promptForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const input = document.getElementById('promptInput').value;
            const loading = document.getElementById('loading');
            const results = document.getElementById('results');
            
            if (!input.trim()) return;
            loading.classList.remove('hidden');
            results.classList.add('hidden');
            
            try {
                const response = await fetch('/api/generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt: input })
                });
                const data = await response.json();
                loading.classList.add('hidden');
                
                if (data.success && data.prompts && data.prompts.length > 0) {
                    displayResults(data.prompts);
                } else {
                    displayError('Failed to generate prompts. Please try again.');
                }
            } catch (error) {
                loading.classList.add('hidden');
                displayError('Network error. Please check your connection and try again.');
            }
        });
        
        function displayResults(prompts) {
            const results = document.getElementById('results');
            results.innerHTML = '';
            
            prompts.forEach(prompt => {
                const card = document.createElement('div');
                card.className = 'prompt-card glass rounded-xl p-6 cursor-pointer';
                card.innerHTML = `
                    <div class="flex items-start justify-between mb-4">
                        <div class="flex items-center gap-3">
                            <i class="fas fa-${getPlatformIcon(prompt.platform)} text-2xl text-cyan-400"></i>
                            <div>
                                <h3 class="text-lg font-semibold text-white">${prompt.platform}</h3>
                                <p class="text-white/70 text-sm">${prompt.category}</p>
                            </div>
                        </div>
                        <button onclick="copyPrompt(this, '${prompt.content.replace(/'/g, "\\'")}')" 
                                class="px-4 py-2 bg-cyan-500 hover:bg-cyan-600 text-white rounded-lg transition-colors">
                            <i class="fas fa-copy mr-2"></i>Copy
                        </button>
                    </div>
                    <p class="text-white/90 leading-relaxed">${prompt.content}</p>
                `;
                results.appendChild(card);
            });
            results.classList.remove('hidden');
        }
        
        function displayError(message) {
            const results = document.getElementById('results');
            results.innerHTML = `
                <div class="glass rounded-xl p-6 text-center">
                    <i class="fas fa-exclamation-triangle text-4xl text-yellow-400 mb-4"></i>
                    <p class="text-white">${message}</p>
                </div>
            `;
            results.classList.remove('hidden');
        }
        
        function getPlatformIcon(platform) {
            const icons = { 'ChatGPT': 'comments', 'Midjourney': 'image', 'Claude': 'brain', 'DALL-E': 'palette', 'Gemini': 'gem' };
            return icons[platform] || 'robot';
        }
        
        function copyPrompt(button, content) {
            navigator.clipboard.writeText(content).then(() => {
                const originalText = button.innerHTML;
                button.innerHTML = '<i class="fas fa-check mr-2"></i>Copied!';
                button.className = button.className.replace('bg-cyan-500 hover:bg-cyan-600', 'bg-green-500');
                setTimeout(() => {
                    button.innerHTML = originalText;
                    button.className = button.className.replace('bg-green-500', 'bg-cyan-500 hover:bg-cyan-600');
                }, 2000);
            });
        }
    </script>
</body>
</html>'''

def detect_platform(prompt_text):
    prompt_lower = prompt_text.lower()
    if any(word in prompt_lower for word in ['chatgpt', 'gpt', 'openai']):
        return 'ChatGPT'
    elif any(word in prompt_lower for word in ['midjourney', 'mj', 'image', 'art', 'visual']):
        return 'Midjourney'
    elif any(word in prompt_lower for word in ['claude', 'anthropic']):
        return 'Claude'
    elif any(word in prompt_lower for word in ['dall-e', 'dalle', 'openai image']):
        return 'DALL-E'
    elif any(word in prompt_lower for word in ['gemini', 'bard', 'google']):
        return 'Gemini'
    else:
        return 'ChatGPT'

def generate_with_openrouter(user_prompt):
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        return None
    
    try:
        platform = detect_platform(user_prompt)
        system_prompt = f"""You are an expert prompt engineer. Create a ready-to-use, professional {platform} prompt based on the user's request.

IMPORTANT: Create a prompt that the user can directly copy and paste into {platform}. DO NOT create instructions about how to use {platform} - create the actual prompt they need.

The prompt should:
1. Be a complete, ready-to-use prompt for {platform}
2. Include specific instructions, context, and format requirements
3. Be 150-300 words and highly detailed
4. Include examples, parameters, or specifications when helpful
5. For image platforms: include technical specs, style, quality parameters
6. For text platforms: include role, context, format, and step-by-step instructions

Return JSON format:
{{"platform": "{platform}", "category": "appropriate category", "content": "the complete ready-to-use prompt"}}"""
        
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": "anthropic/claude-3.5-sonnet",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "response_format": {"type": "json_object"}
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            content = data['choices'][0]['message']['content']
            return json.loads(content)
    except Exception as e:
        print(f"OpenRouter API error: {e}")
    return None

def generate_fallback_prompt(user_prompt):
    platform = detect_platform(user_prompt)
    
    # Extract the core request from user input
    clean_request = user_prompt.lower()
    for keyword in ['create', 'generate', 'make', 'build', 'write', 'chatgpt', 'midjourney', 'claude', 'dall-e', 'gemini', 'prompt', 'for']:
        clean_request = clean_request.replace(keyword, '').strip()
    
    fallback_prompts = {
        'ChatGPT': {
            'content': f"""You are an expert {clean_request} specialist with extensive knowledge and practical experience.

Task: {clean_request}

Instructions:
- Analyze the specific requirements carefully
- Provide detailed, step-by-step guidance 
- Include practical examples and real-world applications
- Address potential challenges and solutions
- Offer best practices and professional tips
- Suggest relevant tools and resources

Format Requirements:
- Use clear headings and bullet points
- Provide actionable steps
- Include specific details and examples
- Make recommendations concrete and implementable

Tone: Professional, helpful, and thorough while remaining accessible.

Please provide comprehensive guidance on {clean_request}, ensuring your response is detailed, practical, and immediately actionable.""",
            'category': 'Expert Assistant'
        },
        'Midjourney': {
            'content': f"""Create a stunning, highly detailed image of {clean_request}, hyper-realistic, professional photography quality, perfect composition and lighting, 8K ultra-high definition, studio-quality lighting with perfect shadows and highlights, rich vibrant colors with excellent color grading, rule of thirds composition, razor-sharp focus on main subject with appropriate depth of field, professional cinematic quality, intricate textures, realistic materials, authentic proportions, complementary background that enhances the main subject, shot with professional DSLR, prime lens, optimal aperture for subject isolation --ar 16:9 --v 6 --style raw --q 2""",
            'category': 'Professional Image Generation'
        },
        'Claude': {
            'content': f"""Analyze {clean_request} comprehensively using the following framework:

1. Initial Assessment: Break down the key components and context
2. Multi-Perspective Analysis: Consider various angles and stakeholder viewpoints  
3. Evidence-Based Reasoning: Support findings with logical reasoning and available evidence
4. Practical Applications: Identify real-world implications and applications
5. Potential Challenges: Anticipate obstacles and provide mitigation strategies
6. Actionable Recommendations: Conclude with specific, implementable suggestions

Methodology:
- Use systematic approach to ensure thoroughness
- Apply critical thinking to identify assumptions and biases
- Maintain balanced perspective acknowledging limitations and uncertainties
- Communicate clearly with structured presentation

Provide a comprehensive analysis that includes background context, detailed examination, practical insights, and actionable recommendations for {clean_request}.""",
            'category': 'Comprehensive Analysis'
        },
        'DALL-E': {
            'content': f"""Create a professional-quality, highly detailed image of {clean_request}. Photorealistic with artistic flair, professional-grade quality suitable for commercial use, high-definition with crisp details, expertly framed with balanced elements, harmonious color palette that enhances the subject, professional lighting setup with proper shadows and highlights, realistic textures and materials with fine detail, appropriate depth of field to create visual interest, crystal clear focus on main elements, well-balanced contrast for visual impact, rich vibrant colors without oversaturation, realistic proportions and accurate representations. Create an engaging atmosphere that draws the viewer in and conveys the intended message. The final image should be portfolio-worthy and demonstrate exceptional attention to detail and artistic composition.""",
            'category': 'Professional AI Art'
        },
        'Gemini': {
            'content': f"""Research and provide comprehensive, accurate, up-to-date information about {clean_request}.

Research Approach:
1. Multi-Source Analysis: Draw from diverse, reliable sources to ensure accuracy
2. Current Information: Prioritize the most recent and relevant data available
3. Comprehensive Coverage: Address multiple aspects and dimensions of the topic
4. Fact-Checking: Verify information and note any limitations or uncertainties
5. Practical Application: Focus on actionable insights and real-world relevance

Structure your response with:
- Background and Context: Essential foundational information
- Current State: Latest developments and current situation  
- Key Insights: Most important findings and implications
- Trends and Patterns: Emerging developments and future directions
- Practical Recommendations: Actionable steps and best practices
- Resources: Additional sources and tools for further exploration

Ensure accuracy through multiple reliable sources, focus on what's most important and useful, present complex information in understandable terms, maintain balanced perspective with acknowledged limitations. Provide detailed, research-backed information with practical applications for {clean_request}.""",
            'category': 'Research & Information'
        }
    }
    
    return {
        'platform': platform,
        'category': fallback_prompts[platform]['category'],
        'content': fallback_prompts[platform]['content']
    }

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/generate', methods=['POST'])
def generate_prompts():
    try:
        data = request.get_json()
        user_prompt = data.get('prompt', '').strip()
        if not user_prompt:
            return jsonify({'success': False, 'error': 'Prompt is required'})
        
        ai_result = generate_with_openrouter(user_prompt)
        if ai_result:
            prompts = [ai_result]
        else:
            prompts = [generate_fallback_prompt(user_prompt)]
        
        return jsonify({'success': True, 'prompts': prompts})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': 'Failed to generate prompts'})

@app.route('/api/stats')
def get_stats():
    return jsonify({'totalPrompts': 1000, 'totalCategories': 8, 'totalPlatforms': 5, 'dailyUsers': 50000})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)