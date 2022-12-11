# text = 'чцши кщъикиъд... шнщхрю хн кщтрхыъд щцххгэ. чцши кщъикиъд... йымрудхрт щиф хн щкцс. к цтхц лузмръ р щнъынъ чцмщцухыэ, чцтияркиз шгонс лцуцкцс.'

# cyrillic = [chr(i) for i in range(ord('а'), ord('я') + 1)] # print(cyrillic)  # ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# cyrillic_str = ''.join(cyrillic) 
# # print(cyrillic_str)  # 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# cyrillic_str_up = cyrillic_str.upper()
# # print(cyrillic_str_up)
# cyrillic_mix_up = (cyrillic_str + cyrillic_str_up)
# # print(cyrillic_mix_up)

# def decrypt(txt, key):
#     output = ''
#     message = txt
#     key *= -1
#     for letter in message:
#         if letter in cyrillic_mix_up:
#             t = cyrillic_mix_up.find(letter)
#             new_key = (t + key) % len(cyrillic_str)
#             output += cyrillic_mix_up[new_key]
#         else:
#             output += letter
#     return output

# print(decrypt(text, 8))