import re, os

exts = {'.jpg','.jpeg','.png','.webp','.svg','.gif','.ico','.mp3','.mp4'}
missing=[]
for root, dirs, files in os.walk('.'):
    norm = os.path.normpath(root)
    if '.git' in norm.split(os.sep):
        continue
    for fn in files:
        if fn.lower().endswith(('.html','.css','.js')):
            path = os.path.join(root, fn)
            text = open(path, 'r', encoding='utf-8', errors='ignore').read()
            for m in re.findall(r'["\']([^"\']+\.(?:jpg|jpeg|png|webp|svg|gif|ico|mp3|mp4))["\']', text, flags=re.I):
                if m.startswith('http') or m.startswith('data:'):
                    continue
                ref = m.lstrip('/')
                if ref and not os.path.exists(ref):
                    missing.append((os.path.relpath(path), m))
print('MISSING REFERENCES:')
for path, m in missing:
    print(path, '->', m)
