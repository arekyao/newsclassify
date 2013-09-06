import jieba


def getWordsFromTextFile(fileName):
    """
     * Code for reading a file.  you probably don't want to modify anything here, 
     * unless you don't like the way we segment files.
    """
    contents = []
    f = open(fileName)
    for line in f:
        contents.append(line.replace('\n',''))
    f.close()

    seg_result = segmentWords(''.join(contents))

    result = (", ".join(seg_result)).encode('utf-8').split(",")

    return result

def segmentWords(str):
    """
     * Splits lines on whitespace for file reading
    """
    return jieba.cut(str, cut_all=False)




