import re


class Type_1_Motifs(object):

    # NOTE: Matches for the FGFAGR Motif
    FGFAGR = re.compile(r'''
        (^\>.+)\n
        (.+FGFAGR.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the FXFAXR Motif
    FXFAXR = re.compile(r'''
        (^\>.+)\n
        (.+F.FA.R.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the FGFXXR Motif
    FGFXXR = re.compile(r'''
        (^\>.+)\n
        (.+FGF..R.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the FGFXGX Motif
    FGFXGX = re.compile(r'''
        (^\>.+)\n
        (.+FGF.G..+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the FGXXGR Motif
    FGXXGR = re.compile(r'''
        (^\>.+)\n
        (.+FG..GR.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the FXFXXR Motif
    FXFXXR = re.compile(r'''
        (^\>.+)\n
        (.+F.F..R.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the YXFAXR Motif
    YXFAXR = re.compile(r'''
        (^\>.+)\n
        (.+Y.FA.R.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the YGFXXR Motif
    YGFXXR = re.compile(r'''
        (^\>.+)\n
        (.+YGF..R.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the YGFXGX Motif
    YGFXGX = re.compile(r'''
        (^\>.+)\n
        (.+YGF.G..+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the YGXXGR Motif
    YGXXGR = re.compile(r'''
        (^\>.+)\n
        (.+YG..GR.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the YXFXXR Motif
    YXFXXR = re.compile(r'''
        (^\>.+)\n
        (.+Y.F..R.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the FGYXXR Motif
    FGYXXR = re.compile(r'''
        (^\>.+)\n
        (.+FGY..R.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the FXYXXR Motif
    FXYXXR = re.compile(r'''
        (^\>.+)\n
        (.+F.Y..R.+)\n
            ''', re.VERBOSE | re.M)


class Type_2_Motifs(object):

    # NOTE: Matches for the VEKSSSSF Motif
    VEKSSSSF = re.compile(r'''
        (^\>.+)\n
        (.+VEKSSSSF.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the SSSS Motif
    SSSS = re.compile(r'''
        (^\>.+)\n
        (.+SSSS.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the EKSSSS Motif
    EKSSSS = re.compile(r'''
        (^\>.+)\n
        (.+EKSSSS.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the XXXSSSSX Motif
    XXXSSSSX = re.compile(r'''
        (^\>.+)\n
        (.+...SSSS..+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for XhXXSSSSXh Motif
    XhXXSSSSXh = re.compile(r'''
        (^\>.+)\n
        (.+[AILMFVPG]..SSSS[AILMFVPG].+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the XXpXpSSSSX Motif
    XXpXpSSSSX = re.compile(r'''
        (^\>.+)\
        (.+.[QNHSTYC][QNHSTYC]SSSS..+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the XhXpXpSSSSXh Motif
    XhXpXpSSSSXh = re.compile(r'''
        (^\>.+)\n
        (.+[AILMFVPG][QNHSTYC][QNHSTYC]SSSS[AILMFVPG].+)\n
            ''', re.VERBOSE | re.M)


class Type_2_Combo(object):

    # NOTE: Matches for the VEKSSSSF Motif
    VEKSSSSF = re.compile(r'''
        (^\>.+)\n
        (.+VEKSSSSF.+)\n
        (.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the SSSS Motif
    SSSS = re.compile(r'''
        (^\>.+)\n
        (.+SSSS.+)\n
        (.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the EKSSSS Motif
    EKSSSS = re.compile(r'''
        (^\>.+)\n
        (.+EKSSSS.+)\n
        (.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the XXXSSSSX Motif
    XXXSSSSX = re.compile(r'''
        (^\>.+)\n
        (.+...SSSS..+)\n
        (.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for XhXXSSSSXh Motif
    XhXXSSSSXh = re.compile(r'''
        (^\>.+)\n
        (.+[AILMFVPG]..SSSS[AILMFVPG].+)\n
        (.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the XXpXpSSSSX Motif
    XXpXpSSSSX = re.compile(r'''
        (^\>.+)\
        (.+.[QNHSTYC][QNHSTYC]SSSS..+)\n
        (.+)\n
            ''', re.VERBOSE | re.M)

    # NOTE: Matches for the XhXpXpSSSSXh Motif
    XhXpXpSSSSXh = re.compile(r'''
        (^\>.+)\n
        (.+[AILMFVPG][QNHSTYC][QNHSTYC]SSSS[AILMFVPG].+)\n
        (.+)\n
            ''', re.VERBOSE | re.M)


class Validate(object):

    Protein = re.compile(r'''
        (^\>.+)\n                   # NOTE: Matches for title
        (.+)\n                      # NOTE: Matches for Protein Seq
        .+span\=\(([0-9]+)\,\s      # NOTE: Matches for start of Type 1 Motif
        ([0-9]+)\)\,                # NOTE: Matches for the end of Type 1 Motif
        .+match\=\'([A-Z]+)\'.+\n   # NOTE: Matches for the Type 1 Motif
        .+span\=\(([0-9]+)\,\s      # NOTE: Matches for start of Type 2 Motif
        ([0-9]+)\)\,                # NOTE: Matches for the end of Type2 Motif
        .+match\=\'([A-Z]+)\'.+\n   # NOTE: Matches for the Type 2 Motif
            ''', re.VERBOSE | re.M)

    NP = re.compile(r'''
            NP_[0-9]+\.[0-9]
                ''', re.VERBOSE | re.M)

    WP = re.compile(r'''
            WP_[0-9]+\.[0-9]
                ''', re.VERBOSE | re.M)

    ALM = re.compile(r'''
            ALM[0-9]+\.[0-9]
                ''', re.VERBOSE | re.M)
