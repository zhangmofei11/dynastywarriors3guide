import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/8a02faad964c47b5c2ad3c045f68786b"></script>
<script data-cfasync="false" src="https://bauval.org/14/2eff1633b8fdcdabcd48e270e9a70207"></script>
<script>
  atOptions = {
    'key' : 'e2d5cbc72e40cba08ff7090268ff5b97',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/e2d5cbc72e40cba08ff7090268ff5b97"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-8a02faad964c47b5c2ad3c045f68786b"></div>
</div>'''

files = ['index.html', 'weapons.html', 'characters.html', 'fusion.html', 'musou-modes.html', 'stages.html', 'tier-list.html', 'secrets.html', 'tips.html', 'about.html', 'privacy-policy.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if 'e2d5cbc72e40cba08ff7090268ff5b97' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-8a02faad964c47b5c2ad3c045f68786b' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')