import librosa
from sklearn import linear_model

#데이터가 있는 경로 지정
datapath = ''

y, sr = librosa.load(datapath)
mfcc = librosa.feature.mfcc(y=y, sr=sr)

#(20, number_of_frames)가 출력됨
#print(mfcc.shape)

logreg = linear_model.LogisticRegression()
logreg.fit(x_train, y_train)
y_test_estimated = logreg.predict(x_test)

print(y_test_estimated)
