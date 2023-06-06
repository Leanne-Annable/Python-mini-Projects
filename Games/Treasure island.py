print("\nWelcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print('''You awake to find yourself on a strange island with a bump on your head and no memory.

As you look around the area you notice two pathways,
the path on the right leads to a clearing with fallen leaves scattered about,
the path to the left leads deeper into the forest, but it is too dark to see what lies ahead.
''')
choice1 = input("Do you go right into the clearing, or left into the woods? (left/right): \n").strip().lower()

if choice1 == "left":
  print('''
  You make your way through the woods. 
  After a while you can see the trees have started thinning out and you eventually find yourself at the edge of a lake.
  In the middle of the lake you notice a small island with a house on it.
  The house appears to have a fire going as you can see smoke coming from the chimney.
  It has been a few hours since you awoke on the island and you are cold and hungry. 
  You decide to make your way over to the island, it's not that far but the water looks very dark.
  In the distance on the other side of the lake you can see a small boat
  ''')
  choice2 = input("Do you attempt to swim across, or do you want to make the journey to get the boat? (swim/boat): \n").strip().lower()
  if choice2 == "boat":
    print('''
    You make the hike over to the boat. It wasn't as far as it looked!
    You cross the lake with ease and find youself in front of the house.
    The front door is already open and when you peer inside you notice there are three doors.
    One is red, one is blue and the final door is yellow.
    ''')
    choice3 = input("Which door would you like to open? (red/blue/yellow): \n").strip().lower()
    if choice3 == "red":
      print('''
      You open the door to find yourself engulfed in flames, 
      someone really did have a fire going.... out of control!
      Unfortunately they are not here to help put the flames out and you burn to a crisp!
      
      GAME OVER!
      ''')
    elif choice3 == "blue":
      print('''
      It would appear that someone left the tap running!
      The room was filled with water and as soon as you opened the door
      SWOOOOOOSHHHH!
      You get swept out of the house and into the lake.
      Unfortunately the shower curtain got swept away too and you ended up being wrapped in it!
      You can't get out of it in time to stop yourself from drowning!
      
      GAME OVER!!!''')
    elif choice3 == "yellow":
      print('''
      As you open the door you see a man and woman.
      They appear to be cooking some delicious smelling food,
      you notice the dining table is set for three and they gesture for you to take a seat.
      
      "Welcome home dear! We wondered where you had got to! 
      Oh no! It looks like you have bumped your head! Let me take care of that and then we can all have some food."
      
      It turns out that this was your home and these are your parents! 
      They take care of your wounds and you all sit down to a lovely meal together.
      Later you all sit by the fireplace and play games together.

      What can be more of a treasure than spending time with the ones you love,
      and lots of yummy food om nom nom!''')
    else:
      print('''
      You decide this place isn't for you!
      You head back out to explore the rest of the island.
      Unfortunately the boat seems to have sprung a leak!
      You find out that you can't swim! 
      Down, down, down you go, into those murky depths!
      
      GAME OVER!!!''')

  elif choice2 == "swim":
    print('''
    You decide to swim across the water, it's not that far!
    
    unfortunately you soon realize that you don't actually know how to swim!
    
    Down into the murky depths you go!
    
    GAME OVER!!''')
  else:
    print('''
    You decide after all that you don't want to go to the house afterall!
    You end up wandering the island. 
    Unfortunately you stumble into an animal trap!
    No one can hear your cries for help and you slowly fade away.
    
    GAME OVER!!!''')
  
elif choice1 == "right":
  print('''
  You decide to give the dark and scary woods a miss!
  As you start making your way along the clearing, 
  you come to realize that you're not alone on this island.
  Unfortunately you notice too late! 
  As you walk over some of the leaves you feel something give way below you,
  you fall feet first into a pit trap!
  
  GAME OVER!!!''')

else:
  print("Paths aren't for you! Unfortunately neither are games apparently! GAME OVER!!!")





