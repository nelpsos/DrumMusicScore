from sklearn import linear_model
import librosa
import os
import sys

def all_files(dirname):
    # input: directory path
    # output: file names in the directory
    filenames = os.listdir(dirname) 
    KD = []
    HH = []
    SD = []
    MIX = []
    TESTSET = {"KD": [], "HH": [], "SD": []}
    for filename in filenames:
        if "#train" in filename:
            if "#KD" in filename:
                KD.append(feature_extraction(os.path.join(dirname, filename)))
            if "#HH" in filename:
                HH.append(feature_extraction(os.path.join(dirname, filename)))
            if "#SD" in filename:
                SD.append(feature_extraction(os.path.join(dirname, filename)))
        else:
            if "#MIX" in filename:
                MIX.append(feature_extraction(os.path.join(dirname, filename)))
            if "#KD" in filename:
                TESTSET["KD"].append(feature_extraction(os.path.join(dirname, filename)))
            if "#HH" in filename:
                TESTSET["HH"].append(feature_extraction(os.path.join(dirname, filename)))
            if "#SD" in filename:
                TESTSET["SD"].append(feature_extraction(os.path.join(dirname, filename)))
    
    return KD, HH, SD, MIX, TESTSET


def feature_extraction(f):
    y, sr = librosa.load(f)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    return mfcc.shape


def classifier(x_train, y_train, x_test, y_test):
    logreg = linear_model.LogisticRegression()
    logreg.fit(x_train, y_train)
    y_test_estimated = logreg.predict(x_test)
    return y_test_estimated, logreg


def file_set_maker(KD, HH, SD, TESTSET):
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    x_train += KD
    x_train += HH
    x_train += SD
    x_test += TESTSET["KD"]
    x_test += TESTSET["HH"]
    x_test += TESTSET["SD"]

    for i in range(len(KD)):
        y_train.append(0)
    for i in range(len(HH)):
        y_train.append(1)
    for i in range(len(SD)):
        y_train.append(2)

    for i in range(len(TESTSET["KD"])):
        y_test.append(0)
    for i in range(len(TESTSET["HH"])):
        y_test.append(1)
    for i in range(len(TESTSET["SD"])):
        y_test.append(2)

    return x_train, y_train, x_test, y_test


def predictor(drum_test, logreg):
    drum_test_estimated = logreg.predict(drum_test)
    return drum_test_estimated


# def main(file_path, drum_path):
def main(file_path):
    KD, HH, SD, MIX, TESTSET = all_files(file_path)
    
    x_train, y_train, x_test, y_test = file_set_maker(KD, HH, SD, TESTSET)
    y_test_estimated, logreg = classifier(x_train, y_train, x_test, y_test)
    # train_result = comparer(y_test, y_test_estimated)
    # drum_result = predictor(drum_path, logreg)
    # print(drum_result)
    print(y_test_estimated)
    return 1

    

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    if len(sys.argv) < 2:
        print("usage: python looper.py <path> <drum_path>")
        print("   <path>:\tPath of input audio files to machine learning")
        print("   <drum_path>:\tPath of input audio files to extract")
    else:
        file_path = sys.argv[1]
        # drum_path = sys.argv[2]
        try:
            # main(file_path, drum_path)
            main(file_path)
        except Exception as e:
            print(e)