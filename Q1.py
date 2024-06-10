def exercise1(tp, fp, fn):
    # Check kiểu dữ liệu của input
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return

    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return

    # Tính Precision và Recall
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    # Tính F1-Score
    if precision + recall == 0:
        f1_score = 0
    else:
        f1_score = 2 * (precision * recall) / (precision + recall)

    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}')

exercise1(tp =2,fp =3,fn =4)
exercise1(tp ='a',fp =3,fn =4)