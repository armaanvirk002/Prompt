from flask import Flask, request, jsonify, render_template_string
import requests
import json
import os
from datetime import datetime

app = Flask(__name__)

# HTML template with all the SEO optimization
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Primary SEO Meta Tags -->
    <title>PromptNest - FREE AI Prompt Generator | 1000+ Best ChatGPT, Midjourney & Claude Prompts 2025</title>
    <meta name="description" content="🚀 Get the best AI prompts instantly! 1000+ FREE prompts for ChatGPT, Midjourney, Claude & DALL-E. Generate viral content, stunning art & professional copy in seconds. Used by 50,000+ creators daily!">
    <meta name="keywords" content="free AI prompts 2025, best ChatGPT prompts, Midjourney prompt generator, Claude AI prompts, DALL-E prompts, viral content prompts, AI writing assistant, prompt engineering, content creation tools, AI marketing prompts, coding prompts, SEO prompts, business prompts, creative writing prompts, AI art prompts">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="🔥 PromptNest - Get 1000+ FREE AI Prompts | ChatGPT, Midjourney & More!">
    <meta property="og:description" content="💎 Discover the ultimate AI prompt library! Generate viral content, stunning visuals & professional copy instantly. Join 50,000+ creators using our FREE prompts daily!">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="🚀 FREE AI Prompts That Actually Work! | PromptNest 2025">
    <meta name="twitter:description" content="💯 Get 1000+ premium AI prompts for FREE! Create viral content, stunning art & convert like crazy. Used by top creators & marketers worldwide. Try now!">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#8B5CF6',
                        secondary: '#06B6D4'
                    }
                }
            }
        }
    </script>
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Google Analytics 4 - Reliable Format -->
    <script type="text/javascript">
        function loadGoogleAnalytics() {
            var gaId = 'G-XXXXXXXXXX';
            var script = document.createElement('script');
            script.async = true;
            script.src = 'https://www.googletagmanager.com/gtag/js?id=' + gaId;
            document.head.appendChild(script);
            
            window.dataLayer = window.dataLayer || [];
            function gtag() { dataLayer.push(arguments); }
            window.gtag = gtag;
            gtag('js', new Date());
            gtag('config', gaId);
            
            console.log('Google Analytics 4 loaded successfully: ' + gaId);
        }
        
        // Load GA4 when page is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', loadGoogleAnalytics);
        } else {
            loadGoogleAnalytics();
        }
    </script>
    
    <!-- Microsoft Clarity Analytics - Reliable Format -->
    <script type="text/javascript">
        function loadClarity() {
            var clarityId = 'sme4b33o32';
            window.clarity = window.clarity || function() {
                (window.clarity.q = window.clarity.q || []).push(arguments);
            };
            
            var script = document.createElement('script');
            script.type = 'text/javascript';
            script.async = true;
            script.src = 'https://www.clarity.ms/tag/' + clarityId;
            
            var firstScript = document.getElementsByTagName('script')[0];
            firstScript.parentNode.insertBefore(script, firstScript);
            
            console.log('Microsoft Clarity loaded successfully: ' + clarityId);
        }
        
        // Load Clarity when page is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', loadClarity);
        } else {
            loadClarity();
        }
    </script>
    
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .glass {
            backdrop-filter: blur(16px);
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .prompt-card {
            transition: all 0.3s ease;
        }
        .prompt-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <div class="min-h-screen py-8">
        <div class="container mx-auto px-4">
            <!-- Header -->
            <div class="text-center mb-12">
                <h1 class="text-4xl md:text-6xl font-bold text-white mb-4">
                    <i class="fas fa-magic text-yellow-400 mr-4"></i>
                    PromptNest
                </h1>
                <p class="text-xl text-white/90 max-w-3xl mx-auto">
                    Generate platform-specific AI prompts instantly. Free, powerful, and optimized for ChatGPT, Midjourney, Claude & DALL-E.
                </p>
            </div>

            <!-- AI Generator -->
            <div class="max-w-4xl mx-auto mb-12">
                <div class="glass rounded-2xl p-8 shadow-2xl">
                    <h2 class="text-2xl font-bold text-white mb-6 text-center">
                        <i class="fas fa-robot text-cyan-400 mr-3"></i>
                        AI Prompt Generator
                    </h2>
                    
                    <!-- Instructions -->
                    <div class="glass rounded-lg p-4 mb-6">
                        <p class="text-white/90 text-sm font-medium mb-2">💡 How to use:</p>
                        <div class="text-white/80 text-sm space-y-1">
                            <p>• "Create prompt for <strong class="text-cyan-300">ChatGPT</strong> to write professional emails"</p>
                            <p>• "Generate <strong class="text-purple-300">Midjourney</strong> prompt for realistic portraits"</p>
                            <p>• "Make <strong class="text-orange-300">Claude</strong> prompt for data analysis"</p>
                            <p>• "Build <strong class="text-cyan-300">Gemini</strong> prompt for research tasks"</p>
                        </div>
                    </div>
                    
                    <!-- Input Form -->
                    <form id="promptForm" class="space-y-4">
                        <div class="flex flex-col md:flex-row gap-4">
                            <input 
                                type="text" 
                                id="promptInput" 
                                placeholder="e.g., 'Create ChatGPT prompt for writing emails' or 'Generate Midjourney prompt for fantasy art'"
                                class="flex-1 px-6 py-4 bg-white/20 backdrop-blur-sm border border-white/30 rounded-xl text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-cyan-400 focus:border-transparent"
                                required
                            >
                            <button 
                                type="submit"
                                class="px-8 py-4 bg-gradient-to-r from-cyan-500 to-purple-500 hover:from-cyan-600 hover:to-purple-600 text-white font-semibold rounded-xl transition-all duration-300 transform hover:scale-105 shadow-lg"
                            >
                                <i class="fas fa-magic mr-2"></i>
                                Generate Prompts
                            </button>
                        </div>
                    </form>
                    
                    <!-- Loading -->
                    <div id="loading" class="hidden text-center py-8">
                        <i class="fas fa-spinner fa-spin text-4xl text-cyan-400 mb-4"></i>
                        <p class="text-white">Generating your perfect prompts...</p>
                    </div>
                    
                    <!-- Results -->
                    <div id="results" class="hidden mt-8 space-y-6"></div>
                </div>
            </div>

            <!-- Stats -->
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
            
            // Show loading
            loading.classList.remove('hidden');
            results.classList.add('hidden');
            
            try {
                const response = await fetch('/api/generate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ prompt: input })
                });
                
                const data = await response.json();
                
                // Hide loading
                loading.classList.add('hidden');
                
                if (data.success && data.prompts && data.prompts.length > 0) {
                    // Track successful prompt generation with Google Analytics
                    if (typeof gtag !== 'undefined') {
                        gtag('event', 'generate_prompt', {
                            'platform': data.prompts[0].platform,
                            'category': data.prompts[0].category,
                            'event_category': 'engagement',
                            'event_label': data.prompts[0].platform + '_prompt'
                        });
                    }
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
            const icons = {
                'ChatGPT': 'comments',
                'Midjourney': 'image',
                'Claude': 'brain',
                'DALL-E': 'palette',
                'Gemini': 'gem'
            };
            return icons[platform] || 'robot';
        }
        
        function copyPrompt(button, content) {
            navigator.clipboard.writeText(content).then(() => {
                // Track copy action with Google Analytics
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'copy_prompt', {
                        'event_category': 'interaction',
                        'event_label': 'prompt_copied'
                    });
                }
                
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
</html>
'''

def detect_platform(prompt_text):
    """Detect AI platform from user input"""
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
        return 'ChatGPT'  # Default

def generate_with_openrouter(user_prompt):
    """Generate prompt using OpenRouter API"""
    api_key = os.getenv('OPENROUTER_API_KEY')
    
    if not api_key:
        return None
    
    try:
        platform = detect_platform(user_prompt)
        
        system_prompt = f"""You are an expert prompt engineer. Create a comprehensive, detailed, and structured prompt for {platform} based on the user's request.

CRITICAL REQUIREMENTS:
- Create DETAILED, STRUCTURED prompts (150-300 words) that are ready-to-use
- Include step-by-step instructions, bullet points, and clear formatting
- Add specific role definitions, context, and expected outputs
- Include examples, constraints, and formatting guidelines
- Make it immediately actionable and professional
- DO NOT create meta-instructions - create the actual detailed prompt

STRUCTURE TEMPLATE:
- Role/Identity: Define the AI's expertise
- Task: Clear, specific instructions with bullet points
- Format: Expected output structure  
- Examples: When helpful
- Constraints: Important limitations or requirements

Return a JSON object with this structure:
{{
    "platform": "{platform}",
    "category": "appropriate category",
    "content": "the comprehensive, detailed, structured prompt (150-300 words)"
}}"""

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
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
    """Generate fallback prompt when API is unavailable"""
    platform = detect_platform(user_prompt)
    
    # Create detailed, structured fallback prompts based on the request
    task = user_prompt.replace('chatgpt', '').replace('ChatGPT', '').replace('claude', '').replace('Claude', '').replace('midjourney', '').replace('Midjourney', '').replace('dall-e', '').replace('DALL-E', '').replace('gemini', '').replace('Gemini', '').strip()
    
    fallback_prompts = {
        'ChatGPT': {
            'content': f"""You are an expert professional assistant specialized in {task}.

Your task:
- 🎯 Purpose: {task}
- 👤 Target Audience: [Specify who this is for]
- 📝 Tone: [Choose tone - e.g. professional, casual, technical]
- 🔑 Key Requirements: [List specific requirements]

Format your response with:
- Clear structure with headings and bullet points
- Actionable steps or recommendations  
- Relevant examples when applicable
- Professional yet engaging language
- Include a strong conclusion if applicable

Additional guidelines:
- Be thorough and comprehensive
- Include practical tips and best practices
- Consider different perspectives and approaches
- Provide specific, actionable advice

Provide:
1. [Primary deliverable]
2. [Supporting information]
3. [Next steps or recommendations]""",
            'category': 'Professional Assistant'
        },
        'Midjourney': {
            'content': f"""{task}, ultra-detailed, professional photography style, perfect composition, studio lighting, high-end camera quality, 8K resolution, award-winning photography.

Style specifications:
- Lighting: Professional studio lighting, soft shadows, perfect exposure
- Composition: Rule of thirds, balanced framing, visual hierarchy
- Quality: Ultra-sharp focus, fine details, rich textures
- Color: Vibrant yet natural color palette, proper white balance
- Mood: [Specify desired mood/atmosphere]

Technical parameters:
- Camera: Professional DSLR equivalent, 85mm lens
- Settings: f/2.8 aperture, optimal depth of field
- Post-processing: Color grading, professional retouching
- Resolution: 8K, print-ready quality

Additional elements:
- Background: [Specify background style]
- Props/Elements: [List relevant props]
- Style inspiration: Contemporary commercial photography
- Trending on: Behance, Pinterest, professional portfolios

--ar 16:9 --v 6 --style raw --quality 2""",
            'category': 'Professional Photography'
        },
        'Claude': {
            'content': f"""As an expert analyst and researcher, provide a comprehensive analysis of {task}.

Analysis Framework:
- 🔍 Overview: Provide clear context and background
- 📊 Key Components: Break down main elements
- ⚖️ Pros & Cons: Balanced evaluation
- 💡 Insights: Evidence-based conclusions
- 🎯 Recommendations: Actionable next steps

Research methodology:
- Use current, reliable sources
- Apply critical thinking and logical reasoning
- Consider multiple perspectives and stakeholder views
- Identify potential biases and limitations
- Provide evidence-based conclusions

Structure your response:
1. Executive Summary (2-3 sentences)
2. Detailed Analysis (main body with subheadings)
3. Key Findings (bullet points)
4. Recommendations (specific, actionable)
5. Conclusion (synthesis and next steps)

Ensure accuracy, objectivity, and comprehensive coverage while maintaining clarity and professional presentation.""",
            'category': 'Research & Analysis'
        },
        'DALL-E': {
            'content': f"""Create a highly detailed, professional-quality image of {task}.

Artistic specifications:
- Style: Photorealistic with artistic enhancement
- Composition: Balanced, visually appealing layout
- Lighting: Professional studio lighting, dramatic shadows
- Color palette: Rich, vibrant colors with perfect saturation
- Texture: Fine details, realistic materials and surfaces

Technical requirements:
- Resolution: High-definition, crisp and clear
- Focus: Sharp foreground with appropriate depth of field
- Quality: Professional photography standard
- Format: Optimized for both digital and print use

Creative elements:
- Mood: [Specify desired emotional tone]
- Atmosphere: Professional yet engaging
- Visual hierarchy: Clear focal points and flow
- Style inspiration: Contemporary digital art and photography
- Professional polish: Commercial-grade finishing

Additional considerations:
- Lighting setup: Multi-point lighting with key, fill, and rim lights
- Background: Complementary but not distracting
- Props and elements: Carefully curated and positioned
- Overall aesthetic: Modern, clean, and professional""",
            'category': 'Professional Digital Art'
        },
        'Gemini': {
            'content': f"""As Google's advanced AI, provide comprehensive research and analysis on {task}.

Research approach:
- 🌐 Current Information: Latest data and trends
- 📈 Data Analysis: Quantitative and qualitative insights
- 🔗 Source Verification: Reliable, authoritative sources
- 🎯 Multi-perspective: Various viewpoints and approaches
- 💡 Practical Applications: Real-world implications

Structure your response:
1. Current State Analysis
   - Latest developments and trends
   - Key statistics and data points
   - Market conditions (if applicable)

2. Comprehensive Overview
   - Background and context
   - Important factors and variables
   - Stakeholder perspectives

3. Evidence-Based Insights
   - Research findings and conclusions
   - Expert opinions and studies
   - Case studies and examples

4. Future Implications
   - Predicted trends and developments
   - Potential challenges and opportunities
   - Strategic recommendations

5. Actionable Next Steps
   - Specific recommendations
   - Implementation strategies
   - Success metrics and evaluation

Ensure accuracy, depth, and practical value while maintaining clarity and professional presentation.""",
            'category': 'Advanced Research'
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
        
        # Try OpenRouter API first
        ai_result = generate_with_openrouter(user_prompt)
        
        if ai_result:
            prompts = [ai_result]
        else:
            # Fallback to manual generation
            prompts = [generate_fallback_prompt(user_prompt)]
        
        return jsonify({
            'success': True,
            'prompts': prompts
        })
        
    except Exception as e:
        print(f"Error generating prompts: {e}")
        return jsonify({
            'success': False,
            'error': 'Failed to generate prompts'
        })

@app.route('/api/stats')
def get_stats():
    return jsonify({
        'totalPrompts': 1000,
        'totalCategories': 8,
        'totalPlatforms': 5,
        'dailyUsers': 50000
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)