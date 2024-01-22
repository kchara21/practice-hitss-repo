#este es un comentario

#Este es un cambio para el pull request

url="https://previexappdev.azurewebsites.net/Contrato/EditEmpresarial/395"
ID_Contrato = ""
i = len(url) - 1

while i >= 0 and url[i].isdigit():
    ID_Contrato = url[i] + ID_Contrato
    i -= 1

print (ID_Contrato)