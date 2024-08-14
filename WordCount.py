from collections import Counter
import re


def get_frequency(text: str, k: int) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common(k)


def word_count(n: int = 5) -> None:
    text: str = input().strip()
    word_frequency: list[tuple[str, int]] = get_frequency(text, n)
    for word, count in word_frequency:
        print(f'{word}: {count}')
