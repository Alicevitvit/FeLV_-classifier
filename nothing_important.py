from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import balanced_accuracy_score
import pandas as p

data = p.read_csv(r"C:\Users\user\Desktop\cats\data_cats\data.csv", sep=";")
ih = data["Ill_Healthy"]
hgb = data["Hgb"]
hct = data["Hct"]
rbc = data["Rbc"]
mcv = data["MCV"]
arg, ans = [], []

for i in range(len(data)):
    arg.append([hgb[i], hct[i], rbc[i], mcv[i]])
    ans.append(ih[i])


# print(clf.predict(arg_train))
# print(ans_test)

tp, tn, fp, fn = 0, 0, 0, 0
av_tp, av_tn, av_fp, av_fn = 0, 0, 0, 0
cnt = 0

for i in range(500):
    cnt += 1
    print(i)
    arg_train, arg_test, ans_train, ans_test = train_test_split(arg, ans, test_size=0.3, train_size=0.7)
    clf = LogisticRegression(random_state=0, max_iter=10000, class_weight={1: 5, 0: 1}).fit(arg_train, ans_train)
    for i in range(len(ans_test)):
        if ans_test[i] == clf.predict(arg_test)[i] and ans_test[i] == 1:
            tp += 1
        elif ans_test[i] == clf.predict(arg_test)[i] and ans_test[i] == 0:
            tn += 1
        elif ans_test[i] != clf.predict(arg_test)[i] and ans_test[i] == 1:
            fn += 1
        else:
            fp += 1


av_tp = tp/cnt
av_tn = tn/cnt
av_fp = fp/cnt
av_fn = fn/cnt
print(balanced_accuracy_score(ans_test, clf.predict(arg_test)))
print(f"av_tp: {av_tp}, av_tn: {av_tn}, av_fp: {av_fp}, av_fn: {av_fn}")
print(av_tp + av_tn + av_fp + av_fn)
# clf = GradientBoostingClassifier().fit(arg_train, ans_train)







