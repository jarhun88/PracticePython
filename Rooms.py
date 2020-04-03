# An interactive Room Visit

def Start():
    
    living_room = input("You are in the living Room. Proceed to: Kitchen or Bedroom")
    kitchen = input("You are in the Kitchen. Proceed to: Living Room")
    bedroom = input("You are in the Bedroom. Proceed to: Living Room")
    current_room = living_room
    
    while current_room == living_room:
        if living_room == "Kitchen":
            current_room = kitchen
        elif living_room == "Bedroom":
            current_room = bedroom
    if current_room == kitchen:
        if kitchen == "Living Room":
            current_room = living_room
    elif current_room == "Bedroom":
        if bedroom == "Living Room":
            current_room = living_room
            
    
    

                        
