from ..utils import applier


def fix_caps(text):
    if text and text[0].isupper() and (text[-1].islower() or len(text) == 2):
        return text[0].upper() + text[1:].lower()
    return text


apply = applier(fix_caps)
