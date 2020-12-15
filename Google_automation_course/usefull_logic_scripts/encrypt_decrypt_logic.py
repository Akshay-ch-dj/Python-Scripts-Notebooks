
def encrypt(text, n):

    if text and n > 0:
        str1, str2 = '', ''
        # get the text in even and odd index
        for i in range(0, len(text), 2):
            str1 += text[i]
            if i < len(text) - 1:
                str2 += text[i + 1]
        text = str2 + str1
        n -= 1
        return encrypt(text, n)

    return text


def decrypt(encrypted_text, n):

    if encrypted_text and n > 0:
        # separate the pieces to even and odd sections
        eIStr = encrypted_text[int(len(encrypted_text)/2):]
        oIStr = encrypted_text[:int(len(encrypted_text)/2)]

        # join them in a interlaced way
        orStr = "".join([a + b for a, b in zip(eIStr, oIStr)])

        # Add the extra element
        if len(eIStr) > len(oIStr):
            orStr = orStr + eIStr[-1]
        n -= 1
        return decrypt(orStr, n)
    return encrypted_text
