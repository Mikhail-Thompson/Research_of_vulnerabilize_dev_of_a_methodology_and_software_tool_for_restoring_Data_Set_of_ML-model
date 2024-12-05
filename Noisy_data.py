import pandas as pd
import numpy as np
import json
from tkinter import *
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

# Функция для загрузки JSON файла
def load_json_data(file_path):
    df = pd.read_json(file_path, orient='records', lines=True)
    return df

# Применение фильтрации с использованием скользящего окна
def moving_average_filter(df, window_size=5):
    df['Smoothed_Value'] = df['Value'].rolling(window=window_size, min_periods=1).mean()
    return df

# Сохранение отфильтрованных данных в JSON
def save_filtered_data(df, output_file):
    df.to_json(output_file, orient='records', lines=True)

# Графический интерфейс для загрузки файла, фильтрации и сохранения результатов
def filter_data_gui():
    root = Tk()
    root.title("Загрузка и фильтрация данных")
    
    def load_and_filter():
        # Открытие диалога для выбора файла
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        
        if file_path:
            # Загрузка данных
            df = load_json_data(file_path)
            
            # Применение скользящего среднего
            window_size = 5  # Размер окна фильтра
            filtered_df = moving_average_filter(df, window_size)
            
            # Отображение оригинальных и сглаженных данных
            plt.figure(figsize=(10, 6))
            plt.plot(df['Value'], label="Оригинальные данные", color='blue')
            plt.plot(filtered_df['Smoothed_Value'], label=f"Отфильтрованные данные (окно={window_size})", color='red')
            plt.legend()
            plt.title("Сравнение данных с фильтрацией")
            plt.show()
            
            # Сохранение отфильтрованных данных
            output_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
            if output_file:
                save_filtered_data(filtered_df, output_file)
                messagebox.showinfo("Успех", f"Отфильтрованные данные сохранены в {output_file}!")

    # Кнопка загрузки и фильтрации
    filter_button = Button(root, text="Загрузить и применить фильтрацию", command=load_and_filter)
    filter_button.pack(pady=20)
    
    root.mainloop()

# Запуск интерфейса
filter_data_gui()

#Комментарии по коду:
#load_json_data() — Функция для загрузки данных из JSON файла.
#moving_average_filter() — Функция для применения фильтрации методом скользящего окна с размером окна по умолчанию 5. 
# Фильтрация выполняется с использованием rolling(window=5).mean() в Pandas.
#save_filtered_data() — Сохраняет отфильтрованные данные в новый JSON файл.