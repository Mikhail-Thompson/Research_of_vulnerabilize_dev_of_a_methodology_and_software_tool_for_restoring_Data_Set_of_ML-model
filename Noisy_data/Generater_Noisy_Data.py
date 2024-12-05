import pandas as pd
import numpy as np
import random
import json
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

# Функция для генерации шумных данных
def generate_noisy_data():
    # Генерация числовых данных (например, значений температуры)
    data = np.random.randn(100) * 10 + 20  # нормальное распределение с шумом
    # Генерация строковых данных (например, категорий)
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    labels = [random.choice(categories) for _ in range(100)]
    
    # Добавляем шум в категориальные данные
    noisy_labels = []
    for label in labels:
        if random.random() < 0.1:  # 10% вероятность добавить ошибку
            noisy_labels.append(random.choice(categories))
        else:
            noisy_labels.append(label)
    
    # Создание DataFrame
    df = pd.DataFrame({
        'Value': data.tolist(),
        'Category': noisy_labels
    })
    
    # Сохраняем DataFrame в JSON файл
    df.to_json('noisy_data.json', orient='records', lines=True)
    return df

# Графический интерфейс для генерации данных
def generate_data_gui():
    root = Tk()
    root.title("Генерация данных с шумом")
    
    def on_generate():
        # Генерация и сохранение данных
        df = generate_noisy_data()
        messagebox.showinfo("Успех", "Данные сгенерированы и сохранены в 'noisy_data.json'!")
        
        # Визуализация
        df['Value'].plot(title="Шумные данные", figsize=(10,6))
        plt.show()

    generate_button = Button(root, text="Сгенерировать данные", command=on_generate)
    generate_button.pack(pady=20)
    
    root.mainloop()

# Запуск интерфейса
generate_data_gui()

#Комментарии по коду:
#generate_noisy_data() — Функция генерирует 100 случайных чисел с добавлением шума и 100 случайных категорий. 
#Каждая категория имеет 10% шанс быть замененной на другую категорию.