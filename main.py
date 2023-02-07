from nfelib.v4_00 import leiauteNFe_sub as parser
import pandas as pd
import os
import time

def runNFe(Arquivo):
    nota = parser.parse(Arquivo, silence=True)
    Arquivo = Arquivo.replace("nfe/","")

    ########################################################################################################################################################################################################
    dict_ide = {"cUF": None,"cNF": None,"natOp": None,"mod": None,"serie": None,"nNF": None,"dhEmi": None,"tpNF": None,"idDest": None,"cMunFG": None,"tpImp": None,"tpEmis": None,"cDV": None,"tpAmb": None,"finNFe": None,"indFinal": None,"indPres": None,"procEmi": None,"verProc": None, "Arquivo": None
    }

    dict_ide['cUF']=nota.infNFe.ide.cUF
    dict_ide['cNF']=nota.infNFe.ide.cNF
    dict_ide['natOp']=nota.infNFe.ide.natOp
    dict_ide['mod']=nota.infNFe.ide.mod
    dict_ide['serie']=nota.infNFe.ide.serie
    dict_ide['nNF']=nota.infNFe.ide.nNF
    dict_ide['dhEmi']=nota.infNFe.ide.dhEmi
    dict_ide['tpNF']=nota.infNFe.ide.tpNF
    dict_ide['idDest']=nota.infNFe.ide.idDest
    dict_ide['cMunFG']=nota.infNFe.ide.cMunFG
    dict_ide['tpImp']=nota.infNFe.ide.tpImp
    dict_ide['tpEmis']=nota.infNFe.ide.tpEmis
    dict_ide['cDV']=nota.infNFe.ide.cDV
    dict_ide['tpAmb']=nota.infNFe.ide.tpAmb
    dict_ide['finNFe']=nota.infNFe.ide.finNFe
    dict_ide['indFinal']=nota.infNFe.ide.indFinal
    dict_ide['indPres']=nota.infNFe.ide.indPres
    dict_ide['procEmi']=nota.infNFe.ide.procEmi
    dict_ide['verProc']=nota.infNFe.ide.verProc
    dict_ide['Arquivo']=Arquivo

    df_ide = pd.DataFrame(dict_ide, index=[0])

    ########################################################################################################################################################################################################
    dict_emit = {"CNPJ": None,"xNome": None,"xFant": None,"xLgr": None,"nro": None,"xCpl": None,"xBairro": None,"cMun": None,"xMun": None,"UF": None,"CEP": None,"cPais": None,"xPais": None,"fone": None,"IE": None,"CRT": None, "Arquivo": None}

    dict_emit['CNPJ']=nota.infNFe.emit.CNPJ
    dict_emit['xNome']=nota.infNFe.emit.xNome
    dict_emit['xFant']=nota.infNFe.emit.xFant
    dict_emit['xLgr']=nota.infNFe.emit.enderEmit.xLgr
    dict_emit['nro']=nota.infNFe.emit.enderEmit.nro
    dict_emit['xCpl']=nota.infNFe.emit.enderEmit.xCpl
    dict_emit['xBairro']=nota.infNFe.emit.enderEmit.xBairro
    dict_emit['cMun']=nota.infNFe.emit.enderEmit.cMun
    dict_emit['xMun']=nota.infNFe.emit.enderEmit.xMun
    dict_emit['UF']=nota.infNFe.emit.enderEmit.UF
    dict_emit['CEP']=nota.infNFe.emit.enderEmit.CEP
    dict_emit['cPais']=nota.infNFe.emit.enderEmit.cPais
    dict_emit['xPais']=nota.infNFe.emit.enderEmit.xPais
    dict_emit['fone']=nota.infNFe.emit.enderEmit.fone
    dict_emit['IE']=nota.infNFe.emit.IE
    dict_emit['CRT']=nota.infNFe.emit.CRT
    dict_emit['Arquivo']=Arquivo

    df_emit = pd.DataFrame(dict_emit, index=[0])

    ########################################################################################################################################################################################################
    dict_infNFe = {"chNFe": None, 'Arquivo': None}
    dict_infNFe['chNFe']=str(nota.infNFe.Id).replace("NFe", "")
    dict_infNFe['Arquivo']=Arquivo

    df_infNFe = pd.DataFrame(dict_infNFe, index=[0])

    ########################################################################################################################################################################################################
    list_dict_det = []
    for i in nota.infNFe.det:
        dict_det = {"cProd": None,"cEAN": None,"xProd": None,"NCM": None,"CEST": None,"EXTIPI": None,"CFOP": None,"uCom": None,"qCom": None,"vUnCom": None,"vProd": None,"cEANTrib": None,"uTrib": None,"qTrib": None,"vUnTrib": None,"indTot": None,"xPed": None,"nItemPed": None,"nFCI": None, "nItem": None, "cEnq": None, "IPINT": None, "det_icms_orig": None,"det_icms_CST": None,"det_icms_modBC": None,"det_icms_vBC": None,"det_icms_pICMS": None,"det_icms_vICMS": None,"det_icms_modBCST": None,"det_icms_pMVAST": None,"det_icms_vBCST": None,"det_icms_pICMSST": None,"det_icms_vICMSST": None,"det_icms_identity": None, "PISNT": None, "COFINSNT": None, "PISAliq_CST": None, "PISAliq_vBC": None, "PISAliq_pPIS": None, "PISAliq_vPIS": None, "COFINSAliq": None, "COFINSAliq_CST": None, "COFINSAliq_vBC": None, "COFINSAliq_pCOFINS": None, "COFINSAliq_vCOFINS": None, "Arquivo": None}  

        dict_det['Arquivo']=Arquivo
        dict_det['cProd']=i.prod.cProd
        dict_det['cEAN']=i.prod.cEAN
        dict_det['xProd']=i.prod.xProd
        dict_det['NCM']=i.prod.NCM
        dict_det['EXTIPI']=i.prod.EXTIPI
        dict_det['CFOP']=i.prod.CFOP
        dict_det['uCom']=i.prod.uCom
        dict_det['qCom']=i.prod.qCom
        dict_det['vUnCom']=i.prod.vUnCom
        dict_det['vProd']=i.prod.vProd
        dict_det['cEANTrib']=i.prod.cEANTrib
        dict_det['uTrib']=i.prod.uTrib
        dict_det['qTrib']=i.prod.qTrib
        dict_det['vUnTrib']=i.prod.vUnTrib
        dict_det['indTot']=i.prod.indTot
        dict_det['xPed']=i.prod.xPed    
        dict_det['nItemPed']=i.prod.nItemPed 
        dict_det['nFCI']=i.prod.nFCI 
        dict_det['cEnq']=i.imposto.IPI.cEnq
        dict_det['IPINT']=i.imposto.IPI.IPINT.CST
        dict_det['nItem']=i.nItem
        try:
            dict_det['PISNT']=i.imposto.PIS.PISNT.CST
        except:
            None
        try:
            dict_det['COFINSNT']=i.imposto.COFINS.COFINSNT.CST
        except:
            None
        try:
            dict_det['PISAliq_CST']=i.imposto.PIS.PISAliq.CST
        except:
            None
        try:
            dict_det['PISAliq_vBC']=i.imposto.COFINS.PISAliq.vBC
        except:
            None  
        try:
            dict_det['PISAliq_pPIS']=i.imposto.PIS.PISAliq.pPIS
        except:
            None
        try:
            dict_det['PISAliq_vPIS']=i.imposto.COFINS.PISAliq.vPIS
        except:
            None   

        try:
            dict_det['COFINSAliq_CST']=i.imposto.PIS.COFINSAliq.CST
        except:
            None
        try:
            dict_det['COFINSAliq_vBC']=i.imposto.COFINS.COFINSAliq.vBC
        except:
            None  
        try:
            dict_det['COFINSAliq_pCOFINS']=i.imposto.PIS.COFINSAliq.pCOFINS
        except:
            None
        try:
            dict_det['COFINSAliq_vCOFINS']=i.imposto.COFINS.COFINSAliq.vCOFINS
        except:
            None                        

        #loop pelos ICMS
        impostos = {
            "ICMS10": i.imposto.ICMS.ICMS10
            ,"ICMS20": i.imposto.ICMS.ICMS20
            ,"ICMS30": i.imposto.ICMS.ICMS30
            ,"ICMS40": i.imposto.ICMS.ICMS40
            ,"ICMS51": i.imposto.ICMS.ICMS51
            ,"ICMS60": i.imposto.ICMS.ICMS60
            ,"ICMS70": i.imposto.ICMS.ICMS70
            ,"ICMS90": i.imposto.ICMS.ICMS90
            ,"ICMSPart": i.imposto.ICMS.ICMSPart
            ,"ICMSST": i.imposto.ICMS.ICMSST
            ,"ICMSSN101": i.imposto.ICMS.ICMSSN101
        }

        for imposto in impostos:
            try:
                dict_det['det_icms_orig']=impostos[imposto].orig
                dict_det['det_icms_CST']=impostos[imposto].CST 
                dict_det['det_icms_modBC']=impostos[imposto].modBC 
                dict_det['det_icms_vBC']=impostos[imposto].vBC 
                dict_det['det_icms_pICMS']=impostos[imposto].pICMS 
                dict_det['det_icms_vICMS']=impostos[imposto].vICMS 
                dict_det['det_icms_modBCST']=impostos[imposto].modBCST 
                dict_det['det_icms_pMVAST']=impostos[imposto].pMVAST 
                dict_det['det_icms_vBCST']=impostos[imposto].vBCST 
                dict_det['det_icms_pICMSST']=impostos[imposto].pICMSST 
                dict_det['det_icms_vICMSST']=impostos[imposto].vICMSST 
                dict_det['det_icms_identity']=imposto 
                break
            except:
                None     


        list_dict_det.append(dict_det)


    if len(list_dict_det) > 0:
        df_det = pd.DataFrame(list_dict_det)
    else:
        df_det = pd.DataFrame(list_dict_det, index=[0])

    ########################################################################################################################################################################################################
    df_ = df_ide.merge(df_emit, how="left", on="Arquivo")
    df_ = df_.merge(df_infNFe, how="left", on="Arquivo" )
    df_ = df_.merge(df_det, how="left", on="Arquivo")

    return df_


if __name__ == '__main__':
    start = time.time()

    folder_path = 'nfe'
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(folder_path, filename)
            df = runNFe(file_path)
            df.to_csv(file_path.replace("xml", "csv").replace("nfe", "convert"), sep=";", encoding="utf8", index=False)

    tempoExec = time.time() - start
    print("Tempo de execução: {} segundos".format(tempoExec))      


              

    






