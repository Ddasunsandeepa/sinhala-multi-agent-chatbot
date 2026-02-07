def detect_intent(tokens):

    if "ආයුබෝවන්" in tokens or "හයි" in tokens or "hello" in tokens:
        return "greeting"

    if "ලයිබ්රරි" in tokens or "library" in tokens:
        return "faq"

    if "විශ්වවිද්‍යාලය" in tokens or "university" in tokens:
        return "university"

    if "කොහොමද" in tokens:
        return "smalltalk"

    return "fallback"
