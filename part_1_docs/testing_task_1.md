### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  #None of the methods below require 'self' as an input parameter.


  def check_for_ace(self, card):
    #should be a double equals sign (==) not a single equals sign (=)
    if card.value = 1:
      return True
    #there should be a comma after 'else'.
    else
      return False
   
  #should be 'def' to define a new function not 'dif', and there is a missing comma betweeen card1 and card2.
  dif highest_card(self, card1 card2):
  #The indentation is not correct below.
  if card1.value > card2.value:
    #there is no variable called card, it should be card1.
    return card
  else:
    return card2
  

#the indentation is not correct below, because this function is not currently nested within the CardGame class
def cards_total(self, cards):
  #the total variable below should be set to zero initally.
  total
  for card in cards:
    total += card.value
    #this return should be outside the loop, otherwise it will just return the value of the first card.
    #string concatenation will not work like this, you would need to convert the total variable into a string first, 
    # and it would be better readability for the user if there was a space after the word 'of'.
    return "You have a total of" + total
  
```
