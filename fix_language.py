import re

html = open('index.html', 'r', encoding='utf-8', errors='ignore').read()

translations = {
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
    'Listen': 'Ouvir',
}

for en_text, pt_text in translations.items():
    en_escaped = re.escape(en_text)
    pattern = rf'(<[^>]+>)({en_escaped})(</[^>]+>)'
    def add_attr(m, pt=pt_text):
        return f'{m.group(1)}<span data-lang="en">{m.group(2)}</span><span data-lang="pt-BR" style="display:none">{pt}</span>{m.group(3)}'
    html = re.sub(pattern, add_attr, html)

toggle_script = """
<script>
(function() {
    function toggleLanguage() {
        const current = document.documentElement.lang;
        const next = current === 'en' ? 'pt-BR' : 'en';
        document.documentElement.lang = next;
        
        document.querySelectorAll('[data-lang]').forEach(el => {
            const lang = el.getAttribute('data-lang');
            el.style.display = lang === next ? '' : 'none';
        });
        
        document.querySelectorAll('.language-button').forEach(btn => {
            const btnLang = btn.getAttribute('data-lang');
            if (btnLang === next) {
                btn.classList.add('bg-zinc-950', 'text-gray-100', 'neon-text', 'neon-border');
                btn.classList.remove('bg-zinc-800/70', 'hover:bg-zinc-700/50', 'text-gray-300');
            } else {
                btn.classList.remove('bg-zinc-950', 'text-gray-100', 'neon-text', 'neon-border');
                btn.classList.add('bg-zinc-800/70', 'hover:bg-zinc-700/50', 'text-gray-300');
            }
        });
    }
    
    window.toggleLanguage = toggleLanguage;
    
    // Start in English since this is the primary language for foreign employers
    if (document.documentElement.lang !== 'en') {
        toggleLanguage();
    }
})();
</script>
"""

html = html.replace('</body>', toggle_script + '</body>')

open('index.html', 'w', encoding='utf-8', errors='ignore').write(html)
print('Added language toggle and PT-BR translations')
