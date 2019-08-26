
def countCharacters(self, words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    res = 0
    for word in words:
        indicator = True
        for i in word:
            if word.count(i) > chars.count(i):
                indicator = False
                break
        if indicator:
            res += len(word)
    return res
