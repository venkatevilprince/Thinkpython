print (4.0/3)*(3.14*5**3)
print (24.95-24.95*.4)*60-3-(.75*59)



easy = (8 * 60 + 15)* 2 
tempo = (7 * 60 + 12) * 3
total_time=easy +tempo


current_time = 6 * 3600 + 52 * 60
end_time = current_time + total_time


end_hours = end_time / 3600
end_minutes = (end_time % 3600) / 60
new_time = end_hours, ':', end_minutes

print "%d:%d " %(end_hours,end_minutes)
