import pandas as pd

# Basit bir veri seti oluşturuyoruz
data = {
    'Name': ['Ali', 'Ayşe', 'Mehmet', 'Fatma'],
    'Age': [25, 30, 22, 35],
    'Salary': [5000, 6000, 4500, 7000]
}

df = pd.DataFrame(data)

# Ortalama maaşı hesapla
average_salary = df['Salary'].mean()

print(f'Average Salary: {average_salary}')
