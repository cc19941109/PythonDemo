sentence = input('sentence:')

t_width = len(sentence)
b_width = t_width + 6
left_margin = (b_width - t_width) // 2
right_margin = b_width - left_margin - t_width

print()
print('+' + '-' * (left_margin + b_width - right_margin) + '+')
print('|' + ' ' * (left_margin) + ' ' * (b_width - right_margin) + '|')
print('|' + ' ' * (left_margin) + sentence + ' ' * (b_width - right_margin - t_width) + '|')
print('|' + ' ' * (left_margin) + ' ' * (b_width - right_margin) + '|')
print('+' + '-' * (left_margin + b_width - right_margin) + '+')
print()


print(t_width)
print(b_width)
print(left_margin)
print(right_margin)
