import unittest
import main


class TestModule4(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual(35, main.task_1("inIg"))
        self.assertEqual(0, main.task_1(""))
        self.assertEqual(68, main.task_1("zYt"))
        self.assertEqual(16, main.task_1("q"))
        self.assertEqual(57, main.task_1("btv Q"))
        self.assertEqual(10, main.task_1("k"))
        self.assertEqual(754, main.task_1("jioezJiUVQDs fhs JzeDmatLmmj xnoDbl iqeTEMAuMxjEkNEeN rRWQXS YfU hWW "))
        self.assertEqual(924,
                         main.task_1("GAJIbktZkpMNuKzLvy vja gMhcmSTHXkXuSEgVykXDRewjotzcMWGtFpqKcXh  CXyoSM Q NQ"))
        self.assertEqual(795, main.task_1("GoQHfZWKk o CwrML CLIwIjmB SmGALtaCZw WIJqUgsGobtmSZHeekvYgzcfBSI chGv Nym"))
        self.assertEqual(644, main.task_1("HmNI UVJYdOHcyJpvFbgIHChWwkJjZ pFU UVVDhoym qj HsHmubINfIq "))
        self.assertEqual(476, main.task_1("YIFpt VsXpknKtJ qCjOQZqVwQjPi L tjTU "))
        self.assertEqual(774, main.task_1("GnkOIzOGOeBtHMRCH  fRQ QZtT fDLWuhhCsS rAr kMhPoPObn xjtMUSKw nHj qJILeU"))
        self.assertEqual(495, main.task_1(" hEYoyMOtiRZrYas jWxZWxqgdjiOrj BQawdgO"))
        self.assertEqual(560, main.task_1("xqLgL YtocxwT  OsWK F C  IkBMIDRtPCopT kjJlUKfM HNQRIJ"))
        self.assertEqual(657, main.task_1("ZHIV  BgTueKQrzFLuybPEZFA Ea P L kUQMD sllX inFEHYllqgacQ opvyR"))
        self.assertEqual(390, main.task_1("ikvgCOkMdrF CdHaQEmDDyGYGCupKBhB FSqnQwEmKA"))
        self.assertEqual(843,
                         main.task_1("  MSkBRHcyxMvEvUfDsaHPLT DMP r wchYDxzWCECdJmIHcgp U yUW rB aSnLOnQNvyau x oaY"))
        self.assertEqual(393, main.task_1("dLVPXwmbKwkIziODi Hb xjCjNGbXgzYqM"))
        self.assertEqual(639, main.task_1("dFOERwBnLMJ A KRHWeXwiGdMeQIEemNmWs h   wM TiBqzLYBPIo jKzQaGSmCa"))
        self.assertEqual(841,
                         main.task_1("X EbfBFsUqIAGBpytoW FpecwzfzaJIeLUxOAblELUDuIWAuNqiQjC q S fFWSkOuUl mTzUHV"))
        self.assertEqual(380, main.task_1("v JX tcY XZhAj   icoCaREIZjZX BaY PW T"))
        self.assertEqual(407, main.task_1("ysjYnnTtcpmwEiFmO sBocQm aDAC OvfFUoHu"))
        self.assertEqual(1002,
                         main.task_1("VZeFCuJtwK LQKJHvDhqSwxSbZY f WkXduQXpy FOQXEWGGJjNxjDy EZvzsvlbVxa ybYrhvEGN"))
        self.assertEqual(562, main.task_1(" ZPIt dSgtLfwscHGTHCQ k jZTOxEe R  UKO D o  LsIdgKbH j qdAa nfmcbkN"))
        self.assertEqual(728, main.task_1("BqridryJLWCU kzKL  nOSsmFwYnOiXCoXp   TdWbEJ brLIMeEBYvWbVa EcQaWBiQk"))
        self.assertEqual(930,
                         main.task_1("OiDqvN KFmMZ uxgKqMqZxFjWfeP RXVQb a gnOkozvsrgifUvzHg bhkRyRPhextyQeyc  PLXD"))
        self.assertEqual(722, main.task_1(" qHrBCLbMwvx KEqAedspPVtKY dBXIubkfG PkSxRp kGRxJb YzC DeDFfx Z GjvlIp  "))
        self.assertEqual(516, main.task_1("BsBrg OUbB frRvVlonIZekDYUU QkT amrYLujxdGol J "))
        self.assertEqual(773, main.task_1("y kJk qCYHipLv yRgyrUtbBumPUu GXH jtzCI RDIVINwMtGnLyl adzwFnbtz "))
        self.assertEqual(807, main.task_1("EmVX bOnDFxdZFa jUypZdpKFmH jNVZuB  mTpUAzdR NN  CRswpSzLHhpPahnT RrrW"))
        self.assertEqual(909,
                         main.task_1("CEYTghjRT TrpLX flTSPvF  WuLquoBiyWPfilbXnmI yypBXax xG c ETfyYfwIhnovY qm K"))

    def test_task_2(self):
        self.assertEqual([27, 40, 55],
                         main.task_2("WD gbjnpDjesQpMprLw  lHvhDYJBBQO yKxpggNJBWXzGbsWzEvvQEJjxIh  d h", "J"))
        self.assertEqual([12, 24, 55, 58],
                         main.task_2("T mUM nyBA VF m KkqwhlbEFZLUCiWHNjKNRwAmo UynDfz qGGB OFNaFLTMEDgAVGdKxnCxwvXyOc",
                                     "F"))
        self.assertEqual([13, 19, 84], main.task_2(
            "owctPEtQV k ijDtko j qCA Fz aNuFpYELKr beEZUh pHvProc  nVNH   unDFtUi bwQy MbByEXVJTjYCLFUt hNISJ", "j"))
        self.assertEqual([3], main.task_2("zJXVsLARxv Pt yzobyZYiEzYbrFjvjKFAEhEuE aCNlQSPx zG  OUOOuw", "V"))
        self.assertEqual([41], main.task_2("TbaKlUCSqKnANVafZgmCLLBZKQYBObVyp e cpazBWqlAKqwAj FirmDyBhZ", "W"))
        self.assertEqual([3, 43, 54], main.task_2("Rr pn Bri  OFPjIKG MXi DTYXuiumRkFEHNiFIgBdp dCrRbCJIkpW", "p"))
        self.assertEqual([42], main.task_2(
            "oNcnZHYqkp tfG AyWNvUUBzcpe oZxybpmKw bCyrPXiRRSDuJJUrlMB nKqkSrwjMhReoeHGe f sTdReX", "P"))
        self.assertEqual([17, 21, 27, 33, 38, 41, 48, 49, 55, 56, 62, 86], main.task_2(
            "sYVPiAeHKaCuPjgWN wYw PufNH dcRIQ kEgv pd CZDuxE  syElk  obTDQ iYXqjtGNZloGcYVErkTiTDW O", " "))
        self.assertEqual([2, 3], main.task_2("qqSS ZT oBWmzOEgLxcc mOWtYzXhBjQRWafQbvQeshbNksJmRegZHagKdqd lok", "S"))
        self.assertEqual([48], main.task_2("ERSUsy fZj KiUSSM snYTPFmmecRDHwyVwCUIOMXg  ZBcYur", "u"))
        self.assertEqual([45, 77], main.task_2(
            "pJW BRVVtWMUQ yDdiSsdmG TPzTiLzbwY aPoWLDgJYOqMFo EWRsNLzMcvJKYjBtBBTumZ callqoVsutdub", "q"))
        self.assertEqual([], main.task_2("joRhf E xLnURnffr OniZQcoYLVWeGhWYBZGkag imKa ZakIE ctQySwccPi", "D"))
        self.assertEqual([0, 10, 34, 46, 54, 56],
                         main.task_2(" jiwHtTUAB oJdwkLLWxQnfcxXJksTMpqQ mOHlNojLlMy tLVUXmP n gaLFgkDoLWWGSufjHc",
                                     " "))
        self.assertEqual([11],
                         main.task_2("QHzWmTNr IrObrEKUbC  hm JPAMHmBP h wzZtxhaJEhFXIVonKC  HjoHfYIRqdxlmKshDXP VNDx",
                                     "O"))
        self.assertEqual([27, 54],
                         main.task_2("wIv toRQfuPFuQFvvKiElzmusnYxZSjLP RizYJwUHRsB cyOI blrxKJiTeSVyHJC WHY", "x"))
        self.assertEqual([47], main.task_2(
            "QomCQS SRXzlJXHKiao afp WhherNV XdlB oIYjhWnoGcFnPosD WvOuxhhmL  S UEVVjKuL CmvYrQff  fQXVuuAiPgodtz",
            "F"))
        self.assertEqual([47], main.task_2("UPVifmVITTlOMUqbAcqiGlHTCtmaFh AywV H LlgGq EzmWXXrgzf", "W"))
        self.assertEqual([36], main.task_2("CzHHaxWHLhplXnUKgfpsayBXc nwsE eZ SFGsqlAc pEsNTUXc Rtt aWFegBaPydH", "G"))
        self.assertEqual([2, 12, 29],
                         main.task_2("v PLBRBnGWLePQbXugniZqvFzcEzqPSOcAisIE ZZIp BMeLeguCDOqGtFm Sl  ", "P"))
        self.assertEqual([],
                         main.task_2("luOvAjn Zl GVNXqSuIbr oZaxTYaqLYRUvigAIfxgPNPOZRcoIkLv smrIalS QHR  M Qojb", "w"))
        self.assertEqual([12, 16, 34, 46, 52],
                         main.task_2("ZPGZnhdxjOML MHN GPKGCWbkaQYRygHXx AqPCVFbqjGp rQCXN mPbnTPSSh", " "))
        self.assertEqual([],
                         main.task_2("itbxpq HBH PPw HJOcams fke IMT hXcc ckPFhX  EhjpEhRchsUNZqMfWZAhKanEuHLCsZ I qA ",
                                     "l"))
        self.assertEqual([57], main.task_2(" af LGEpibSxelK VkyrMoT WJpllABhqbWunuIBaoEIpw aHtbMGztpsYu tqZ", "Y"))
        self.assertEqual([2, 7, 22], main.task_2(
            "F nflbTnBGdGAmdey TUhGngKJRdBMtd tPFYTaHKcuZdUaTmhjatPS cJQkBrh fJuVXc  SxsZXCyrGE p", "n"))
        self.assertEqual([], main.task_2("cXGxHbDHe O G kQGeoeDEhq WEzaYgyW BPHFEqsyAf HjQFSa", "l"))
        self.assertEqual([9], main.task_2(
            " kBIAiPAdbxtmkttmMIusumSo PZUpwN VlgJcUB t  Z aDhcjO oQ fqvikJ zCIzHXtQBq dOYCBsDcpBqg xGKf", "b"))
        self.assertEqual([55], main.task_2("wUgNgQQ ZOwIjkjrxNe sOmwDfA  cU mnwFCJGbhGyj pR QBHlHnKdbvXcfT", "d"))
        self.assertEqual([], main.task_2("LEhxqGuxKq XxpzOddzWpTubwwBkY SgYpEmuqlMdtN JMSbkwy  yjZrViaVj", "v"))
        self.assertEqual([4, 40, 61],
                         main.task_2("uWjIlDQLA NXa qBIyDynBfGeygfH iPVzKcH sJl DEkiFKKTABdQ hRcKH lhCfLzdaVjHOyY VkU",
                                     "l"))
        self.assertEqual([],
                         main.task_2("YkNPYJmwhYPk pmngaWB BLEXfSTYpRFcom hygJYhVpkPvSTbfbhSP iJ SOqD ImXFhBh KlIX ",
                                     "d"))

    def test_task_3(self):
        self.assertEqual(False, main.task_3(
            "Wo AfdHudkvvHxEX tNHJgMNzCFLikQPCoSUP ClpYVQTloPMnF w OZfuDtUZWJKg G WmoC wxZU lpTUqMJprqtCUvSYXTK",
            "brxpMGK QPC kIndx"))
        self.assertEqual(True, main.task_3("vp RG dOX G QOprmDpLfwxWbtUjtoeA RVEcdLtElVAQy evpz NdCIwnXfkOfA HQ",
                                           "prmDpLfwx"))
        self.assertEqual(True,
                         main.task_3("LAxZsTkNxIno tSeEORtiO HQZFpaOUxXPbxbaxacESMegae LmzZiQVR", "no tSeEORtiO "))
        self.assertEqual(False,
                         main.task_3("GpddwwjnrVuOez  PIJZ jH slTbTCAWYdkywOtV  sJYT CilCVxx w", "wMUwCa  UMCieURh"))
        self.assertEqual(False, main.task_3("xYQeeIQQZhhI AsSqGKbuYfzTcVb VLWDOlxMzlyVJAaRGRMpWYlhVloURpojKyKdjJqBWxIO",
                                            "JoXNyIzKyF ylxeY"))
        self.assertEqual(True, main.task_3(" YVIJ prIynyhwNcvFbNulAWhwFHVNvJj JDjoP xCbX sGgFo", "FbNulA"))
        self.assertEqual(True, main.task_3(
            "ggNeJmOgitYaiZ vxrFGSl by JHsXajUzMTcx qfldYRMZzIFplNyEs uOCKqavjfFZVt PosVrgjZHoM", "S"))
        self.assertEqual(True, main.task_3("rL dVqpsjdH IwdFuJdf thBL JSuksYyaXR  hWraEgGPISMl Ju O KPwCKvGz",
                                           "FuJdf thBL J"))
        self.assertEqual(True, main.task_3("hD LwvcfYHAPFcXblXWL GKz ee TabdIwvyvtKyha cldd FK IuvVno zgXJUlrs",
                                           "FcXblXWL G"))
        self.assertEqual(False, main.task_3(
            "dLKJdPWMZJzIvqgy Lbb dkmzbuJcVmG DbcwlzKoQj  rPKRH tD CfysTGpe T   HYdmvm HeJZaKhlAg", "mwW xkWJHb"))
        self.assertEqual(True, main.task_3(
            "M hb  dIopj tVmfVxrDLqsheFbHKf HqQKjqJt sUTzUD UJTFmASkUJN nLYwcGrNgLzdIHpJQhGbZFh", "mfVxrDLqsheF"))
        self.assertEqual(True, main.task_3(
            " kjaShG vDGDvG XhIFIWfxs WkLDcfgpkvA NaaaFaZQYT BkxHCMHj lIU zjbYGwTIkC lykdjdAPL vX RyuF wdmEehYE",
            "vG XhIFIWfxs WkLD"))
        self.assertEqual(False, main.task_3(
            "tUvCHiDjLRgqOUZbjnaJWpYIz i kdn  pIXs   QhgDHjjKwqfHJq gQlSxvchPwUpkCAPNVB gSHsorxRbT pRxQeanVcwM",
            "XBy fXIrbevjWMVk"))
        self.assertEqual(True, main.task_3(
            "XuTZWmU W ooYrIpUPHQgEHSTmZxb QwNvfEZz nGNsaPLqdRtySsleOqGG WrQjVtktL tvnppR Fv UwmJhK VI", "gEHSTm"))
        self.assertEqual(True, main.task_3(
            "fgrLvLuw kE  GwaajGSeCQGOFxXhWwRufWzk SC MsoaFORvlgkOThlLZLwZiNFwFNlJZ  hIX XFSLSE ", "aajGSeCQGOFx"))
        self.assertEqual(False, main.task_3(
            "TYibAzVjZ  BKjeGzT RJOPLq MpGVBmp b c SvgDQc oJRhCvsaKUhxWzxxuHLVEpyMHSNgMh gFJjMNr Tg fVU",
            "MmKrjKnvUShfKdu"))
        self.assertEqual(True, main.task_3(
            " dGLuUafgaglwaXX OAGEW tHP VmDQ vCHzGqeSVVhDZoahA zwOyARLIWH NWdymTm b TD kv  b WUAYFV jXZChm", " OAGE"))
        self.assertEqual(False, main.task_3("ALMwxYruRF FxxiKJFu tS deuseZ agketgZ BFDaCtGvHpQM", "ZaPHKEGMOltcOVXSO"))
        self.assertEqual(True, main.task_3("I neQTj nrVMyVlIo bzbZKELrIiVOzGrtAjeaBmnIgRFCZLXyar  PNyxfDVoa FhMU",
                                           "VMyVlIo bzbZKELr"))
        self.assertEqual(True, main.task_3("SvfdOV MV mpRt ceQidTbFKcUAEXnSxa CVdLrLTJjqUdcI fcKFTS", "QidT"))
        self.assertEqual(False, main.task_3("yEDPDvPpVnTFF aUqeo  SFdTHOuzJq pIKNXIHcEaKQYDNyYMzTLyHK izxEv NOgKr",
                                            "CDaDbQNrlYtkLtpJ"))
        self.assertEqual(False,
                         main.task_3("nSK mxJE atcizEwET SofTLHGL  bvEK e MF xLWhfuqC WmrC QSOQUmxynO  yzlXGbcFt cLxo",
                                     "xqnvNssFeXCbtyQeORH"))
        self.assertEqual(True, main.task_3("Heze rCEHOUUH qtLPyySKJsjgrLz doacVjepaKvrQVxJq tPOSr", "UUH qtLPyySKJsjg"))
        self.assertEqual(True, main.task_3(" kJLphYntaQuAwBvjKneCwolWBtPQHHLqHbHfDP US VQfwJV aQJSoAj zJHKKvWXJrD",
                                           "CwolWBtP"))
        self.assertEqual(True, main.task_3(" BjC rBqDTVtLoYYPPVHgslqWR JidYCNcHCFrjSLXwn MbLkyC", "YYPPVHgslqWR "))
        self.assertEqual(False, main.task_3(
            "CzyGdNQuX  fPiJCMXMvJMvUkudy fZ XMuFbtQnegmmUIeqSDSH RYthQVPfHeSAHCIEznHbZPsGTdeJBiXKLIsYWKB",
            " exlgCW Zqt d"))
        self.assertEqual(False,
                         main.task_3("HtveSnnkuUY  ldnymxL mUYgbKWHZqf QXdOEt hEfEi Nmd wCXchmfntzBtPOcIcugeLobaRplKH",
                                     "CeeBI Ocn ojNM"))
        self.assertEqual(False, main.task_3(
            "PwILFDKaDmpjkwuULVok EKir WIkOSRogS o kM qDMPnQSbMnJMJvqYVgESW oDbXaflDzJnIHV QIu", "wM ztE sPqP  "))
        self.assertEqual(False, main.task_3(
            "Dh XDdqPY JzuYeyl IIjxtnotozBwBRvMyP jUI lnqiOSQcxAJjUNdK  CabkYwRRIodxBxwTXuEOzGTe SzJynHYqwnKB",
            "TISaGssYKP"))
        self.assertEqual(False, main.task_3(
            "Ezh TyKUKPT c Uk olyqnuOVnUAo X rSWu GiEkAcrlud  XFZE FTe HhdPEOwxDxhoYkR XXC FVRLYa",
            "JmxpsCCTwE mpiaWobC"))

    def test_task_4(self):
        self.assertEqual(['iP anzgViuh', 'C ', 'd fUyY RgGDVGparG', 'zoQ', 'lNLNglx', '  BAV'],
                         main.task_4("iP anzgViuhjC Zd fUyY RgGDVGparGZzoQHlNLNglxZ  BAV", ['j', 'K', 'H', 'Z']))
        self.assertEqual(
            ['ngfutgpXaNx', 'absJtT', 'G ro', 'o', ' uNsLifMb', ' ABL EcoB', '', 'LOUTh', 'UY j ', 'gE', ' yi', 'b',
             ' LsE  S', 'Lrmpuh', '', 'Iue  fPI'],
            main.task_4("ngfutgpXaNxZabsJtTlG rodoz uNsLifMbQ ABL EcoBzDLOUThlUY j zgEk yiRbD LsE  SzLrmpuhdQIue  fPI",
                        ['R', 'Z', 'D', 'H', 'q', 'z', 'l', 'k', 'd', 'Q']))
        self.assertEqual(['zFPScnk', '', 'akNVR lktc ec  jbAVFrBmvamEM vXpO ovfSmS', 'ZuljvPkB DZYfnV inBNvttG'],
                         main.task_4("zFPScnkTUakNVR lktc ec  jbAVFrBmvamEM vXpO ovfSmSTZuljvPkB DZYfnV inBNvttG",
                                     ['U', 'T']))
        self.assertEqual(
            ['gVvqKsQlnAqb', 'iwPOZHzqZEb', 'SQivDOpqfIEmvm  oJuvDqcHjOglWbDf ', 'mwHnW  Dr zuwBS', 'tiRHjlWl'],
            main.task_4("gVvqKsQlnAqbMiwPOZHzqZEbMSQivDOpqfIEmvm  oJuvDqcHjOglWbDf xmwHnW  Dr zuwBSFtiRHjlWl",
                        ['N', 'x', 'X', 'F', 'M']))
        self.assertEqual(['cRaaoZnj s Nj zC', 'HYUO', 'H b', 'rNbJWibg', 'aJT J  utqQwzI LHTQKUu '],
                         main.task_4("cRaaoZnj s Nj zCXHYUOVH bVrNbJWibgvaJT J  utqQwzI LHTQKUu ",
                                     ['v', 'V', 'M', 'v', 'X']))
        self.assertEqual(
            ['Ug', 'e', 'gXacV', 'RtoUWePQHiBHjdFbZWDU', '', 'cWYXgZCBjcYWXRYvYiyBvOk', 'zCQoxsInHvTX', 'HnTFYNRyePNx',
             'OudQ', 'LUNZRncu', 'x'], main.task_4(
                "Ug e gXacVGRtoUWePQHiBHjdFbZWDU GcWYXgZCBjcYWXRYvYiyBvOkmzCQoxsInHvTX HnTFYNRyePNx OudQ LUNZRncu x",
                [' ', ' ', 'S', 'G', ' ', 'r', 'm']))
        self.assertEqual(['hGEVPxNXcz', 'ndM', 'uZwc', 'EEDsRtwQUrwJgJlogIdxcFdsC', 'P', '', 'N', 'IULjl'],
                         main.task_4("hGEVPxNXczWndM uZwc EEDsRtwQUrwJgJlogIdxcFdsC P WN IULjl", ['m', 'W', ' ']))
        self.assertEqual(
            ['', 'j', 'pP', 'xDGyP', '', 'XR', 'hMF', 'IxvPLXc m SS', 'KzHZ', 'jd', 'vx I EF', 'yRavHjFsIt oFo', 'JXX',
             'Unz', 'z V '], main.task_4("BjfpPqxDGyPbkXRbhMFBIxvPLXc m SSfKzHZgjdfvx I EFgyRavHjFsIt oFokJXXbUnzgz V ",
                                         ['r', 'k', 'b', 'q', 'f', 'g', 'W', 'g', 'B']))
        self.assertEqual(
            ['VyVb', 'ns', '', 'TmiF', 'X ve NmsXPa', 'uMAUI vEPX', 'h', 'k MDVn Fu', '', 'l', 'q SZyZ  D', ' pzXP uv',
             'ZYs CSUyfElrvfRBBCIw'],
            main.task_4("VyVbdnsWjTmiFoX ve NmsXPaxuMAUI vEPXxhjk MDVn FuWWlWq SZyZ  Dd pzXP uvoZYs CSUyfElrvfRBBCIw",
                        ['d', 'o', 'L', 'W', 'j', 'x', 'L']))
        self.assertEqual(['ICEjauTwUGP', 'Ii f', '', 'URCF uvA', 'i', 'quAsIAhqQr qa Fx U bmX', 'Cnr eKWvH  j'],
                         main.task_4("ICEjauTwUGPVIi flyURCF uvAyiVquAsIAhqQr qa Fx U bmXyCnr eKWvH  j",
                                     ['y', 'V', 'l']))
        self.assertEqual(
            ['TFF MLWyov  AdAocPOd', 'FzfjGm  gzGJlVxEywU', 'dZoKroYH W', 'MLzq I', 'lDS eNiCx ', 'X', 'RyNvhtpHU'],
            main.task_4("TFF MLWyov  AdAocPOdbFzfjGm  gzGJlVxEywUbdZoKroYH WQMLzq IQlDS eNiCx QXQRyNvhtpHU",
                        ['Q', 'b']))
        self.assertEqual(['oueaDj  dnXZ', 'JzgGcqd Dw x   SG', 'Tp hZ   LFPlN', 'ZI v', '', 'o', 'od lGvFlM'],
                         main.task_4("oueaDj  dnXZAJzgGcqd Dw x   SGfTp hZ   LFPlNAZI vUfofod lGvFlM",
                                     ['U', 'A', 'f', 'C']))
        self.assertEqual(['lyRk TtK', 'FJ', '', 'qQvzxzR', 'yuxCBMB', 'hrG aFBSqHhtS ', 'VAzWv', 'nnakP'],
                         main.task_4("lyRk TtKoFJsdqQvzxzRpyuxCBMBphrG aFBSqHhtS sVAzWvonnakP",
                                     ['s', 'd', 'm', 'f', 'p', 'O', 'O', 'o']))
        self.assertEqual(['FORCapdMaAtabgYVUyyRF', 'oUqjoTqVM', '', 'KUC', '', 'dn', '', 'fap', 'S', 'RScbpfL'],
                         main.task_4("FORCapdMaAtabgYVUyyRF oUqjoTqVM  KUCerdne fapESNRScbpfL",
                                     ['i', 'N', 'e', 'Q', 'E', ' ', 'h', 'r']))
        self.assertEqual(
            ['TwW', 'ADpIZMPuD', 'TZPO', 'LDmIJ', 'jj', 'n', 'dyqLQCMPsrC', '', 'NS', 'jKYF', 'IPL', 'W', 'R', 'ysaMw'],
            main.task_4("TwW ADpIZMPuD TZPOkLDmIJzjjongdyqLQCMPsrC  NSVjKYFxIPLVWoR ysaMw",
                        ['k', 'x', 'o', 'V', ' ', ' ', 'z', 'g']))
        self.assertEqual(
            ['BpL', 'g', 'WDg', ' d', '', 'BGe ', 'ae', '', '', '', 'hS h', 'SDc NANIS', 'k me  J', 'IIrr', ' p', '',
             'K H N', '', ' m Lp', 'Tb'],
            main.task_4("BpLsgsWDgw dwUBGe waeswlQhS hnSDc NANISlk me  JlIIrrs plUK H Nlu m LpsTb",
                        ['w', 'Q', 'n', 'O', 'q', 'U', 'u', 'l', 's']))
        self.assertEqual(
            ['ZiWJYRuKMLOSG', 'W', '', 'X', 'bL', 'rBaL', 'CssBsJUBM', 'UDJzgow', 'yoOJG', 'GSisNNYAXZDU', 'iM', 'EZpu',
             'j', 'CB'], main.task_4("ZiWJYRuKMLOSGQWPQX bL rBaLQCssBsJUBMhUDJzgowQyoOJGQGSisNNYAXZDUeiM EZpuIj CB",
                                     ['P', 'd', 'Q', 'P', ' ', 'P', 'h', 'e', 'I']))
        self.assertEqual(
            ['', 'Nnx', 'iTcSYyr', '', 'pU', '', 'nZWVHnLNCmIzuNmOZhukb', 'MOAWK', 'lt', 'PvN', '', 'HGL', '',
             'GeWThEKbaaTjHLc', 'VVp', 'ysEeL'],
            main.task_4(" Nnx iTcSYyr DpUJdnZWVHnLNCmIzuNmOZhukbdMOAWKdltDPvN  HGL dGeWThEKbaaTjHLc VVpdysEeL",
                        ['D', ' ', 'd', 'd', 'J']))
        self.assertEqual(['d', 'qae', 'gfyJFWTfztXbVTJJE', 't', 'NCREc', 'XHzgQRmEDp', 'RuXntJ', 'Stq', 'IOer', ''],
                         main.task_4("d qae gfyJFWTfztXbVTJJE t NCREckXHzgQRmEDpGRuXntJ Stq IOerk",
                                     ['k', ' ', 'h', 'k', 'G', ' ', 'v']))
        self.assertEqual(['pYNmKHvFjxniADmSjPQ yDLmUJyk mZHJdWAxWKNgLRRKhSojdnPGZLrOI lqa'],
                         main.task_4("pYNmKHvFjxniADmSjPQ yDLmUJyk mZHJdWAxWKNgLRRKhSojdnPGZLrOI lqa", ['c', 'B']))
        self.assertEqual(['', 'tYRZUs', 'VAY', 'Sk', 'ugUW', 'VcfxoyHedKP', 'NOk', 'HipxlkKUDxc', 'JHVHHnWMzrFYi',
                          'DmFEKQPVacfaSEHr'],
                         main.task_4("TtYRZUs VAYTSk ugUWIVcfxoyHedKPLNOkIHipxlkKUDxcGJHVHHnWMzrFYi DmFEKQPVacfaSEHr",
                                     ['L', 'G', ' ', 'T', 'I', 'v']))
        self.assertEqual(
            ['', ' ', 'P tGZolhCCDEEyzQ', 'YhTUnR', 'sfpCY', '', 'IXdUjLnWI Es mUE AB ', 'U', 'KFpAyyzu', 'R'],
            main.task_4("w iP tGZolhCCDEEyzQwYhTUnRisfpCYigIXdUjLnWI Es mUE AB kUgKFpAyyzuaR",
                        ['g', 'i', 'k', 'v', 'a', 'S', 'w']))
        self.assertEqual(['', 'gjzWQt wyGaV', 'c wP', 'W', 'kQZ', 'H qCtV ', ' FfP', 'y', ' P', 'x OCGvEB'],
                         main.task_4("dgjzWQt wyGaVXc wPdWXkQZXH qCtV d FfPXyL PUx OCGvEB",
                                     ['p', 'i', 'U', 'X', 'U', 'u', 'L', 'd']))
        self.assertEqual(
            ['lwrnjEBQCM', ' ', 'rpgs', 'sIJc POP ', 'OywtIL', 'kaUrcabio UDEUQJBsrJmBVczELw', 'OaA  G', '', '', 'hNB',
             'px Ly'], main.task_4("lwrnjEBQCMe FrpgsFsIJc POP ZOywtILRkaUrcabio UDEUQJBsrJmBVczELwFOaA  GeYehNBFpx Ly",
                                   ['R', 'F', 'Y', 'u', 'e', 'Z']))
        self.assertEqual(
            ['AnTWS', 'MXmcsf yYox', 'J', '', '', 'ATFgSzAqljxs', 'idR ', 'Fn', 'MiR', 'TES    fgA ', 'sPpORt', 'T',
             'Yx', 'pp'], main.task_4("AnTWSkMXmcsf yYoxKJVDQATFgSzAqljxskidR QFnKMiRDTES    fgA LsPpORtkTDYxwpp",
                                      ['D', 'K', 'D', 'L', 'V', 'Q', 'b', 'k', 'D', 'w']))
        self.assertEqual(
            ['', 'HvR', 'Hnrvg', 'qqP lxPXgvt x H ', 'UwJjEM v', 'ei', ' Hy P WJqIvnJuWMRQU', 'Jx EuEPBXRwE',
             'HYJby rEYmomsIT  O'],
            main.task_4("SHvRAHnrvgcqqP lxPXgvt x H AUwJjEM vAeiG Hy P WJqIvnJuWMRQUFJx EuEPBXRwEGHYJby rEYmomsIT  O",
                        ['c', 'S', 'F', 'G', 'K', 'A']))
        self.assertEqual(
            ['kOzKSSucVjsUlYizgxBpZS', 'WljpUyC vBzuskvFkZcpcpbdvqyEK F LGKbIFT upkhUZrw', 'PgPjVPUnMDlBnMNzevOlpi'],
            main.task_4(
                "kOzKSSucVjsUlYizgxBpZSfWljpUyC vBzuskvFkZcpcpbdvqyEK F LGKbIFT upkhUZrwoPgPjVPUnMDlBnMNzevOlpi",
                ['o', 't', 'f']))
        self.assertEqual(
            ['rbL', 'ARiiVldmEs', 'Q', 'Yp', '', 'BzBrEQlTuXPx', 'iOIQADeUwrcu', 'lWQP', 'HFPmRUgx', 'TuR', 'Etd',
             'qYIXQbSmx', 'YfsR', 'AZYK', '', '', 'im', 'zJt'], main.task_4(
                "rbL ARiiVldmEsjQjYp  BzBrEQlTuXPx iOIQADeUwrcu lWQP HFPmRUgx TuR EtdaqYIXQbSmxhYfsRhAZYK  aimjzJt",
                ['a', ' ', 'j', 'h']))
        self.assertEqual(['K', ' kzTg G H ZPJJDpAJ', 'FlMVx fCRQvHNFC', '', 'BOf Opiy rcmak'],
                         main.task_4("KS kzTg G H ZPJJDpAJhFlMVx fCRQvHNFCttBOf Opiy rcmak", ['S', 'h', 't', 'Y']))
        self.assertEqual(
            ['  qxbg ', 'EQ FHWRsOhArhepjWqEcZWRinf ', 'eH', 'q', 'kN NW xytN', 'oqQvHKvdJvyqHmtvLIevNpvdqB', 'Hct ',
             'Ofb MhD uL'], main.task_4(
                "  qxbg PEQ FHWRsOhArhepjWqEcZWRinf PeHSqUkN NW xytNXoqQvHKvdJvyqHmtvLIevNpvdqBXHct SOfb MhD uL",
                ['w', 'X', 'P', 'U', 'S']))

    def test_task_5(self):
        self.assertEqual(
            "AaBdJKKmoQStVvWXx adfghiQqRRVvy GiM fgIJKlPvVwxz bchjKOpSuXY T HhiJKKmmPQQRtTYZZz CeeFqTuV MMMOWxX",
            main.task_5(
                "QSmKJoBAXKWtVvdxa yRVQfivqdhgaR iGM vxJVIgflKzPw XKhcYubjpSO T ZimJmtQHQYRhZKKPzT ueTeCFVq OxMWMXM"))
        self.assertEqual("aAbBCcceGgjooPUvxXyyzzZ BcDEFhIjkLOpqRtXxyYz aAacDDddfJnPpTtuVwXXxY",
                         main.task_5("voCyUbzGazyxZcXojAcPegB cOXpELhRBIqtyxkFzjYD PXXpDTcYDndVufwtaAJxad"))
        self.assertEqual("AAaaBCcEfFGIjklLlmQTVwXYZ bbCcgGhhHhiJLmnnpqQrTWW GhqQy hIosW",
                         main.task_5("wBIVQCXGlTfFAkcZjALlmaYEa hgbrhiHmqnTCWcpWQhLbGJn qQGyh oWhsI"))
        self.assertEqual("bEElmNtuVvyzZ Hkm AacdfFGmnoPqssSTwXxxzZ cCEFJjKmTV bchkOPtuxy",
                         main.task_5("uNVzvtyEmZbEl mHk XwxPmTfqxdoAFzansZscGS KmcJVFjCTE POchutbxyk"))
        self.assertEqual("cKWxXyy cdEJjnnOqtVyyYz bBCeeoqu bBceemmooqqrtUwwXXz AcDeRt GkmquX",
                         main.task_5("xyKcyWX ndVJyyYtEqjOncz CqebuBeo UmetocwoXqbrBqzweXm ADecRt kXumqG"))
        self.assertEqual(
            "s CDeeIpQRT bbcDefkllMmPPqqUxXyyZ EMNQsSUuX AcElnqru cdntuw aabfHhiKLlmmMorTTTTUuVYy fgMOPqwxz",
            main.task_5(
                "s DCpITeQeR bklqyylDMPUfxcZemqPXb XMENUsuQS nluArcqE ndcwtu TmUTiTuafbKVYyTHoaLmhMrl OMwfqPzxg"))
        self.assertEqual("c AaCddelmnsvZ EFhIQquuVw CEw x BKTwWXy EeehkKLNPqqTTww BBDhHHijLNOoPqqrtUVvyzz p BMq  dfh",
                         main.task_5(
                             "c dAslevdmZaCn FuwVIQhEqu CEw x TyBKwWX ELeqheNqkTwwPKT rjqizOyVhtBzHqLvNPDoBUH p qMB  dhf"))
        self.assertEqual("HL GT A ajmnNPPQrVVwxz cCEelqt MQQWyZ ccHTzz  gmoPrsTu",
                         main.task_5("HL TG A QrVxnzVNjPmPwa cCltEqe QyWMQZ zTHczc  TuPgmros"))
        self.assertEqual(
            " aCcELLNnSxYZ AHKnoOWx DinrSTv DeILlNT BbeFJU adeffgjJjKMqr aCccCCCeffIjJLPQQqrRrSstVWXY  aAHnOP",
            main.task_5(
                " ZSYCLNnLaEcx oxWHKOAn vnSTriD LIeNDlT eBJFUb fgfjJdeMaqrKj IQrXCcQteRfacqjPWCrSLJCVfCYs  OanPHA"))
        self.assertEqual("bnqRV ABhIPpSs aNwy afGio fGkmSuyy aAceEFhJLMnPpqQRVvWwxXyyZZz ",
                         main.task_5("nqVRb PhSspIAB Nway Gofai GfyymukS WyqRZhnZyQeLEFJVzxwaXAcMPvp "))
        self.assertEqual("tUXX CfFghq cDEFGHiJNOPqsvw cJLlpt DEjptTWwZzZ BCcdEeFFFGgGGhhiIjjMMnnpSsTTuuVVvx hNsVw ",
                         main.task_5(
                             "XtXU qfhCFg OwGvEcHDqJPsFiN LcpltJ DZEzZjWtwpT hpGVSgunTjhCBVijEFTnGxdMeMcsIFuFGv sVhwN "))
        self.assertEqual(
            " qx Lt cCEeGHjjklNOPqSTy eP U  bdDfGhInNNppqRTxy dEEFkKOPpqrSSuWY X AccDeFFGghIJKnsy AbeFhiLPSXY",
            main.task_5(
                " xq tL ycHlkGEeCNTjPjSqO Pe U  fTydnRINGDNpxbhqp SFdPOEpukKEYWSqr X cGgAchesKFyDFJIn YSbeXhFAPiL"))
        self.assertEqual("AKms AbBDDeeEHHHHIillmmNprsttuWxXz chHjKKlQqtUW ABCcehLlLOVXxXxZ",
                         main.task_5("mAsK HemxHuNItrbetEplHlBisHmAzXDWD QKjlhUHWqcKt XxXOCeLZAhlBcVxL"))
        self.assertEqual("BJrRu HJrsuVZ BegJnOOpTZ aAFimoOoqstUUvXz ggkRy RuW Lt cDdiNOpPssuyz hnSuZ EeFIiKlNnPSy H",
                         main.task_5(
                             "rJuRB HJVusZr ZpOeTgBJOn UXvaUqoisOomFztA kygRg uWR tL zNuisOpyDsPcd hunZS NnEeSIyFPKli H"))
        self.assertEqual("ACGgijLpQrtuxZ ennz  DFjKmMpTVxy ABBccdddeeeeFFfGHJjjJJlNOpqqssTUUxz IY AXY CffIJJpRswwxZ",
                         main.task_5(
                             "uAQrGZigtLpCjx eznn  mFDxjMTpyKV JeUxFFfdNqjsdBeslpOGeTeAjJHccJzBdqU IY YXA IxZJfpfJwCswR"))
        self.assertEqual("abefillnNnoqTUWWZ bePS ACIkLmOovWY ADRRyZ bfhIlqTUWY BCEffIjKmOoOQrRSt hjpsw",
                         main.task_5("iZUfqWnNTeallonWb PeSb OYvoCWLAmIk yZDRAR IlWYqhbUTf EmrSKOofOfRQtBCjI swhpj"))
        self.assertEqual(
            "EgGHHquu aCeFFKmOy r tu gGiLmMnPttuUWx ALO bBBjLMoPVy AcDeFgjpQtvwY  BEeHIIjklPsuU cDEeegnOQSx",
            main.task_5(
                "gEuHHGuq FCeOymFaK r tu mPuMUinxtLgtGW OAL jbyBBPVoLM AgQweFvYDctjp  uklHIsIEBeUjP OngEeSQcxDe"))
        self.assertEqual(" BBBcDDdDEhKLLMmMnnoPPRStwyyZZ  bDegiImOooPqqrrsSTUvVWYZ  Ww BIms dDehhKmT DGMOprtU",
                         main.task_5(
                             " BLBnZPZPDcKyMRDmESMdyBDhowtnL  PsqYrZOrgvboiWVITmqUDSoe  Ww sBIm eKmhdDhT rDtGUOMp"))
        self.assertEqual("ly GhkW hlsT  bLosW CfFjkRRy fHIkMnqqruz  AabBcDfiIKKOrVXz annpQWxx",
                         main.task_5("ly hGkW Tlhs  sLobW RCfkjyFR qHzqnrfuIMk  AbKiaIzDKOrXcfBV xQnxaWnp"))
        self.assertEqual("GH  LrS cJpwx GijLlnR aBbCceGghiJNPSwxxyz dGjMoRuv CcCdFIkmnQRSsuYy giJjLPpPstwY BEmqy",
                         main.task_5(
                             "GH  rLS xwpJc GnRLjil BSaGehyJgCbPwxicxNz GudjoMvR SmFndCkQuIcCYsRy PgJwtpLsjYiP EmyqB"))
        self.assertEqual("FGgIilRVVWYyyZ bIptyz  Cnv Aj AdEmP CkqSY AggGiJmoPppssuUWx EFgGJlmMNqrUvWxYYz Mr",
                         main.task_5(
                             "lIWYGyFZgVViyR zbIypt  vCn jA EdPmA SYqCk ouWsxgUPgiJpGAmsp EmlrgFxMUqJYzWGvYN rM"))
        self.assertEqual("imv OQ defjLlmPpStyyzzz io fiJnoQVWy hIIKlZ BGHjllMMnoPQQuuVw y",
                         main.task_5("vim OQ PmtSzpdeLzljfyzy oi VoJfWnyQi lIKhZI GQnljMMuwoQPVBluH y"))
        self.assertEqual(
            "fhmMOz GPrU dox mP EjJjjKLmPprRwx aAbBbCEEghhIKLmoOPRRrSTwWWWWxxyz aaBdDGGHHhiijkLMnPPSSVWyyZZ   h",
            main.task_5(
                "zhmOfM UGPr dox Pm PjrxLKJjEmpwRj bSBERxyPzwRrWxKoOmThWWgbLIWEhaCA ZyiadkDPGSaMLHWHyjBZhVGSniP   h"))
        self.assertEqual("ImNnPSTTv x fhU gIllLQrruwZ CR  g  C b EEggqWwXZ LX Gz",
                         main.task_5("TPNnITmvS x Ufh uwIQgrllrZL RC  g  C b qXZWEwEgg LX Gz"))
        self.assertEqual("aAbbbcDefFHIiJKLLoOpPRUUwwxZ w aBBBbcegiijJjLmMmNnOoPpQqQQQRSTTVvvY",
                         main.task_5("IwJpRfUbPocDaHebFZUAKxLibOLw w RNTQVvBLjiPpaTqQQJnYBmvOMQBoecjSbigm"))
        self.assertEqual("AeILQQ FPqY bD F aHjV AAaBcEjnsUW m BBbcdDEfFgGGhiJjJKkkMmNOpPpRRvWwwXZ",
                         main.task_5("eAQILQ PFqY Db F VaHj WBjcAEUAans m RpJMZfvNXBmOKRPgBcbWGFEdGwpjkkwhiDJ"))
        self.assertEqual("bEFfFkPSsTvvxY jlMnpRStv Elo BefFIklnPXY ahijjouvvW aBddIQuW Jm cGHo",
                         main.task_5("SkvFEfFxTYsPvb tMSjnvlRp lEo nXfBkYIelPF vjvoujhWia uWIBQdda Jm ocHG"))
        self.assertEqual(" bDgGHiJjjtV  s rTV dHNNQrvwX ru myz jOS BG  bLmqs aKqU s acJmRstUv A",
                         main.task_5(" JtgHiGDjjVb  s rVT HQvrXwdNN ru zym OjS GB  mLbqs qaKU s scJRtUmav A"))
        self.assertEqual("EGPU cCfGNY bWY aCDEHhhKmmNoOpqrSuxy wz  EHjMp ddFggHKKLLMNoopqTVvWY",
                         main.task_5("PUEG YGcCfN YbW HmhDuoSCxyahOrEqNpmK zw  pjMEH VqYLKdMoFLNpgvKgTdHWo"))
        self.assertEqual(
            "BiiKoopRRRTUwwZ ACDFLNRTUuww ghjku adeFhHIKoORruUuVXXXy beGgT  aAFiKKKLNpqQRRTuvVwWXyZ dHkTv BQUw bE",
            main.task_5(
                "piTRoUiwZBRwoRK LUFDuARCwTwN ujhkg oFuXVUhXXeaRurIOyKdH eTbGg  KaivKRNwFpyqWXVLAKuZTRQ dHvTk UBwQ bE"))

