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

string_ab = "one WaY Oo solVe an enNKYpOeU messaRe, Pf We knoW POs lanRQaRe, Ps Oo fPnU a UPffeKenO plaPnOeXO of Ohe same lanRQaRe lonR enoQRh Oo fPll one sheeO oK so, anU Ohen We NoQnO Ohe oNNQKKenNes of eaNh leOOeK. We Nall Ohe mosO fKeqQenOlY oNNQKKPnR leOOeK Ohe 'fPKsO', Ohe neXO mosO oNNQKKPnR leOOeK Ohe 'seNonU' Ohe folloWPnR mosO oNNQKKPnR leOOeK Ohe 'OhPKU', anU so on, QnOPl We aNNoQnO foK all Ohe UPffeKenO leOOeKs Pn Ohe plaPnOeXO sample. Ohen We look aO Ohe NPpheK OeXO We WanO Oo solVe anU We also NlassPfY POs sYmbols. We fPnU Ohe mosO oNNQKKPnR sYmbol anU NhanRe PO Oo Ohe foKm of Ohe 'fPKsO' leOOeK of Ohe plaPnOeXO sample, Ohe neXO mosO Nommon sYmbol Ps NhanReU Oo Ohe foKm of Ohe 'seNonU' leOOeK, anU Ohe folloWPnR mosO Nommon sYmbol Ps NhanReU Oo Ohe foKm of Ohe 'OhPKU' leOOeK, anU so on, QnOPl We aNNoQnO foK all sYmbols of Ohe NKYpOoRKam We WanO Oo solVe."
string_cd = string_ab.replace("K","r")
print(string_cd)

string_ef = "one WaY Oo solVe an enNrYpOeU messaRe, Pf We knoW POs lanRQaRe, Ps Oo fPnU a UPfferenO plaPnOeXO of Ohe same lanRQaRe lonR enoQRh Oo fPll one sheeO or so, anU Ohen We NoQnO Ohe oNNQrrenNes of eaNh leOOer. We Nall Ohe mosO freqQenOlY oNNQrrPnR leOOer Ohe 'fPrsO', Ohe neXO mosO oNNQrrPnR leOOer Ohe 'seNonU' Ohe folloWPnR mosO oNNQrrPnR leOOer Ohe 'OhPrU', anU so on, QnOPl We aNNoQnO for all Ohe UPfferenO leOOers Pn Ohe plaPnOeXO sample. Ohen We look aO Ohe NPpher OeXO We WanO Oo solVe anU We also NlassPfY POs sYmbols. We fPnU Ohe mosO oNNQrrPnR sYmbol anU NhanRe PO Oo Ohe form of Ohe 'fPrsO' leOOer of Ohe plaPnOeXO sample, Ohe neXO mosO Nommon sYmbol Ps NhanReU Oo Ohe form of Ohe 'seNonU' leOOer, anU Ohe folloWPnR mosO Nommon sYmbol Ps NhanReU Oo Ohe form of Ohe 'OhPrU' leOOer, anU so on, QnOPl We aNNoQnO for all sYmbols of Ohe NrYpOoRram We WanO Oo solVe."
string_ba = string_ef.replace("L","s")
print(string_ba)

string_ma = "one WaY Oo solVe an enNrYpOeU messaRe, Pf We knoW POs lanRQaRe, Ps Oo fPnU a UPfferenO plaPnOeXO of Ohe same lanRQaRe lonR enoQRh Oo fPll one sheeO or so, anU Ohen We NoQnO Ohe oNNQrrenNes of eaNh leOOer. We Nall Ohe mosO freqQenOlY oNNQrrPnR leOOer Ohe 'fPrsO', Ohe neXO mosO oNNQrrPnR leOOer Ohe 'seNonU' Ohe folloWPnR mosO oNNQrrPnR leOOer Ohe 'OhPrU', anU so on, QnOPl We aNNoQnO for all Ohe UPfferenO leOOers Pn Ohe plaPnOeXO sample. Ohen We look aO Ohe NPpher OeXO We WanO Oo solVe anU We also NlassPfY POs sYmbols. We fPnU Ohe mosO oNNQrrPnR sYmbol anU NhanRe PO Oo Ohe form of Ohe 'fPrsO' leOOer of Ohe plaPnOeXO sample, Ohe neXO mosO Nommon sYmbol Ps NhanReU Oo Ohe form of Ohe 'seNonU' leOOer, anU Ohe folloWPnR mosO Nommon sYmbol Ps NhanReU Oo Ohe form of Ohe 'OhPrU' leOOer, anU so on, QnOPl We aNNoQnO for all sYmbols of Ohe NrYpOoRram We WanO Oo solVe."
string_aa = string_ma.replace("N","c")
print(string_aa)

string_bb = "one WaY Oo solVe an encrYpOeU messaRe, Pf We knoW POs lanRQaRe, Ps Oo fPnU a UPfferenO plaPnOeXO of Ohe same lanRQaRe lonR enoQRh Oo fPll one sheeO or so, anU Ohen We coQnO Ohe occQrrences of each leOOer. We call Ohe mosO freqQenOlY occQrrPnR leOOer Ohe 'fPrsO', Ohe neXO mosO occQrrPnR leOOer Ohe 'seconU' Ohe folloWPnR mosO occQrrPnR leOOer Ohe 'OhPrU', anU so on, QnOPl We accoQnO for all Ohe UPfferenO leOOers Pn Ohe plaPnOeXO sample. Ohen We look aO Ohe cPpher OeXO We WanO Oo solVe anU We also classPfY POs sYmbols. We fPnU Ohe mosO occQrrPnR sYmbol anU chanRe PO Oo Ohe form of Ohe 'fPrsO' leOOer of Ohe plaPnOeXO sample, Ohe neXO mosO common sYmbol Ps chanReU Oo Ohe form of Ohe 'seconU' leOOer, anU Ohe folloWPnR mosO common sYmbol Ps chanReU Oo Ohe form of Ohe 'OhPrU' leOOer, anU so on, QnOPl We accoQnO for all sYmbols of Ohe crYpOoRram We WanO Oo solVe."
string_cc = string_bb.replace("O","t")
print(string_cc)

string_ol = "one WaY to solVe an encrYpteU messaRe, Pf We knoW Pts lanRQaRe, Ps to fPnU a UPfferent plaPnteXt of the same lanRQaRe lonR enoQRh to fPll one sheet or so, anU then We coQnt the occQrrences of each letter. We call the most freqQentlY occQrrPnR letter the 'fPrst', the neXt most occQrrPnR letter the 'seconU' the folloWPnR most occQrrPnR letter the 'thPrU', anU so on, QntPl We accoQnt for all the UPfferent letters Pn the plaPnteXt sample. then We look at the cPpher teXt We Want to solVe anU We also classPfY Pts sYmbols. We fPnU the most occQrrPnR sYmbol anU chanRe Pt to the form of the 'fPrst' letter of the plaPnteXt sample, the neXt most common sYmbol Ps chanReU to the form of the 'seconU' letter, anU the folloWPnR most common sYmbol Ps chanReU to the form of the 'thPrU' letter, anU so on, QntPl We accoQnt for all sYmbols of the crYptoRram We Want to solVe."
string_dd = string_ol.replace("P","i")
print(string_dd)

string_go = "one WaY to solVe an encrYpteU messaRe, if We knoW its lanRQaRe, is to finU a Uifferent plainteXt of the same lanRQaRe lonR enoQRh to fill one sheet or so, anU then We coQnt the occQrrences of each letter. We call the most freqQentlY occQrrinR letter the 'first', the neXt most occQrrinR letter the 'seconU' the folloWinR most occQrrinR letter the 'thirU', anU so on, Qntil We accoQnt for all the Uifferent letters in the plainteXt sample. then We look at the cipher teXt We Want to solVe anU We also classifY its sYmbols. We finU the most occQrrinR sYmbol anU chanRe it to the form of the 'first' letter of the plainteXt sample, the neXt most common sYmbol is chanReU to the form of the 'seconU' letter, anU the folloWinR most common sYmbol is chanReU to the form of the 'thirU' letter, anU so on, Qntil We accoQnt for all sYmbols of the crYptoRram We Want to solVe."
string_fn = string_go.replace("Q","u")
print(string_fn)

string_se = "one WaY to solVe an encrYpteU messaRe, if We knoW its lanRuaRe, is to finU a Uifferent plainteXt of the same lanRuaRe lonR enouRh to fill one sheet or so, anU then We count the occurrences of each letter. We call the most frequentlY occurrinR letter the 'first', the neXt most occurrinR letter the 'seconU' the folloWinR most occurrinR letter the 'thirU', anU so on, until We account for all the Uifferent letters in the plainteXt sample. then We look at the cipher teXt We Want to solVe anU We also classifY its sYmbols. We finU the most occurrinR sYmbol anU chanRe it to the form of the 'first' letter of the plainteXt sample, the neXt most common sYmbol is chanReU to the form of the 'seconU' letter, anU the folloWinR most common sYmbol is chanReU to the form of the 'thirU' letter, anU so on, until We account for all sYmbols of the crYptoRram We Want to solVe."
string_ot = string_se.replace("R","g")
print(string_ot)

string_ls = "one WaY to solVe an encrYpteU message, if We knoW its language, is to finU a Uifferent plainteXt of the same language long enough to fill one sheet or so, anU then We count the occurrences of each letter. We call the most frequentlY occurring letter the 'first', the neXt most occurring letter the 'seconU' the folloWing most occurring letter the 'thirU', anU so on, until We account for all the Uifferent letters in the plainteXt sample. then We look at the cipher teXt We Want to solVe anU We also classifY its sYmbols. We finU the most occurring sYmbol anU change it to the form of the 'first' letter of the plainteXt sample, the neXt most common sYmbol is changeU to the form of the 'seconU' letter, anU the folloWing most common sYmbol is changeU to the form of the 'thirU' letter, anU so on, until We account for all sYmbols of the crYptogram We Want to solVe."
string_dl = string_ls.replace("U","d")
print(string_dl)

string_ma = "one WaY to solVe an encrYpted message, if We knoW its language, is to find a different plainteXt of the same language long enough to fill one sheet or so, and then We count the occurrences of each letter. We call the most frequentlY occurring letter the 'first', the neXt most occurring letter the 'second' the folloWing most occurring letter the 'third', and so on, until We account for all the different letters in the plainteXt sample. then We look at the cipher teXt We Want to solVe and We also classifY its sYmbols. We find the most occurring sYmbol and change it to the form of the 'first' letter of the plainteXt sample, the neXt most common sYmbol is changed to the form of the 'second' letter, and the folloWing most common sYmbol is changed to the form of the 'third' letter, and so on, until We account for all sYmbols of the crYptogram We Want to solVe."
string_zy = string_ma.replace("V","v")
print(string_zy)

string_tu = "one WaY to solve an encrYpted message, if We knoW its language, is to find a different plainteXt of the same language long enough to fill one sheet or so, and then We count the occurrences of each letter. We call the most frequentlY occurring letter the 'first', the neXt most occurring letter the 'second' the folloWing most occurring letter the 'third', and so on, until We account for all the different letters in the plainteXt sample. then We look at the cipher teXt We Want to solve and We also classifY its sYmbols. We find the most occurring sYmbol and change it to the form of the 'first' letter of the plainteXt sample, the neXt most common sYmbol is changed to the form of the 'second' letter, and the folloWing most common sYmbol is changed to the form of the 'third' letter, and so on, until We account for all sYmbols of the crYptogram We Want to solve."
string_yz = string_tu.replace("W","w")
print(string_yz)

string_po = "one waY to solve an encrYpted message, if we know its language, is to find a different plainteXt of the same language long enough to fill one sheet or so, and then we count the occurrences of each letter. we call the most frequentlY occurring letter the 'first', the neXt most occurring letter the 'second' the following most occurring letter the 'third', and so on, until we account for all the different letters in the plainteXt sample. then we look at the cipher teXt we want to solve and we also classifY its sYmbols. we find the most occurring sYmbol and change it to the form of the 'first' letter of the plainteXt sample, the neXt most common sYmbol is changed to the form of the 'second' letter, and the following most common sYmbol is changed to the form of the 'third' letter, and so on, until we account for all sYmbols of the crYptogram we want to solve."
string_es = string_po.replace("X","x")
print(string_es)

string_cu = "one waY to solve an encrYpted message, if we know its language, is to find a different plaintext of the same language long enough to fill one sheet or so, and then we count the occurrences of each letter. we call the most frequentlY occurring letter the 'first', the next most occurring letter the 'second' the following most occurring letter the 'third', and so on, until we account for all the different letters in the plaintext sample. then we look at the cipher text we want to solve and we also classifY its sYmbols. we find the most occurring sYmbol and change it to the form of the 'first' letter of the plaintext sample, the next most common sYmbol is changed to the form of the 'second' letter, and the following most common sYmbol is changed to the form of the 'third' letter, and so on, until we account for all sYmbols of the crYptogram we want to solve."
string_an = string_cu.replace("Y","y")
print(string_an)

