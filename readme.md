#Django Application

python version == 3.4
django version == 2.0.4

dependecies == social-auth-app-django

Tables : 

Album == [user, artist, album_title, genre]
Song == [album, song_title, song_link]

urls : 
   For login : http://akimabhishek.pythonanywhere.com/music/login/,
   For Album : http://akimabhishek.pythonanywhere.com/music/
   For ALbum Create : http://akimabhishek.pythonanywhere.com/music/create_album/
   For Song Create : http://akimabhishek.pythonanywhere.com/music/<index>/create_song
  
Social authentication used : Facebook (issue in login)
login credential : username == admin password == admin1234
                   username == akimabhishek password == admin1234
                   
login credential developed using == django-authentication framework 


