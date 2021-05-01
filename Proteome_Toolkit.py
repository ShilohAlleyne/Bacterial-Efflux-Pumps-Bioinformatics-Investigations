import re
from Efflux_Pump_Motifs_Patterns import Type_1_Motifs
from Efflux_Pump_Motifs_Patterns import Type_2_Motifs
from Efflux_Pump_Motifs_Patterns import Type_2_Combo
from Efflux_Pump_Motifs_Patterns import Validate


global X
global Y


class Type_1_Search(object):

    # NOTE: Searches for the FGFAGR Motif and generates a file with the matches
    def FGFAGR(Hypo_Proteins):
        FGFAGR_1_Motif_Matches = Type_1_Motifs.FGFAGR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in FGFAGR_1_Motif_Matches:
                FGFAGR_1_Motif_Position = re.search(r'FGFAGR', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(FGFAGR_1_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the FXFAXR Motif and generates a file with the matches
    def FXFAXR(Hypo_Proteins):
        FXFAXR_2_Motif_Matches = Type_1_Motifs.FXFAXR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in FXFAXR_2_Motif_Matches:
                FXFAXR_2_Motif_Position = re.search(r'F.FA.R', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(FXFAXR_2_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the FGFXXR Motif and generates a file with the matches
    def FGFXXR(Hypo_Proteins):
        FGFXXR_3_Motif_Matches = Type_1_Motifs.FGFXXR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in FGFXXR_3_Motif_Matches:
                FGFXXR_3_Motif_Position = re.search(r'FGF..R', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(FGFXXR_3_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the FGFXGX Motif and generates a file with the matches
    def FGFXGX(Hypo_Proteins):
        FGFXGX_4_Motif_Matches = Type_1_Motifs.FGFXGX.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in FGFXGX_4_Motif_Matches:
                FGFXGX_4_Motif_Position = re.search(r'FGF.G.', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(FGFXGX_4_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the FGXXGR Motif and generates a file with the matches
    def FGXXGR(Hypo_Proteins):
        FGXXGR_5_Motif_Matches = Type_1_Motifs.FGXXGR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in FGXXGR_5_Motif_Matches:
                FGXXGR_5_Motif_Position = re.search(r'FG..GR', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(FGXXGR_5_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the FXFXXR Motif and generates a file with the matches
    def FXFXXR(Hypo_Proteins):
        FXFXXR_6_Motif_Matches = Type_1_Motifs.FXFXXR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in FXFXXR_6_Motif_Matches:
                FXFXXR_6_Motif_Position = re.search(r'F.F..R', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(FXFXXR_6_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the YXFAXR Motif and generates a file with the matches
    def YXFAXR(Hypo_Proteins):
        YXFAXR_7_Motif_Matches = Type_1_Motifs.YXFAXR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as f:
            for match in YXFAXR_7_Motif_Matches:
                YXFAXR_7_Motif_Position = re.search(r'Y.FA.R', match[1])
                print(match[0], file=f)
                print(match[1], file=f)
                print(YXFAXR_7_Motif_Position, file=f)
                print('\n', file=f)

    # NOTE: Searches for the YGFXXR Motif and generates a file with the matches
    def YGFXXR(Hypo_Proteins):
        YGFXXR_8_Motif_Matches = Type_1_Motifs.YGFXXR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in YGFXXR_8_Motif_Matches:
                YGFXXR_8_Motif_Position = re.search(r'YGF..R', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(YGFXXR_8_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the YGFXGX Motif and generates a file with the matches
    def YGFXGX(Hypo_Proteins):
        YGFXGX_9_Motif_Matches = Type_1_Motifs.YGFXGX.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in YGFXGX_9_Motif_Matches:
                YGFXGX_9_Motif_Position = re.search(r'YGF.G.', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(YGFXGX_9_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the YGXXGR Motif and generates a file with the matches
    def YGXXGR(Hypo_Proteins):
        YGXXGR_10_Motif_Matches = Type_1_Motifs.YGXXGR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in YGXXGR_10_Motif_Matches:
                YGXXGR_10_Motif_Position = re.search(r'YG..GR', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(YGXXGR_10_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the YXFXXR Motif and generates a file with the matches
    def YXFXXR(Hypo_Proteins):
        YXFXXR_11_Motif_Matches = Type_1_Motifs.YXFXXR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in YXFXXR_11_Motif_Matches:
                YXFXXR_11_Motif_Position = re.search(r'Y.F..R', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(YXFXXR_11_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the FGYXXR Motif and generates a file with the matches
    def FGYXXR(Hypo_Proteins):
        FGYXXR_12_Motif_Matches = Type_1_Motifs.FGYXXR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in FGYXXR_12_Motif_Matches:
                FGYXXR_12_Motif_Position = re.search(r'FGY..R', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(FGYXXR_12_Motif_Position, file=X)
                print('\n', file=X)

    # NOTE: Searches for the FXYXXR Motif and generates a file with the matches
    def FXYXXR(Hypo_Proteins):
        FXYXXR_13_Motif_Matches = Type_1_Motifs.FXYXXR.findall(
            str(Hypo_Proteins))
        with open('Type 1 Motifs.txt', 'a') as X:
            for match in FXYXXR_13_Motif_Matches:
                FXYXXR_13_Motif_Position = re.search(r'F.Y..R', match[1])
                print(match[0], file=X)
                print(match[1], file=X)
                print(FXYXXR_13_Motif_Position, file=X)
                print('\n', file=X)


class Type_2_Search(object):

    # NOTE: Searches for the VEKSSSSF Motif
    # NOTE: and generates a file with the matches
    def VEKSSSSF(Hypo_Proteins):
        VEKSSSSF_1_Motif_Matches = Type_2_Combo.VEKSSSSF.findall(
            str(Hypo_Proteins))
        with open('Type 1 & 2 Motifs.txt', 'a') as Y:
            for match in VEKSSSSF_1_Motif_Matches:
                VEKSSSSF_1_Motif_Position = re.search(r'VEKSSSSF', match[1])
                print(match[0], file=Y)
                print(match[1], file=Y)
                print(match[2], file=Y)
                print(VEKSSSSF_1_Motif_Position, file=Y)
                print('\n', file=Y)

    # NOTE: Searches for the SSSS Motif and generates a file with the matches
    def SSSS(Hypo_Proteins):
        SSSS_2_Motif_Matches = Type_2_Combo.SSSS.findall(
            str(Hypo_Proteins))
        with open('Type 1 & 2 Motifs.txt', 'a')as Y:
            for match in SSSS_2_Motif_Matches:
                SSSS_2_Motif_Position = re.search(r'SSSS', match[1])
                print(match[0], file=Y)
                print(match[1], file=Y)
                print(match[2], file=Y)
                print(SSSS_2_Motif_Position, file=Y)
                print('\n', file=Y)

    # NOTE: Searches for the EKSSSS Motif and generates a file with the matches
    def EKSSSS(Hypo_Proteins):
        EKSSSS_3_Motif_Matches = Type_2_Combo.EKSSSS.findall(
            str(Hypo_Proteins))
        with open('Type 1 & 2 Motifs.txt', 'a') as Y:
            for match in EKSSSS_3_Motif_Matches:
                EKSSSS_3_Motif_Position = re.search(r'EKSSSS', match[1])
                print(match[0], file=Y)
                print(match[1], file=Y)
                print(match[2], file=Y)
                print(EKSSSS_3_Motif_Position, file=Y)
                print('\n', file=Y)

    # NOTE:  Searches for the XXXSSSSX Motif
    # NOTE: and generates a file with the matches
    def XXXSSSSX(Hypo_Proteins):
        XXXSSSSX_4_Motif_Matches = Type_2_Combo.XXXSSSSX.findall(
            str(Hypo_Proteins))
        with open('Type 1 & 2 Motifs.txt', 'a') as Y:
            for match in XXXSSSSX_4_Motif_Matches:
                XXXSSSSX_4_Motif_Position = re.search(r'...SSSS.', match[1])
                print(match[0], file=Y)
                print(match[1], file=Y)
                print(match[2], file=Y)
                print(XXXSSSSX_4_Motif_Position, file=Y)
                print('\n', file=Y)

    # NOTE:  Searches for the XhXXSSSSXh Motif
    # NOTE:  and generates a file with the matches
    def XhXXSSSSXh(Hypo_Proteins):
        XhXXSSSSXh_5_Motif_Matches = Type_2_Combo.XhXXSSSSXh.findall(
            str(Hypo_Proteins))
        with open('Type 1 & 2 Motifs.txt', 'a') as Y:
            for match in XhXXSSSSXh_5_Motif_Matches:
                XhXXSSSSXh_5_Motif_Position = re.search(
                    r'[AILMFVPG]..SSSS[AILMFVPG]', match[1])
                print(match[0], file=Y)
                print(match[1], file=Y)
                print(match[2], file=Y)
                print(XhXXSSSSXh_5_Motif_Position, file=Y)
                print('\n', file=Y)

    # NOTE: Searches for the XXpXpSSSSX Motif
    # NOTE: and generates a file with the matches
    def XXpXpSSSSX(Hypo_Proteins):
        XXpXpSSSSX_6_Motif_Matches = Type_2_Combo.XXpXpSSSSX.findall(
            str(Hypo_Proteins))
        with open('Type 1 & 2 Motifs.txt', 'a') as Y:
            for match in XXpXpSSSSX_6_Motif_Matches:
                XXpXpSSSSX_6_Motif_Position = re.search(
                    r'.[QNHSTYC][QNHSTYC]SSSS.', match[1])
                print(match[0], file=Y)
                print(match[1], file=Y)
                print(match[2], file=Y)
                print(XXpXpSSSSX_6_Motif_Position, file=Y)
                print('\n', file=Y)

    # NOTE: Matches for the XhXpXpSSSSXh Motif
    # NOTE: and generates a file with the matches
    def XhXpXpSSSSXh(Hypo_Proteins):
        XhXpXpSSSSXh_7_Motif_Matches =\
            Type_2_Combo.XhXpXpSSSSXh.findall(str(Hypo_Proteins))
        with open('Type 1 & 2 Motifs.txt', 'a') as Y:
            for match in XhXpXpSSSSXh_7_Motif_Matches:
                XhXpXpSSSSXh_7_Motif_Position = re.search(
                    r'[AILMFVPG][QNHSTYC][QNHSTYC]SSSS[AILMFVPG]', match[1])
                print(match[0], file=Y)
                print(match[1], file=Y)
                print(match[2], file=Y)
                print(XhXpXpSSSSXh_7_Motif_Position, file=Y)
                print('\n', file=Y)


class Type_1_Count(object):

    # NOTE: Counts the number of Hypo Proteins with the FGFAGR Motif
    def FGFAGR(Hypo_Proteins):
        print('[1] FGFAGR Protein Number =', len(
            Type_1_Motifs.FGFAGR.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the FXFAXR Motif
    def FXFAXR(Hypo_Proteins):
        print('[2] FXFAXR Protein Number =', len(
            Type_1_Motifs.FXFAXR.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the FGFAGR Motif
    def FGFXXR(Hypo_Proteins):
        print('[3] FGFXXR Protein Number = ', len(
            Type_1_Motifs.FGFXXR.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the FGFXGX Motif
    def FGFXGX(Hypo_Proteins):
        print('[4] FGFXGX Protein Number =', len(
            Type_1_Motifs.FGFXGX.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the FGXXGR Motif
    def FGXXGR(Hypo_Proteins):
        print('[5] FGXXGR Protein Number =', len(
            Type_1_Motifs.FGXXGR.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the FXFXXR Motif
    def FXFXXR(Hypo_Proteins):
        print('[6] FXFXXR Protein Number =', len(
            Type_1_Motifs.FXFXXR.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the YXFAXR Motif
    def YXFAX(Hypo_Proteins):
        print('[7] YXFAXR Protein Number =', len(
            Type_1_Motifs.YXFAXR.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the YGFXXR Motif
    def YGFXXR(Hypo_Proteins):
        print('[8] YGFXXR Protein Number =', len(
            Type_1_Motifs.YGFXXR.findall(Hypo_Proteins)))

    # NOTE: Counts the number Hypo Proteins with the YGFXGX Motif
    def YGFXGX(Hypo_Proteins):
        print('[9] YGFXGX Protein Number =', len(
            Type_1_Motifs.YGFXGX.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the YGXXGR Motif
    def YGXXGR(Hypo_Proteins):
        print('[10] YGXXGR Protein Number =', len(
            Type_1_Motifs.YGXXGR.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the YXFXXR Motif
    def YXFXXR(Hypo_Proteins):
        print('[11] YXFXXR Protein Number =', len(
            Type_1_Motifs.YXFXXR.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the FGYXXR Motif
    def FGYXXR(Hypo_Proteins):
        print('[12] FGYXXR Protein Number =', len(
            Type_1_Motifs.FGYXXR.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the FXYXXR Motif
    def FXYXXR(Hypo_Proteins):
        print('[13] FXYXXR Protein Number =', len(
            Type_1_Motifs.FXYXXR.findall(Hypo_Proteins)))


class Type_2_Count(object):

    # NOTE:  Counts the number of Hypo Proteins with the VEKSSSSF Motif
    def VEKSSSSF(Hypo_Proteins):
        print('[1] VEKSSSSF Protein Number =', len(
            Type_2_Motifs.VEKSSSSF.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the SSSS Motif
    def SSSS(Hypo_Proteins):
        print('[2] SSSS Protein Number =', len(
            Type_2_Motifs.SSSS.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the EKSSSS Motif
    def EKSSSS(Hypo_Proteins):
        print('[3] EKSSSS Protein Number =', len(
            Type_2_Motifs.EKSSSS.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the XXXSSSSX Motif
    def XXXSSSSX(Hypo_Proteins):
        print('[4] XXXSSSSX Protein number =', len(
            Type_2_Motifs.XXXSSSSX.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Hypo Proteins with the XhXXSSSSXh Motif
    def XhXXSSSSXh(Hypo_Proteins):
        print('[5] XhXXSSSSXh Protein number =', len(
            Type_2_Motifs.XhXXSSSSXh.findall(Hypo_Proteins)))

    # NOTE: Counts the number of proteins with the XhXpXpSSSSXh Motif
    def XXpXpSSSSX(Hypo_Proteins):
        print('[6] XhXpXpSSSSX Protein number =', len(
            Type_2_Motifs.XXpXpSSSSX.findall(Hypo_Proteins)))

    # NOTE: Counts the number of Proteins with the XhXpXpSSSSXh
    def XhXpXpSSSSXh(Hypo_Proteins):
        print('[7] XhXpXpSSSSXh Protien number =', len(
            Type_2_Motifs.XhXpXpSSSSXh.findall(Hypo_Proteins)))


class Double_Motif(object):
    # NOTE: Matches Hypo Proteins contains type 1 & 2 motifs within positions
    # NOTE: 600-700 and 100-160 repectively with sequnces longer than 850
    def Validate(Protein):
        Val_Matches = Validate.Protein.findall(str(Protein))
        with open('Valid Proteins.txt', 'w') as a, open(
                'Invalid Proteis.txt', 'w') as b:
            for match in Val_Matches:
                T1_Motif_Start = int(match[2])
                T1_Motif_End = int(match[3])
                T2_Motif_Start = int(match[5])
                T2_Motif_End = int(match[6])
                if len(match[1]) >= 850\
                        and T1_Motif_Start >= 600 and T1_Motif_End <= 700\
                        and T2_Motif_Start >= 100 and T2_Motif_End <= 160:
                    print(match[0], 'Valid')
                    print(match[0], file=a)
                    print(match[1], file=a)
                    print('Motif =', match[4], end='', file=a)
                    print(' | ' 'Motif Position =', match[2], end='-', file=a)
                    print(match[3], file=a)
                    print('Motif =', match[7], end='', file=a)
                    print(' | ' 'Motif Position =', match[5], end='-', file=a)
                    print(match[6], file=a)
                    print('\n', file=a)
                else:
                    print(match[0], 'Not Valid')
                    print(match[0], 'Not Valid', file=b)
                    print('\n', file=b)

    # NOTE: Counts the number of proteins that contain both types of motifs and
    # NOTE: Removes dupilcates
    def Count(Protein):
        Double_Motif_NP = Validate.NP.findall(Protein)
        Double_Motif_WP = Validate.WP.findall(Protein)
        Double_Motif_ALM = Validate.ALM.findall(Protein)
        ListNP = list(match for match in Double_Motif_NP)
        ListWP = list(match for match in Double_Motif_WP)
        ListALM = list(match for match in Double_Motif_ALM)
        NPNoDupes = tuple(dict.fromkeys(ListNP))
        WPNoDupes = tuple(dict.fromkeys(ListWP))
        ALMNoDupes = tuple(dict.fromkeys(ListALM))
        if len(NPNoDupes) > 0:
            print('Double Motif Protein Number =',  len(NPNoDupes))
            for i in NPNoDupes:
                print(i, sep='')
        if len(WPNoDupes) > 0:
            print('Double Motif Protein Number =',  len(WPNoDupes))
            for i in WPNoDupes:
                print(i, sep='')
        if len(ALMNoDupes) > 0:
            print('Double Motif Protein Number =',  len(ALMNoDupes))
            for i in ALMNoDupes:
                print(i, sep='')

    # NOTE: Counts the number of proteins that match the search criteria
    def Count_Valid(Protein):
        print('Valid Protein Number = ', len(
            Validate.Protein.findall(Protein)))
