import re, os

repls = {
    '/1 copy copy copy.jpg': '/1.jpg',
    '/2 copy copy copy.jpg': '/2.jpg',
    '/3 copy copy copy.jpg': '/3.jpg',
    '/4 copy copy copy.jpg': '/4.jpg',
    '/5 copy copy copy.jpg': '/5.jpg',
    '/1 copy copy.jpg': '/1.jpg',
    '/2 copy copy.jpg': '/2.jpg',
    '/3 copy copy.jpg': '/3.jpg',
    '/4 copy copy.jpg': '/4.jpg',
    '/5 copy copy.jpg': '/5.jpg',
    '/1 copy.jpg': '/1.jpg',
    '/2 copy.jpg': '/2.jpg',
    '/3 copy.jpg': '/3.jpg',
    '/4 copy.jpg': '/4.jpg',
    '/5 copy.jpg': '/5.jpg',
}
changed = []
for root, dirs, files in os.walk('.'):
    norm = os.path.normpath(root)
    if '.git' in norm.split(os.sep):
        continue
    for fn in files:
        if fn.lower().endswith(('.html','.css','.js')):
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, '.')
            text = open(path, 'r', encoding='utf-8', errors='ignore').read()
            updated = text
            for old, ref in repls.items():
                if old in updated:
                    updated = updated.replace(old, ref)
            if updated != text:
                open(path, 'w', encoding='utf-8', errors='ignore').write(updated)
                changed.append(rel)
print('CHANGED:')
for c in changed:
    print(' ', c)
