# SeventhSeaRollGenerator
A generator of rolls for the 2nd edition of the 7th Sea tabletop RPG


NOTE: for this dice roller, it was assumed, for the rerolls, that you would always
want to reroll the lowest die/dice, which helped reduce the clutter on the UI enormously.

NOTE 2: from what I've seen, this roll generator works well for rolls of up to 22 or so dice.
Any more than that, and it starts getting big delays due to the amount of calculations it must make.

 As you can see, the UI isn't the friendlist of all, but trust me, it does work! It was the 
simplest I could do it while also allowing all possible rolls to be executed. Thus, if you have an Avalon sorcerer
with 5 in athletics, academy, legendary trait, strength of many and all the luck-based Brawn glamours, you could
use this generator to make his rolls. The price, however, is that it'll probably take a while to get used to its 
layout :(

Now, on to the instructions!

 For a basic roll, just select the amount of dice you'll be rolling, and press the 'roll' button.

 This will make the roll, show the result and automatically group them in the necessary successes.

 If you want to make a roll where the dice explode, or where you count 2 successes on a higher difficulty, just check the
 "10s explode" or "Skill rank 4" boxes and you'll be good to go.

 Keep in mind that you don't need to change the difficulty in order for the skill rank 4 property to work well:
 that box is set for those times where the GM increases the base difficulty by using a Danger Point.

 Things get a bit less friendly when you can reroll a single die, ie rolling a rank 3 skill. For this,
check the "Reroll one die" box and roll. You'll notice that the "reroll lowest die" buttons will 
now work normally, and that the "results" window only shows the roll, without grouping. 
This way, you can decide whether rerolling the die is worth the risk.

For "Devil's Luck" it's similar: you check the box, make the roll, but instead of selecting "yes" or "no",
you input the amount of dice you want to reroll, which will start from the lowest and going forward. If you don't
want to reroll any dice, just input "0" and press the Reroll button. You can't enter a number higher than the size of the
roll.

 Next we have the "Add to each die" drop menu. This works for advantages such as "strength of many"
or "academy", which add a certain amount to all dice. The maximum is 6, in the case of a roll of
Strength of Many 5 where Academy is also applicable. I don't think it's possible to go further than that,
but let me know if I'm wrong!

Legendary trait works very simply: just check the box, and it will automatically turn of your dice into a 10,
which will explode if that checkbox is filled.

If you have both Devil's Luck and Skill Rank 3 (reroll one die), you can take either of those decisions first. The
same happens for the glamours, explained below.

If you want a clean slate, just press the "reset" button and everything will restart!

Up to this part should cover every possible roll on the core rulebook, UNLESS you happen to be an Avalon sorcerer,
in which case things get, unfortunately, more complicated.

If you want to use Petty Luck, you should select your rank on the glamour in the "petty luck" drop menu,
then roll, at which point you can decide if you want to use it on your lowest die or not.

For Mythic, you should check the "has mythic" box, then roll, select the amount of dice you want to 
reroll, which will once again start from the lowest, and then the "mythic reroll" button. If you select 0, the roll stays as it is.

If your roll is affected by Mad Luck, you can write the dice added in the text bar under "Mad Luck Dice",
just make sure to use spaces as separation, not commas. So, if you are adding a 2 and a 3 to a roll, you would
write "2 3" on the text bar. You can't enter numbers below 1 or above 10.

Finally, for Greater Luck, you select your ranks on the drop down menu, roll the dice, and then you
can select which dice you want to add the amount to: 1 will be the first, 2 will be the second, etc. 
If you decide you don't want to add to any dice, just input 0 on the bar and press the Greater Luck button.
