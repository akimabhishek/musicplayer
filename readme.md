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
   For Song Create : http://akimabhishek.pythonanywhere.com/music/index/create_song
   For Album Delete : http://akimabhishek.pythonanywhere.com/music/index/delete_album
   For Song Delete : http://akimabhishek.pythonanywhere.com/music/album_id/create_song/song_id
   
Social authentication used : Facebook (issue in login)
login credential : username == admin password == admin1234 , or ,
                   username == akimabhishek password == admin1234
                   
login credential developed using == django-authentication framework 
deployment service used == pythonanywhere

issues to be resolved : 
1) url redirect 
2) facebook privacy setting : Insecure Login Blocked
3) Verification of url 
4) Update option on hold.

Note : For present debug has been turned on so error 404 not visible. 

Database used : sqlite3

git update : gmail auth also added but not pushed in deployment. Presently updating search bar options. 

Unit Test Cases : 

1) Login via credential as well as Facebook.
2) Create, delete
3) Navigation to random urls without login will redirect to login page ("@login required" used)
4) Top navigation bar. 
5) Page is responsive. 
6) Logout functioning. 
7) Logout page displays login option. 





