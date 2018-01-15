from collections import Counter


def detect_anagrams(word, candidates):
    return [candidate for candidate in candidates
            if Counter(candidate.lower()) == Counter(word.lower())
            and candidate.lower() != word.lower()]
