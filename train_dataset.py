import zipfile
import os
import pandas as pd

# Definir la ruta del archivo zip y el directorio de extracción
zip_file_path = 'data.zip'
extract_folder = 'data'

# Extraer el archivo zip
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# Función para leer los archivos de texto y obtener los datos
def read_files(folder):
    data = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    text = f.read()
                    sentiment = os.path.basename(root)
                    data.append((text, sentiment))
    return data

# Leer los datos de train y test
train_data = read_files(os.path.join(extract_folder, 'train'))
test_data = read_files(os.path.join(extract_folder, 'test'))

# Convertir los datos a DataFrame de pandas
train_df = pd.DataFrame(train_data, columns=['phrase', 'sentiment'])
test_df = pd.DataFrame(test_data, columns=['phrase', 'sentiment'])

# Escribir los DataFrames a archivos CSV
train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)
#print("Archivos CSV generados exitosamente.")
