import requests
r = requests.get('https://translate.google.co.in/translate_a/single?client=t&sl=en&tl=zh&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=btn&rom=1&ssel=0&tsel=4&kc=0&tk=186965.301202&q=how')
print type(r), r.text
