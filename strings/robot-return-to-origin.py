def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    charCount = collections.Counter(moves)
    if charCount["U"] == charCount["D"] and charCount["L"] == charCount["R"]:
        return True
    return False
