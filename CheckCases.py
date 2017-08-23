
import requests
import json
r = requests.get("https://api.gdc.cancer.gov/v0/legacy/cases?facets=project.project_id&fields=project.project_id,&from=1&size=1&sort=case_id:asc");

data = json.loads(r.text)
current_data = data['data']['aggregations']['project.project_id']['buckets']
reference_data = [{'key': 'TARGET-ALL-P2', 'doc_count': 1553}, {'key': 'TARGET-NBL', 'doc_count': 1127}, {'key': 'TCGA-BRCA', 'doc_count': 1098}, {'key': 'TARGET-AML', 'doc_count': 988}, {'key': 'TARGET-WT', 'doc_count': 652}, {'key': 'TCGA-GBM', 'doc_count': 617}, {'key': 'TCGA-OV', 'doc_count': 608}, {'key': 'TCGA-LUAD', 'doc_count': 585}, {'key': 'TCGA-UCEC', 'doc_count': 560}, {'key': 'TCGA-KIRC', 'doc_count': 537}, {'key': 'TCGA-HNSC', 'doc_count': 528}, {'key': 'TCGA-LGG', 'doc_count': 516}, {'key': 'TCGA-THCA', 'doc_count': 507}, {'key': 'TCGA-LUSC', 'doc_count': 504}, {'key': 'TCGA-PRAD', 'doc_count': 500}, {'key': 'TCGA-SKCM', 'doc_count': 470}, {'key': 'TCGA-COAD', 'doc_count': 461}, {'key': 'TCGA-STAD', 'doc_count': 443}, {'key': 'TCGA-BLCA', 'doc_count': 412}, {'key': 'TARGET-OS', 'doc_count': 381}, {'key': 'TCGA-LIHC', 'doc_count': 377}, {'key': 'TCGA-CESC', 'doc_count': 307}, {'key': 'TCGA-KIRP', 'doc_count': 291}, {'key': 'TCGA-SARC', 'doc_count': 261}, {'key': 'TARGET-ALL-P1', 'doc_count': 214}, {'key': 'TCGA-LAML', 'doc_count': 200}, {'key': 'CCLE-LUSC', 'doc_count': 186}, {'key': 'TCGA-ESCA', 'doc_count': 185}, {'key': 'TCGA-PAAD', 'doc_count': 185}, {'key': 'TCGA-PCPG', 'doc_count': 179}, {'key': 'TCGA-READ', 'doc_count': 172}, {'key': 'TCGA-TGCT', 'doc_count': 150}, {'key': 'TCGA-THYM', 'doc_count': 124}, {'key': 'TCGA-KICH', 'doc_count': 113}, {'key': 'TCGA-ACC', 'doc_count': 92}, {'key': 'TCGA-MESO', 'doc_count': 87}, {'key': 'CCLE-LCLL', 'doc_count': 81}, {'key': 'TCGA-UVM', 'doc_count': 80}, {'key': 'TARGET-RT', 'doc_count': 75}, {'key': 'CCLE-LGG', 'doc_count': 65}, {'key': 'CCLE-BRCA', 'doc_count': 63}, {'key': 'CCLE-DLBC', 'doc_count': 60}, {'key': 'CCLE-COAD', 'doc_count': 59}, {'key': 'TCGA-DLBC', 'doc_count': 58}, {'key': 'TCGA-UCS', 'doc_count': 57}, {'key': 'CCLE-SKCM', 'doc_count': 52}, {'key': 'TCGA-CHOL', 'doc_count': 51}, {'key': 'CCLE-OV', 'doc_count': 46}, {'key': 'CCLE-PAAD', 'doc_count': 41}, {'key': 'CCLE-SARC', 'doc_count': 40}, {'key': 'CCLE-STAD', 'doc_count': 39}, {'key': 'CCLE-HNSC', 'doc_count': 34}, {'key': 'CCLE-LIHC', 'doc_count': 33}, {'key': 'CCLE-BLCA', 'doc_count': 26}, {'key': 'CCLE-ESCA', 'doc_count': 26}, {'key': 'CCLE-MM', 'doc_count': 26}, {'key': 'CCLE-KIRC', 'doc_count': 25}, {'key': 'CCLE-CESC', 'doc_count': 24}, {'key': 'TARGET-CCSK', 'doc_count': 13}, {'key': 'CCLE-THCA', 'doc_count': 12}, {'key': 'CCLE-PRAD', 'doc_count': 7}, {'key': 'CCLE-UCEC', 'doc_count': 4}, {'key': 'CCLE-MESO', 'doc_count': 1}]

print('Cases per project from API')
for x in current_data:
    print(x['key'],':',x['doc_count'])

if current_data==reference_data:
    print('The number of cases per project is correct')
else:
    print('The number of cases per project is incorrect')

