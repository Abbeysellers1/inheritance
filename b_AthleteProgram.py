import b_AthleteClass as ac

generic_athlete = ac.Athlete(6,220,0.2)

quarterback = ac.Football_Player(6.2,250,0.15,'quarterback','offense')


print("The height for the generic athlete is:",generic_athlete.get_ht())

#print("The team of the generic athlete is:",generic_athlete.get_team())
#the team error of the above does not work because the athlete does not have a team, that is only an attribute 
#of a football player, remember can only work down not up as you go

print("The weight for the football player is:",quarterback.get_wt())

print("The position of the football player is:",quarterback.get_position())
