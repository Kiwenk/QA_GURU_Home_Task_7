import os
import requests


def script_download_file_by_click_pdf(folder_path):
    pdf_url = 'https://docs.pytest.org/_/downloads/en/stable/pdf/'
    content = requests.get(url=pdf_url, verify=False).content
    with open(os.path.join(str(folder_path), "test_file_pdf.pdf"), "wb") as file:
        file.write(content)


def script_download_file_by_click_xlsx(folder_path):
    xlsx_url = 'https://itsm365.com/documents_rus/web/Content/Resources/doc/import_ou_xlsx.xlsx'
    content = requests.get(url=xlsx_url, verify=False).content
    with open(os.path.join(str(folder_path), "test_file_xlsx.xlsx"), "wb") as file:
        file.write(content)


def script_download_file_by_click_csv(folder_path):
    csv_url = 'https://itsm365.com/documents_rus/web/Content/Resources/doc/import_ou_csv.csv'
    content = requests.get(url=csv_url, verify=False).content
    with open(os.path.join(str(folder_path), "test_file_csv.csv"), "wb") as file:
        file.write(content)
