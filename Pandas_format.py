import pandas as pd
import xlwt
import tkinter as tk

def formatar_arquivo():
    input_value = entry1.get()
    output_value = entry2.get()
# Ler os dados da planilha .xlsx existente em um DataFrame, trata os elementos nulos como strings vazias
    dataframe = pd.read_excel(f'{input_value}.xlsx', header=None).fillna('')

    # Cria um novo arquivo .xls e adiciona uma planilha a ele
    new_file = f'/home/gabmats/Downloads/sinapi_08_2023/{output_value}.xls'
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet 1')

    # Escrever os dados do DataFrame na nova planilha
    for row_index, row in enumerate(dataframe.values):
        for col_index, cell_value in enumerate(row):
            worksheet.write(row_index, col_index, cell_value)

    # Salva o arquivo .xls
    workbook.save(new_file)
    print('Arquivo salvo com sucesso')



# Criar uma janela
janela = tk.Tk()
janela.title("Entrada de Dois Valores")

# Criar rótulos e campos de entrada para os dois valores
label1 = tk.Label(janela, text="Digite o primeiro valor:")
label1.pack()

entry1 = tk.Entry(janela)
entry1.pack()

label2 = tk.Label(janela, text="Digite o segundo valor:")
label2.pack()

entry2 = tk.Entry(janela)
entry2.pack()

# Criar um botão para confirmar a entrada dos valores
botao = tk.Button(janela, text="Confirmar", command=formatar_arquivo)
botao.pack()

# Iniciar a interface gráfica
janela.mainloop()