from pathlib import Path
import re

html = Path('index.html').read_text(encoding='utf-8', errors='ignore')

# Add data-i18n attributes to key text elements
replacements = [
    ('Creative Technologist — Music, Art, Design, Code & Cyber Security', 'data-i18n="hero.role"'),
    ('Alex Proença</h1>', 'data-i18n="hero.name"'),
    ('I build at the intersection of sound, visuals, code and security. Not as separate skills — as one practice.', 'data-i18n="hero.summary"'),
    ('>Selected Work</button>', 'data-i18n="hero.cta_work"'),
    ('>Projects & Software</button>', 'data-i18n="hero.cta_projects"'),
    ('>Music</button>', 'data-i18n="hero.cta_music"'),
    ('<h2 class="text-5xl md:text-7xl font-bold tracking-tighter glitch" data-text="Alex Proença">Alex Proença</h1>', '<h2 class="text-5xl md:text-7xl font-bold tracking-tighter glitch" data-text="Alex Proença" data-i18n="hero.name">Alex Proença</h2>'),
    ('Selected Work</a>', 'data-i18n="work.title"'),
    ('Service-oriented work in creative technology, AI, secure web systems and audio.</p>', 'data-i18n="work.subtitle"'),
    ('Creative Technology & Interactive Experiences', 'data-i18n="work.card1.title"'),
    ('Music-driven interfaces, generative visuals, and playful web apps.', 'data-i18n="work.card1.desc"'),
    ('AI & Visual Systems', 'data-i18n="work.card2.title"'),
    ('Portrait enhancement, style transfer, and restoration pipelines.', 'data-i18n="work.card2.desc"'),
    ('Secure Web Applications', 'data-i18n="work.card3.title"'),
    ('Front-end systems with defense-minded architecture and clean UX.', 'data-i18n="work.card3.desc"'),
    ('Music & Audio', 'data-i18n="work.card4.title"'),
    ('Original compositions and audio-driven projects.', 'data-i18n="work.card4.desc"'),
    ('About</h2>', 'data-i18n="about.title"'),
    ('Contact</h2>', 'data-i18n="contact.title"'),
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)

# Add the i18n script before </body>
i18n_script = '''
<script>
(function(){
  const i18n = {
    'en': {
      'hero.role': 'Creative Technologist — Music, Art, Design, Code & Cyber Security',
      'hero.name': 'Alex Proença',
      'hero.summary': 'I build at the intersection of sound, visuals, code and security. Not as separate skills — as one practice.',
      'hero.cta_work': 'Selected Work',
      'hero.cta_projects': 'Projects & Software',
      'hero.cta_music': 'Music',
      'work.title': 'Selected Work',
      'work.subtitle': 'Service-oriented work in creative technology, AI, secure web systems and audio.',
      'work.card1.title': 'Creative Technology & Interactive Experiences',
      'work.card1.desc': 'Music-driven interfaces, generative visuals, and playful web apps.',
      'work.card1.cta': 'View Projects',
      'work.card2.title': 'AI & Visual Systems',
      'work.card2.desc': 'Portrait enhancement, style transfer, and restoration pipelines.',
      'work.card2.cta': 'View AI Work',
      'work.card3.title': 'Secure Web Applications',
      'work.card3.desc': 'Front-end systems with defense-minded architecture and clean UX.',
      'work.card3.cta': 'View Web Work',
      'work.card4.title': 'Music & Audio',
      'work.card4.desc': 'Original compositions and audio-driven projects.',
      'work.card4.cta': 'Listen',
      'about.title': 'About',
      'about.p1': 'I build at the intersection of music, art, design, code and cyber security. With more than 15 years of experience since 2008, I create digital products and experiences that are technically solid, visually intentional, and safe by design.',
      'about.p2': 'My work spans front-end engineering, interactive design, audio-driven projects, and secure web systems. I care about clean interfaces, performance, usability, and defense-minded architecture — not as separate skills, but as one consistent way of building.',
      'about.p3': 'When I am not shipping features or studying attack surfaces, I am composing, designing, prototyping, or exploring new tools across creative technology and security.',
      'about.p4': 'I am available for roles and collaborations with international teams. If you want someone who can move between creative and technical tracks without losing quality, let us talk.',
      'contact.title': 'Contact',
      'contact.hint': 'Tell me about your project or role. I reply faster when the message is specific.',
      'contact.submit': 'Send'
    },
    'pt-BR': {
      'hero.role': 'Tecnólogo Criativo — Música, Arte, Design, Código & Cyber Security',
      'hero.name': 'Alex Proença',
      'hero.summary': 'Construo na interseção de som, visuais, código e segurança. Não como habilidades separadas — como uma prática única.',
      'hero.cta_work': 'Trabalhos Selecionados',
      'hero.cta_projects': 'Projetos & Software',
      'hero.cta_music': 'Música',
      'work.title': 'Trabalhos Selecionados',
      'work.subtitle': 'Trabalhos orientados a serviço em tecnologia criativa, IA, sistemas web seguros e áudio.',
      'work.card1.title': 'Tecnologia Criativa & Experiências Interativas',
      'work.card1.desc': 'Interfaces musicais, visuais generativos e web apps interativos.',
      'work.card1.cta': 'Ver Projetos',
      'work.card2.title': 'Sistemas de IA & Visual',
      'work.card2.desc': 'Realce de retratos, transferência de estilo e restauração.',
      'work.card2.cta': 'Ver Trabalho em IA',
      'work.card3.title': 'Aplicações Web Seguras',
      'work.card3.desc': 'Sistemas front-end com arquitetura segura e UX limpa.',
      'work.card3.cta': 'Ver Trabalho Web',
      'work.card4.title': 'Música & Áudio',
      'work.card4.desc': 'Composições originais e projetos orientados por áudio.',
      'work.card4.cta': 'Ouvir',
      'about.title': 'Sobre',
      'about.p1': 'Construo na interseção de música, arte, design, código e cyber security. Com mais de 15 anos de experiência desde 2008, crio produtos e experiências digitais tecnicamente sólidos, visualmente intencionais e seguros por design.',
      'about.p2': 'Meu trabalho abrange engenharia front-end, design interativo, projetos de áudio e sistemas web seguros. Valorizo interfaces limpas, performance, usabilidade e arquitetura defensiva — não como habilidades separadas, mas como uma forma consistente de construir.',
      'about.p3': 'Quando não estou lançando features ou estudando vetores de ataque, estou compondo, desenhando, prototipando ou explorando novas ferramentas entre tecnologia criativa e segurança.',
      'about.p4': 'Estou disponível para vagas e colaborações com equipes internacionais. Se você quer alguém que transita entre trilhas criativas e técnicas sem perder qualidade, vamos conversar.',
      'contact.title': 'Contato',
      'contact.hint': 'Conte sobre seu projeto ou vaga. Respondo mais rápido quando a mensagem é específica.',
      'contact.submit': 'Enviar'
    }
  };

  let current = 'en';

  function applyLang(lang) {
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      const k = el.getAttribute('data-i18n');
      if (i18n[lang] && i18n[lang][k]) el.textContent = i18n[lang][k];
    });
    document.documentElement.lang = lang;
  }

  window.setLang = function(lang) {
    current = lang;
    applyLang(lang);
    document.querySelectorAll('.lang-btn').forEach(function(btn){
      const active = btn.getAttribute('data-lang') === lang;
      btn.classList.toggle('active', active);
    });
  };

  applyLang('en');
})();
</script>
'''

if '</body>' in html:
    html = html.replace('</body>', i18n_script + '</body>', 1)
else:
    html += i18n_script

Path('index.html').write_text(html, encoding='utf-8')
print('Added i18n to original design')
print('File size:', len(html))
