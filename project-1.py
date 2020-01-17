print('There is a fun myth about the inventor of chess.')
print('There is a popular myth about the man who invented chess. The local ruler was so\n'
 'pleased with the invention that he offered the inventor a great amount of gold. The \n'
 'inventor suggested an alternative reward: he would get one grain of wheat on the first\n'
 'square of the chess board, two grains on the second square, 4 on the third, 8 on the \n'
 'fourth, and so on, doubling the number of grains each time. The ruler saw that this \n'
 'must be a much better deal for him and so he accepted.')

numGrains = 1
for i in range(64):
    numGrains*=2

print(f'Since the  board has 64 squares, the king would have to pay the inventor roughly {numGrains/1000000000000000000:.3f} pentillion grains.')
print(f'That much grain would weigh {(numGrains*50)/1000000000000000000:.3f} hexillion kilograms!')
print('Thats an inconcievabley large number. Lets see how much that would be at your house.')
print('What is the area of your town in meters?')
area = int(input('-->:'))

grainVol = (numGrains*(0.06**3))/100
grainDepth = grainVol/(area**2)

print(f'That is so much grain, if it were spread over your town, it would be {grainDepth/1000:.3f} kilometers deep!')
