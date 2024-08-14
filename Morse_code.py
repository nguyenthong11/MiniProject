MORSE_CODE_DICT: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/', '!': '-.-.--',
}


def text2morse(text: str) -> str:
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)


def morse2text(text: str) -> str:
    text_list = list(MORSE_CODE_DICT.keys())
    morse_list = list(MORSE_CODE_DICT.values())
    text_morse_list = text.split()
    return ''.join(text_list[morse_list.index(t)] for t in text_morse_list)
