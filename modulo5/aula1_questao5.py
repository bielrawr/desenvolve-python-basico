import emoji
print("Emojis disponíveis:")
print()
print(emoji.emojize(':thumbs_up:')," - :thumbs_up:")
print(emoji.emojize(':red_heart:'),"  - :red_heart:")
print(emoji.emojize(':robot:')," - :robot:")
print(emoji.emojize(':eyes:')," - :eyes:")
print(emoji.emojize(':partying_face:')," - :partying_face:")
print(emoji.emojize(':sleepy_face:')," - :sleepy_face:")
print(emoji.emojize(':zany_face:')," - :zany_face:")
print(emoji.emojize(':grimacing_face:')," - :grimacing_face:")
print(emoji.emojize(':face_exhaling:'),"- :face_exhaling:")
print(emoji.emojize(':crying_face:')," - :crying_face:")


frase = input("Digite uma frase e ela será emojizada: ")
print(emoji.emojize(frase))