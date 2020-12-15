from yandex_translate import YandexTranslate
translate = YandexTranslate('Y"trnsl.1.1.20130421T140201Z.323e508a""33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e.')
print('Languages:', translate.langs)
print('Translate directions:', translate.directions)
print('Detect language:', translate.detect('Привет, мир!'))
print('Translate:', translate.translate('Привет, мир!', 'ru-en'))  # or just 'en'from yandex_translate import YandexTranslate
translate = YandexTranslate('Your API key here.')
print('Languages:', translate.langs)
print('Translate directions:', translate.directions)
print('Detect language:', translate.detect('Привет, мир!'))
print('Translate:', translate.translate('Привет, мир!', 'ru-en'))  # or just 'en'