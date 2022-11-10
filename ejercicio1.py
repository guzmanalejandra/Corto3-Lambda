D = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
order = lambda listDicc, keyOrd: (lambda items, listDicc, keyOrd: [dicc for i in items for dicc in listDicc if dicc.get(keyOrd)==i])(sorted(list({d.get(keyOrd) for d in listDicc})), listDicc, keyOrd)
print(order(D, 'make'))
