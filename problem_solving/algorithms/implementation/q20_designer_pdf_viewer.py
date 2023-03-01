def designerPdfViewer(h, word):
    height = 0
    for i in word:
        var = h[ord(i) - 97]
        if var > height:
            height = var
    return height*len(word)
