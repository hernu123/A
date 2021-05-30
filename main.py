"""
Python Program:
 Using collections.Counter() to print the char frequency in string
"""
from collections import Counter

input_string = "GFS WMY OG LGDVS MF SFNKYHOSU ESLLMRS, PC WS BFGW POL DMFRQMRS, PL OG CPFU M UPCCSKSFO HDMPFOSXO GC OIS LMES DMFRQMRS DGFR SFGQRI OG CPDD GFS LISSO GK LG, MFU OISF WS NGQFO OIS GNNQKKSFNSL GC SMNI DSOOSK. WS NMDD OIS EGLO CKSJQSFODY GNNQKKPFR DSOOSK OIS 'CPKLO', OIS FSXO EGLO GNNQKKPFR DSOOSK OIS 'LSNGFU' OIS CGDDGWPFR EGLO GNNQKKPFR DSOOSK OIS 'OIPKU', MFU LG GF, QFOPD WS MNNGQFO CGK MDD OIS UPCCSKSFO DSOOSKL PF OIS HDMPFOSXO LMEHDS. OISF WS DGGB MO OIS NPHISK OSXO WS WMFO OG LGDVS MFU WS MDLG NDMLLPCY POL LYEAGDL. WS CPFU OIS EGLO GNNQKKPFR LYEAGD MFU NIMFRS PO OG OIS CGKE GC OIS 'CPKLO' DSOOSK GC OIS HDMPFOSXO LMEHDS, OIS FSXO EGLO NGEEGF LYEAGD PL NIMFRSU OG OIS CGKE GC OIS 'LSNGFU' DSOOSK, MFU OIS CGDDGWPFR EGLO NGEEGF LYEAGD PL NIMFRSU OG OIS CGKE GC OIS 'OIPKU' DSOOSK, MFU LG GF, QFOPD WS MNNGQFO CGK MDD LYEAGDL GC OIS NKYHOGRKME WS WMFO OG LGDVS."
frequency_per_char = Counter(input_string)

# Show Output
print ("Per char frequency in '{}' is :\n {}".format(input_string, str(frequency_per_char)))
print ("Typeof frequency_per_char is: ",type(frequency_per_char))


string_a = "GFS WMY OG LGDVS MF SFNKYHOSU ESLLMRS, PC WS BFGW POL DMFRQMRS, PL OG CPFU M UPCCSKSFO HDMPFOSXO GC OIS LMES DMFRQMRS DGFR SFGQRI OG CPDD GFS LISSO GK LG, MFU OISF WS NGQFO OIS GNNQKKSFNSL GC SMNI DSOOSK. WS NMDD OIS EGLO CKSJQSFODY GNNQKKPFR DSOOSK OIS 'CPKLO', OIS FSXO EGLO GNNQKKPFR DSOOSK OIS 'LSNGFU' OIS CGDDGWPFR EGLO GNNQKKPFR DSOOSK OIS 'OIPKU', MFU LG GF, QFOPD WS MNNGQFO CGK MDD OIS UPCCSKSFO DSOOSKL PF OIS HDMPFOSXO LMEHDS. OISF WS DGGB MO OIS NPHISK OSXO WS WMFO OG LGDVS MFU WS MDLG NDMLLPCY POL LYEAGDL. WS CPFU OIS EGLO GNNQKKPFR LYEAGD MFU NIMFRS PO OG OIS CGKE GC OIS 'CPKLO' DSOOSK GC OIS HDMPFOSXO LMEHDS, OIS FSXO EGLO NGEEGF LYEAGD PL NIMFRSU OG OIS CGKE GC OIS 'LSNGFU' DSOOSK, MFU OIS CGDDGWPFR EGLO NGEEGF LYEAGD PL NIMFRSU OG OIS CGKE GC OIS 'OIPKU' DSOOSK, MFU LG GF, QFOPD WS MNNGQFO CGK MDD LYEAGDL GC OIS NKYHOGRKME WS WMFO OG LGDVS."
string_b = string_a.replace("G","o")
print(string_a)
print(string_b)

string_c = "oFS WMY Oo LoDVS MF SFNKYHOSU ESLLMRS, PC WS BFoW POL DMFRQMRS, PL Oo CPFU M UPCCSKSFO HDMPFOSXO oC OIS LMES DMFRQMRS DoFR SFoQRI Oo CPDD oFS LISSO oK Lo, MFU OISF WS NoQFO OIS oNNQKKSFNSL oC SMNI DSOOSK. WS NMDD OIS EoLO CKSJQSFODY oNNQKKPFR DSOOSK OIS 'CPKLO', OIS FSXO EoLO oNNQKKPFR DSOOSK OIS 'LSNoFU' OIS CoDDoWPFR EoLO oNNQKKPFR DSOOSK OIS 'OIPKU', MFU Lo oF, QFOPD WS MNNoQFO CoK MDD OIS UPCCSKSFO DSOOSKL PF OIS HDMPFOSXO LMEHDS. OISF WS DooB MO OIS NPHISK OSXO WS WMFO Oo LoDVS MFU WS MDLo NDMLLPCY POL LYEAoDL. WS CPFU OIS EoLO oNNQKKPFR LYEAoD MFU NIMFRS PO Oo OIS CoKE oC OIS 'CPKLO' DSOOSK oC OIS HDMPFOSXO LMEHDS, OIS FSXO EoLO NoEEoF LYEAoD PL NIMFRSU Oo OIS CoKE oC OIS 'LSNoFU' DSOOSK, MFU OIS CoDDoWPFR EoLO NoEEoF LYEAoD PL NIMFRSU Oo OIS CoKE oC OIS 'OIPKU' DSOOSK, MFU Lo oF, QFOPD WS MNNoQFO CoK MDD LYEAoDL oC OIS NKYHOoRKME WS WMFO Oo LoDVS."
string_d = string_c.replace("F","n")
print(string_c)
print(string_d)

string_e = "onS WMY Oo LoDVS Mn SnNKYHOSU ESLLMRS, PC WS BnoW POL DMnRQMRS, PL Oo CPnU M UPCCSKSnO HDMPnOSXO oC OIS LMES DMnRQMRS DonR SnoQRI Oo CPDD onS LISSO oK Lo, MnU OISn WS NoQnO OIS oNNQKKSnNSL oC SMNI DSOOSK. WS NMDD OIS EoLO CKSJQSnODY oNNQKKPnR DSOOSK OIS 'CPKLO', OIS nSXO EoLO oNNQKKPnR DSOOSK OIS 'LSNonU' OIS CoDDoWPnR EoLO oNNQKKPnR DSOOSK OIS 'OIPKU', MnU Lo on, QnOPD WS MNNoQnO CoK MDD OIS UPCCSKSnO DSOOSKL Pn OIS HDMPnOSXO LMEHDS. OISn WS DooB MO OIS NPHISK OSXO WS WMnO Oo LoDVS MnU WS MDLo NDMLLPCY POL LYEAoDL. WS CPnU OIS EoLO oNNQKKPnR LYEAoD MnU NIMnRS PO Oo OIS CoKE oC OIS 'CPKLO' DSOOSK oC OIS HDMPnOSXO LMEHDS, OIS nSXO EoLO NoEEon LYEAoD PL NIMnRSU Oo OIS CoKE oC OIS 'LSNonU' DSOOSK, MnU OIS CoDDoWPnR EoLO NoEEon LYEAoD PL NIMnRSU Oo OIS CoKE oC OIS 'OIPKU' DSOOSK, MnU Lo on, QnOPD WS MNNoQnO CoK MDD LYEAoDL oC OIS NKYHOoRKME WS WMnO Oo LoDVS."
string_f = string_e.replace("S","e")
print(string_f)

string_g = "one WMY Oo LoDVe Mn enNKYHOeU EeLLMRe, PC We BnoW POL DMnRQMRe, PL Oo CPnU M UPCCeKenO HDMPnOeXO oC OIe LMEe DMnRQMRe DonR enoQRI Oo CPDD one LIeeO oK Lo, MnU OIen We NoQnO OIe oNNQKKenNeL oC eMNI DeOOeK. We NMDD OIe EoLO CKeJQenODY oNNQKKPnR DeOOeK OIe 'CPKLO', OIe neXO EoLO oNNQKKPnR DeOOeK OIe 'LeNonU' OIe CoDDoWPnR EoLO oNNQKKPnR DeOOeK OIe 'OIPKU', MnU Lo on, QnOPD We MNNoQnO CoK MDD OIe UPCCeKenO DeOOeKL Pn OIe HDMPnOeXO LMEHDe. OIen We DooB MO OIe NPHIeK OeXO We WMnO Oo LoDVe MnU We MDLo NDMLLPCY POL LYEAoDL. We CPnU OIe EoLO oNNQKKPnR LYEAoD MnU NIMnRe PO Oo OIe CoKE oC OIe 'CPKLO' DeOOeK oC OIe HDMPnOeXO LMEHDe, OIe neXO EoLO NoEEon LYEAoD PL NIMnReU Oo OIe CoKE oC OIe 'LeNonU' DeOOeK, MnU OIe CoDDoWPnR EoLO NoEEon LYEAoD PL NIMnReU Oo OIe CoKE oC OIe 'OIPKU' DeOOeK, MnU Lo on, QnOPD We MNNoQnO CoK MDD LYEAoDL oC OIe NKYHOoRKME We WMnO Oo LoDVe."
string_h = string_g.replace("M","a")
print(string_h)

string_i = "one WaY Oo LoDVe an enNKYHOeU EeLLaRe, PC We BnoW POL DanRQaRe, PL Oo CPnU a UPCCeKenO HDaPnOeXO oC OIe LaEe DanRQaRe DonR enoQRI Oo CPDD one LIeeO oK Lo, anU OIen We NoQnO OIe oNNQKKenNeL oC eaNI DeOOeK. We NaDD OIe EoLO CKeJQenODY oNNQKKPnR DeOOeK OIe 'CPKLO', OIe neXO EoLO oNNQKKPnR DeOOeK OIe 'LeNonU' OIe CoDDoWPnR EoLO oNNQKKPnR DeOOeK OIe 'OIPKU', anU Lo on, QnOPD We aNNoQnO CoK aDD OIe UPCCeKenO DeOOeKL Pn OIe HDaPnOeXO LaEHDe. OIen We DooB aO OIe NPHIeK OeXO We WanO Oo LoDVe anU We aDLo NDaLLPCY POL LYEAoDL. We CPnU OIe EoLO oNNQKKPnR LYEAoD anU NIanRe PO Oo OIe CoKE oC OIe 'CPKLO' DeOOeK oC OIe HDaPnOeXO LaEHDe, OIe neXO EoLO NoEEon LYEAoD PL NIanReU Oo OIe CoKE oC OIe 'LeNonU' DeOOeK, anU OIe CoDDoWPnR EoLO NoEEon LYEAoD PL NIanReU Oo OIe CoKE oC OIe 'OIPKU' DeOOeK, anU Lo on, QnOPD We aNNoQnO CoK aDD LYEAoDL oC OIe NKYHOoRKaE We WanO Oo LoDVe."
string_j = string_i.replace("L","s")
print(string_j)

string_k = "one WaY Oo soDVe an enNKYHOeU EessaRe, PC We BnoW POs DanRQaRe, Ps Oo CPnU a UPCCeKenO HDaPnOeXO oC OIe saEe DanRQaRe DonR enoQRI Oo CPDD one sIeeO oK so, anU OIen We NoQnO OIe oNNQKKenNes oC eaNI DeOOeK. We NaDD OIe EosO CKeJQenODY oNNQKKPnR DeOOeK OIe 'CPKsO', OIe neXO EosO oNNQKKPnR DeOOeK OIe 'seNonU' OIe CoDDoWPnR EosO oNNQKKPnR DeOOeK OIe 'OIPKU', anU so on, QnOPD We aNNoQnO CoK aDD OIe UPCCeKenO DeOOeKs Pn OIe HDaPnOeXO saEHDe. OIen We DooB aO OIe NPHIeK OeXO We WanO Oo soDVe anU We aDso NDassPCY POs sYEAoDs. We CPnU OIe EosO oNNQKKPnR sYEAoD anU NIanRe PO Oo OIe CoKE oC OIe 'CPKsO' DeOOeK oC OIe HDaPnOeXO saEHDe, OIe neXO EosO NoEEon sYEAoD Ps NIanReU Oo OIe CoKE oC OIe 'seNonU' DeOOeK, anU OIe CoDDoWPnR EosO NoEEon sYEAoD Ps NIanReU Oo OIe CoKE oC OIe 'OIPKU' DeOOeK, anU so on, QnOPD We aNNoQnO CoK aDD sYEAoDs oC OIe NKYHOoRKaE We WanO Oo soDVe."
string_l = string_k.replace("A","b")
print(string_l)

string_m = "one WaY Oo soDVe an enNKYHOeU EessaRe, PC We BnoW POs DanRQaRe, Ps Oo CPnU a UPCCeKenO HDaPnOeXO oC OIe saEe DanRQaRe DonR enoQRI Oo CPDD one sIeeO oK so, anU OIen We NoQnO OIe oNNQKKenNes oC eaNI DeOOeK. We NaDD OIe EosO CKeJQenODY oNNQKKPnR DeOOeK OIe 'CPKsO', OIe neXO EosO oNNQKKPnR DeOOeK OIe 'seNonU' OIe CoDDoWPnR EosO oNNQKKPnR DeOOeK OIe 'OIPKU', anU so on, QnOPD We aNNoQnO CoK aDD OIe UPCCeKenO DeOOeKs Pn OIe HDaPnOeXO saEHDe. OIen We DooB aO OIe NPHIeK OeXO We WanO Oo soDVe anU We aDso NDassPCY POs sYEboDs. We CPnU OIe EosO oNNQKKPnR sYEboD anU NIanRe PO Oo OIe CoKE oC OIe 'CPKsO' DeOOeK oC OIe HDaPnOeXO saEHDe, OIe neXO EosO NoEEon sYEboD Ps NIanReU Oo OIe CoKE oC OIe 'seNonU' DeOOeK, anU OIe CoDDoWPnR EosO NoEEon sYEboD Ps NIanReU Oo OIe CoKE oC OIe 'OIPKU' DeOOeK, anU so on, QnOPD We aNNoQnO CoK aDD sYEboDs oC OIe NKYHOoRKaE We WanO Oo soDVe."
string_n = string_m.replace("B","k")
print(string_n)

string_o = "one WaY Oo soDVe an enNKYHOeU EessaRe, PC We knoW POs DanRQaRe, Ps Oo CPnU a UPCCeKenO HDaPnOeXO oC OIe saEe DanRQaRe DonR enoQRI Oo CPDD one sIeeO oK so, anU OIen We NoQnO OIe oNNQKKenNes oC eaNI DeOOeK. We NaDD OIe EosO CKeJQenODY oNNQKKPnR DeOOeK OIe 'CPKsO', OIe neXO EosO oNNQKKPnR DeOOeK OIe 'seNonU' OIe CoDDoWPnR EosO oNNQKKPnR DeOOeK OIe 'OIPKU', anU so on, QnOPD We aNNoQnO CoK aDD OIe UPCCeKenO DeOOeKs Pn OIe HDaPnOeXO saEHDe. OIen We Dook aO OIe NPHIeK OeXO We WanO Oo soDVe anU We aDso NDassPCY POs sYEboDs. We CPnU OIe EosO oNNQKKPnR sYEboD anU NIanRe PO Oo OIe CoKE oC OIe 'CPKsO' DeOOeK oC OIe HDaPnOeXO saEHDe, OIe neXO EosO NoEEon sYEboD Ps NIanReU Oo OIe CoKE oC OIe 'seNonU' DeOOeK, anU OIe CoDDoWPnR EosO NoEEon sYEboD Ps NIanReU Oo OIe CoKE oC OIe 'OIPKU' DeOOeK, anU so on, QnOPD We aNNoQnO CoK aDD sYEboDs oC OIe NKYHOoRKaE We WanO Oo soDVe."
string_p = string_o.replace("C","f")
print(string_p)

string_q = "one WaY Oo soDVe an enNKYHOeU EessaRe, Pf We knoW POs DanRQaRe, Ps Oo fPnU a UPffeKenO HDaPnOeXO of OIe saEe DanRQaRe DonR enoQRI Oo fPDD one sIeeO oK so, anU OIen We NoQnO OIe oNNQKKenNes of eaNI DeOOeK. We NaDD OIe EosO fKeJQenODY oNNQKKPnR DeOOeK OIe 'fPKsO', OIe neXO EosO oNNQKKPnR DeOOeK OIe 'seNonU' OIe foDDoWPnR EosO oNNQKKPnR DeOOeK OIe 'OIPKU', anU so on, QnOPD We aNNoQnO foK aDD OIe UPffeKenO DeOOeKs Pn OIe HDaPnOeXO saEHDe. OIen We Dook aO OIe NPHIeK OeXO We WanO Oo soDVe anU We aDso NDassPfY POs sYEboDs. We fPnU OIe EosO oNNQKKPnR sYEboD anU NIanRe PO Oo OIe foKE of OIe 'fPKsO' DeOOeK of OIe HDaPnOeXO saEHDe, OIe neXO EosO NoEEon sYEboD Ps NIanReU Oo OIe foKE of OIe 'seNonU' DeOOeK, anU OIe foDDoWPnR EosO NoEEon sYEboD Ps NIanReU Oo OIe foKE of OIe 'OIPKU' DeOOeK, anU so on, QnOPD We aNNoQnO foK aDD sYEboDs of OIe NKYHOoRKaE We WanO Oo soDVe."
string_r = string_q.replace("D","l")
print(string_r)

string_s = "one WaY Oo solVe an enNKYHOeU EessaRe, Pf We knoW POs lanRQaRe, Ps Oo fPnU a UPffeKenO HlaPnOeXO of OIe saEe lanRQaRe lonR enoQRI Oo fPll one sIeeO oK so, anU OIen We NoQnO OIe oNNQKKenNes of eaNI leOOeK. We Nall OIe EosO fKeJQenOlY oNNQKKPnR leOOeK OIe 'fPKsO', OIe neXO EosO oNNQKKPnR leOOeK OIe 'seNonU' OIe folloWPnR EosO oNNQKKPnR leOOeK OIe 'OIPKU', anU so on, QnOPl We aNNoQnO foK all OIe UPffeKenO leOOeKs Pn OIe HlaPnOeXO saEHle. OIen We look aO OIe NPHIeK OeXO We WanO Oo solVe anU We also NlassPfY POs sYEbols. We fPnU OIe EosO oNNQKKPnR sYEbol anU NIanRe PO Oo OIe foKE of OIe 'fPKsO' leOOeK of OIe HlaPnOeXO saEHle, OIe neXO EosO NoEEon sYEbol Ps NIanReU Oo OIe foKE of OIe 'seNonU' leOOeK, anU OIe folloWPnR EosO NoEEon sYEbol Ps NIanReU Oo OIe foKE of OIe 'OIPKU' leOOeK, anU so on, QnOPl We aNNoQnO foK all sYEbols of OIe NKYHOoRKaE We WanO Oo solVe."
string_t = string_s.replace("E","m")
print(string_t)

string_u = "one WaY Oo solVe an enNKYHOeU messaRe, Pf We knoW POs lanRQaRe, Ps Oo fPnU a UPffeKenO HlaPnOeXO of OIe same lanRQaRe lonR enoQRI Oo fPll one sIeeO oK so, anU OIen We NoQnO OIe oNNQKKenNes of eaNI leOOeK. We Nall OIe mosO fKeJQenOlY oNNQKKPnR leOOeK OIe 'fPKsO', OIe neXO mosO oNNQKKPnR leOOeK OIe 'seNonU' OIe folloWPnR mosO oNNQKKPnR leOOeK OIe 'OIPKU', anU so on, QnOPl We aNNoQnO foK all OIe UPffeKenO leOOeKs Pn OIe HlaPnOeXO samHle. OIen We look aO OIe NPHIeK OeXO We WanO Oo solVe anU We also NlassPfY POs sYmbols. We fPnU OIe mosO oNNQKKPnR sYmbol anU NIanRe PO Oo OIe foKm of OIe 'fPKsO' leOOeK of OIe HlaPnOeXO samHle, OIe neXO mosO Nommon sYmbol Ps NIanReU Oo OIe foKm of OIe 'seNonU' leOOeK, anU OIe folloWPnR mosO Nommon sYmbol Ps NIanReU Oo OIe foKm of OIe 'OIPKU' leOOeK, anU so on, QnOPl We aNNoQnO foK all sYmbols of OIe NKYHOoRKam We WanO Oo solVe."
string_v = string_u.replace("H","p")
print(string_v)

string_w = "one WaY Oo solVe an enNKYpOeU messaRe, Pf We knoW POs lanRQaRe, Ps Oo fPnU a UPffeKenO plaPnOeXO of OIe same lanRQaRe lonR enoQRI Oo fPll one sIeeO oK so, anU OIen We NoQnO OIe oNNQKKenNes of eaNI leOOeK. We Nall OIe mosO fKeJQenOlY oNNQKKPnR leOOeK OIe 'fPKsO', OIe neXO mosO oNNQKKPnR leOOeK OIe 'seNonU' OIe folloWPnR mosO oNNQKKPnR leOOeK OIe 'OIPKU', anU so on, QnOPl We aNNoQnO foK all OIe UPffeKenO leOOeKs Pn OIe plaPnOeXO sample. OIen We look aO OIe NPpIeK OeXO We WanO Oo solVe anU We also NlassPfY POs sYmbols. We fPnU OIe mosO oNNQKKPnR sYmbol anU NIanRe PO Oo OIe foKm of OIe 'fPKsO' leOOeK of OIe plaPnOeXO sample, OIe neXO mosO Nommon sYmbol Ps NIanReU Oo OIe foKm of OIe 'seNonU' leOOeK, anU OIe folloWPnR mosO Nommon sYmbol Ps NIanReU Oo OIe foKm of OIe 'OIPKU' leOOeK, anU so on, QnOPl We aNNoQnO foK all sYmbols of OIe NKYpOoRKam We WanO Oo solVe."
string_x = string_w.replace("I","h")
print(string_x)

string_y = "one WaY Oo solVe an enNKYpOeU messaRe, Pf We knoW POs lanRQaRe, Ps Oo fPnU a UPffeKenO plaPnOeXO of Ohe same lanRQaRe lonR enoQRh Oo fPll one sheeO oK so, anU Ohen We NoQnO Ohe oNNQKKenNes of eaNh leOOeK. We Nall Ohe mosO fKeJQenOlY oNNQKKPnR leOOeK Ohe 'fPKsO', Ohe neXO mosO oNNQKKPnR leOOeK Ohe 'seNonU' Ohe folloWPnR mosO oNNQKKPnR leOOeK Ohe 'OhPKU', anU so on, QnOPl We aNNoQnO foK all Ohe UPffeKenO leOOeKs Pn Ohe plaPnOeXO sample. Ohen We look aO Ohe NPpheK OeXO We WanO Oo solVe anU We also NlassPfY POs sYmbols. We fPnU Ohe mosO oNNQKKPnR sYmbol anU NhanRe PO Oo Ohe foKm of Ohe 'fPKsO' leOOeK of Ohe plaPnOeXO sample, Ohe neXO mosO Nommon sYmbol Ps NhanReU Oo Ohe foKm of Ohe 'seNonU' leOOeK, anU Ohe folloWPnR mosO Nommon sYmbol Ps NhanReU Oo Ohe foKm of Ohe 'OhPKU' leOOeK, anU so on, QnOPl We aNNoQnO foK all sYmbols of Ohe NKYpOoRKam We WanO Oo solVe."
string_z = string_y.replace("J","q")
print(string_z)


