paperThicc = 1/200

print('Have you ever wondered how thick a paper will get after a certain number of folds?')
print('Well I can tell you!')
print('How many folds?')

folds = int(input('-->:'))

for i in range(folds):
    paperThicc *= 2

paperThicc /= 100
print(f'The paper would be {paperThicc} m thick')