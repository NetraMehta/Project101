import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BIBd8EoyRxyWNi1gKEr1xk4KuBLYrco0JBpqvrGzcErNrU_LU3LphcVCpW653MabBrno3w8qm0hMeEW069MxSMx20z7tXotTgybIsDO_K4Ykds7ZX4xJCOGVwqcKdj1pg5uha29WlVE'
    transferData = TransferData(access_token)
    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter the full path to upload to dropbox: ')

    transferData.upload_file(file_from, file_to)
    print('File has been moved')

main()