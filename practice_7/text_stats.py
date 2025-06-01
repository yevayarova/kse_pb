def count_words(text):
    slova = text.split()
    return len(slova)

def average_word_length(text):
    words = text.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)