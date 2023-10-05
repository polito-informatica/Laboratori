# Esercizio 02.2.4
# Emoji

# Ipotizziamo che le mie Emoji più frequenti siano le seguenti:
" 👍 🙂 😲 "

# Per conoscere il codice Unicode si può usare la funzione ord()
# ord('👍') --> 128077
# Nelle tabelle Unicode solitamente si usa il valore espresso in base 16
# che si può ottenere dalla funzione hex()
# hex(128077) --> '0x1f44d'
# o direttamente: hex(ord('👍')) --> '0x1f44d'

emoji1 = '👍'
rank1 = 4 # from https://home.unicode.org/emoji/emoji-frequency/
unicode1 = '1F44D' # from https://unicode-table.com/en/1F44D/
name1 = 'Thumbs Up Sign'

emoji2 = '🙂'
rank2 = 28 # from https://home.unicode.org/emoji/emoji-frequency/
unicode2 = '1F642' # from https://unicode-table.com/en/1F642/
name2 = 'Slightly Smiling Face'

emoji3 = '😲'
rank3 = 111 # from https://home.unicode.org/emoji/emoji-frequency/
unicode3 = '1F632' # from https://unicode-table.com/en/1F632/
name3 = 'Astonished Face'

print("Emoji 1", emoji1)
print(f'Posizione={rank1}, numero={unicode1}, nome={name1}')

print("Emoji 2", emoji2)
print(f'Posizione={rank2}, numero={unicode2}, nome={name2}')

print("Emoji 3", emoji3)
print(f'Posizione={rank3}, numero={unicode3}, nome={name3}')

# Nota: se leggete bene l'articolo citato nel testo, verso il fondo fa riferimento a questo documento
# https://docs.google.com/spreadsheets/d/1Zs13WJYdZL1pNZP0dCIXkWau_tZOjK3mmJz0KNq4I30/edit#gid=196891844
# che contiene in forma tabulare tutte le informazioni che ci servono!
# Leggere fino in fondo conviene sempre...
