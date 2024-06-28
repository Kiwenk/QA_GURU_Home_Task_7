import requests

#моя попытка в скачивание файлов и работы с ними в дальнейшем, но я не смог их в конфтест добавить, так чтобы работало.
def script_download_file_by_click_pdf(folder_path = str):
    pdf_url = 'https://docs.pytest.org/_/downloads/en/stable/pdf/'
    content = requests.get(url=pdf_url, verify=False).content
    with open(f"{folder_path}\test_file_pdf.pdf",
              "wb") as file:
        file.write(content)
def script_download_file_by_click_xlsx(folder_path = str):
    xlsx_url = 'https://itsm365.com/documents_rus/web/Content/Resources/doc/import_ou_xlsx.xlsx'
    content = requests.get(url=xlsx_url, verify=False).content
    with open(f"{folder_path}\test_file_xlsx.xlsx",
              "wb") as file:
        file.write(content)
def script_download_file_by_click_csv(folder_path = str):
    csv_url = 'https://itsm365.com/documents_rus/web/Content/Resources/doc/import_ou_csv.csv'
    content = requests.get(url=csv_url, verify=False).content
    with open(f"{folder_path}\test_file_csv.csv",
          "wb") as file:
        file.write(content)