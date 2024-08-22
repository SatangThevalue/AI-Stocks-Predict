import yfinance as yf
import pandas as pd

all_ticker_list = [
    "EE.bk",
    "GFPT.bk",
    "LEE.bk",
    "MAX.bk",
    "NER.bk",
    "PPPM.bk",
    "STA.bk",
    "TEGH.bk",
    "TFM.bk",
    "TRUBB.bk",
    "TWPC.bk",
    "UPOIC.bk",
    "UVAN.bk",
    "VPO.bk",
    "AAI.bk",
    "APURE.bk",
    "ASIAN.bk",
    "BR.bk",
    "BRR.bk",
    "BTG.bk",
    "CBG.bk",
    "CFRESH.bk",
    "CH.bk",
    "CHOTI.bk",
    "CM.bk",
    "CPF.bk",
    "CPI.bk",
    "F&D.bk",
    "GLOCON.bk",
    "HTC.bk",
    "ICHI.bk",
    "JDF.bk",
    "KBS.bk",
    "KSL.bk",
    "KTIS.bk",
    "LST.bk",
    "M.bk",
    "MALEE.bk",
    "MINT.bk",
    "NRF.bk",
    "NSL.bk",
    "OISHI.bk",
    "OSP.bk",
    "PB.bk",
    "PLUS.bk",
    "PM.bk",
    "PRG.bk",
    "RBF.bk",
    "SAPPE.bk",
    "SAUCE.bk",
    "SFP.bk",
    "SNNP.bk",
    "SNP.bk",
    "SORKON.bk",
    "SSC.bk",
    "SSF.bk",
    "SST.bk",
    "SUN.bk",
    "TC.bk",
    "TFG.bk",
    "TFMAMA.bk",
    "TIPCO.bk",
    "TKN.bk",
    "TU.bk",
    "TVO.bk",
    "W.bk",
    "ZEN.bk",
    "AFC.bk",
    "BTNC.bk",
    "CPH.bk",
    "CPL.bk",
    "NC.bk",
    "PAF.bk",
    "PDJ.bk",
    "PG.bk",
    "SABINA.bk",
    "SAWANG.bk",
    "SUC.bk",
    "TNL.bk",
    "TR.bk",
    "TTI.bk",
    "TTT.bk",
    "UPF.bk",
    "WACOAL.bk",
    "WFX.bk",
    "AJA.bk",
    "DTCI.bk",
    "FANCY.bk",
    "FTI.bk",
    "KYE.bk",
    "L&E.bk",
    "MODERN.bk",
    "OGC.bk",
    "ROCK.bk",
    "SIAM.bk",
    "TCMC.bk",
    "TSR.bk",
    "APCO.bk",
    "BIZ.bk",
    "DDD.bk",
    "JCT.bk",
    "KISS.bk",
    "NV.bk",
    "OCC.bk",
    "S&J.bk",
    "STGT.bk",
    "STHAI.bk",
    "TNR.bk",
    "TOG.bk",
    "BAY.bk",
    "BBL.bk",
    "CIMBT.bk",
    "KBANK.bk",
    "KKP.bk",
    "KTB.bk",
    "LHFG.bk",
    "SCB.bk",
    "TCAP.bk",
    "TISCO.bk",
    "TTB.bk",
    "AEONTS.bk",
    "AMANAH.bk",
    "ASAP.bk",
    "ASK.bk",
    "ASP.bk",
    "BAM.bk",
    "BYD.bk",
    "CGH.bk",
    "CHAYO.bk",
    "ECL.bk",
    "FNS.bk",
    "FSS.bk",
    "GBX.bk",
    "GL.bk",
    "HENG.bk",
    "IFS.bk",
    "JMT.bk",
    "KCAR.bk",
    "KGI.bk",
    "KTC.bk",
    "MFC.bk",
    "MICRO.bk",
    "ML.bk",
    "MST.bk",
    "MTC.bk",
    "NCAP.bk",
    "PL.bk",
    "S11.bk",
    "SAK.bk",
    "SAWAD.bk",
    "SCAP.bk",
    "TH.bk",
    "THANI.bk",
    "TIDLOR.bk",
    "TK.bk",
    "TNITY.bk",
    "UOBKH.bk",
    "XPG.bk",
    "AYUD.bk",
    "BKI.bk",
    "BLA.bk",
    "BUI.bk",
    "CHARAN.bk",
    "INSURE.bk",
    "KWI.bk",
    "MTI.bk",
    "NKI.bk",
    "NSI.bk",
    "SMK.bk",
    "TGH.bk",
    "THRE.bk",
    "THREL.bk",
    "TIPH.bk",
    "TLI.bk",
    "TQM.bk",
    "TSI.bk",
    "TVI.bk",
    "3K-BAT.bk",
    "ACG.bk",
    "AH.bk",
    "CWT.bk",
    "EASON.bk",
    "GYT.bk",
    "HFT.bk",
    "IHL.bk",
    "INGRS.bk",
    "IRC.bk",
    "PCSGH.bk",
    "POLY.bk",
    "SAT.bk",
    "SPG.bk",
    "STANLY.bk",
    "TKT.bk",
    "TNPC.bk",
    "TRU.bk",
    "TSC.bk",
    "ALLA.bk",
    "ASEFA.bk",
    "CPT.bk",
    "CRANE.bk",
    "CTW.bk",
    "FMT.bk",
    "HTECH.bk",
    "KKC.bk",
    "PK.bk",
    "SNC.bk",
    "STARK.bk",
    "TCJ.bk",
    "TPCS.bk",
    "VARO.bk",
    "UTP.bk",
    "BCT.bk",
    "CMAN.bk",
    "GC.bk",
    "GGC.bk",
    "GIFT.bk",
    "IVL.bk",
    "NFC.bk",
    "PATO.bk",
    "PMTA.bk",
    "PTTGC.bk",
    "SUTHA.bk",
    "TCCC.bk",
    "TPA.bk",
    "UAC.bk",
    "UP.bk",
    "AJ.bk",
    "ALUCON.bk",
    "BGC.bk",
    "CSC.bk",
    "NEP.bk",
    "PTL.bk",
    "SCGP.bk",
    "SFLEX.bk",
    "SITHAI.bk",
    "SLP.bk",
    "SMPC.bk",
    "SPACK.bk",
    "TCOAT.bk",
    "TFI.bk",
    "THIP.bk",
    "TMD.bk",
    "TOPP.bk",
    "TPAC.bk",
    "TPBI.bk",
    "TPP.bk",
    "2S.bk",
    "AMC.bk",
    "BSBM.bk",
    "CEN.bk",
    "CITY.bk",
    "CSP.bk",
    "GJS.bk",
    "GSTEEL.bk",
    "INOX.bk",
    "LHK.bk",
    "MCS.bk",
    "MILL.bk",
    "PAP.bk",
    "PERM.bk",
    "SAM.bk",
    "SMIT.bk",
    "SSSC.bk",
    "TGPRO.bk",
    "THE.bk",
    "TMT.bk",
    "TSTH.bk",
    "TWP.bk",
    "TYCN.bk",
    "CCP.bk",
    "COTTO.bk",
    "DCC.bk",
    "DCON.bk",
    "DRT.bk",
    "EPG.bk",
    "GEL.bk",
    "PPP.bk",
    "Q-CON.bk",
    "SCC.bk",
    "SCCC.bk",
    "SCP.bk",
    "SKN.bk",
    "STECH.bk",
    "TASCO.bk",
    "TOA.bk",
    "TPIPL.bk",
    "UMI.bk",
    "VNG.bk",
    "WIIK.bk",
    "A.bk",
    "AMATA.bk",
    "AMATAV.bk",
    "ANAN.bk",
    "AP.bk",
    "APEX.bk",
    "AQ.bk",
    "ASW.bk",
    "AWC.bk",
    "BLAND.bk",
    "BRI.bk",
    "BROCK.bk",
    "CGD.bk",
    "CI.bk",
    "CMC.bk",
    "CPN.bk",
    "ESTAR.bk",
    "EVER.bk",
    "FPT.bk",
    "GLAND.bk",
    "J.bk",
    "JCK.bk",
    "KC.bk",
    "LALIN.bk",
    "LH.bk",
    "LPN.bk",
    "MBK.bk",
    "MJD.bk",
    "MK.bk",
    "NCH.bk",
    "NNCL.bk",
    "NOBLE.bk",
    "NUSA.bk",
    "NVD.bk",
    "ORI.bk",
    "PACE.bk",
    "PEACE.bk",
    "PF.bk",
    "PIN.bk",
    "PLAT.bk",
    "POLAR.bk",
    "PRECHA.bk",
    "PRIN.bk",
    "PSH.bk",
    "QH.bk",
    "RICHY.bk",
    "RML.bk",
    "ROJNA.bk",
    "S.bk",
    "SA.bk",
    "SAMCO.bk",
    "SC.bk",
    "SENA.bk",
    "SIRI.bk",
    "SPALI.bk",
    "U.bk",
    "UV.bk",
    "WHA.bk",
    "WIN.bk",
    "AIMCG.bk",
    "AIMIRT.bk",
    "ALLY.bk",
    "AMATAR.bk",
    "B-WORK.bk",
    "BAREIT.bk",
    "BKKCP.bk",
    "BOFFICE.bk",
    "CPNCG.bk",
    "CPNREIT.bk",
    "CPTGF.bk",
    "CTARAF.bk",
    "DREIT.bk",
    "ERWPF.bk",
    "FTREIT.bk",
    "FUTUREPF.bk",
    "GAHREIT.bk",
    "GROREIT.bk",
    "GVREIT.bk",
    "HPF.bk",
    "IMPACT.bk",
    "INETREIT.bk",
    "KPNPF.bk",
    "KTBSTMR.bk",
    "LHHOTEL.bk",
    "LHPF.bk",
    "LHSC.bk",
    "LPF.bk",
    "LUXF.bk",
    "M-II.bk",
    "M-PAT.bk",
    "M-STOR.bk",
    "MIPF.bk",
    "MIT.bk",
    "MJLF.bk",
    "MNIT.bk",
    "MNIT2.bk",
    "MNRF.bk",
    "POPF.bk",
    "PPF.bk",
    "PROSPECT.bk",
    "QHHR.bk",
    "QHOP.bk",
    "QHPF.bk",
    "SHREIT.bk",
    "SIRIP.bk",
    "SPRIME.bk",
    "SRIPANWA.bk",
    "SSPF.bk",
    "SSTRT.bk",
    "TIF1.bk",
    "TLHPF.bk",
    "TNPF.bk",
    "TPRIME.bk",
    "TTLPF.bk",
    "TU-PF.bk",
    "URBNPF.bk",
    "WHABT.bk",
    "WHAIR.bk",
    "WHART.bk",
    "APCS.bk",
    "BJCHI.bk",
    "BKD.bk",
    "CIVIL.bk",
    "CK.bk",
    "CNT.bk",
    "EMC.bk",
    "ITD.bk",
    "NWR.bk",
    "PLE.bk",
    "PREB.bk",
    "PYLON.bk",
    "RT.bk",
    "SEAFCO.bk",
    "SQ.bk",
    "SRICHA.bk",
    "STEC.bk",
    "STI.bk",
    "STPI.bk",
    "SYNTEC.bk",
    "TEAMG.bk",
    "TEKA.bk",
    "TPOLY.bk",
    "TRC.bk",
    "TRITN.bk",
    "TTCL.bk",
    "UNIQ.bk",
    "WGE.bk",
    "7UP.bk",
    "ABPIF.bk",
    "ACC.bk",
    "ACE.bk",
    "AGE.bk",
    "AI.bk",
    "AIE.bk",
    "AKR.bk",
    "BAFS.bk",
    "BANPU.bk",
    "BBGI.bk",
    "BCP.bk",
    "BCPG.bk",
    "BGRIM.bk",
    "BPP.bk",
    "BRRGIF.bk",
    "CKP.bk",
    "CV.bk",
    "DEMCO.bk",
    "EA.bk",
    "EASTW.bk",
    "EGATIF.bk",
    "EGCO.bk",
    "EP.bk",
    "ESSO.bk",
    "ETC.bk",
    "GPSC.bk",
    "GREEN.bk",
    "GULF.bk",
    "GUNKUL.bk",
    "IFEC.bk",
    "IRPC.bk",
    "JR.bk",
    "KBSPIF.bk",
    "LANNA.bk",
    "MDX.bk",
    "NOVA.bk",
    "OR.bk",
    "PCC.bk",
    "PRIME.bk",
    "PTG.bk",
    "PTT.bk",
    "PTTEP.bk",
    "QTC.bk",
    "RATCH.bk",
    "RPC.bk",
    "SCG.bk",
    "SCI.bk",
    "SCN.bk",
    "SGP.bk",
    "SKE.bk",
    "SOLAR.bk",
    "SPCG.bk",
    "SPRC.bk",
    "SSP.bk",
    "SUPER.bk",
    "SUPEREIF.bk",
    "SUSCO.bk",
    "TAE.bk",
    "TCC.bk",
    "TGE.bk",
    "TOP.bk",
    "TPIPP.bk",
    "TSE.bk",
    "TTW.bk",
    "UBE.bk",
    "WHAUP.bk",
    "WP.bk",
    "THL.bk",
    "B52.bk",
    "BEAUTY.bk",
    "BIG.bk",
    "BJC.bk",
    "COM7.bk",
    "CPALL.bk",
    "CPW.bk",
    "CRC.bk",
    "CSS.bk",
    "DOHOME.bk",
    "FN.bk",
    "FTE.bk",
    "GLOBAL.bk",
    "HMPRO.bk",
    "ICC.bk",
    "ILM.bk",
    "IT.bk",
    "KAMART.bk",
    "LOXLEY.bk",
    "MAKRO.bk",
    "MC.bk",
    "MEGA.bk",
    "MIDA.bk",
    "RS.bk",
    "RSP.bk",
    "SABUY.bk",
    "SCM.bk",
    "SINGER.bk",
    "SPC.bk",
    "SPI.bk",
    "SVT.bk",
    "AHC.bk",
    "BCH.bk",
    "BDMS.bk",
    "BH.bk",
    "CHG.bk",
    "CMR.bk",
    "EKH.bk",
    "KDH.bk",
    "LPH.bk",
    "M-CHAI.bk",
    "NEW.bk",
    "NTV.bk",
    "PR9.bk",
    "PRINC.bk",
    "RAM.bk",
    "RJH.bk",
    "RPH.bk",
    "SKR.bk",
    "SVH.bk",
    "THG.bk",
    "VIBHA.bk",
    "VIH.bk",
    "WPH.bk",
    "AMARIN.bk",
    "AQUA.bk",
    "AS.bk",
    "BEC.bk",
    "FE.bk",
    "GPI.bk",
    "GRAMMY.bk",
    "JKN.bk",
    "MACO.bk",
    "MAJOR.bk",
    "MATCH.bk",
    "MATI.bk",
    "MCOT.bk",
    "MONO.bk",
    "MPIC.bk",
    "NATION.bk",
    "ONEE.bk",
    "PLANB.bk",
    "POST.bk",
    "PRAKIT.bk",
    "PTECH.bk",
    "SE-ED.bk",
    "TKS.bk",
    "VGI.bk",
    "WAVE.bk",
    "WORK.bk",
    "BWG.bk",
    "GENCO.bk",
    "PRO.bk",
    "SISB.bk",
    "SO.bk",
    "ASIA.bk",
    "BEYOND.bk",
    "CENTEL.bk",
    "CSR.bk",
    "DUSIT.bk",
    "ERW.bk",
    "GRAND.bk",
    "LRH.bk",
    "MANRIN.bk",
    "OHTL.bk",
    "ROH.bk",
    "SHANG.bk",
    "SHR.bk",
    "VRANDA.bk",
    "AAV.bk",
    "AOT.bk",
    "ASIMAR.bk",
    "B.bk",
    "BA.bk",
    "BEM.bk",
    "BIOTEC.bk",
    "BTS.bk",
    "BTSGIF.bk",
    "DMT.bk",
    "III.bk",
    "JWD.bk",
    "KEX.bk",
    "KIAT.bk",
    "KWC.bk",
    "MENA.bk",
    "NOK.bk",
    "NYT.bk",
    "PORT.bk",
    "PRM.bk",
    "PSL.bk",
    "RCL.bk",
    "TFFIF.bk",
    "THAI.bk",
    "TSTE.bk",
    "TTA.bk",
    "WICE.bk",
    "CCET.bk",
    "DELTA.bk",
    "HANA.bk",
    "KCE.bk",
    "METCO.bk",
    "NEX.bk",
    "SMT.bk",
    "SVI.bk",
    "TEAM.bk",
    "ADVANC.bk",
    "AIT.bk",
    "ALT.bk",
    "AMR.bk",
    "BLISS.bk",
    "DIF.bk",
    "DTAC.bk",
    "FORTH.bk",
    "HUMAN.bk",
    "ILINK.bk",
    "INET.bk",
    "INSET.bk",
    "INTUCH.bk",
    "ITEL.bk",
    "JAS.bk",
    "JASIF.bk",
    "JMART.bk",
    "JTS.bk",
    "MFEC.bk",
    "MSC.bk",
    "PT.bk",
    "SAMART.bk",
    "SAMTEL.bk",
    "SDC.bk",
    "SIS.bk",
    "SKY.bk",
    "SVOA.bk",
    "SYMC.bk",
    "SYNEX.bk",
    "THCOM.bk",
    "TKC.bk",
    "TRUE.bk",
    "TWZ.bk",
]
interval = '1d'
start = '2009-8-01'
end = '2024-8-01'
for ticker in all_ticker_list:
  df = yf.download(ticker,interval=interval,start=start,end=end)
  df.to_csv(f'./data/tickers_data/' + ticker + '.csv')
  print('Load data ticker'+ ticker + ' OK!!!')