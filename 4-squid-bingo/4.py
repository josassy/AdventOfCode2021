from typing import Tuple


class BingoCard:
  def __init__(self, numbers):
    self.numbers = numbers
    self.map = [[0 for x in range(5)] for x in range(5)]
  
  # mark the sheet with the specified number
  def mark(self, number) -> bool:
    ret = False
    for i in range(len(self.numbers)):
      for j in range(len(self.numbers[0])):
        if self.numbers[i][j] == number:
          self.map[i][j] = 1
          self.last_mark = number
          ret = True
    return ret

  def check(self) -> bool:
    # check rows for line of 1's
    for i in range(5):
      count = 0
      for j in range(5):
        if self.map[i][j]:
          count += 1
        else:
          break
      if count == 5:
        return True
    # check columns for line of 1's
    for i in range(5):
      count = 0
      for j in range(5):
        if self.map[j][i]:
          count += 1
        else:
          break
      if count == 5:
        return True
    return False

  def score(self) -> int:
    has_win = self.check()
    score = 0
    if has_win:
      # if board win, add up all the unmarked spots
      for i, row in enumerate(self.numbers):
        for j, number in enumerate(row):
          if not self.map[i][j]:
            score += number
    return score * self.last_mark

  def __str__(self) -> str:
    return str(self.numbers) + '\n' + str(self.map)

  def __repr__(self) -> str:
    return str(self.numbers) + '\n' + str(self.map)

def play_check(card: BingoCard, number: int):
  if card.mark(number):
    score = card.score()
    if score:
      return score
  return 0

def setup_game():
  with open('input.txt') as f:
    bingo_input = [int(x) for x in f.readline().strip(' \n').split(',')]
    remaining_lines = [x.strip(' \n') for x in f.readlines() if x.strip(' \n') != '']
  bingo_cards = []
  for i in range(len(remaining_lines) // 5):
    base_index = i * 5
    bingo_lines = []
    for j in range(5):
      bingo_lines.append([int(x) for x in remaining_lines[base_index+j].strip(' \n').split(' ') if x != ''])
    bingo_cards.append(BingoCard(bingo_lines))
  return bingo_input, bingo_cards
  

def winning_bingo(bingo_input, bingo_cards):
  # we have the bingo cards now. iterate through the inputs and check to see which card wins first
  winning_score = 0
  for number in bingo_input:
    for card in bingo_cards:
      # mark each card with number
      score = play_check(card, number)
      if score > 0:
          winning_score = score
          print('winning card', card)
          print('score of', winning_score)
          break
    if winning_score:
      break

def losing_bingo(bingo_input, bingo_cards):
  cards = bingo_cards
  for number in bingo_input:
    new_cards = [x for x in cards if not play_check(x, number) > 0]
    if len(new_cards) > 1:
      cards = new_cards
    elif len(new_cards) == 1:
      cards = new_cards
      print('last card', cards[0])
    else:
      losing_card = cards[0]
      print('losing card', losing_card)
      print('score of', losing_card.score())
      break
  
def p1():
  bingo_input, bingo_cards = setup_game()
  winning_bingo(bingo_input, bingo_cards)

def p2():
  bingo_input, bingo_cards = setup_game()
  losing_bingo(bingo_input, bingo_cards)

# p1()
p2()
