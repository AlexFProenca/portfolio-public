import re

html = open('index.html', 'r', encoding='utf-8', errors='ignore').read()

new_script = """<script>
(function() {
    var translations = {
        'en': {
            'Creative Technologist — Music, Art, Design, Code & Cyber Security': 'Creative Technologist — Music, Art, Design, Code & Cyber Security',
            'Selected Work': 'Selected Work',
            'Creative Technology & Interactive Experiences': 'Creative Technology & Interactive Experiences',
            'Music-driven interfaces, generative visuals, and playful web apps.': 'Music-driven interfaces, generative visuals, and playful web apps.',
            'AI & Visual Systems': 'AI & Visual Systems',
            'Portrait enhancement, style transfer, and restoration pipelines.': 'Portrait enhancement, style transfer, and restoration pipelines.',
            'Secure Web Applications': 'Secure Web Applications',
            'Front-end systems with defense-minded architecture and clean UX.': 'Front-end systems with defense-minded architecture and clean UX.',
            'Music & Audio': 'Music & Audio',
            'Original compositions and audio-driven projects.': 'Original compositions and audio-driven projects.',
            'About': 'About',
            'I build at the intersection of music, art, design, code and cyber security. With more than 15 years of experience since 2008, I create digital products and experiences that are technically solid, visually intentional, and safe by design.': 'I build at the intersection of music, art, design, code and cyber security. With more than 15 years of experience since 2008, I create digital products and experiences that are technically solid, visually intentional, and safe by design.',
            'My work spans front-end engineering, interactive design, audio-driven projects, and secure web systems. I care about clean interfaces, performance, usability, and defense-minded architecture — not as separate skills, but as one consistent way of building.': 'My work spans front-end engineering, interactive design, audio-driven projects, and secure web systems. I care about clean interfaces, performance, usability, and defense-minded architecture — not as separate skills, but as one consistent way of building.',
            'When I am not shipping features or studying attack surfaces, I am composing, designing, prototyping, or exploring new tools across creative technology and security.': 'When I am not shipping features or studying attack surfaces, I am composing, designing, prototyping, or exploring new tools across creative technology and security.',
            'I am available for roles and collaborations with international teams. If you want someone who can move between creative and technical tracks without losing quality, let us talk.': 'I am available for roles and collaborations with international teams. If you want someone who can move between creative and technical tracks without losing quality, let us talk.',
            'Contact': 'Contact',
            'Tell me about your project or role. I reply faster when the message is specific.': 'Tell me about your project or role. I reply faster when the message is specific.',
            'View Projects': 'View Projects',
            'View AI Work': 'View AI Work',
            'View Web Work': 'View Web Work',
            'Listen': 'Listen'
        },
        'pt-BR': {
            'Creative Technologist — Music, Art, Design, Code & Cyber Security': 'Tecnólogo Criativo — Música, Arte, Design, Código & Cyber Security',
            'Selected Work': 'Trabalhos Selecionados',
            'Creative Technology & Interactive Experiences': 'Tecnologia Criativa & Experiências Interativas',
            'Music-driven interfaces, generative visuals, and playful web apps.': 'Interfaces musicais, visuais generativos e web apps interativos.',
            'AI & Visual Systems': 'Sistemas de IA & Visual',
            'Portrait enhancement, style transfer, and restoration pipelines.': 'Realce de retratos, transferência de estilo e restauração.',
            'Secure Web Applications': 'Aplicações Web Seguras',
            'Front-end systems with defense-minded architecture and clean UX.': 'Sistemas front-end com arquitetura segura e UX limpa.',
            'Music & Audio': 'Música & Áudio',
            'Original compositions and audio-driven projects.': 'Composições originais e projetos orientados por áudio.',
            'About': 'Sobre',
            'I build at the intersection of music, art, design, code and cyber security. With more than 15 years of experience since 2008, I create digital products and experiences that are technically solid, visually intentional, and safe by design.': 'Construo na interseção de música, arte, design, código e cyber security. Com mais de 15 anos de experiência desde 2008, crio produtos e experiências digitais tecnicamente sólidos, visualmente intencionais e seguros por design.',
            'My work spans front-end engineering, interactive design, audio-driven projects, and secure web systems. I care about clean interfaces, performance, usability, and defense-minded architecture — not as separate skills, but as one consistent way of building.': 'Meu trabalho abrange engenharia front-end, design interativo, projetos de áudio e sistemas web seguros. Eu valorizo interfaces limpas, performance, usabilidade e arquitetura defensiva — não como habilidades separadas, mas como uma forma consistente de construir.',
            'When I am not shipping features or studying attack surfaces, I am composing, designing, prototyping, or exploring new tools across creative technology and security.': 'Quando não estou lançando features ou estudando vetores de ataque, estou compondo, desenhando, prototipando ou explorando novas ferramentas entre tecnologia criativa e segurança.',
            'I am available for roles and collaborations with international teams. If you want someone who can move between creative and technical tracks without losing quality, let us talk.': 'Estou disponível para vagas e colaborações com equipes internacionais. Se você quer alguém que transita entre trilhas criativas e técnicas sem perder qualidade, vamos conversar.',
            'Contact': 'Contato',
            'Tell me about your project or role. I reply faster when the message is specific.': 'Conte sobre seu projeto ou vaga. Respondo mais rápido quando a mensagem é específica.',
            'View Projects': 'Ver Projetos',
            'View AI Work': 'Ver Trabalho em IA',
            'View Web Work': 'Ver Trabalho Web',
            'Listen': 'Ouvir'
        }
    };
    
    function toggleLanguage() {
        const html = document.documentElement;
        const current = html.getAttribute('lang');
        const next = current === 'en' ? 'pt-BR' : 'en';
        html.setAttribute('lang', next);
        
        // Swap text directly
        Object.keys(translations['en']).forEach(function(enText) {
            const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
            let node;
            while (node = walker.nextNode()) {
                if (node.textContent.trim() === enText) {
                    node.textContent = translations[next][enText] || enText;
                }
            }
        });
        
        // Update button styles
        document.querySelectorAll('.language-button').forEach(function(btn) {
            const btnLang = btn.getAttribute('data-lang');
            if (btnLang === next) {
                btn.style.background = '#18181b';
                btn.style.color = '#f3f4f6';
                btn.style.border = '1px solid #3b82f6';
                btn.style.boxShadow = '0 0 8px rgba(59,130,246,0.5)';
            } else {
                btn.style.background = 'rgba(39,39,42,0.7)';
                btn.style.color = '#d4d4d8';
                btn.style.border = '1px solid rgba(161,161,170,0.3)';
                btn.style.boxShadow = 'none';
            }
        });
    }
    
    window.toggleLanguage = toggleLanguage;
    document.documentElement.lang = 'en';
})();
</script>"""

# Replace any existing toggle script
html = re.sub(r'<script>\s*\(function\(\)\s*\{[^}]*toggleLanguage[^}]*\}[^<]*</script>', new_script, html, flags=re.DOTALL)

# Make sure we have the toggle script before </body>
if '</body>' in html and new_script not in html:
    html = html.replace('</body>', new_script + '</body>')

open('index.html', 'w', encoding='utf-8', errors='ignore').write(html)
print('Script replaced with text-swapping version')
