import pandas as pd

def one_hot_encode(df, column):
    """
    Функция преобразует столбец в one hot вид.

    Args:
        df (DataFrame): DataFrame для преобразования
        column (str): имя столбца, который нужно преобразовать

    Returns:
        DataFrame: DataFrame с преобразованным столбцом в one hot вид
    """

    # Создаем пустой DataFrame с индексами исходного столбца
    one_hot = pd.DataFrame(index=df[column].unique(), columns=df[column].unique())

    # Заполняем DataFrame нулями
    one_hot.fillna(0, inplace=True)

    # Подставляем значения из исходного DataFrame
    one_hot.iloc[df.index, df[column]] = 1

    # Возвращаем DataFrame
    return one_hot

# Генерируем случайный DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Преобразуем столбец в one hot вид
one_hot = one_hot_encode(data, 'whoAmI')

# Выводим результат
print(one_hot)
