def bananabid(my_player_number, my_bananas, monkey_position, opponent_bananas, past_bid_list, turn_number):
   if abs(monkey_position) >= 3:
       return 0
   if my_bananas >= 200:
      return 51

   elif my_bananas >= 149:
      return 61

   elif my_bananas >= 88:
      return 88
   else:
      return 0
