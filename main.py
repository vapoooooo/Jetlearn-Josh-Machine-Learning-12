import pandas as pd  

sentim = pd.read_csv('sentiments.txt', sep = ';', names = ['sentence','emotion'])
print(sentim.head())
print(sentim.info())

print(sentim['emotion'].value_counts())

#sentim.loc[sentim['emotion'] == 'joy', 'emotion'] = 1

#print(sentim['emotion'].value_counts())

sentim.replace({'joy': 1, 'love': 1, 'surprise': 1, 'sadness': 0, 'anger': 0, 'fear': 0}, inplace = True)
print(sentim['emotion'].value_counts())