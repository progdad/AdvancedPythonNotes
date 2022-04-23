def permute(seq):
    """
    This function returns all the possible unique mixes of symbols in sequence

    Example with "xyz" string:
        xyz, xzy, zxy, zyx, yxz, yzx

    :param seq: any sequence
    """

    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]
            for x in permute(rest):
                yield seq[i:i + 1] + x


string1, string2 = ["h", "a", "r", "d"], "truly"
print(*(permute(string1)))  # ['h', 'a', 'r', 'd'] ['h', 'a', 'd', 'r'] ['h', 'r', 'a', 'd'] ['h', 'r', 'd', 'a'] ['h', 'd', 'a', 'r'] ['h', 'd', 'r', 'a'] ['a', 'h', 'r', 'd'] ['a', 'h', 'd', 'r'] ['a', 'r', 'h', 'd'] ['a', 'r', 'd', 'h'] ['a', 'd', 'h', 'r'] ['a', 'd', 'r', 'h'] ['r', 'h', 'a', 'd'] ['r', 'h', 'd', 'a'] ['r', 'a', 'h', 'd'] ['r', 'a', 'd', 'h'] ['r', 'd', 'h', 'a'] ['r', 'd', 'a', 'h'] ['d', 'h', 'a', 'r'] ['d', 'h', 'r', 'a'] ['d', 'a', 'h', 'r'] ['d', 'a', 'r', 'h'] ['d', 'r', 'h', 'a'] ['d', 'r', 'a', 'h']
print(*(permute(string2)))  # truly truyl trluy trlyu tryul trylu turly turyl tulry tulyr tuyrl tuylr tlruy tlryu tlury tluyr tlyru tlyur tyrul tyrlu tyurl tyulr tylru tylur rtuly rtuyl rtluy rtlyu rtyul rtylu rutly rutyl rulty rulyt ruytl ruylt rltuy rltyu rluty rluyt rlytu rlyut rytul rytlu ryutl ryult ryltu rylut utrly utryl utlry utlyr utyrl utylr urtly urtyl urlty urlyt urytl urylt ultry ultyr ulrty ulryt ulytr ulyrt uytrl uytlr uyrtl uyrlt uyltr uylrt ltruy ltryu ltury ltuyr ltyru ltyur lrtuy lrtyu lruty lruyt lrytu lryut lutry lutyr lurty luryt luytr luyrt lytru lytur lyrtu lyrut lyutr lyurt ytrul ytrlu yturl ytulr ytlru ytlur yrtul yrtlu yrutl yrult yrltu yrlut yutrl yutlr yurtl yurlt yultr yulrt yltru yltur ylrtu ylrut ylutr ylurt
