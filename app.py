import os
import xmltodict
import pandas as pd

# Extrair os dados dos variso dets diferentes
def extract_produtcts(det_elements):
    data = []

    if not isinstance(det_elements, list):
        det_elements = [det_elements]

    for det in det_elements:
        nf_product = {
            'nome':det['prod']['xProd'],
            'ncm':det['prod']['NCM'],
            'quantidade':det['prod']['qCom'],
            'unidade':det['prod']['uTrib']
        }  

        data.append(nf_product)

    return data

def xml_structure(dic_nf, file_name):
        nf  = {}
        try:
            if 'NFe' in dic_nf:
                nf = dic_nf['NFe']['infNFe']
                print('nfe')
            
            elif 'procEventoNFe' in  dic_nf:
                nf  = dic_nf['procEventoNFe']['evento']['infEvento']['detEvento']['descEvento']
                print('proceEvento')

            elif 'procInutNFe' in  dic_nf:
                print('Inutilizada 1')

            elif 'inutNFe' in dic_nf:
                print('Inutilazada 2')

            else :
                nf = dic_nf['nfeProc']['NFe']['infNFe']
                print('nfeProc')

        except Exception as e:
            print(f'Error {e}, in file {file_name}')
            reise

        return nf

        
def filter_data(file_name, path, data, count):
   print(f'Path {path} File {file_name} number {count} uploaded!') 

   with open(f'nfs2/estoque-xml/{path}/{file_name}', 'rb') as xml:
        dic_nf = xmltodict.parse(xml)
        nf = xml_structure(dic_nf, file_name) 
       
        # if(nf ):
        #     produtos = products_extract(nf['det'])

        # for produto in produtos:
        #     nf_json = {
        #         'numero': nf['@Id'],
        #         'emitente': nf['emit']['xNome'],
        #         'nome': produto['nome'],
        #         'ncm': produto['ncm'],
        #         'quantidade': produto['quantidade'],
        #         'unidade': produto['unidade']
        #     }

        #     data.append(nf_json)
                    
        
count = 1 
valores = []
paths = ['202401', '202402', '202403', '202404', '202405', '202406', '202407', '202408']

for path in paths:
    files_names = os.listdir(f'nfs2/estoque-xml/{path}')

    for file in files_names:
        filter_data(file, path, valores, count)
        count = count + 1



# df = pd.DataFrame(valores)
# df.columns = ['Numero NF', 'Emitente', 'Produto', 'NCM', 'Quantidade', 'Unidade']

print(df)
