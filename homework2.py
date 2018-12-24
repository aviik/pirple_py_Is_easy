"""This programme incorporates functions that print individual attributes(3) as they are called"""


#function to Genre
def genre():
    return "Blues"


#function to Artist
def artist():
    return "Daniel Castro"


#function to Year
def year():
    return "1999"



#Attribute variables
song = "  I'll Play The Blues For You"
#artist = "Daniel Castro"
albumn = "No Surrender"
#year = 1999
#genre = "Blues"
sub_genre = "Blues-Contemporary"    #string
track_number = 8            #int
song_duration = 7.42        #float 
cd_available = True         #boolean value

#Attribute Labels 
print("")
print("")
print("Song:      ", song)
print("Artist:      ", artist())        #function "artist()" called here
print("Albumn:      ", albumn)
print("Year:        ", year())          #function "year()" called here
print("Genre:       ", genre())         #function "genre()" called here
print("Sub-genre:   ", sub_genre)
print("Track Number:",track_number)
print("Length:      ", song_duration)
print("CD available:", cd_available)