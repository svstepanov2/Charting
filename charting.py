import pandas as pd
values = ['robot', 'robot', 'robot', 'robot', 'robot', 'human', 'human', 'human', 'human', 'human']
one_hot = pd.DataFrame(index=values, columns=['robot', 'human'])
one_hot.replace({'robot': 1, 'human': 0}, inplace=True)
print(one_hot)