import librosa
from sklearn import linear_model

datapath = ''

y, sr = librosa.load(datapath)
mfcc = librosa.feature.mfcc(y=y, sr=sr)

#(20, number_of_frames)
#print(mfcc.shape)

logreg = linear_model.LogisticRegression()
logreg.fit(x_train, y_train)
y_test_estimated = logreg.predict(x_test)

print(y_test_estimated)
