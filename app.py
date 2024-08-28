import os
import xmltodict

# Extrair os datos dos variso dets diferentes
def products_extract(det_elements):
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

def filter_data(file_name, data, count):
   print(f'File {file_name} number {count} been changed!') 

   with open(f'nfs/{file_name}', 'rb') as xml:
        dic_nf = xmltodict.parse(xml)
       
        try:
            if 'Nfe'in dic_nf:
                nf = dic_nf['NFe']['infNFe']
            else:
                nf = dic_nf['nfeProc']['NFe']['infNFe']

            nf_json = {
                'numero': nf['@Id'],
                'emitente': nf['emit']['xNome'],
                'produtos': products_extract(nf['det'])
            }

            data.append(nf_json)
                    
        except Exception as e:
            print(f'Error {e}, in file {file_name}')
        

count = 1 
data = []
files_names = os.listdir('nfs')
# files_names = ['35240109227302000171550010000658321000101021-48577231000199-000000000002024-procnfe.xml']
# files_names2 = ['35240104827322000240550010000266001005100174-48577231000199-000000000001920-procnfe.xml']

for file in files_names:
    filter_data(file, data, count)
    count = count + 1

print(data)
