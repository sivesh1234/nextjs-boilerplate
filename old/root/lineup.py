from io import StringIO

DATA = StringIO("""
Act,Day,Stage,X Coordinate,Y Coordinate,Timeslot,Start,Finish,Start Date,Finish Date,Start DateTime,Finish DateTime
Glowbros,Wednesday,Walkabouts,60,33,01:00 - 03:00,01:00,03:00,27/06/2024,27/06/2024,26/06/2024 01:00,27/06/2024 03:00
The Sky At Day,Wednesday,Walkabouts,60,33,10:50 - 11:35,10:50,11:35,26/06/2024,26/06/2024,26/06/2024 10:50,26/06/2024 11:35
Films,Wednesday,Atchin Tan,0,0,11:00 - 12:30,11:00,12:30,26/06/2024,26/06/2024,26/06/2024 11:00,26/06/2024 12:30
Acoustic Open Mic,Wednesday,Croissant Neuf Bandstand,55,21,11:00 - 11:45,11:00,11:45,26/06/2024,26/06/2024,26/06/2024 11:00,26/06/2024 11:45
Activist Intersection,Wednesday,Greenpeace (Beam),54,26,11:00 - 14:00,11:00,14:00,26/06/2024,26/06/2024,26/06/2024 11:00,26/06/2024 14:00
Magical Musical Time Machine,Wednesday,Walkabouts,60,33,11:00 - 11:45,11:00,11:45,26/06/2024,26/06/2024,26/06/2024 11:00,26/06/2024 11:45
Be Prepared,Wednesday,Walkabouts,60,33,11:15 - 12:00,11:15,12:00,26/06/2024,26/06/2024,26/06/2024 11:15,26/06/2024 12:00
Ministry Of Happy,Wednesday,Walkabouts,60,33,11:30 - 12:15,11:30,12:15,26/06/2024,26/06/2024,26/06/2024 11:30,26/06/2024 12:15
Open,Wednesday,Bimble Inn,41,16,12:00 - 03:00,12:00,03:00,26/06/2024,27/06/2024,26/06/2024 12:00,27/06/2024 03:00
Joanna & The Dropouts,Wednesday,Croissant Neuf Bandstand,55,21,12:00 - 12:30,12:00,12:30,26/06/2024,26/06/2024,26/06/2024 12:00,26/06/2024 12:30
Tba,Wednesday,Greenpeace,55,26,12:00 - 12:45,12:00,12:45,26/06/2024,26/06/2024,26/06/2024 12:00,26/06/2024 12:45
Jay Rawlings,Wednesday,Walkabouts,60,33,12:00 - 12:45,12:00,12:45,26/06/2024,26/06/2024,26/06/2024 12:00,26/06/2024 12:45
Worldroots Acapella,Wednesday,Walkabouts,60,33,12:00 - 14:00,12:00,14:00,26/06/2024,26/06/2024,26/06/2024 12:00,26/06/2024 14:00
Trish Reilly: Music,Wednesday,Atchin Tan,0,0,12:30 - 13:15,12:30,13:15,26/06/2024,26/06/2024,26/06/2024 12:30,26/06/2024 13:15
Theo Warrington,Wednesday,Croissant Neuf Bandstand,55,21,12:45 - 13:15,12:45,13:15,26/06/2024,26/06/2024,26/06/2024 12:45,26/06/2024 13:15
The Sky At Day,Wednesday,Walkabouts,60,33,12:50 - 13:35,12:50,13:35,26/06/2024,26/06/2024,26/06/2024 12:50,26/06/2024 13:35
Jo Bucket,Wednesday,Carhenge,58,36,13:00 - 14:00,13:00,14:00,26/06/2024,26/06/2024,26/06/2024 13:00,26/06/2024 14:00
Georgia D'Arcy Roden,Wednesday,Crooner'S Corner,0,0,13:00 - 13:45,13:00,13:45,26/06/2024,26/06/2024,26/06/2024 13:00,26/06/2024 13:45
Dance Class: Salsa,Wednesday,Glasto Latino,58,27,13:00 - 14:00,13:00,14:00,26/06/2024,26/06/2024,26/06/2024 13:00,26/06/2024 14:00
Kung Fu Panda 4 Pg,Wednesday,Pilton Palais Cinema,64,36,13:00 - 14:35,13:00,14:35,26/06/2024,26/06/2024,26/06/2024 13:00,26/06/2024 14:35
"Myanmar & Friends & Families Of Travellers - Chris Gunness, Billy Welch, Sindy Joyce.",Wednesday,Speakers Forum,0,0,13:00 - 14:00,13:00,14:00,26/06/2024,26/06/2024,26/06/2024 13:00,26/06/2024 14:00
Fftp: Music,Wednesday,Atchin Tan,0,0,13:15 - 14:00,13:15,14:00,26/06/2024,26/06/2024,26/06/2024 13:15,26/06/2024 14:00
Be Prepared,Wednesday,Walkabouts,60,33,13:15 - 14:00,13:15,14:00,26/06/2024,26/06/2024,26/06/2024 13:15,26/06/2024 14:00
Izzie Derry,Wednesday,Croissant Neuf Bandstand,55,21,13:30 - 16:00,13:30,16:00,26/06/2024,26/06/2024,26/06/2024 13:30,26/06/2024 16:00
Welcome To The Laboratory,Wednesday,Laboratory Stage,0,0,13:30 - 14:00,13:30,14:00,26/06/2024,26/06/2024,26/06/2024 13:30,26/06/2024 14:00
Charlotte May,Wednesday,Crooner'S Corner,0,0,14:00 - 14:45,14:00,14:45,26/06/2024,26/06/2024,26/06/2024 14:00,26/06/2024 14:45
Dance Class: Samba,Wednesday,Glasto Latino,58,27,14:00 - 15:00,14:00,15:00,26/06/2024,26/06/2024,26/06/2024 14:00,26/06/2024 15:00
Occupying A Shell Oil Rig At Sea,Wednesday,Greenpeace (Beam),54,26,14:00 - 15:00,14:00,15:00,26/06/2024,26/06/2024,26/06/2024 14:00,26/06/2024 15:00
Comics Without Borders - Kate Evans,Wednesday,Speakers Forum,0,0,14:00 - 15:00,14:00,15:00,26/06/2024,26/06/2024,26/06/2024 14:00,26/06/2024 15:00
Groovy Guy,Wednesday,The Pavement,0,0,14:00 - 14:30,14:00,14:30,26/06/2024,26/06/2024,26/06/2024 14:00,26/06/2024 14:30
Gateway Girl,Wednesday,Croissant Neuf Bandstand,55,21,14:15 - 14:45,14:15,14:45,26/06/2024,26/06/2024,26/06/2024 14:15,26/06/2024 14:45
Wildlife Kate - Get Wild In Your Space!,Wednesday,Laboratory Stage,0,0,14:15 - 14:45,14:15,14:45,26/06/2024,26/06/2024,26/06/2024 14:15,26/06/2024 14:45
Celestials,Wednesday,Walkabouts,60,33,14:15 - 14:45,14:15,14:45,26/06/2024,26/06/2024,26/06/2024 14:15,26/06/2024 14:45
"Damian Le Bas, Talk: The Journey Of Writing 'The Stopping Places: A Journey Through Gypsy Britain'",Wednesday,Atchin Tan,0,0,14:30 - 15:15,14:30,15:15,26/06/2024,26/06/2024,26/06/2024 14:30,26/06/2024 15:15
Magical Musical Time Machine,Wednesday,Walkabouts,60,33,14:30 - 15:15,14:30,15:15,26/06/2024,26/06/2024,26/06/2024 14:30,26/06/2024 15:15
Mario Morris Magic,Wednesday,The Pavement,0,0,14:35 - 15:05,14:35,15:05,26/06/2024,26/06/2024,26/06/2024 14:35,26/06/2024 15:05
Barbie 12,Wednesday,Pilton Palais Cinema,64,36,14:45 - 16:40,14:45,16:40,26/06/2024,26/06/2024,26/06/2024 14:45,26/06/2024 16:40
Kitty Stewart,Wednesday,Croissant Neuf Bandstand,55,21,15:00 - 15:45,15:00,15:45,26/06/2024,26/06/2024,26/06/2024 15:00,26/06/2024 15:45
Mama Tokus,Wednesday,Crooner'S Corner,0,0,15:00 - 15:45,15:00,15:45,26/06/2024,26/06/2024,26/06/2024 15:00,26/06/2024 15:45
Dance Class: Salsa,Wednesday,Glasto Latino,58,27,15:00 - 16:00,15:00,16:00,26/06/2024,26/06/2024,26/06/2024 15:00,26/06/2024 16:00
Sounds Of Space,Wednesday,Laboratory Stage,0,0,15:00 - 15:45,15:00,15:45,26/06/2024,26/06/2024,26/06/2024 15:00,26/06/2024 15:45
David Celia,Wednesday,Lunched Out Lizards,0,0,15:00 - 16:00,15:00,16:00,26/06/2024,26/06/2024,26/06/2024 15:00,26/06/2024 16:00
Organising For Free Movement: 10 Years Of Alarm Phone - Philippa Metcalfe,Wednesday,Speakers Forum,0,0,15:00 - 16:00,15:00,16:00,26/06/2024,26/06/2024,26/06/2024 15:00,26/06/2024 16:00
Jay Rawlings,Wednesday,Walkabouts,60,33,15:00 - 15:45,15:00,15:45,26/06/2024,26/06/2024,26/06/2024 15:00,26/06/2024 15:45
Yann Elvis,Wednesday,The Pavement,0,0,15:10 - 15:40,15:10,15:40,26/06/2024,26/06/2024,26/06/2024 15:10,26/06/2024 15:40
Thomas Mccarthy: Music,Wednesday,Atchin Tan,0,0,15:30 - 16:15,15:30,16:15,26/06/2024,26/06/2024,26/06/2024 15:30,26/06/2024 16:15
Bigheads,Wednesday,Greenpeace,55,26,15:30 - 16:00,15:30,16:00,26/06/2024,26/06/2024,26/06/2024 15:30,26/06/2024 16:00
Actions Skills Workshops,Wednesday,Greenpeace (Beam),54,26,15:30 - 17:00,15:30,17:00,26/06/2024,26/06/2024,26/06/2024 15:30,26/06/2024 17:00
Ministry Of Happy,Wednesday,Walkabouts,60,33,15:30 - 16:15,15:30,16:15,26/06/2024,26/06/2024,26/06/2024 15:30,26/06/2024 16:15
Mr Peewee The Drumming Puppet,Wednesday,The Pavement,0,0,15:45 - 16:15,15:45,16:15,26/06/2024,26/06/2024,26/06/2024 15:45,26/06/2024 16:15
Mike Dennis,Wednesday,Croissant Neuf Bandstand,55,21,16:00 - 17:00,16:00,17:00,26/06/2024,26/06/2024,26/06/2024 16:00,26/06/2024 17:00
Gracie Barry Tait,Wednesday,Crooner'S Corner,0,0,16:00 - 16:45,16:00,16:45,26/06/2024,26/06/2024,26/06/2024 16:00,26/06/2024 16:45
Dance Class: Samba,Wednesday,Glasto Latino,58,27,16:00 - 17:00,16:00,17:00,26/06/2024,26/06/2024,26/06/2024 16:00,26/06/2024 17:00
Bassie Gracie,Wednesday,Greenpeace,55,26,16:00 - 16:45,16:00,16:45,26/06/2024,26/06/2024,26/06/2024 16:00,26/06/2024 16:45
Edie Blue,Wednesday,Laboratory Stage,0,0,16:00 - 16:45,16:00,16:45,26/06/2024,26/06/2024,26/06/2024 16:00,26/06/2024 16:45
Mal Webb And Kylie Morrigan,Wednesday,Mandala Stage,0,0,16:00 - 17:00,16:00,17:00,26/06/2024,26/06/2024,26/06/2024 16:00,26/06/2024 17:00
"Grenfell, The Fight For Truth And Justice - Karim Mussilhy",Wednesday,Speakers Forum,0,0,16:00 - 17:00,16:00,17:00,26/06/2024,26/06/2024,26/06/2024 16:00,26/06/2024 17:00
"Billy Welch And Sindy Joyce, Talk: Raising Awareness And Solidarity For Romany And Irish Traveller Communities",Wednesday,Atchin Tan,0,0,16:15 - 17:00,16:15,17:00,26/06/2024,26/06/2024,26/06/2024 16:15,26/06/2024 17:00
Goldie Fiasco,Wednesday,The Pavement,0,0,16:20 - 16:50,16:20,16:50,26/06/2024,26/06/2024,26/06/2024 16:20,26/06/2024 16:50
Danimal Crackers,Wednesday,Lunched Out Lizards,0,0,16:30 - 17:30,16:30,17:30,26/06/2024,26/06/2024,26/06/2024 16:30,26/06/2024 17:30
The Suitcase Escape Game,Wednesday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,26/06/2024,26/06/2024,26/06/2024 16:30,26/06/2024 17:15
The Fall Guy 12A,Wednesday,Pilton Palais Cinema,64,36,16:45 - 18:55,16:45,18:55,26/06/2024,26/06/2024,26/06/2024 16:45,26/06/2024 18:55
Kiki & Pascal,Wednesday,The Pavement,0,0,16:55 - 17:25,16:55,17:25,26/06/2024,26/06/2024,26/06/2024 16:55,26/06/2024 17:25
Jo Bucket,Wednesday,Carhenge,58,36,17:00 - 18:00,17:00,18:00,26/06/2024,26/06/2024,26/06/2024 17:00,26/06/2024 18:00
Georgia D'Arcy Roden,Wednesday,Crooner'S Corner,0,0,17:00 - 17:45,17:00,17:45,26/06/2024,26/06/2024,26/06/2024 17:00,26/06/2024 17:45
Dance Class: Salsa,Wednesday,Glasto Latino,58,27,17:00 - 18:00,17:00,18:00,26/06/2024,26/06/2024,26/06/2024 17:00,26/06/2024 18:00
Gilan,Wednesday,Laboratory Stage,0,0,17:00 - 17:45,17:00,17:45,26/06/2024,26/06/2024,26/06/2024 17:00,26/06/2024 17:45
"West Afrika, Climate And The Global North - Gail Bradbrook",Wednesday,Speakers Forum,0,0,17:00 - 18:00,17:00,18:00,26/06/2024,26/06/2024,26/06/2024 17:00,26/06/2024 18:00
Celestials,Wednesday,Walkabouts,60,33,17:00 - 17:30,17:00,17:30,26/06/2024,26/06/2024,26/06/2024 17:00,26/06/2024 17:30
Fortuni & Fae,Wednesday,Walkabouts,60,33,17:00 - 17:45,17:00,17:45,26/06/2024,26/06/2024,26/06/2024 17:00,26/06/2024 17:45
Overeasy Music Quiz,Wednesday,West Holts Bar,59,29,17:00 - 00:00,17:00,00:00,26/06/2024,27/06/2024,26/06/2024 17:00,27/06/2024 00:00
Martin Furey: Music,Wednesday,Atchin Tan,0,0,17:15 - 18:00,17:15,18:00,26/06/2024,26/06/2024,26/06/2024 17:15,26/06/2024 18:00
The Disappointments,Wednesday,Croissant Neuf Bandstand,55,21,17:30 - 18:30,17:30,18:30,26/06/2024,26/06/2024,26/06/2024 17:30,26/06/2024 18:30
David Celia,Wednesday,Mandala Stage,0,0,17:30 - 18:30,17:30,18:30,26/06/2024,26/06/2024,26/06/2024 17:30,26/06/2024 18:30
Go Bananas,Wednesday,The Pavement,0,0,17:30 - 18:00,17:30,18:00,26/06/2024,26/06/2024,26/06/2024 17:30,26/06/2024 18:00
Alexandra Haddow,Wednesday,Greenpeace,55,26,18:00 - 18:45,18:00,18:45,26/06/2024,26/06/2024,26/06/2024 18:00,26/06/2024 18:45
Opening Ceremony,Wednesday,Humblewell Active Platform,42,21,18:00 - 19:00,18:00,19:00,26/06/2024,26/06/2024,26/06/2024 18:00,26/06/2024 19:00
Millie Watson,Wednesday,Lunched Out Lizards,0,0,18:00 - 19:00,18:00,19:00,26/06/2024,26/06/2024,26/06/2024 18:00,26/06/2024 19:00
Gaza; Flowers Don'T Grow Where Bombs Drop - Aisha Kerallah,Wednesday,Speakers Forum,0,0,18:00 - 19:00,18:00,19:00,26/06/2024,26/06/2024,26/06/2024 18:00,26/06/2024 19:00
The Trouble Notes,Wednesday,Croissant Neuf Bandstand,55,21,18:45 - 19:30,18:45,19:30,26/06/2024,26/06/2024,26/06/2024 18:45,26/06/2024 19:30
Adriana'S Keys,Wednesday,Mandala Stage,0,0,18:45 - 19:10,18:45,19:10,26/06/2024,26/06/2024,26/06/2024 18:45,26/06/2024 19:10
Migration U,Wednesday,Pilton Palais Cinema,64,36,19:00 - 21:35,19:00,21:35,26/06/2024,26/06/2024,26/06/2024 19:00,26/06/2024 21:35
Palestine: An Unprecedented Movement - Reel News Films Q & A,Wednesday,Speakers Forum,0,0,19:00 - 20:00,19:00,20:00,26/06/2024,26/06/2024,26/06/2024 19:00,26/06/2024 20:00
Opening Ceremony & Fire Procession,Wednesday,Tree Stage,44,51,19:00 - 19:30,19:00,19:30,26/06/2024,26/06/2024,26/06/2024 19:00,26/06/2024 19:30
Carnival,Wednesday,Glasto Latino,58,27,19:30 - 20:00,19:30,20:00,26/06/2024,26/06/2024,26/06/2024 19:30,26/06/2024 20:00
Jacob Szulecki,Wednesday,Mandala Stage,0,0,19:30 - 20:30,19:30,20:30,26/06/2024,26/06/2024,26/06/2024 19:30,26/06/2024 20:30
The Common Opening Ceremony: Fuego Nuevo Musical Ritual– Return To The Heart,Wednesday,Temple Uprising,0,0,19:30 - 20:30,19:30,20:30,26/06/2024,26/06/2024,26/06/2024 19:30,26/06/2024 20:30
Jan Van Ijken & Entity - The Art Of Flying,Wednesday,Tree Stage,44,51,19:30 - 20:15,19:30,20:15,26/06/2024,26/06/2024,26/06/2024 19:30,26/06/2024 20:15
Nature Is Noisy,Wednesday,Croissant Neuf Bandstand,55,21,20:00 - 20:45,20:00,20:45,26/06/2024,26/06/2024,26/06/2024 20:00,26/06/2024 20:45
Indira Roman Y Aji Pa' Ti (Acoustic),Wednesday,Glasto Latino,58,27,20:00 - 21:30,20:00,21:30,26/06/2024,26/06/2024,26/06/2024 20:00,26/06/2024 21:30
River Roots,Wednesday,Lunched Out Lizards,0,0,20:00 - 21:00,20:00,21:00,26/06/2024,26/06/2024,26/06/2024 20:00,26/06/2024 21:00
Everything Must Change - Reel News Films Q & A,Wednesday,Speakers Forum,0,0,20:00 - 21:30,20:00,21:30,26/06/2024,26/06/2024,26/06/2024 20:00,26/06/2024 21:30
Open,Wednesday,The Rocket Lounge,64,16,20:00 - 00:00,20:00,00:00,26/06/2024,27/06/2024,26/06/2024 20:00,27/06/2024 00:00
Jasmin Harsono - Opening Meditation,Wednesday,Tree Stage,44,51,20:15 - 21:00,20:15,21:00,26/06/2024,26/06/2024,26/06/2024 20:15,26/06/2024 21:00
Billy Connolly: Big Banana Feet 12A,Wednesday,Pilton Palais Cinema,64,36,20:45 - 22:05,20:45,22:05,26/06/2024,26/06/2024,26/06/2024 20:45,26/06/2024 22:05
The Mandala Folk Jam,Wednesday,Mandala Stage,0,0,21:00 - 23:45,21:00,23:45,26/06/2024,26/06/2024,26/06/2024 21:00,26/06/2024 23:45
Youth Ft Jake Storm - Allen Ginsberg'S Iron Horse,Wednesday,Tree Stage,44,51,21:00 - 21:30,21:00,21:30,26/06/2024,26/06/2024,26/06/2024 21:00,26/06/2024 21:30
Acoustic Open Mic,Wednesday,Croissant Neuf Bandstand,55,21,21:15 - 22:00,21:15,22:00,26/06/2024,26/06/2024,26/06/2024 21:15,26/06/2024 22:00
Wonderment Presents Chris Fitchew & Friends,Wednesday,Greenpeace,55,26,21:30 - 23:30,21:30,23:30,26/06/2024,26/06/2024,26/06/2024 21:30,26/06/2024 23:30
Merlin Sheldrake Q&A With Emily Eavis,Wednesday,Tree Stage,44,51,21:30 - 22:30,21:30,22:30,26/06/2024,26/06/2024,26/06/2024 21:30,26/06/2024 22:30
Gusto Gusto,Wednesday,Lunched Out Lizards,0,0,22:00 - 23:00,22:00,23:00,26/06/2024,26/06/2024,26/06/2024 22:00,26/06/2024 23:00
Glowbros,Wednesday,Walkabouts,60,33,22:00 - 00:00,22:00,00:00,26/06/2024,27/06/2024,26/06/2024 22:00,27/06/2024 00:00
The Lost Boys 15,Wednesday,Pilton Palais Cinema,64,36,22:15 - 23:55,22:15,23:55,26/06/2024,26/06/2024,26/06/2024 22:15,26/06/2024 23:55
Fulu Miziki,Wednesday,Carhenge,58,36,22:30 - 23:40,22:30,23:40,26/06/2024,26/06/2024,26/06/2024 22:30,26/06/2024 23:40
"Sam Lee - An Oak Song, A Folksong And A Nightingale",Wednesday,Tree Stage,44,51,22:30 - 23:30,22:30,23:30,26/06/2024,26/06/2024,26/06/2024 22:30,26/06/2024 23:30
Acoustic Jam Session,Wednesday,Lunched Out Lizards,0,0,23:00 - 00:00,23:00,00:00,26/06/2024,27/06/2024,26/06/2024 23:00,27/06/2024 00:00
David R Abram - Prehistoric Britain From The Air,Wednesday,Tree Stage,44,51,23:30 - 00:15,23:30,00:15,26/06/2024,27/06/2024,26/06/2024 23:30,27/06/2024 00:15
Anil,Thursday,Arrivals,0,0,00:00 - 01:00,00:00,01:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:00
Rukus,Thursday,Babylon Uprising,0,0,00:00 - 01:00,00:00,01:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:00
The Plumps B2B Kraft Kuts,Thursday,Bbc Music Introducing,45,44,00:00 - 01:30,00:00,01:30,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:30
&? (Blendid Takeover),Thursday,Cornish Arms,0,0,00:00 - 02:00,00:00,02:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 02:00
Acid Joe,Thursday,Deluxe Diner,64,17,00:00 - 01:30,00:00,01:30,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:30
¥///0 $#£[[,Thursday,Firmly Rooted,43,43,00:00 - 03:00,00:00,03:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 03:00
Eliza Rose,Thursday,Genosys,0,0,00:00 - 01:30,00:00,01:30,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:30
Adelphi Music Factory,Thursday,Greenpeace,55,26,00:00 - 01:30,00:00,01:30,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:30
Shygirl Presents Club Shy,Thursday,Levels,42,44,00:00 - 01:30,00:00,01:30,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:30
Dj Hollyhox,Thursday,Lunched Out Lizards,0,0,00:00 - 01:00,00:00,01:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:00
Copperdollar Selectors,Thursday,Mez Yard,0,0,00:00 - 02:00,00:00,02:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 02:00
Booty Bass X Popola: Devolicious X Thai Chi,Thursday,Nomad,0,0,00:00 - 00:30,00:00,00:30,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 00:30
Retro Cassetta,Thursday,Platform 23,0,0,00:00 - 01:00,00:00,01:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:00
Dj Boring,Thursday,Stonebridge Bar,42,18,00:00 - 01:30,00:00,01:30,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:30
Slicknbobby,Thursday,Strummerville,48,12,00:00 - 00:50,00:00,00:50,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 00:50
A.K.D.,Thursday,The Bandstand,56,38,00:00 - 01:00,00:00,01:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:00
Los Dedos,Thursday,The Rocket Lounge,64,16,00:00 - 01:00,00:00,01:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:00
Grove,Thursday,The Rum Shack,0,0,00:00 - 00:30,00:00,00:30,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 00:30
Nathan X,Thursday,The Salon Carousel,0,0,00:00 - 01:00,00:00,01:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:00
Purina Alpha + Mica,Thursday,The Sistxrhood,0,0,00:00 - 01:00,00:00,01:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 01:00
Kevin & Perry Ibiza Rave,Thursday,Village Inn,0,0,00:00 - 02:00,00:00,02:00,28/06/2024,28/06/2024,27/06/2024 00:00,28/06/2024 02:00
Leather Lungs + Master Reblasters,Thursday,Sensation Seekers Stage,0,0,00:05 - 00:50,00:05,00:50,28/06/2024,28/06/2024,27/06/2024 00:05,28/06/2024 00:50
Oppidan,Thursday,Blind Tiger,0,0,00:15 - 01:00,00:15,01:00,28/06/2024,28/06/2024,27/06/2024 00:15,28/06/2024 01:00
Chicha Morada,Thursday,Peace Stage,0,0,00:15 - 00:45,00:15,00:45,28/06/2024,28/06/2024,27/06/2024 00:15,28/06/2024 00:45
Das Brass,Thursday,West Holts Bar,59,29,00:20 - 01:20,00:20,01:20,28/06/2024,28/06/2024,27/06/2024 00:20,28/06/2024 01:20
Dresden [Ivan Smagghe & Manfredas],Thursday,Assembly,40,42,00:30 - 02:00,00:30,02:00,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 02:00
Phil Hartnoll(Orbital) B2B Conradical,Thursday,Bimble Inn,41,16,00:30 - 03:00,00:30,03:00,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 03:00
Shy One,Thursday,Glade,51,29,00:30 - 02:00,00:30,02:00,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 02:00
Massacre,Thursday,Kinetic,0,0,00:30 - 01:30,00:30,01:30,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 01:30
Trigg3R,Thursday,Mandala Stage,0,0,00:30 - 01:30,00:30,01:30,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 01:30
Booty Bass X Popola: Ivicore X Mc Fedzilla X Mc La Musica,Thursday,Nomad,0,0,00:30 - 01:00,00:30,01:00,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 01:00
Abigail 18,Thursday,Pilton Palais Cinema,64,36,00:30 - 02:00,00:30,02:00,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 02:00
Daisy Doris May,Thursday,Scissors,42,21,00:30 - 00:45,00:30,00:45,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 00:45
Greentea Selecta,Thursday,The Rum Shack,0,0,00:30 - 02:00,00:30,02:00,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 02:00
"Uncommon Records Takeover: Frd, Jimbitch, Katalyst & My-R",Thursday,The Temple,0,0,00:30 - 02:00,00:30,02:00,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 02:00
Musspell,Thursday,Toad Hall,0,0,00:30 - 01:30,00:30,01:30,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 01:30
2Fox (Dj Set),Thursday,Wishing Well,42,20,00:30 - 01:30,00:30,01:30,28/06/2024,28/06/2024,27/06/2024 00:30,28/06/2024 01:30
Raz And Afla,Thursday,Peace Stage,0,0,00:45 - 01:30,00:45,01:30,28/06/2024,28/06/2024,27/06/2024 00:45,28/06/2024 01:30
Mela Sounds,Thursday,Scissors,42,21,00:45 - 01:45,00:45,01:45,28/06/2024,28/06/2024,27/06/2024 00:45,28/06/2024 01:45
Youth,Thursday,Tree Stage,44,51,00:50 - 01:40,00:50,01:40,28/06/2024,28/06/2024,27/06/2024 00:50,28/06/2024 01:40
Pxssy Palace,Thursday,Arrivals,0,0,01:00 - 02:00,01:00,02:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 02:00
Aæe & Friends,Thursday,Babylon Uprising,0,0,01:00 - 02:45,01:00,02:45,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 02:45
Gardna & Friends,Thursday,Blind Tiger,0,0,01:00 - 01:45,01:00,01:45,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 01:45
Ahadadream B2B Nikki Nair B2B Raji Rags [Dialled In Takeover],Thursday,Lonely Hearts Club,44,41,01:00 - 03:00,01:00,03:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 03:00
Buffos Wake,Thursday,Lunched Out Lizards,0,0,01:00 - 02:00,01:00,02:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 02:00
Booty Bass X Popola: Ngaio,Thursday,Nomad,0,0,01:00 - 01:30,01:00,01:30,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 01:30
The Carry Nation,Thursday,Nyc Downlow,0,0,01:00 - 03:00,01:00,03:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 03:00
Brighter Days Family,Thursday,Platform 23,0,0,01:00 - 03:00,01:00,03:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 03:00
Job Jobse,Thursday,San Remo,45,47,01:00 - 03:00,01:00,03:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 03:00
Joei Supernova,Thursday,Strummerville,48,12,01:00 - 03:00,01:00,03:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 03:00
Greg Belson'S Divine Disco,Thursday,The Meatrack,0,0,01:00 - 03:00,01:00,03:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 03:00
(The) Us,Thursday,The Rocket Lounge,64,16,01:00 - 02:00,01:00,02:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 02:00
Oko,Thursday,The Salon Carousel,0,0,01:00 - 02:00,01:00,02:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 02:00
Tamboi,Thursday,The Sistxrhood,0,0,01:00 - 02:00,01:00,02:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 02:00
Russell Betts,Thursday,The Taphouse,0,0,01:00 - 03:00,01:00,03:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 03:00
Glowbros,Thursday,Walkabouts,60,33,01:00 - 03:00,01:00,03:00,28/06/2024,28/06/2024,27/06/2024 01:00,28/06/2024 03:00
Wheel Of Four Tunes,Thursday,Sensation Seekers Stage,0,0,01:05 - 02:05,01:05,02:05,28/06/2024,28/06/2024,27/06/2024 01:05,28/06/2024 02:05
Iicon Av:3D,Thursday,Iicon,66,21,01:15 - 01:30,01:15,01:30,28/06/2024,28/06/2024,27/06/2024 01:15,28/06/2024 01:30
Russ Ryan & Mo Fingaz,Thursday,West Holts Bar,59,29,01:20 - 03:00,01:20,03:00,28/06/2024,28/06/2024,27/06/2024 01:20,28/06/2024 03:00
Martha,Thursday,Bbc Music Introducing,45,44,01:30 - 02:30,01:30,02:30,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 02:30
Noble & Heath,Thursday,Deluxe Diner,64,17,01:30 - 03:00,01:30,03:00,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 03:00
Heidi,Thursday,Genosys,0,0,01:30 - 03:00,01:30,03:00,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 03:00
Yung Singh,Thursday,Greenpeace,55,26,01:30 - 03:00,01:30,03:00,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 03:00
Carista,Thursday,Iicon,66,21,01:30 - 03:00,01:30,03:00,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 03:00
Dj Shorty & Mister Lees,Thursday,Kinetic,0,0,01:30 - 03:00,01:30,03:00,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 03:00
Dove,Thursday,Levels,42,44,01:30 - 03:00,01:30,03:00,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 03:00
Booty Bass X Popola: Benzo,Thursday,Nomad,0,0,01:30 - 02:00,01:30,02:00,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 02:00
Fizzy Gillespie,Thursday,Peace Stage,0,0,01:30 - 02:00,01:30,02:00,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 02:00
Sally C,Thursday,Stonebridge Bar,42,18,01:30 - 03:00,01:30,03:00,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 03:00
Bryte,Thursday,Wishing Well,42,20,01:30 - 02:15,01:30,02:15,28/06/2024,28/06/2024,27/06/2024 01:30,28/06/2024 02:15
Dj Rap,Thursday,Glade Dome,49,29,01:40 - 02:55,01:40,02:55,28/06/2024,28/06/2024,27/06/2024 01:40,28/06/2024 02:55
Steve Hillage & Miquette Giraudy Performing Rainbow Dome Musick,Thursday,Tree Stage,44,51,01:40 - 02:55,01:40,02:55,28/06/2024,28/06/2024,27/06/2024 01:40,28/06/2024 02:55
Emily Makis & Hi Phi,Thursday,Blind Tiger,0,0,01:45 - 02:15,01:45,02:15,28/06/2024,28/06/2024,27/06/2024 01:45,28/06/2024 02:15
He.She.They. Presents Fancy Shews! B2B Maze & Masters,Thursday,Scissors,42,21,01:45 - 03:00,01:45,03:00,28/06/2024,28/06/2024,27/06/2024 01:45,28/06/2024 03:00
Thempress,Thursday,Arrivals,0,0,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
Decius [Live],Thursday,Assembly,40,42,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
Leaf (31 Recordings),Thursday,Cornish Arms,0,0,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
Miss Mash,Thursday,Mez Yard,0,0,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
Booty Bass X Popola: B2B,Thursday,Nomad,0,0,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
Fat Dog,Thursday,Peace Stage,0,0,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
The Trojans,Thursday,The Rocket Lounge,64,16,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
Rosa Pistola,Thursday,The Rum Shack,0,0,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
Soz Lad,Thursday,The Salon Carousel,0,0,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
Dj Dakilai,Thursday,The Sistxrhood,0,0,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
[Ivy],Thursday,The Temple,0,0,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
Mauvey,Thursday,Toad Hall,0,0,02:00 - 03:00,02:00,03:00,28/06/2024,28/06/2024,27/06/2024 02:00,28/06/2024 03:00
Pola & Bryson,Thursday,Blind Tiger,0,0,02:15 - 03:00,02:15,03:00,28/06/2024,28/06/2024,27/06/2024 02:15,28/06/2024 03:00
Regan (Dj Set),Thursday,Wishing Well,42,20,02:15 - 03:00,02:15,03:00,28/06/2024,28/06/2024,27/06/2024 02:15,28/06/2024 03:00
K Motionz,Thursday,Glade Dome,49,29,02:25 - 01:40,02:25,01:40,28/06/2024,28/06/2024,27/06/2024 02:25,28/06/2024 01:40
Yoga Like Water With Dan Peppiatt,Thursday,Humblewell Active Platform,42,21,08:30 - 09:30,08:30,09:30,27/06/2024,27/06/2024,27/06/2024 08:30,27/06/2024 09:30
Shakti Shake With Dina Cohen,Thursday,Humblewell Retreat Yurt,42,21,08:45 - 09:30,08:45,09:30,27/06/2024,27/06/2024,27/06/2024 08:45,27/06/2024 09:30
Improv Voice Circle With Leti,Thursday,Humblewell Active Platform,42,21,09:45 - 10:45,09:45,10:45,27/06/2024,27/06/2024,27/06/2024 09:45,27/06/2024 10:45
Crystal Singing Bowls With Yogic Sound,Thursday,Humblewell Retreat Yurt,42,21,09:45 - 10:15,09:45,10:15,27/06/2024,27/06/2024,27/06/2024 09:45,27/06/2024 10:15
Nipsy,Thursday,Cornish Arms,0,0,10:00 - 11:00,10:00,11:00,27/06/2024,27/06/2024,27/06/2024 10:00,27/06/2024 11:00
Ravers 2 Runners,Thursday,Greenpeace,55,26,10:00 - 10:15,10:00,10:15,27/06/2024,27/06/2024,27/06/2024 10:00,27/06/2024 10:15
Activist Intersection,Thursday,Greenpeace (Beam),54,26,10:00 - 10:30,10:00,10:30,27/06/2024,27/06/2024,27/06/2024 10:00,27/06/2024 10:30
Room Service,Thursday,San Remo,45,47,10:00 - 12:00,10:00,12:00,27/06/2024,27/06/2024,27/06/2024 10:00,27/06/2024 12:00
Climate Justice Means Migrant Justice - Tyrone Scott,Thursday,Speakers Forum,0,0,10:00 - 11:00,10:00,11:00,27/06/2024,27/06/2024,27/06/2024 10:00,27/06/2024 11:00
Arctic 30: On Thin Ice Putin Vs Greenpeace,Thursday,Greenpeace (Beam),54,26,10:30 - 11:30,10:30,11:30,27/06/2024,27/06/2024,27/06/2024 10:30,27/06/2024 11:30
Heart Coherence - The Breath That Connects You To Life,Thursday,Humblewell Retreat Yurt,42,21,10:30 - 12:00,10:30,12:00,27/06/2024,27/06/2024,27/06/2024 10:30,27/06/2024 12:00
Sounds Of Science Dj Set,Thursday,Laboratory Stage,0,0,10:30 - 11:00,10:30,11:00,27/06/2024,27/06/2024,27/06/2024 10:30,27/06/2024 11:00
Jersey Girls,Thursday,Walkabouts,60,33,10:30 - 11:00,10:30,11:00,27/06/2024,27/06/2024,27/06/2024 10:30,27/06/2024 11:00
Rishi Gordon,Thursday,Walkabouts,60,33,10:45 - 11:30,10:45,11:30,27/06/2024,27/06/2024,27/06/2024 10:45,27/06/2024 11:30
The Fabularium - Carnival Of Animals,Thursday,Walkabouts,60,33,10:45 - 11:30,10:45,11:30,27/06/2024,27/06/2024,27/06/2024 10:45,27/06/2024 11:30
The Sky At Day,Thursday,Walkabouts,60,33,10:50 - 11:35,10:50,11:35,27/06/2024,27/06/2024,27/06/2024 10:50,27/06/2024 11:35
Films,Thursday,Atchin Tan,0,0,11:00 - 12:30,11:00,12:30,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 12:30
Jo Bucket,Thursday,Carhenge,58,36,11:00 - 12:00,11:00,12:00,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 12:00
Lazy Technician,Thursday,Cornish Arms,0,0,11:00 - 12:00,11:00,12:00,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 12:00
Acoustic Open Mic,Thursday,Croissant Neuf Bandstand,55,21,11:00 - 11:45,11:00,11:45,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 11:45
Om And Bass Yoga With Dina Cohen,Thursday,Humblewell Active Platform,42,21,11:00 - 11:50,11:00,11:50,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 11:50
Welcome Party,Thursday,Meeting Place Bar,0,0,11:00 - 13:00,11:00,13:00,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 13:00
Climate Emergency Centres - Phoenix,Thursday,Speakers Forum,0,0,11:00 - 12:00,11:00,12:00,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 12:00
Common Uprising! The Procession,Thursday,Temple Uprising,0,0,11:00 - 12:45,11:00,12:45,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 12:45
Joe Wicks,Thursday,The Gateway,0,0,11:00 - 11:45,11:00,11:45,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 11:45
Mindful Movement With Laurie Clothier,Thursday,Toad Hall,0,0,11:00 - 12:00,11:00,12:00,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 12:00
Entity,Thursday,Tree Stage,44,51,11:00 - 11:30,11:00,11:30,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 11:30
Magical Musical Time Machine,Thursday,Walkabouts,60,33,11:00 - 11:45,11:00,11:45,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 11:45
The Family Tree,Thursday,Walkabouts,60,33,11:00 - 11:45,11:00,11:45,27/06/2024,27/06/2024,27/06/2024 11:00,27/06/2024 11:45
Giant Seagulls,Thursday,Walkabouts,60,33,11:05 - 11:50,11:05,11:50,27/06/2024,27/06/2024,27/06/2024 11:05,27/06/2024 11:50
The Tea Ladies On Tour,Thursday,Walkabouts,60,33,11:05 - 11:50,11:05,11:50,27/06/2024,27/06/2024,27/06/2024 11:05,27/06/2024 11:50
Dapper Chaps,Thursday,Walkabouts,60,33,11:10 - 11:55,11:10,11:55,27/06/2024,27/06/2024,27/06/2024 11:10,27/06/2024 11:55
Ravers 2 Runners (Warm Down Party),Thursday,Greenpeace,55,26,11:15 - 11:45,11:15,11:45,27/06/2024,27/06/2024,27/06/2024 11:15,27/06/2024 11:45
Science-Based Meditation,Thursday,Laboratory Stage,0,0,11:15 - 11:45,11:15,11:45,27/06/2024,27/06/2024,27/06/2024 11:15,27/06/2024 11:45
The Buzzing Bees,Thursday,Walkabouts,60,33,11:15 - 12:15,11:15,12:15,27/06/2024,27/06/2024,27/06/2024 11:15,27/06/2024 12:15
Tba,Thursday,Mandala Stage,0,0,11:30 - 12:30,11:30,12:30,27/06/2024,27/06/2024,27/06/2024 11:30,27/06/2024 12:30
Jan Van Ijken & Entity - Planktonium,Thursday,Tree Stage,44,51,11:30 - 12:10,11:30,12:10,27/06/2024,27/06/2024,27/06/2024 11:30,27/06/2024 12:10
Ministry Of Happy,Thursday,Walkabouts,60,33,11:30 - 12:15,11:30,12:15,27/06/2024,27/06/2024,27/06/2024 11:30,27/06/2024 12:15
Natural Diversions,Thursday,Walkabouts,60,33,11:30 - 12:15,11:30,12:15,27/06/2024,27/06/2024,27/06/2024 11:30,27/06/2024 12:15
Fairly Fresh Fish Co,Thursday,Walkabouts,60,33,11:40 - 12:25,11:40,12:25,27/06/2024,27/06/2024,27/06/2024 11:40,27/06/2024 12:25
Space Cadets,Thursday,Walkabouts,60,33,11:45 - 12:30,11:45,12:30,27/06/2024,27/06/2024,27/06/2024 11:45,27/06/2024 12:30
Jack Francis,Thursday,The Hive,0,0,11:50 - 12:35,11:50,12:35,27/06/2024,27/06/2024,27/06/2024 11:50,27/06/2024 12:35
Groovy Guy,Thursday,A Little More Sensation,0,0,12:00 - 12:30,12:00,12:30,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:30
Meare Gentlemans Sports & Leisure,Thursday,Babylon Uprising,0,0,12:00 - 15:00,12:00,15:00,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 15:00
Open,Thursday,Bimble Inn,41,16,12:00 - 13:30,12:00,13:30,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 13:30
Kray-Z Legz,Thursday,Blind Tiger,0,0,12:00 - 12:45,12:00,12:45,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:45
Stone Jets,Thursday,Bread And Roses,0,0,12:00 - 12:40,12:00,12:40,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:40
Lewis,Thursday,Cornish Arms,0,0,12:00 - 12:10,12:00,12:10,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:10
Josh Roberts,Thursday,Croissant Neuf Bandstand,55,21,12:00 - 12:00,12:00,12:00,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:00
Activism Is Not A Crime,Thursday,Greenpeace (Beam),54,26,12:00 - 12:30,12:00,12:30,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:30
Easy Tai Chi With Joe May,Thursday,Humblewell Active Platform,42,21,12:00 - 12:45,12:00,12:45,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:45
Live Demo - Rocket Science!,Thursday,Laboratory Stage,0,0,12:00 - 12:30,12:00,12:30,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:30
Wasted Space & Manuel Darquart,Thursday,San Remo,45,47,12:00 - 13:30,12:00,13:30,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 13:30
How Would The Suffragettes Stop Banks Lending To Oil Companies ? - Sophie Cowen & Clare Farrell,Thursday,Speakers Forum,0,0,12:00 - 13:00,12:00,13:00,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 13:00
Dennis Just Dennis,Thursday,Strummerville,48,12,12:00 - 12:30,12:00,12:30,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:30
Go Bananas,Thursday,The Glebe,60,33,12:00 - 12:30,12:00,12:30,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:30
Hilby,Thursday,The Pavement,0,0,12:00 - 12:30,12:00,12:30,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:30
The Very Best Of Tommy Cooper,Thursday,Walkabouts,60,33,12:00 - 12:45,12:00,12:45,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 12:45
Worldroots Acapella,Thursday,Walkabouts,60,33,12:00 - 14:00,12:00,14:00,27/06/2024,27/06/2024,27/06/2024 12:00,27/06/2024 14:00
Land Of The Giants,Thursday,The Gateway,0,0,12:05 - 12:35,12:05,12:35,27/06/2024,27/06/2024,27/06/2024 12:05,27/06/2024 12:35
Oliver Sudden,Thursday,Cornish Arms,0,0,12:10 - 13:00,12:10,13:00,27/06/2024,27/06/2024,27/06/2024 12:10,27/06/2024 13:00
Mat Collishaw - Even To The End,Thursday,Tree Stage,44,51,12:10 - 12:30,12:10,12:30,27/06/2024,27/06/2024,27/06/2024 12:10,27/06/2024 12:30
Charlotte May,Thursday,Crooner'S Corner,0,0,12:15 - 13:00,12:15,13:00,27/06/2024,27/06/2024,27/06/2024 12:15,27/06/2024 13:00
Replay Music Uke Workshop,Thursday,Toad Hall,0,0,12:15 - 13:15,12:15,13:15,27/06/2024,27/06/2024,27/06/2024 12:15,27/06/2024 13:15
Disco Robot Girlz,Thursday,Walkabouts,60,33,12:15 - 13:00,12:15,13:00,27/06/2024,27/06/2024,27/06/2024 12:15,27/06/2024 13:00
The Natural Theatre Company,Thursday,Walkabouts,60,33,12:15 - 13:00,12:15,13:00,27/06/2024,27/06/2024,27/06/2024 12:15,27/06/2024 13:00
Blockbuster Factory,Thursday,Walkabouts,60,33,12:15 - 13:10,12:15,13:10,27/06/2024,27/06/2024,27/06/2024 12:15,27/06/2024 13:10
The Flying Seagull Project,Thursday,Kidzfield Big Top,0,0,12:20 - 13:00,12:20,13:00,27/06/2024,27/06/2024,27/06/2024 12:20,27/06/2024 13:00
"John Doe, Talk: Life With The Horses On The Road",Thursday,Atchin Tan,0,0,12:30 - 13:15,12:30,13:15,27/06/2024,27/06/2024,27/06/2024 12:30,27/06/2024 13:15
Fulu Miziki,Thursday,Greenpeace,55,26,12:30 - 13:15,12:30,13:15,27/06/2024,27/06/2024,27/06/2024 12:30,27/06/2024 13:15
Shamanic Drum Circle With Tracy Turnell,Thursday,Humblewell Retreat Yurt,42,21,12:30 - 13:30,12:30,13:30,27/06/2024,27/06/2024,27/06/2024 12:30,27/06/2024 13:30
Novara Media Presents: Radical Connections,Thursday,Nomad,0,0,12:30 - 13:30,12:30,13:30,27/06/2024,27/06/2024,27/06/2024 12:30,27/06/2024 13:30
Merlin Sheldrake,Thursday,Tree Stage,44,51,12:30 - 13:15,12:30,13:15,27/06/2024,27/06/2024,27/06/2024 12:30,27/06/2024 13:15
The Fabularium - Carnival Of Animals,Thursday,Walkabouts,60,33,12:30 - 13:15,12:30,13:15,27/06/2024,27/06/2024,27/06/2024 12:30,27/06/2024 13:15
Yann Elvis,Thursday,A Little More Sensation,0,0,12:35 - 13:05,12:35,13:05,27/06/2024,27/06/2024,27/06/2024 12:35,27/06/2024 13:05
Jack Defrost - Traceworks Dance,Thursday,The Glebe,60,33,12:35 - 12:50,12:35,12:50,27/06/2024,27/06/2024,27/06/2024 12:35,27/06/2024 12:50
Tony & Ray,Thursday,The Pavement,0,0,12:35 - 12:50,12:35,12:50,27/06/2024,27/06/2024,27/06/2024 12:35,27/06/2024 12:50
Old Time Rags,Thursday,The Gateway,0,0,12:40 - 13:10,12:40,13:10,27/06/2024,27/06/2024,27/06/2024 12:40,27/06/2024 13:10
Ki Dub,Thursday,Blind Tiger,0,0,12:45 - 13:30,12:45,13:30,27/06/2024,27/06/2024,27/06/2024 12:45,27/06/2024 13:30
Chloe Leigh,Thursday,Croissant Neuf Bandstand,55,21,12:45 - 13:15,12:45,13:15,27/06/2024,27/06/2024,27/06/2024 12:45,27/06/2024 13:15
Science Shorts - The Science And Magic Of Medicinal Mushrooms,Thursday,Laboratory Stage,0,0,12:45 - 13:15,12:45,13:15,27/06/2024,27/06/2024,27/06/2024 12:45,27/06/2024 13:15
Route 500,Thursday,The Hive,0,0,12:45 - 13:25,12:45,13:25,27/06/2024,27/06/2024,27/06/2024 12:45,27/06/2024 13:25
The Bigheads,Thursday,Walkabouts,60,33,12:45 - 13:25,12:45,13:25,27/06/2024,27/06/2024,27/06/2024 12:45,27/06/2024 13:25
Gnomes,Thursday,Walkabouts,60,33,12:45 - 13:30,12:45,13:30,27/06/2024,27/06/2024,27/06/2024 12:45,27/06/2024 13:30
The Sky At Day,Thursday,Walkabouts,60,33,12:50 - 13:35,12:50,13:35,27/06/2024,27/06/2024,27/06/2024 12:50,27/06/2024 13:35
Grant Goldie,Thursday,The Glebe,60,33,12:55 - 13:25,12:55,13:25,27/06/2024,27/06/2024,27/06/2024 12:55,27/06/2024 13:25
Mr Peewee The Drumming Puppet,Thursday,The Pavement,0,0,12:55 - 13:25,12:55,13:25,27/06/2024,27/06/2024,27/06/2024 12:55,27/06/2024 13:25
Cocoa Butter Club Cabaret,Thursday,10 Aces,0,0,13:00 - 13:30,13:00,13:30,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 13:30
Mary Middlefield,Thursday,Bbc Music Introducing,45,44,13:00 - 13:30,13:00,13:30,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 13:30
Aine Dean,Thursday,Bread And Roses,0,0,13:00 - 13:40,13:00,13:40,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 13:40
Fulu Miziki,Thursday,Carhenge,58,36,13:00 - 14:00,13:00,14:00,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 14:00
Curt & Andy,Thursday,Cornish Arms,0,0,13:00 - 15:00,13:00,15:00,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 15:00
Paper Dragon,Thursday,Glade Dome,49,29,13:00 - 14:00,13:00,14:00,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 14:00
Dance Class: Salsa,Thursday,Glasto Latino,58,27,13:00 - 14:00,13:00,14:00,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 14:00
Actions Skills Workshops,Thursday,Greenpeace (Beam),54,26,13:00 - 15:00,13:00,15:00,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 15:00
African Dance With Penny Avery,Thursday,Humblewell Active Platform,42,21,13:00 - 13:30,13:00,13:30,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 13:30
Andrew Maxwell Morris,Thursday,Mandala Stage,0,0,13:00 - 14:00,13:00,14:00,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 14:00
Hitide,Thursday,Meeting Place Bar,0,0,13:00 - 17:00,13:00,17:00,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 17:00
The Garfield Movie U,Thursday,Pilton Palais Cinema,64,36,13:00 - 14:40,13:00,14:40,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 14:40
Aviation Flying In The Face Of Climate Science - Alice Larkin,Thursday,Speakers Forum,0,0,13:00 - 14:00,13:00,14:00,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 14:00
Eats Everything And Pokes,Thursday,Stonebridge Bar,42,18,13:00 - 14:00,13:00,14:00,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 14:00
Rosie Aldridge,Thursday,Strummerville,48,12,13:00 - 13:40,13:00,13:40,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 13:40
"The Right Time For Revolution, From Putney To Peru With Ulula Roots",Thursday,Temple Uprising,0,0,13:00 - 13:45,13:00,13:45,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 13:45
Jersey Girls,Thursday,Walkabouts,60,33,13:00 - 13:30,13:00,13:30,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 13:30
Steve Faulkner,Thursday,Walkabouts,60,33,13:00 - 13:45,13:00,13:45,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 13:45
Taliesin,Thursday,Wishing Well,42,20,13:00 - 13:45,13:00,13:45,27/06/2024,27/06/2024,27/06/2024 13:00,27/06/2024 13:45
Freddieno Show,Thursday,A Little More Sensation,0,0,13:10 - 13:40,13:10,13:40,27/06/2024,27/06/2024,27/06/2024 13:10,27/06/2024 13:40
Martin Furey: Music,Thursday,Atchin Tan,0,0,13:15 - 14:00,13:15,14:00,27/06/2024,27/06/2024,27/06/2024 13:15,27/06/2024 14:00
Fladam Presents: Green Fingers,Thursday,Kidzfield Big Top,0,0,13:15 - 14:10,13:15,14:10,27/06/2024,27/06/2024,27/06/2024 13:15,27/06/2024 14:10
"Flame Of Hope: 'Hope Is An Action - Israelis And Palestinians Unite': Danielle Bett (Peace Activist - Yachad), Hamze Awawde (Conflict Resolution Expert - Hands Of Peace), Hiba Qasas (Peacebuilder, Development Leader - Principles For Peace Foundation), Maoz Inon (Peace Entrepreneur, Ted Speaker), Hosted By Layla Moran (Mp - Lib Dem)",Thursday,The Information,41,41,13:15 - 14:15,13:15,14:15,27/06/2024,27/06/2024,27/06/2024 13:15,27/06/2024 14:15
Mixmaster Morris,Thursday,Tree Stage,44,51,13:15 - 14:15,13:15,14:15,27/06/2024,27/06/2024,27/06/2024 13:15,27/06/2024 14:15
Paul Lambourne,Thursday,Crooner'S Corner,0,0,13:20 - 13:50,13:20,13:50,27/06/2024,27/06/2024,27/06/2024 13:20,27/06/2024 13:50
Otto And Astrid - Die Roten Punkte,Thursday,The Gateway,0,0,13:25 - 14:10,13:25,14:10,27/06/2024,27/06/2024,27/06/2024 13:25,27/06/2024 14:10
Cardinal Sound,Thursday,Blind Tiger,0,0,13:30 - 14:15,13:30,14:15,27/06/2024,27/06/2024,27/06/2024 13:30,27/06/2024 14:15
Josh Hazelden,Thursday,Croissant Neuf Bandstand,55,21,13:30 - 14:00,13:30,14:00,27/06/2024,27/06/2024,27/06/2024 13:30,27/06/2024 14:00
Gilan,Thursday,Laboratory Stage,0,0,13:30 - 14:00,13:30,14:00,27/06/2024,27/06/2024,27/06/2024 13:30,27/06/2024 14:00
Danny Fucking Price Presents: The Anarchy Assembly,Thursday,Nomad,0,0,13:30 - 16:00,13:30,16:00,27/06/2024,27/06/2024,27/06/2024 13:30,27/06/2024 16:00
Ruby Savage,Thursday,San Remo,45,47,13:30 - 15:00,13:30,15:00,27/06/2024,27/06/2024,27/06/2024 13:30,27/06/2024 15:00
"Talk: Alexis Lee (Style Me Sunday), Towards Collectivism",Thursday,Scissors,42,21,13:30 - 14:15,13:30,14:15,27/06/2024,27/06/2024,27/06/2024 13:30,27/06/2024 14:15
A Day At The Beach,Thursday,The Glebe,60,33,13:30 - 14:00,13:30,14:00,27/06/2024,27/06/2024,27/06/2024 13:30,27/06/2024 14:00
Kiki Bittovabitsch,Thursday,The Pavement,0,0,13:30 - 14:00,13:30,14:00,27/06/2024,27/06/2024,27/06/2024 13:30,27/06/2024 14:00
Cerian,Thursday,Toad Hall,0,0,13:30 - 14:15,13:30,14:15,27/06/2024,27/06/2024,27/06/2024 13:30,27/06/2024 14:15
The Jukeboxes,Thursday,Walkabouts,60,33,13:30 - 15:00,13:30,15:00,27/06/2024,27/06/2024,27/06/2024 13:30,27/06/2024 15:00
Jeanie White,Thursday,The Hive,0,0,13:35 - 14:05,13:35,14:05,27/06/2024,27/06/2024,27/06/2024 13:35,27/06/2024 14:05
Rezon8 Artist Showcase,Thursday,10 Aces,0,0,13:40 - 14:10,13:40,14:10,27/06/2024,27/06/2024,27/06/2024 13:40,27/06/2024 14:10
Rishi Gordon,Thursday,Walkabouts,60,33,13:40 - 14:25,13:40,14:25,27/06/2024,27/06/2024,27/06/2024 13:40,27/06/2024 14:25
The Family Tree,Thursday,Walkabouts,60,33,13:40 - 14:25,13:40,14:25,27/06/2024,27/06/2024,27/06/2024 13:40,27/06/2024 14:25
Tba,Thursday,A Little More Sensation,0,0,13:45 - 14:15,13:45,14:15,27/06/2024,27/06/2024,27/06/2024 13:45,27/06/2024 14:15
Arxx,Thursday,Greenpeace,55,26,13:45 - 14:30,13:45,14:30,27/06/2024,27/06/2024,27/06/2024 13:45,27/06/2024 14:30
African Dance With Penny Avery,Thursday,Humblewell Active Platform,42,21,13:45 - 14:15,13:45,14:15,27/06/2024,27/06/2024,27/06/2024 13:45,27/06/2024 14:15
Life Drawing With Fra Beecher,Thursday,Humblewell Retreat Yurt,42,21,13:45 - 14:45,13:45,14:45,27/06/2024,27/06/2024,27/06/2024 13:45,27/06/2024 14:45
Enchanted Flower Show Globe,Thursday,Walkabouts,60,33,13:45 - 14:30,13:45,14:30,27/06/2024,27/06/2024,27/06/2024 13:45,27/06/2024 14:30
The Buzzing Bees,Thursday,Walkabouts,60,33,13:45 - 14:45,13:45,14:45,27/06/2024,27/06/2024,27/06/2024 13:45,27/06/2024 14:45
Team Pickles (Dj Set),Thursday,Wishing Well,42,20,13:45 - 14:45,13:45,14:45,27/06/2024,27/06/2024,27/06/2024 13:45,27/06/2024 14:45
Scary & Spooky Skeletons,Thursday,Walkabouts,60,33,13:50 - 14:35,13:50,14:35,27/06/2024,27/06/2024,27/06/2024 13:50,27/06/2024 14:35
Cousin Kula,Thursday,Bbc Music Introducing,45,44,14:00 - 14:30,14:00,14:30,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 14:30
Thrill Collins,Thursday,Bread And Roses,0,0,14:00 - 14:40,14:00,14:40,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 14:40
The Nextmen Ft Kiko Bun,Thursday,Glade Dome,49,29,14:00 - 15:30,14:00,15:30,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 15:30
Dance Class: Samba,Thursday,Glasto Latino,58,27,14:00 - 15:00,14:00,15:00,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 15:00
Renewable Energy - Everything In 55 Mins - Fergal Mcentee,Thursday,Speakers Forum,0,0,14:00 - 15:00,14:00,15:00,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 15:00
Lens,Thursday,Stonebridge Bar,42,18,14:00 - 15:00,14:00,15:00,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 15:00
Calum Bowie,Thursday,Strummerville,48,12,14:00 - 14:40,14:00,14:40,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 14:40
"Tupac, The Condor And The Eagle - Storytelling From Peru With Kary Stewart",Thursday,Temple Uprising,0,0,14:00 - 14:30,14:00,14:30,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 14:30
Hodmadoddery,Thursday,The Bandstand,56,38,14:00 - 15:00,14:00,15:00,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 15:00
Notting Hill St Pauls Carnival,Thursday,The Bug,41,25,14:00 - 15:30,14:00,15:30,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 15:30
Ittman,Thursday,Village Inn,0,0,14:00 - 16:00,14:00,16:00,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 16:00
Bowjangles,Thursday,Walkabouts,60,33,14:00 - 15:00,14:00,15:00,27/06/2024,27/06/2024,27/06/2024 14:00,27/06/2024 15:00
Tony And Ray,Thursday,The Glebe,60,33,14:05 - 14:20,14:05,14:20,27/06/2024,27/06/2024,27/06/2024 14:05,27/06/2024 14:20
Rob Roy Collins,Thursday,The Pavement,0,0,14:05 - 14:35,14:05,14:35,27/06/2024,27/06/2024,27/06/2024 14:05,27/06/2024 14:35
The Suitcase Escape Game,Thursday,Walkabouts,60,33,14:05 - 14:50,14:05,14:50,27/06/2024,27/06/2024,27/06/2024 14:05,27/06/2024 14:50
Gracie Barry Tait,Thursday,Crooner'S Corner,0,0,14:10 - 14:55,14:10,14:55,27/06/2024,27/06/2024,27/06/2024 14:10,27/06/2024 14:55
Rose Popay & Sidekick Saffy,Thursday,Walkabouts,60,33,14:10 - 14:55,14:10,14:55,27/06/2024,27/06/2024,27/06/2024 14:10,27/06/2024 14:55
Dealo Brown,Thursday,Blind Tiger,0,0,14:15 - 15:00,14:15,15:00,27/06/2024,27/06/2024,27/06/2024 14:15,27/06/2024 15:00
Izzie Derry,Thursday,Croissant Neuf Bandstand,55,21,14:15 - 14:45,14:15,14:45,27/06/2024,27/06/2024,27/06/2024 14:15,27/06/2024 14:45
Ai Vs. Nature (Q&A With Gordon Blair),Thursday,Laboratory Stage,0,0,14:15 - 14:45,14:15,14:45,27/06/2024,27/06/2024,27/06/2024 14:15,27/06/2024 14:45
E. M. Kane,Thursday,The Hive,0,0,14:15 - 15:00,14:15,15:00,27/06/2024,27/06/2024,27/06/2024 14:15,27/06/2024 15:00
Fish56Octagon Ambient Dj Set,Thursday,Tree Stage,44,51,14:15 - 15:15,14:15,15:15,27/06/2024,27/06/2024,27/06/2024 14:15,27/06/2024 15:15
Celestials,Thursday,Walkabouts,60,33,14:15 - 14:45,14:15,14:45,27/06/2024,27/06/2024,27/06/2024 14:15,27/06/2024 14:45
Disco Robot Girlz,Thursday,Walkabouts,60,33,14:15 - 15:00,14:15,15:00,27/06/2024,27/06/2024,27/06/2024 14:15,27/06/2024 15:00
Figs In Wigs - Astrology Bingo!,Thursday,10 Aces,0,0,14:20 - 15:20,14:20,15:20,27/06/2024,27/06/2024,27/06/2024 14:20,27/06/2024 15:20
Hilby,Thursday,A Little More Sensation,0,0,14:20 - 14:50,14:20,14:50,27/06/2024,27/06/2024,27/06/2024 14:20,27/06/2024 14:50
Lekiddo Lord Of The Lobsters,Thursday,The Gateway,0,0,14:20 - 14:50,14:20,14:50,27/06/2024,27/06/2024,27/06/2024 14:20,27/06/2024 14:50
Jack Defrost - Traceworks Dance,Thursday,The Glebe,60,33,14:25 - 14:40,14:25,14:40,27/06/2024,27/06/2024,27/06/2024 14:25,27/06/2024 14:40
Disco Fit With Helen Rooney,Thursday,Humblewell Active Platform,42,21,14:30 - 15:00,14:30,15:00,27/06/2024,27/06/2024,27/06/2024 14:30,27/06/2024 15:00
Bodger'S Badger,Thursday,Kidzfield Big Top,0,0,14:30 - 14:50,14:30,14:50,27/06/2024,27/06/2024,27/06/2024 14:30,27/06/2024 14:50
Ash Mandrake And Jenny Bliss,Thursday,Mandala Stage,0,0,14:30 - 15:30,14:30,15:30,27/06/2024,27/06/2024,27/06/2024 14:30,27/06/2024 15:30
"Team Love: Optimism As A Political Act: Zack Polanski (Deputy Leader - Green Party), Dave Harvey (Director - Team Love), Guest Tba, Hosted By Tba",Thursday,The Information,41,41,14:30 - 15:30,14:30,15:30,27/06/2024,27/06/2024,27/06/2024 14:30,27/06/2024 15:30
Magical Musical Time Machine,Thursday,Walkabouts,60,33,14:30 - 15:15,14:30,15:15,27/06/2024,27/06/2024,27/06/2024 14:30,27/06/2024 15:15
Venus,Thursday,The Pavement,0,0,14:40 - 15:10,14:40,15:10,27/06/2024,27/06/2024,27/06/2024 14:40,27/06/2024 15:10
Lee & You Band,Thursday,Toad Hall,0,0,14:40 - 15:25,14:40,15:25,27/06/2024,27/06/2024,27/06/2024 14:40,27/06/2024 15:25
The Acolyte,Thursday,Pilton Palais Cinema,64,36,14:45 - 16:30,14:45,16:30,27/06/2024,27/06/2024,27/06/2024 14:45,27/06/2024 16:30
"Talk: Ruby Rare, Queer Vulnerability",Thursday,Scissors,42,21,14:45 - 15:45,14:45,15:45,27/06/2024,27/06/2024,27/06/2024 14:45,27/06/2024 15:45
How The So-Called 'War On Drugs' Is A Barrier To Securing Climate Justice With Neil Woods And Clemmie James,Thursday,Temple Uprising,0,0,14:45 - 15:30,14:45,15:30,27/06/2024,27/06/2024,27/06/2024 14:45,27/06/2024 15:30
Groovy Guy,Thursday,The Glebe,60,33,14:45 - 15:15,14:45,15:15,27/06/2024,27/06/2024,27/06/2024 14:45,27/06/2024 15:15
The Bigheads,Thursday,Walkabouts,60,33,14:45 - 15:25,14:45,15:25,27/06/2024,27/06/2024,27/06/2024 14:45,27/06/2024 15:25
Natural Diversions,Thursday,Walkabouts,60,33,14:45 - 15:30,14:45,15:30,27/06/2024,27/06/2024,27/06/2024 14:45,27/06/2024 15:30
Caleb Kunle,Thursday,Wishing Well,42,20,14:45 - 15:45,14:45,15:45,27/06/2024,27/06/2024,27/06/2024 14:45,27/06/2024 15:45
Blip,Thursday,Walkabouts,60,33,14:50 - 15:35,14:50,15:35,27/06/2024,27/06/2024,27/06/2024 14:50,27/06/2024 15:35
Go Bananas,Thursday,A Little More Sensation,0,0,14:55 - 15:25,14:55,15:25,27/06/2024,27/06/2024,27/06/2024 14:55,27/06/2024 15:25
Village Cuts - Village Cuts Takeover,Thursday,Babylon Uprising,0,0,15:00 - 16:00,15:00,16:00,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 16:00
Sam Evans,Thursday,Bbc Music Introducing,45,44,15:00 - 15:30,15:00,15:30,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 15:30
John The Hat,Thursday,Blind Tiger,0,0,15:00 - 16:00,15:00,16:00,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 16:00
Twin Sun (Blendid Takeover),Thursday,Cornish Arms,0,0,15:00 - 17:00,15:00,17:00,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 17:00
Larabel,Thursday,Croissant Neuf Bandstand,55,21,15:00 - 15:45,15:00,15:45,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 15:45
Dance Class: Salsa,Thursday,Glasto Latino,58,27,15:00 - 16:00,15:00,16:00,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 16:00
Lambrini Girls,Thursday,Greenpeace,55,26,15:00 - 15:45,15:00,15:45,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 15:45
Laughter Yoga With Joe May,Thursday,Humblewell Retreat Yurt,42,21,15:00 - 16:00,15:00,16:00,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 16:00
Bbc Natural History Unit,Thursday,Laboratory Stage,0,0,15:00 - 15:45,15:00,15:45,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 15:45
Mal Webb & Kylie Morrigan,Thursday,Lunched Out Lizards,0,0,15:00 - 16:00,15:00,16:00,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 16:00
Cc:Disco!,Thursday,San Remo,45,47,15:00 - 17:00,15:00,17:00,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 17:00
Old Time Sailors,Thursday,Sensation Seekers Stage,0,0,15:00 - 16:00,15:00,16:00,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 16:00
Phones Filming For Change - Zoe Broughton,Thursday,Speakers Forum,0,0,15:00 - 16:00,15:00,16:00,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 16:00
Baggy Mondays,Thursday,Stonebridge Bar,42,18,15:00 - 16:30,15:00,16:30,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 16:30
Guise,Thursday,Strummerville,48,12,15:00 - 15:30,15:00,15:30,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 15:30
Atchin Tan,Thursday,The Gateway,0,0,15:00 - 15:40,15:00,15:40,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 15:40
Gliding Butterflies,Thursday,Walkabouts,60,33,15:00 - 15:45,15:00,15:45,27/06/2024,27/06/2024,27/06/2024 15:00,27/06/2024 15:45
Giant Seagulls,Thursday,Walkabouts,60,33,15:05 - 15:50,15:05,15:50,27/06/2024,27/06/2024,27/06/2024 15:05,27/06/2024 15:50
Laura London & Jake Francis,Thursday,Walkabouts,60,33,15:05 - 15:50,15:05,15:50,27/06/2024,27/06/2024,27/06/2024 15:05,27/06/2024 15:50
Daisy Veacock,Thursday,Bread And Roses,0,0,15:10 - 15:50,15:10,15:50,27/06/2024,27/06/2024,27/06/2024 15:10,27/06/2024 15:50
Roger Mcgough'S 'The Sound Collector',Thursday,Kidzfield Big Top,0,0,15:10 - 15:45,15:10,15:45,27/06/2024,27/06/2024,27/06/2024 15:10,27/06/2024 15:45
Dapper Chaps,Thursday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,27/06/2024,27/06/2024,27/06/2024 15:10,27/06/2024 15:55
Jack Thomson,Thursday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,27/06/2024,27/06/2024,27/06/2024 15:10,27/06/2024 15:55
The Very Best Of Tommy Cooper,Thursday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,27/06/2024,27/06/2024,27/06/2024 15:10,27/06/2024 15:55
Mama Tokus,Thursday,Crooner'S Corner,0,0,15:15 - 16:00,15:15,16:00,27/06/2024,27/06/2024,27/06/2024 15:15,27/06/2024 16:00
Hula Hoops With Helen Rooney,Thursday,Humblewell Active Platform,42,21,15:15 - 16:00,15:15,16:00,27/06/2024,27/06/2024,27/06/2024 15:15,27/06/2024 16:00
Michael Baker,Thursday,The Hive,0,0,15:15 - 16:00,15:15,16:00,27/06/2024,27/06/2024,27/06/2024 15:15,27/06/2024 16:00
Fraser Hooper,Thursday,The Pavement,0,0,15:15 - 15:45,15:15,15:45,27/06/2024,27/06/2024,27/06/2024 15:15,27/06/2024 15:45
Plaid Ambient Dj Set,Thursday,Tree Stage,44,51,15:15 - 16:30,15:15,16:30,27/06/2024,27/06/2024,27/06/2024 15:15,27/06/2024 16:30
The Natural Theatre Company,Thursday,Walkabouts,60,33,15:15 - 16:00,15:15,16:00,27/06/2024,27/06/2024,27/06/2024 15:15,27/06/2024 16:00
Beth Porter,Thursday,The Bandstand,56,38,15:20 - 16:00,15:20,16:00,27/06/2024,27/06/2024,27/06/2024 15:20,27/06/2024 16:00
Primary School Assembly Bangers,Thursday,The Glebe,60,33,15:20 - 15:50,15:20,15:50,27/06/2024,27/06/2024,27/06/2024 15:20,27/06/2024 15:50
The Wardens,Thursday,Walkabouts,60,33,15:20 - 15:50,15:20,15:50,27/06/2024,27/06/2024,27/06/2024 15:20,27/06/2024 15:50
Cash Cows,Thursday,10 Aces,0,0,15:30 - 16:15,15:30,16:15,27/06/2024,27/06/2024,27/06/2024 15:30,27/06/2024 16:15
Ballerinas,Thursday,A Little More Sensation,0,0,15:30 - 16:00,15:30,16:00,27/06/2024,27/06/2024,27/06/2024 15:30,27/06/2024 16:00
Trish Reilly: Music,Thursday,Atchin Tan,0,0,15:30 - 16:15,15:30,16:15,27/06/2024,27/06/2024,27/06/2024 15:30,27/06/2024 16:15
King Of The Beats,Thursday,Glade Dome,49,29,15:30 - 17:00,15:30,17:00,27/06/2024,27/06/2024,27/06/2024 15:30,27/06/2024 17:00
Fortuni And Fae,Thursday,Walkabouts,60,33,15:30 - 16:15,15:30,16:15,27/06/2024,27/06/2024,27/06/2024 15:30,27/06/2024 16:15
Meanderthals,Thursday,Walkabouts,60,33,15:30 - 16:15,15:30,16:15,27/06/2024,27/06/2024,27/06/2024 15:30,27/06/2024 16:15
Ministry Of Happy,Thursday,Walkabouts,60,33,15:30 - 16:15,15:30,16:15,27/06/2024,27/06/2024,27/06/2024 15:30,27/06/2024 16:15
Porij (Dj Set),Thursday,Greenpeace,55,26,15:45 - 16:55,15:45,16:55,27/06/2024,27/06/2024,27/06/2024 15:45,27/06/2024 16:55
Heard Collective,Thursday,Mandala Stage,0,0,15:45 - 16:45,15:45,16:45,27/06/2024,27/06/2024,27/06/2024 15:45,27/06/2024 16:45
The Body As A Site Of Activism: A Somatic Lens,Thursday,Temple Uprising,0,0,15:45 - 16:15,15:45,16:15,27/06/2024,27/06/2024,27/06/2024 15:45,27/06/2024 16:15
Tony And Ray,Thursday,The Gateway,0,0,15:45 - 16:00,15:45,16:00,27/06/2024,27/06/2024,27/06/2024 15:45,27/06/2024 16:00
"Bend It Films: 'Celebrating Stories Through Film & Tv': Ambika Mod (Actor - One Day), Antonia Thomas (Actor - Lovesick), Gurinder Chadha (Director - Bend It Like Beckham), Hosted By Anita Rani (Tv Personality, Radio Presenter)",Thursday,The Information,41,41,15:45 - 16:45,15:45,16:45,27/06/2024,27/06/2024,27/06/2024 15:45,27/06/2024 16:45
Gecko,Thursday,Toad Hall,0,0,15:45 - 16:30,15:45,16:30,27/06/2024,27/06/2024,27/06/2024 15:45,27/06/2024 16:30
Mossman (Dj Set),Thursday,Wishing Well,42,20,15:45 - 16:45,15:45,16:45,27/06/2024,27/06/2024,27/06/2024 15:45,27/06/2024 16:45
The Fiery Jack Family,Thursday,The Pavement,0,0,15:50 - 16:05,15:50,16:05,27/06/2024,27/06/2024,27/06/2024 15:50,27/06/2024 16:05
Gnomes,Thursday,Walkabouts,60,33,15:50 - 16:35,15:50,16:35,27/06/2024,27/06/2024,27/06/2024 15:50,27/06/2024 16:35
The Tea Ladies On Tour,Thursday,Walkabouts,60,33,15:50 - 16:35,15:50,16:35,27/06/2024,27/06/2024,27/06/2024 15:50,27/06/2024 16:35
Blockbuster Factory,Thursday,The Glebe,60,33,15:55 - 16:50,15:55,16:50,27/06/2024,27/06/2024,27/06/2024 15:55,27/06/2024 16:50
Future Bounce - Village Cuts Takeover,Thursday,Babylon Uprising,0,0,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
His Lordship,Thursday,Bbc Music Introducing,45,44,16:00 - 16:30,16:00,16:30,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 16:30
Congo Iain,Thursday,Blind Tiger,0,0,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
Doreen Doreen,Thursday,Circus Big Top,57,34,16:00 - 16:45,16:00,16:45,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 16:45
Compère: Bunny Morethan,Thursday,Circus Big Top,57,34,16:00 - 20:30,16:00,20:30,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 20:30
Ben Hemming,Thursday,Croissant Neuf Bandstand,55,21,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
Dance Class: Samba,Thursday,Glasto Latino,58,27,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
Aum Presents Chakra Sounds,Thursday,Kinetic,0,0,16:00 - 17:30,16:00,17:30,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:30
Sounds Of Space,Thursday,Laboratory Stage,0,0,16:00 - 16:45,16:00,16:45,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 16:45
Sista Selecta: Indy Rivers,Thursday,Nomad,0,0,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
Sportsbanger,Thursday,Nowhere,0,0,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
Das Brass,Thursday,Peace Stage,0,0,16:00 - 16:30,16:00,16:30,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 16:30
Ru Robinson,Thursday,Platform 23,0,0,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
"Talk: Yazzie Min, Revolutionary Love (Talk)",Thursday,Scissors,42,21,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
Just Transition - Workers Shifting From Fossil Fuels - Reel News,Thursday,Speakers Forum,0,0,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
Frank Turner,Thursday,Strummerville,48,12,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
Queer House Party,Thursday,The Rum Shack,0,0,16:00 - 18:00,16:00,18:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 18:00
Sistxrhood Open House,Thursday,The Sistxrhood,0,0,16:00 - 16:30,16:00,16:30,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 16:30
Channel One Sound System,Thursday,The Temple,0,0,16:00 - 18:00,16:00,18:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 18:00
Mista Trick (Dj Set & Live Sax),Thursday,Village Inn,0,0,16:00 - 18:00,16:00,18:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 18:00
Steve Faulkner,Thursday,Walkabouts,60,33,16:00 - 16:45,16:00,16:45,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 16:45
The Last Of The Mohicans,Thursday,Walkabouts,60,33,16:00 - 17:00,16:00,17:00,27/06/2024,27/06/2024,27/06/2024 16:00,27/06/2024 17:00
Grant Goldie,Thursday,A Little More Sensation,0,0,16:05 - 16:35,16:05,16:35,27/06/2024,27/06/2024,27/06/2024 16:05,27/06/2024 16:35
Forest Friend Theatre - In The Green Wood,Thursday,Kidzfield Big Top,0,0,16:05 - 16:40,16:05,16:40,27/06/2024,27/06/2024,27/06/2024 16:05,27/06/2024 16:40
Flashmob,Thursday,The Gateway,0,0,16:05 - 16:25,16:05,16:25,27/06/2024,27/06/2024,27/06/2024 16:05,27/06/2024 16:25
Jack Defrost - Traceworks Dance,Thursday,The Pavement,0,0,16:10 - 16:25,16:10,16:25,27/06/2024,27/06/2024,27/06/2024 16:10,27/06/2024 16:25
Bob Knight: Scottish Traveller Storytelling,Thursday,Atchin Tan,0,0,16:15 - 17:00,16:15,17:00,27/06/2024,27/06/2024,27/06/2024 16:15,27/06/2024 17:00
Feel Good Games With Kevin Campbell Davidson,Thursday,Humblewell Active Platform,42,21,16:15 - 17:00,16:15,17:00,27/06/2024,27/06/2024,27/06/2024 16:15,27/06/2024 17:00
Gong Bath With Yogic Sound,Thursday,Humblewell Retreat Yurt,42,21,16:15 - 17:00,16:15,17:00,27/06/2024,27/06/2024,27/06/2024 16:15,27/06/2024 17:00
Enchanted Flower Show Globe,Thursday,Walkabouts,60,33,16:15 - 17:00,16:15,17:00,27/06/2024,27/06/2024,27/06/2024 16:15,27/06/2024 17:00
The Cloudmen,Thursday,Walkabouts,60,33,16:15 - 17:15,16:15,17:15,27/06/2024,27/06/2024,27/06/2024 16:15,27/06/2024 17:15
The Royston Club,Thursday,Bread And Roses,0,0,16:20 - 17:20,16:20,17:20,27/06/2024,27/06/2024,27/06/2024 16:20,27/06/2024 17:20
Paul Lambourne,Thursday,Crooner'S Corner,0,0,16:20 - 16:50,16:20,16:50,27/06/2024,27/06/2024,27/06/2024 16:20,27/06/2024 16:50
Freddieno,Thursday,Sensation Seekers Stage,0,0,16:20 - 16:50,16:20,16:50,27/06/2024,27/06/2024,27/06/2024 16:20,27/06/2024 16:50
Sam Lee,Thursday,The Bandstand,56,38,16:20 - 17:00,16:20,17:00,27/06/2024,27/06/2024,27/06/2024 16:20,27/06/2024 17:00
Sabiyha,Thursday,The Hive,0,0,16:20 - 17:05,16:20,17:05,27/06/2024,27/06/2024,27/06/2024 16:20,27/06/2024 17:05
The Jukeboxes,Thursday,Walkabouts,60,33,16:20 - 17:50,16:20,17:50,27/06/2024,27/06/2024,27/06/2024 16:20,27/06/2024 17:50
Cocoa Butter Club Cabaret,Thursday,10 Aces,0,0,16:25 - 16:55,16:25,16:55,27/06/2024,27/06/2024,27/06/2024 16:25,27/06/2024 16:55
She'S Got Brass,Thursday,Peace Stage,0,0,16:30 - 17:00,16:30,17:00,27/06/2024,27/06/2024,27/06/2024 16:30,27/06/2024 17:00
Mj Cole,Thursday,Stonebridge Bar,42,18,16:30 - 18:00,16:30,18:00,27/06/2024,27/06/2024,27/06/2024 16:30,27/06/2024 18:00
Politics On The Dancefloor With Queer House Party,Thursday,Temple Uprising,0,0,16:30 - 17:15,16:30,17:15,27/06/2024,27/06/2024,27/06/2024 16:30,27/06/2024 17:15
Matthew One Man,Thursday,The Gateway,0,0,16:30 - 17:15,16:30,17:15,27/06/2024,27/06/2024,27/06/2024 16:30,27/06/2024 17:15
Goldie Fiasco,Thursday,The Pavement,0,0,16:30 - 17:00,16:30,17:00,27/06/2024,27/06/2024,27/06/2024 16:30,27/06/2024 17:00
Bexx - Be Experimental Interactive Concert,Thursday,The Sistxrhood,0,0,16:30 - 18:00,16:30,18:00,27/06/2024,27/06/2024,27/06/2024 16:30,27/06/2024 18:00
Interval,Thursday,Tree Stage,44,51,16:30 - 17:30,16:30,17:30,27/06/2024,27/06/2024,27/06/2024 16:30,27/06/2024 17:30
Fairly Fresh Fish Co,Thursday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,27/06/2024,27/06/2024,27/06/2024 16:30,27/06/2024 17:15
The Suitcase Escape Game,Thursday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,27/06/2024,27/06/2024,27/06/2024 16:30,27/06/2024 17:15
A Day At The Beach,Thursday,A Little More Sensation,0,0,16:40 - 17:10,16:40,17:10,27/06/2024,27/06/2024,27/06/2024 16:40,27/06/2024 17:10
Open Deck,Thursday,Bbc Music Introducing,45,44,16:45 - 18:15,16:45,18:15,27/06/2024,27/06/2024,27/06/2024 16:45,27/06/2024 18:15
Pnyc: Portishead - Roseland New York 25Th Anniversary + Intro With Adrian Utley,Thursday,Pilton Palais Cinema,64,36,16:45 - 18:15,16:45,18:15,27/06/2024,27/06/2024,27/06/2024 16:45,27/06/2024 18:15
Bigheads,Thursday,Walkabouts,60,33,16:45 - 17:25,16:45,17:25,27/06/2024,27/06/2024,27/06/2024 16:45,27/06/2024 17:25
Blip,Thursday,Walkabouts,60,33,16:45 - 17:30,16:45,17:30,27/06/2024,27/06/2024,27/06/2024 16:45,27/06/2024 17:30
Tors,Thursday,Wishing Well,42,20,16:45 - 17:45,16:45,17:45,27/06/2024,27/06/2024,27/06/2024 16:45,27/06/2024 17:45
Portraits,Thursday,Toad Hall,0,0,16:50 - 17:35,16:50,17:35,27/06/2024,27/06/2024,27/06/2024 16:50,27/06/2024 17:35
Scary & Spooky Skeletons,Thursday,Walkabouts,60,33,16:50 - 17:35,16:50,17:35,27/06/2024,27/06/2024,27/06/2024 16:50,27/06/2024 17:35
Circus Funtasia,Thursday,Circus Big Top,57,34,16:55 - 18:05,16:55,18:05,27/06/2024,27/06/2024,27/06/2024 16:55,27/06/2024 18:05
Mario Morris Magic,Thursday,The Glebe,60,33,16:55 - 17:25,16:55,17:25,27/06/2024,27/06/2024,27/06/2024 16:55,27/06/2024 17:25
Frank Harvey Trio,Thursday,10 Aces,0,0,17:00 - 17:40,17:00,17:40,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 17:40
Arthi - Village Cuts Takeover,Thursday,Babylon Uprising,0,0,17:00 - 18:00,17:00,18:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:00
"Rompas Reggae Shack - Daddy Nature, Dj Dansey",Thursday,Blind Tiger,0,0,17:00 - 19:00,17:00,19:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 19:00
Jo Bucket,Thursday,Carhenge,58,36,17:00 - 18:00,17:00,18:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:00
Kleptones,Thursday,Cornish Arms,0,0,17:00 - 19:00,17:00,19:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 19:00
The Orb,Thursday,Glade Dome,49,29,17:00 - 18:30,17:00,18:30,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:30
Dance Class: Salsa,Thursday,Glasto Latino,58,27,17:00 - 18:00,17:00,18:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:00
Oneda,Thursday,Greenpeace,55,26,17:00 - 17:55,17:00,17:55,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 17:55
Clown Zazz - Circus Pazaz,Thursday,Kidzfield Big Top,0,0,17:00 - 17:35,17:00,17:35,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 17:35
"Nature On Screen (Q&A With Kat Mansoor, Wildlife Kate & Jonny Keeling)",Thursday,Laboratory Stage,0,0,17:00 - 17:45,17:00,17:45,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 17:45
Mazaika,Thursday,Lunched Out Lizards,0,0,17:00 - 18:00,17:00,18:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:00
,Thursday,Mandala Stage,0,0,17:00 - 18:00,17:00,18:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:00
Chris Read,Thursday,Meeting Place Bar,0,0,17:00 - 20:00,17:00,20:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 20:00
Sista Selecta: I Am Fya,Thursday,Nomad,0,0,17:00 - 18:00,17:00,18:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:00
Sportsbanger,Thursday,Nowhere,0,0,17:00 - 18:00,17:00,18:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:00
Dj Chris Tofu & Debbralee Wells,Thursday,Peace Stage,0,0,17:00 - 17:30,17:00,17:30,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 17:30
Tina Edwards,Thursday,Platform 23,0,0,17:00 - 18:00,17:00,18:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:00
Alex Kassian,Thursday,San Remo,45,47,17:00 - 18:30,17:00,18:30,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:30
Otto & Astrid-Die Roten Punkte,Thursday,Sensation Seekers Stage,0,0,17:00 - 17:45,17:00,17:45,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 17:45
Psychedelic Medicine - Rayyan Zafar,Thursday,Speakers Forum,0,0,17:00 - 18:00,17:00,18:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 18:00
Celestials,Thursday,Walkabouts,60,33,17:00 - 17:30,17:00,17:30,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 17:30
Fortuni And Fae,Thursday,Walkabouts,60,33,17:00 - 17:45,17:00,17:45,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 17:45
Gliding Butterflies,Thursday,Walkabouts,60,33,17:00 - 17:45,17:00,17:45,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 17:45
West Holts Music Quiz,Thursday,West Holts Bar,59,29,17:00 - 19:00,17:00,19:00,27/06/2024,27/06/2024,27/06/2024 17:00,27/06/2024 19:00
Kwabana Lindsay Show,Thursday,The Pavement,0,0,17:05 - 17:35,17:05,17:35,27/06/2024,27/06/2024,27/06/2024 17:05,27/06/2024 17:35
Georgia D'Arcy Roden,Thursday,Crooner'S Corner,0,0,17:10 - 17:55,17:10,17:55,27/06/2024,27/06/2024,27/06/2024 17:10,27/06/2024 17:55
Tom Bright,Thursday,Strummerville,48,12,17:10 - 17:50,17:10,17:50,27/06/2024,27/06/2024,27/06/2024 17:10,27/06/2024 17:50
Jack Thomson,Thursday,Walkabouts,60,33,17:10 - 17:55,17:10,17:55,27/06/2024,27/06/2024,27/06/2024 17:10,27/06/2024 17:55
Rose Popay & Sidekick Saffy,Thursday,Walkabouts,60,33,17:10 - 17:55,17:10,17:55,27/06/2024,27/06/2024,27/06/2024 17:10,27/06/2024 17:55
Tony And Ray,Thursday,A Little More Sensation,0,0,17:15 - 17:30,17:15,17:30,27/06/2024,27/06/2024,27/06/2024 17:15,27/06/2024 17:30
Brewer'S Daughter: Music,Thursday,Atchin Tan,0,0,17:15 - 18:00,17:15,18:00,27/06/2024,27/06/2024,27/06/2024 17:15,27/06/2024 18:00
Ceildh With Kevin Campbell Davidson,Thursday,Humblewell Active Platform,42,21,17:15 - 18:15,17:15,18:15,27/06/2024,27/06/2024,27/06/2024 17:15,27/06/2024 18:15
Gong Bath With Yogic Sound,Thursday,Humblewell Retreat Yurt,42,21,17:15 - 18:00,17:15,18:00,27/06/2024,27/06/2024,27/06/2024 17:15,27/06/2024 18:00
"Talk: Yomi Adegoke, Whose Story Is It Anyway?",Thursday,Scissors,42,21,17:15 - 18:00,17:15,18:00,27/06/2024,27/06/2024,27/06/2024 17:15,27/06/2024 18:00
The Fairy Godmother And The Tooth Fairy,Thursday,Walkabouts,60,33,17:15 - 18:00,17:15,18:00,27/06/2024,27/06/2024,27/06/2024 17:15,27/06/2024 18:00
Swingle Tree,Thursday,The Bandstand,56,38,17:20 - 18:00,17:20,18:00,27/06/2024,27/06/2024,27/06/2024 17:20,27/06/2024 18:00
New York Brass Band,Thursday,The Gateway,0,0,17:25 - 17:55,17:25,17:55,27/06/2024,27/06/2024,27/06/2024 17:25,27/06/2024 17:55
Pushpin,Thursday,The Hive,0,0,17:25 - 18:10,17:25,18:10,27/06/2024,27/06/2024,27/06/2024 17:25,27/06/2024 18:10
The Trouble Notes,Thursday,Croissant Neuf Bandstand,55,21,17:30 - 18:30,17:30,18:30,27/06/2024,27/06/2024,27/06/2024 17:30,27/06/2024 18:30
And What,Thursday,Kinetic,0,0,17:30 - 18:30,17:30,18:30,27/06/2024,27/06/2024,27/06/2024 17:30,27/06/2024 18:30
Hak Baker-Acoustic Set,Thursday,Peace Stage,0,0,17:30 - 18:00,17:30,18:00,27/06/2024,27/06/2024,27/06/2024 17:30,27/06/2024 18:00
Notting Hill St Pauls Carnival,Thursday,The Bug,41,25,17:30 - 19:30,17:30,19:30,27/06/2024,27/06/2024,27/06/2024 17:30,27/06/2024 19:30
Close,Thursday,The Glebe,60,33,17:30 - 21:20,17:30,21:20,27/06/2024,27/06/2024,27/06/2024 17:30,27/06/2024 21:20
Steve Davis & Kavus Torabi Ambient Dj Set,Thursday,Tree Stage,44,51,17:30 - 18:40,17:30,18:40,27/06/2024,27/06/2024,27/06/2024 17:30,27/06/2024 18:40
Meanderthals,Thursday,Walkabouts,60,33,17:30 - 18:15,17:30,18:15,27/06/2024,27/06/2024,27/06/2024 17:30,27/06/2024 18:15
Space Cadets,Thursday,Walkabouts,60,33,17:30 - 18:15,17:30,18:15,27/06/2024,27/06/2024,27/06/2024 17:30,27/06/2024 18:15
Tba,Thursday,A Little More Sensation,0,0,17:35 - 18:05,17:35,18:05,27/06/2024,27/06/2024,27/06/2024 17:35,27/06/2024 18:05
Thrill Collins,Thursday,10 Aces,0,0,17:45 - 18:30,17:45,18:30,27/06/2024,27/06/2024,27/06/2024 17:45,27/06/2024 18:30
Close,Thursday,Sensation Seekers Stage,0,0,17:45 - 20:30,17:45,20:30,27/06/2024,27/06/2024,27/06/2024 17:45,27/06/2024 20:30
Laura London & Jake Francis,Thursday,Walkabouts,60,33,17:45 - 18:30,17:45,18:30,27/06/2024,27/06/2024,27/06/2024 17:45,27/06/2024 18:30
The Wardens,Thursday,Walkabouts,60,33,17:45 - 18:30,17:45,18:30,27/06/2024,27/06/2024,27/06/2024 17:45,27/06/2024 18:30
The Beatles Dub Club (Dj Set),Thursday,Wishing Well,42,20,17:45 - 18:45,17:45,18:45,27/06/2024,27/06/2024,27/06/2024 17:45,27/06/2024 18:45
Music With Mike - The Big Gig,Thursday,Kidzfield Big Top,0,0,17:50 - 18:30,17:50,18:30,27/06/2024,27/06/2024,27/06/2024 17:50,27/06/2024 18:30
Shosh,Thursday,Greenpeace,55,26,17:55 - 18:55,17:55,18:55,27/06/2024,27/06/2024,27/06/2024 17:55,27/06/2024 18:55
Dar Disku B2B Nabihah Iqbal,Thursday,Assembly,40,42,18:00 - 19:30,18:00,19:30,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:30
Coco Em B2B Badman Bantou - Village Cuts Takeover,Thursday,Babylon Uprising,0,0,18:00 - 19:00,18:00,19:00,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:00
The Majorettes - Paradise With Love,Thursday,Bread And Roses,0,0,18:00 - 18:40,18:00,18:40,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 18:40
Scarlett O’Malley [Foundation Fm Takeover],Thursday,Firmly Rooted,43,43,18:00 - 19:30,18:00,19:30,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:30
Kurupt Fm,Thursday,Glade,51,29,18:00 - 19:00,18:00,19:00,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:00
Robin Ince - Arguing About Ghosts With Physicists And Other Monket Cage Conflicts,Thursday,Laboratory Stage,0,0,18:00 - 19:00,18:00,19:00,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:00
Ok Williams B2B Tai Lokun,Thursday,Levels,42,44,18:00 - 19:30,18:00,19:30,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:30
Skream & Benga,Thursday,Lonely Hearts Club,44,41,18:00 - 19:30,18:00,19:30,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:30
Sista Selecta: Mela Sounds,Thursday,Nomad,0,0,18:00 - 19:00,18:00,19:00,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:00
Sportsbanger,Thursday,Nowhere,0,0,18:00 - 19:00,18:00,19:00,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:00
Gia Fu,Thursday,Platform 23,0,0,18:00 - 19:00,18:00,19:00,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:00
Unprepared - Andrew Simms / Rebecca Gibbs,Thursday,Speakers Forum,0,0,18:00 - 19:00,18:00,19:00,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:00
Kitty Amor,Thursday,Stonebridge Bar,42,18,18:00 - 19:30,18:00,19:30,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:30
Aine Deane,Thursday,Strummerville,48,12,18:00 - 18:40,18:00,18:40,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 18:40
D-Lish,Thursday,The Rum Shack,0,0,18:00 - 19:00,18:00,19:00,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:00
Dubkasm Ft. Kiko Bun,Thursday,The Temple,0,0,18:00 - 19:00,18:00,19:00,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:00
Mal Webb & Kyle Morrigan,Thursday,Toad Hall,0,0,18:00 - 18:45,18:00,18:45,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 18:45
Seb Bailey,Thursday,Village Inn,0,0,18:00 - 19:30,18:00,19:30,27/06/2024,27/06/2024,27/06/2024 18:00,27/06/2024 19:30
Bexi - Barbarella,Thursday,Circus Big Top,57,34,18:10 - 18:16,18:10,18:16,27/06/2024,27/06/2024,27/06/2024 18:10,27/06/2024 18:16
Warm Up Dj For Bbc R1 Dance Takeover,Thursday,Bbc Music Introducing,45,44,18:15 - 19:00,18:15,19:00,27/06/2024,27/06/2024,27/06/2024 18:15,27/06/2024 19:00
Showhawk Duo,Thursday,The Bandstand,56,38,18:20 - 19:00,18:20,19:00,27/06/2024,27/06/2024,27/06/2024 18:20,27/06/2024 19:00
Enjoyable Listens,Thursday,The Hive,0,0,18:20 - 18:50,18:20,18:50,27/06/2024,27/06/2024,27/06/2024 18:20,27/06/2024 18:50
Cirk Hes Presents Lizzie,Thursday,Circus Big Top,57,34,18:21 - 18:27,18:21,18:27,27/06/2024,27/06/2024,27/06/2024 18:21,27/06/2024 18:27
Mauvey,Thursday,Bimble Inn,41,16,18:30 - 19:30,18:30,19:30,27/06/2024,27/06/2024,27/06/2024 18:30,27/06/2024 19:30
Fish56Octagon,Thursday,Glade Dome,49,29,18:30 - 19:15,18:30,19:15,27/06/2024,27/06/2024,27/06/2024 18:30,27/06/2024 19:15
Ìyáàlù,Thursday,Kinetic,0,0,18:30 - 19:30,18:30,19:30,27/06/2024,27/06/2024,27/06/2024 18:30,27/06/2024 19:30
Adam Scott Glasspool,Thursday,Mandala Stage,0,0,18:30 - 19:30,18:30,19:30,27/06/2024,27/06/2024,27/06/2024 18:30,27/06/2024 19:30
Bazzookas,Thursday,Peace Stage,0,0,18:30 - 19:15,18:30,19:15,27/06/2024,27/06/2024,27/06/2024 18:30,27/06/2024 19:15
National Theatre Live: Vanya 15,Thursday,Pilton Palais Cinema,64,36,18:30 - 20:55,18:30,20:55,27/06/2024,27/06/2024,27/06/2024 18:30,27/06/2024 20:55
Fafi Abdel Nour,Thursday,San Remo,45,47,18:30 - 20:00,18:30,20:00,27/06/2024,27/06/2024,27/06/2024 18:30,27/06/2024 20:00
"Workshop: Emma Stoner, My Queer Glastonbury Story",Thursday,Scissors,42,21,18:30 - 19:15,18:30,19:15,27/06/2024,27/06/2024,27/06/2024 18:30,27/06/2024 19:15
Head Over Wheels,Thursday,Circus Big Top,57,34,18:32 - 18:40,18:32,18:40,27/06/2024,27/06/2024,27/06/2024 18:32,27/06/2024 18:40
Interval,Thursday,Tree Stage,44,51,18:40 - 18:50,18:40,18:50,27/06/2024,27/06/2024,27/06/2024 18:40,27/06/2024 18:50
Jay Rawlings' World Record Attempt,Thursday,Circus Big Top,57,34,18:45 - 18:53,18:45,18:53,27/06/2024,27/06/2024,27/06/2024 18:45,27/06/2024 18:53
Olivia Nelson,Thursday,Wishing Well,42,20,18:45 - 19:45,18:45,19:45,27/06/2024,27/06/2024,27/06/2024 18:45,27/06/2024 19:45
The Egg Ambient Set,Thursday,Tree Stage,44,51,18:50 - 19:40,18:50,19:40,27/06/2024,27/06/2024,27/06/2024 18:50,27/06/2024 19:40
Boom Circus,Thursday,Circus Big Top,57,34,18:58 - 19:43,18:58,19:43,27/06/2024,27/06/2024,27/06/2024 18:58,27/06/2024 19:43
Jeremiah Asiamah - We Are Friends Takeover,Thursday,Babylon Uprising,0,0,19:00 - 19:45,19:00,19:45,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 19:45
Bbc R1 Dance Takeover,Thursday,Bbc Music Introducing,45,44,19:00 - 23:00,19:00,23:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 23:00
Ulula Roots,Thursday,Blind Tiger,0,0,19:00 - 20:00,19:00,20:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 20:00
Bryte,Thursday,Bread And Roses,0,0,19:00 - 19:40,19:00,19:40,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 19:40
Petebox (Blendid Takeover,Thursday,Cornish Arms,0,0,19:00 - 19:30,19:00,19:30,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 19:30
Banyah,Thursday,Croissant Neuf Bandstand,55,21,19:00 - 20:00,19:00,20:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 20:00
Lauren Lo Sung,Thursday,Glade,51,29,19:00 - 20:15,19:00,20:15,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 20:15
Moonchild Sanelly,Thursday,Greenpeace,55,26,19:00 - 20:00,19:00,20:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 20:00
Fixx: Saba Kia,Thursday,Nomad,0,0,19:00 - 20:00,19:00,20:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 20:00
Sportsbanger,Thursday,Nowhere,0,0,19:00 - 20:00,19:00,20:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 20:00
Worm Soundsystem: Ten Years Of Worm Disco Club,Thursday,Platform 23,0,0,19:00 - 20:00,19:00,20:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 20:00
Metu: Reclaiming Our Unions From Sexism & Misogyny - Reel News,Thursday,Speakers Forum,0,0,19:00 - 20:00,19:00,20:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 20:00
Compère: Stuart Goldsmith,Thursday,The Astrolabe Theatre,0,0,19:00 - 23:10,19:00,23:10,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 23:10
Nadí,Thursday,The Rum Shack,0,0,19:00 - 20:00,19:00,20:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 20:00
Mae Challis Live!,Thursday,The Taphouse,0,0,19:00 - 21:00,19:00,21:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 21:00
"Gardna Live W/ Drs, Emily Makis & Lau.Ra",Thursday,The Temple,0,0,19:00 - 20:00,19:00,20:00,27/06/2024,27/06/2024,27/06/2024 19:00,27/06/2024 20:00
Moss Kissing,Thursday,The Hive,0,0,19:05 - 19:50,19:05,19:50,27/06/2024,27/06/2024,27/06/2024 19:05,27/06/2024 19:50
Antony Szmierek,Thursday,West Holts Bar,59,29,19:10 - 19:55,19:10,19:55,27/06/2024,27/06/2024,27/06/2024 19:10,27/06/2024 19:55
Natty Lou,Thursday,Glade Dome,49,29,19:15 - 20:15,19:15,20:15,27/06/2024,27/06/2024,27/06/2024 19:15,27/06/2024 20:15
Jonathan Pie,Thursday,The Astrolabe Theatre,0,0,19:15 - 20:15,19:15,20:15,27/06/2024,27/06/2024,27/06/2024 19:15,27/06/2024 20:15
Seize The Day,Thursday,Toad Hall,0,0,19:15 - 20:10,19:15,20:10,27/06/2024,27/06/2024,27/06/2024 19:15,27/06/2024 20:10
The Rumble-O'S,Thursday,The Bandstand,56,38,19:20 - 20:00,19:20,20:00,27/06/2024,27/06/2024,27/06/2024 19:20,27/06/2024 20:00
Red Lazer Disco,Thursday,Assembly,40,42,19:30 - 21:00,19:30,21:00,27/06/2024,27/06/2024,27/06/2024 19:30,27/06/2024 21:00
"Count Skylarkin: Dj Derek'S Island Discs, Sounds Of The Late Great Dj Derek (Blendid Takeover)",Thursday,Cornish Arms,0,0,19:30 - 21:00,19:30,21:00,27/06/2024,27/06/2024,27/06/2024 19:30,27/06/2024 21:00
Emma Korantema [Foundation Fm Takeover],Thursday,Firmly Rooted,43,43,19:30 - 21:00,19:30,21:00,27/06/2024,27/06/2024,27/06/2024 19:30,27/06/2024 21:00
Off Yellow,Thursday,Kinetic,0,0,19:30 - 20:30,19:30,20:30,27/06/2024,27/06/2024,27/06/2024 19:30,27/06/2024 20:30
Dr Banana X Lukas Wigflex,Thursday,Levels,42,44,19:30 - 21:00,19:30,21:00,27/06/2024,27/06/2024,27/06/2024 19:30,27/06/2024 21:00
Taylah Elaine [Taylah Elaine & Friends],Thursday,Lonely Hearts Club,44,41,19:30 - 20:30,19:30,20:30,27/06/2024,27/06/2024,27/06/2024 19:30,27/06/2024 20:30
Daniel Avery (Electroclash Set),Thursday,Stonebridge Bar,42,18,19:30 - 21:00,19:30,21:00,27/06/2024,27/06/2024,27/06/2024 19:30,27/06/2024 21:00
Maia Beth,Thursday,Village Inn,0,0,19:30 - 21:00,19:30,21:00,27/06/2024,27/06/2024,27/06/2024 19:30,27/06/2024 21:00
Klein,Thursday,Tree Stage,44,51,19:40 - 20:55,19:40,20:55,27/06/2024,27/06/2024,27/06/2024 19:40,27/06/2024 20:55
Jeremiah Asiamah B2B L-Vis 1990 - We Are Friends Takeover,Thursday,Babylon Uprising,0,0,19:45 - 20:30,19:45,20:30,27/06/2024,27/06/2024,27/06/2024 19:45,27/06/2024 20:30
Gnawa Blues All Stars,Thursday,Peace Stage,0,0,19:45 - 20:30,19:45,20:30,27/06/2024,27/06/2024,27/06/2024 19:45,27/06/2024 20:30
"Talk: Smokin' Jo, You Don'T Need A Dick To Be A Dj",Thursday,Scissors,42,21,19:45 - 20:30,19:45,20:30,27/06/2024,27/06/2024,27/06/2024 19:45,27/06/2024 20:30
Ross Wilson (Dj Set),Thursday,Wishing Well,42,20,19:45 - 20:45,19:45,20:45,27/06/2024,27/06/2024,27/06/2024 19:45,27/06/2024 20:45
Eloise & Jack,Thursday,Circus Big Top,57,34,19:48 - 19:54,19:48,19:54,27/06/2024,27/06/2024,27/06/2024 19:48,27/06/2024 19:54
Toby Walker,Thursday,Circus Big Top,57,34,19:59 - 20:07,19:59,20:07,27/06/2024,27/06/2024,27/06/2024 19:59,27/06/2024 20:07
Bridget.,Thursday,Bimble Inn,41,16,20:00 - 21:00,20:00,21:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:00
"Peng Deli: Dream Mclean, Harley Maxwell, Wallace Rice, C.Rem, Eva, Bubski, Paddy Bars, Dead Weights, Sophie Faith",Thursday,Blind Tiger,0,0,20:00 - 22:00,20:00,22:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 22:00
Atchin Tan Presents: Hosted By Johnson Welch,Thursday,Flying Bus,0,0,20:00 - 00:00,20:00,00:00,27/06/2024,28/06/2024,27/06/2024 20:00,28/06/2024 00:00
Atchin Tan Presents: Billy Welch,Thursday,Flying Bus,0,0,20:00 - 20:05,20:00,20:05,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 20:05
Michelle Manetti B2B Demi Riquisimo,Thursday,Genosys,0,0,20:00 - 21:30,20:00,21:30,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:30
Disco And Cinema,Thursday,Humblewell Active Platform,42,21,20:00 - 01:00,20:00,01:00,27/06/2024,28/06/2024,27/06/2024 20:00,28/06/2024 01:00
Adam Shelton,Thursday,Iicon,66,21,20:00 - 21:30,20:00,21:30,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:30
Pushpin,Thursday,Lunched Out Lizards,0,0,20:00 - 21:00,20:00,21:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:00
The Portraits,Thursday,Mandala Stage,0,0,20:00 - 21:00,20:00,21:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:00
Overeasy Djs,Thursday,Meeting Place Bar,0,0,20:00 - 03:00,20:00,03:00,27/06/2024,28/06/2024,27/06/2024 20:00,28/06/2024 03:00
Mez Yard Guests,Thursday,Mez Yard,0,0,20:00 - 21:00,20:00,21:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:00
Fixx: Big Kani,Thursday,Nomad,0,0,20:00 - 21:00,20:00,21:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:00
Sportsbanger,Thursday,Nowhere,0,0,20:00 - 21:00,20:00,21:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:00
Nat Wendell,Thursday,Nyc Downlow,0,0,20:00 - 21:55,20:00,21:55,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:55
Ella Knight (Dj Set),Thursday,Platform 23,0,0,20:00 - 21:00,20:00,21:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:00
Amaliah,Thursday,San Remo,45,47,20:00 - 21:30,20:00,21:30,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:30
My Extinction Film &Q&A - Josh Appignanesi,Thursday,Speakers Forum,0,0,20:00 - 21:00,20:00,21:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:00
Imperial Wax,Thursday,Strummerville,48,12,20:00 - 20:40,20:00,20:40,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 20:40
"Notting Hill Carnival Presents: Solution Sound, Nick Manasseh, David Hill, Mr Fix It",Thursday,Terminal 1,0,0,20:00 - 03:00,20:00,03:00,27/06/2024,28/06/2024,27/06/2024 20:00,28/06/2024 03:00
Gallegos,Thursday,The Bug,41,25,20:00 - 20:45,20:00,20:45,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 20:45
Girls Of The Internet,Thursday,The Meatrack,0,0,20:00 - 21:30,20:00,21:30,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:30
Dj Ruby Flashman,Thursday,The Rocket Lounge,64,16,20:00 - 03:00,20:00,03:00,27/06/2024,28/06/2024,27/06/2024 20:00,28/06/2024 03:00
Sister Suzie,Thursday,The Rocket Lounge,64,16,20:00 - 21:00,20:00,21:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:00
Dj Shorty,Thursday,The Rum Shack,0,0,20:00 - 20:30,20:00,20:30,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 20:30
Bish B2B Lens,Thursday,The Temple,0,0,20:00 - 21:00,20:00,21:00,27/06/2024,27/06/2024,27/06/2024 20:00,27/06/2024 21:00
Atchin Tan Presents: Johnson Welch,Thursday,Flying Bus,0,0,20:05 - 20:10,20:05,20:10,27/06/2024,27/06/2024,27/06/2024 20:05,27/06/2024 20:10
Sue Veneers,Thursday,Greenpeace,55,26,20:05 - 21:25,20:05,21:25,27/06/2024,27/06/2024,27/06/2024 20:05,27/06/2024 21:25
Persiajoon,Thursday,The Hive,0,0,20:05 - 20:50,20:05,20:50,27/06/2024,27/06/2024,27/06/2024 20:05,27/06/2024 20:50
Luke Gomm & The Works,Thursday,Bread And Roses,0,0,20:10 - 21:10,20:10,21:10,27/06/2024,27/06/2024,27/06/2024 20:10,27/06/2024 21:10
Atchin Tan Presents: Solly,Thursday,Flying Bus,0,0,20:10 - 20:20,20:10,20:20,27/06/2024,27/06/2024,27/06/2024 20:10,27/06/2024 20:20
Cirk Hes Presents Roz,Thursday,Circus Big Top,57,34,20:12 - 20:18,20:12,20:18,27/06/2024,27/06/2024,27/06/2024 20:12,27/06/2024 20:18
Jack Henry + Julie Abbe,Thursday,Croissant Neuf Bandstand,55,21,20:15 - 20:45,20:15,20:45,27/06/2024,27/06/2024,27/06/2024 20:15,27/06/2024 20:45
Love Remain,Thursday,Glade,51,29,20:15 - 21:30,20:15,21:30,27/06/2024,27/06/2024,27/06/2024 20:15,27/06/2024 21:30
Girls Next Door,Thursday,Glade Dome,49,29,20:15 - 21:15,20:15,21:15,27/06/2024,27/06/2024,27/06/2024 20:15,27/06/2024 21:15
The Caravan Of Lost Souls,Thursday,Walkabouts,60,33,20:15 - 22:15,20:15,22:15,27/06/2024,27/06/2024,27/06/2024 20:15,27/06/2024 22:15
Enjoyable Listens,Thursday,West Holts Bar,59,29,20:15 - 21:00,20:15,21:00,27/06/2024,27/06/2024,27/06/2024 20:15,27/06/2024 21:00
Atchin Tan Presents: Thomas Mccarthy,Thursday,Flying Bus,0,0,20:20 - 20:45,20:20,20:45,27/06/2024,27/06/2024,27/06/2024 20:20,27/06/2024 20:45
Peace Delegates,Thursday,The Astrolabe Theatre,0,0,20:20 - 20:30,20:20,20:30,27/06/2024,27/06/2024,27/06/2024 20:20,27/06/2024 20:30
Blackberry Wood,Thursday,The Bandstand,56,38,20:20 - 21:00,20:20,21:00,27/06/2024,27/06/2024,27/06/2024 20:20,27/06/2024 21:00
Ellis Grover,Thursday,Circus Big Top,57,34,20:23 - 20:33,20:23,20:33,27/06/2024,27/06/2024,27/06/2024 20:23,27/06/2024 20:33
Jeremiah Asiamah B2B P-Rallel & Oppidan - We Are Friends Takeover,Thursday,Babylon Uprising,0,0,20:30 - 21:15,20:30,21:15,27/06/2024,27/06/2024,27/06/2024 20:30,27/06/2024 21:15
Compère: Annabelle Holland,Thursday,Circus Big Top,57,34,20:30 - 01:00,20:30,01:00,27/06/2024,28/06/2024,27/06/2024 20:30,28/06/2024 01:00
Wizard Otr,Thursday,Deluxe Diner,64,17,20:30 - 22:30,20:30,22:30,27/06/2024,27/06/2024,27/06/2024 20:30,27/06/2024 22:30
Kossov,Thursday,Kinetic,0,0,20:30 - 21:30,20:30,21:30,27/06/2024,27/06/2024,27/06/2024 20:30,27/06/2024 21:30
Boogaloo Dee,Thursday,Kinetic,0,0,20:30 - 22:30,20:30,22:30,27/06/2024,27/06/2024,27/06/2024 20:30,27/06/2024 22:30
Lady Shaka [Taylah Elaine & Friends],Thursday,Lonely Hearts Club,44,41,20:30 - 21:30,20:30,21:30,27/06/2024,27/06/2024,27/06/2024 20:30,27/06/2024 21:30
Showhawk Duo,Thursday,Sensation Seekers Stage,0,0,20:30 - 21:30,20:30,21:30,27/06/2024,27/06/2024,27/06/2024 20:30,27/06/2024 21:30
Steve Rawlings,Thursday,The Astrolabe Theatre,0,0,20:30 - 21:00,20:30,21:00,27/06/2024,27/06/2024,27/06/2024 20:30,27/06/2024 21:00
Esea Music Presents: Natty Wylah,Thursday,The Rum Shack,0,0,20:30 - 21:00,20:30,21:00,27/06/2024,27/06/2024,27/06/2024 20:30,27/06/2024 21:00
Tennyson King,Thursday,Toad Hall,0,0,20:30 - 21:10,20:30,21:10,27/06/2024,27/06/2024,27/06/2024 20:30,27/06/2024 21:10
Fraser Hooper,Thursday,Circus Big Top,57,34,20:38 - 21:03,20:38,21:03,27/06/2024,27/06/2024,27/06/2024 20:38,27/06/2024 21:03
Atchin Tan Presents: Fftp (Freedom For Travelling People),Thursday,Flying Bus,0,0,20:45 - 21:20,20:45,21:20,27/06/2024,27/06/2024,27/06/2024 20:45,27/06/2024 21:20
Pizza Hotline,Thursday,The Bug,41,25,20:45 - 21:30,20:45,21:30,27/06/2024,27/06/2024,27/06/2024 20:45,27/06/2024 21:30
Lekiddo - Lord Of The Lobsters!,Thursday,Wishing Well,42,20,20:45 - 21:30,20:45,21:30,27/06/2024,27/06/2024,27/06/2024 20:45,27/06/2024 21:30
The Birds,Thursday,Walkabouts,60,33,20:50 - 21:35,20:50,21:35,27/06/2024,27/06/2024,27/06/2024 20:50,27/06/2024 21:35
Steven Wilson The Harmony Codex Title Track In Quadraphonic,Thursday,Tree Stage,44,51,20:55 - 21:05,20:55,21:05,27/06/2024,27/06/2024,27/06/2024 20:55,27/06/2024 21:05
Dj Ritu,Thursday,Arrivals,0,0,21:00 - 22:00,21:00,22:00,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:00
Sugar Free B2B Fonte,Thursday,Assembly,40,42,21:00 - 22:30,21:00,22:30,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:30
Madame Electrifie (Blendid Takeover),Thursday,Cornish Arms,0,0,21:00 - 23:00,21:00,23:00,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 23:00
Mr. B The Gentleman Rhymer,Thursday,Croissant Neuf,55,21,21:00 - 21:30,21:00,21:30,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 21:30
Lagoon Femshayma [Foundation Fm Takeover],Thursday,Firmly Rooted,43,43,21:00 - 22:30,21:00,22:30,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:30
Carnival,Thursday,Glasto Latino,58,27,21:00 - 21:30,21:00,21:30,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 21:30
Joy Orbison,Thursday,Levels,42,44,21:00 - 22:30,21:00,22:30,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:30
The Trouble Notes,Thursday,Lunched Out Lizards,0,0,21:00 - 22:00,21:00,22:00,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:00
Copperdollar: The Spirits Of Mezcal (Show),Thursday,Mez Yard,0,0,21:00 - 23:00,21:00,23:00,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 23:00
Fixx: Lea Lea,Thursday,Nomad,0,0,21:00 - 22:00,21:00,22:00,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:00
Sportsbanger,Thursday,Nowhere,0,0,21:00 - 22:00,21:00,22:00,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:00
Vlure,Thursday,Peace Stage,0,0,21:00 - 21:45,21:00,21:45,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 21:45
Problemista + Intro With Tilda Swinton,Thursday,Pilton Palais Cinema,64,36,21:00 - 22:50,21:00,22:50,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:50
Emma Jean-Thackray (Dj Set),Thursday,Platform 23,0,0,21:00 - 22:00,21:00,22:00,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:00
Zerya,Thursday,Scissors,42,21,21:00 - 21:30,21:00,21:30,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 21:30
Groove Armada (Dj Set),Thursday,Stonebridge Bar,42,18,21:00 - 22:30,21:00,22:30,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:30
Chimer,Thursday,Strummerville,48,12,21:00 - 21:40,21:00,21:40,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 21:40
Marching Skaletons,Thursday,The Rocket Lounge,64,16,21:00 - 22:00,21:00,22:00,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:00
Lb,Thursday,The Sistxrhood,0,0,21:00 - 22:00,21:00,22:00,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:00
Jack Osman B2B Danny Vito,Thursday,The Taphouse,0,0,21:00 - 23:30,21:00,23:30,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 23:30
Kleu B2B Resist,Thursday,The Temple,0,0,21:00 - 22:00,21:00,22:00,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:00
The Mighty Mojo,Thursday,Village Inn,0,0,21:00 - 22:30,21:00,22:30,27/06/2024,27/06/2024,27/06/2024 21:00,27/06/2024 22:30
Stephen Frost Impro Allstars,Thursday,The Astrolabe Theatre,0,0,21:05 - 22:05,21:05,22:05,27/06/2024,27/06/2024,27/06/2024 21:05,27/06/2024 22:05
Sock Drawer,Thursday,The Hive,0,0,21:05 - 21:50,21:05,21:50,27/06/2024,27/06/2024,27/06/2024 21:05,27/06/2024 21:50
Chloe Slomo A/V,Thursday,Tree Stage,44,51,21:05 - 21:55,21:05,21:55,27/06/2024,27/06/2024,27/06/2024 21:05,27/06/2024 21:55
Molly Whitehouse,Thursday,Circus Big Top,57,34,21:08 - 21:14,21:08,21:14,27/06/2024,27/06/2024,27/06/2024 21:08,27/06/2024 21:14
Jeremiah Asiamah B2B Turno Ft Charlotte Plank - We Are Friends Takeover,Thursday,Babylon Uprising,0,0,21:15 - 22:00,21:15,22:00,27/06/2024,27/06/2024,27/06/2024 21:15,27/06/2024 22:00
Mozey,Thursday,Glade Dome,49,29,21:15 - 22:15,21:15,22:15,27/06/2024,27/06/2024,27/06/2024 21:15,27/06/2024 22:15
Esea Music Presents: Jianbo,Thursday,The Rum Shack,0,0,21:15 - 22:00,21:15,22:00,27/06/2024,27/06/2024,27/06/2024 21:15,27/06/2024 22:00
Eloise & Jack,Thursday,Circus Big Top,57,34,21:19 - 21:25,21:19,21:25,27/06/2024,27/06/2024,27/06/2024 21:19,27/06/2024 21:25
Atchin Tan Presnts: Damian Le Bas,Thursday,Flying Bus,0,0,21:20 - 21:35,21:20,21:35,27/06/2024,27/06/2024,27/06/2024 21:20,27/06/2024 21:35
The Starlings,Thursday,The Bandstand,56,38,21:20 - 22:10,21:20,22:10,27/06/2024,27/06/2024,27/06/2024 21:20,27/06/2024 22:10
Jayahadadream,Thursday,West Holts Bar,59,29,21:20 - 22:10,21:20,22:10,27/06/2024,27/06/2024,27/06/2024 21:20,27/06/2024 22:10
Pronghorn,Thursday,The Glebe,60,33,21:25 - 22:10,21:25,22:10,27/06/2024,27/06/2024,27/06/2024 21:25,27/06/2024 22:10
Beans On Toast,Thursday,Bimble Inn,41,16,21:30 - 22:30,21:30,22:30,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 22:30
Caxxianne,Thursday,Bread And Roses,0,0,21:30 - 22:10,21:30,22:10,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 22:10
Duo Santus,Thursday,Circus Big Top,57,34,21:30 - 21:36,21:30,21:36,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 21:36
Nyra,Thursday,Genosys,0,0,21:30 - 23:00,21:30,23:00,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 23:00
Desiree,Thursday,Glade,51,29,21:30 - 23:00,21:30,23:00,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 23:00
Indira Roman Y Aji Pa' Ti,Thursday,Glasto Latino,58,27,21:30 - 23:00,21:30,23:00,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 23:00
Thog,Thursday,Iicon,66,21,21:30 - 23:15,21:30,23:15,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 23:15
Sonique [Dj] [Taylah Elaine & Friends],Thursday,Lonely Hearts Club,44,41,21:30 - 22:30,21:30,22:30,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 22:30
Ju5 Bones,Thursday,Mandala Stage,0,0,21:30 - 22:30,21:30,22:30,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 22:30
Marie Montexier,Thursday,San Remo,45,47,21:30 - 23:00,21:30,23:00,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 23:00
Opening Ceremony: Everyone'S Choir By Xoph,Thursday,Scissors,42,21,21:30 - 21:50,21:30,21:50,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 21:50
Subb-An,Thursday,The Meatrack,0,0,21:30 - 23:00,21:30,23:00,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 23:00
Kangaroo Moon,Thursday,Toad Hall,0,0,21:30 - 22:30,21:30,22:30,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 22:30
The Runaway Chrstmas Fairy Tree,Thursday,Walkabouts,60,33,21:30 - 22:15,21:30,22:15,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 22:15
The Cloudmen,Thursday,Walkabouts,60,33,21:30 - 22:30,21:30,22:30,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 22:30
Us,Thursday,Wishing Well,42,20,21:30 - 22:30,21:30,22:30,27/06/2024,27/06/2024,27/06/2024 21:30,27/06/2024 22:30
Atchin Tan Presnts: Aidan And Luca,Thursday,Flying Bus,0,0,21:35 - 21:50,21:35,21:50,27/06/2024,27/06/2024,27/06/2024 21:35,27/06/2024 21:50
Lynks,Thursday,Greenpeace,55,26,21:35 - 22:30,21:35,22:30,27/06/2024,27/06/2024,27/06/2024 21:35,27/06/2024 22:30
Ivo Dimchev,Thursday,Sensation Seekers Stage,0,0,21:35 - 21:50,21:35,21:50,27/06/2024,27/06/2024,27/06/2024 21:35,27/06/2024 21:50
Charlie Bicknell - Supersonic Woman,Thursday,Circus Big Top,57,34,21:41 - 21:53,21:41,21:53,27/06/2024,27/06/2024,27/06/2024 21:41,27/06/2024 21:53
Mystic Mirror Show Globe,Thursday,Walkabouts,60,33,21:45 - 22:45,21:45,22:45,27/06/2024,27/06/2024,27/06/2024 21:45,27/06/2024 22:45
Atchin Tan Presents: Sugar Shane,Thursday,Flying Bus,0,0,21:50 - 22:30,21:50,22:30,27/06/2024,27/06/2024,27/06/2024 21:50,27/06/2024 22:30
Holly Roxanne,Thursday,Scissors,42,21,21:50 - 22:15,21:50,22:15,27/06/2024,27/06/2024,27/06/2024 21:50,27/06/2024 22:15
Doreen Doreen,Thursday,Sensation Seekers Stage,0,0,21:50 - 22:50,21:50,22:50,27/06/2024,27/06/2024,27/06/2024 21:50,27/06/2024 22:50
Ana Roxanne,Thursday,Tree Stage,44,51,21:55 - 22:50,21:55,22:50,27/06/2024,27/06/2024,27/06/2024 21:55,27/06/2024 22:50
Leo,Thursday,Circus Big Top,57,34,21:58 - 22:04,21:58,22:04,27/06/2024,27/06/2024,27/06/2024 21:58,27/06/2024 22:04
Conviction,Thursday,Arrivals,0,0,22:00 - 23:00,22:00,23:00,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 23:00
Yourboykiran,Thursday,Babylon Uprising,0,0,22:00 - 23:00,22:00,23:00,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 23:00
Murphys Law,Thursday,Blind Tiger,0,0,22:00 - 22:45,22:00,22:45,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 22:45
Fulu Miziki,Thursday,Carhenge,58,36,22:00 - 22:30,22:00,22:30,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 22:30
Afriquoi,Thursday,Croissant Neuf,55,21,22:00 - 23:00,22:00,23:00,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 23:00
Dj Spamalam,Thursday,Lunched Out Lizards,0,0,22:00 - 23:00,22:00,23:00,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 23:00
Fixx: Hazel Marimba,Thursday,Nomad,0,0,22:00 - 23:00,22:00,23:00,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 23:00
Drifty,Thursday,Platform 23,0,0,22:00 - 23:00,22:00,23:00,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 23:00
Sleaze,Thursday,Strummerville,48,12,22:00 - 22:40,22:00,22:40,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 22:40
Kiskadee,Thursday,The Hive,0,0,22:00 - 23:00,22:00,23:00,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 23:00
Pronghorn,Thursday,The Rocket Lounge,64,16,22:00 - 23:00,22:00,23:00,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 23:00
"Kitten Club, Artemis, Esme Banks, Demetria, Eresid",Thursday,The Salon Carousel,0,0,22:00 - 23:00,22:00,23:00,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 23:00
"That Ray'S Trans Cabaret. Performers: That Ray, Purina Alpha, Co Kendrah, Anju Marie",Thursday,The Sistxrhood,0,0,22:00 - 00:00,22:00,00:00,27/06/2024,28/06/2024,27/06/2024 22:00,28/06/2024 00:00
Disrupta B2B Sota,Thursday,The Temple,0,0,22:00 - 23:00,22:00,23:00,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 23:00
Glowbros,Thursday,Walkabouts,60,33,22:00 - 00:00,22:00,00:00,27/06/2024,28/06/2024,27/06/2024 22:00,28/06/2024 00:00
Corvus Angelicus,Thursday,Walkabouts,60,33,22:00 - 22:45,22:00,22:45,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 22:45
High Flyers,Thursday,Walkabouts,60,33,22:00 - 22:45,22:00,22:45,27/06/2024,27/06/2024,27/06/2024 22:00,27/06/2024 22:45
Gecko,Thursday,The Astrolabe Theatre,0,0,22:05 - 22:15,22:05,22:15,27/06/2024,27/06/2024,27/06/2024 22:05,27/06/2024 22:15
United Queendom,Thursday,Circus Big Top,57,34,22:09 - 23:09,22:09,23:09,27/06/2024,27/06/2024,27/06/2024 22:09,27/06/2024 23:09
Bress Underground,Thursday,Nyc Downlow,0,0,22:10 - 23:35,22:10,23:35,27/06/2024,27/06/2024,27/06/2024 22:10,27/06/2024 23:35
Friction,Thursday,Glade Dome,49,29,22:15 - 23:15,22:15,23:15,27/06/2024,27/06/2024,27/06/2024 22:15,27/06/2024 23:15
Lambrini Girls,Thursday,Peace Stage,0,0,22:15 - 23:00,22:15,23:00,27/06/2024,27/06/2024,27/06/2024 22:15,27/06/2024 23:00
Wonderment Presents: Elevate,Thursday,Scissors,42,21,22:15 - 23:15,22:15,23:15,27/06/2024,27/06/2024,27/06/2024 22:15,27/06/2024 23:15
Flash Bang Brass,Thursday,The Astrolabe Theatre,0,0,22:15 - 23:00,22:15,23:00,27/06/2024,27/06/2024,27/06/2024 22:15,27/06/2024 23:00
Cristale,Thursday,The Rum Shack,0,0,22:15 - 23:00,22:15,23:00,27/06/2024,27/06/2024,27/06/2024 22:15,27/06/2024 23:00
Disco Turtle & Fiery Jack Family - Parade,Thursday,Walkabouts,60,33,22:15 - 00:00,22:15,00:00,27/06/2024,28/06/2024,27/06/2024 22:15,28/06/2024 00:00
Dave Harvey B2B Felix Dickinson,Thursday,Assembly,40,42,22:30 - 00:30,22:30,00:30,27/06/2024,28/06/2024,27/06/2024 22:30,28/06/2024 00:30
Land Of The Giants,Thursday,Bread And Roses,0,0,22:30 - 23:30,22:30,23:30,27/06/2024,27/06/2024,27/06/2024 22:30,27/06/2024 23:30
Ethan Forks,Thursday,Deluxe Diner,64,17,22:30 - 00:00,22:30,00:00,27/06/2024,28/06/2024,27/06/2024 22:30,28/06/2024 00:00
Nadine Noor [Foundation Fm Takeover],Thursday,Firmly Rooted,43,43,22:30 - 00:00,22:30,00:00,27/06/2024,28/06/2024,27/06/2024 22:30,28/06/2024 00:00
Atchin Tan Presents: Born On Road,Thursday,Flying Bus,0,0,22:30 - 00:00,22:30,00:00,27/06/2024,28/06/2024,27/06/2024 22:30,28/06/2024 00:00
Jayda G,Thursday,Greenpeace,55,26,22:30 - 00:00,22:30,00:00,27/06/2024,28/06/2024,27/06/2024 22:30,28/06/2024 00:00
Takeover,Thursday,Kinetic,0,0,22:30 - 23:30,22:30,23:30,27/06/2024,27/06/2024,27/06/2024 22:30,27/06/2024 23:30
Mia Koden B2B Tash Lc,Thursday,Levels,42,44,22:30 - 00:00,22:30,00:00,27/06/2024,28/06/2024,27/06/2024 22:30,28/06/2024 00:00
Amlass Babat B2B Arthi [Dialled In Takeover],Thursday,Lonely Hearts Club,44,41,22:30 - 23:45,22:30,23:45,27/06/2024,27/06/2024,27/06/2024 22:30,27/06/2024 23:45
Eats Everything,Thursday,Stonebridge Bar,42,18,22:30 - 00:00,22:30,00:00,27/06/2024,28/06/2024,27/06/2024 22:30,28/06/2024 00:00
Professor Sprout,Thursday,Village Inn,0,0,22:30 - 00:00,22:30,00:00,27/06/2024,28/06/2024,27/06/2024 22:30,28/06/2024 00:00
The Birds,Thursday,Walkabouts,60,33,22:30 - 23:15,22:30,23:15,27/06/2024,27/06/2024,27/06/2024 22:30,27/06/2024 23:15
Freddie And The Freeloaders,Thursday,West Holts Bar,59,29,22:30 - 00:00,22:30,00:00,27/06/2024,28/06/2024,27/06/2024 22:30,28/06/2024 00:00
The Menendez Brothers (Dj Set),Thursday,Wishing Well,42,20,22:30 - 23:30,22:30,23:30,27/06/2024,27/06/2024,27/06/2024 22:30,27/06/2024 23:30
Diddy Sweg,Thursday,The Bandstand,56,38,22:40 - 23:30,22:40,23:30,27/06/2024,27/06/2024,27/06/2024 22:40,27/06/2024 23:30
P-Rallel,Thursday,Blind Tiger,0,0,22:45 - 23:30,22:45,23:30,27/06/2024,27/06/2024,27/06/2024 22:45,27/06/2024 23:30
Violeta Vicci,Thursday,Tree Stage,44,51,22:50 - 23:50,22:50,23:50,27/06/2024,27/06/2024,27/06/2024 22:50,27/06/2024 23:50
Bobby Friction,Thursday,Arrivals,0,0,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
Danny Rankin,Thursday,Babylon Uprising,0,0,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
John Carter,Thursday,Bbc Music Introducing,45,44,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
Celebrating Annie,Thursday,Bbc Music Introducing,45,44,23:00 - 02:30,23:00,02:30,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 02:30
Bass6'S Shout Along Choir (Come Join In!) Tv & Movie Themes (Blendid Takeover),Thursday,Cornish Arms,0,0,23:00 - 23:30,23:00,23:30,27/06/2024,27/06/2024,27/06/2024 23:00,27/06/2024 23:30
Lance Desardi (Live),Thursday,Genosys,0,0,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
Mall Grab,Thursday,Glade,51,29,23:00 - 00:30,23:00,00:30,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:30
Latin Party,Thursday,Glasto Latino,58,27,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
Drass,Thursday,Laboratory Stage,0,0,23:00 - 23:55,23:00,23:55,27/06/2024,27/06/2024,27/06/2024 23:00,27/06/2024 23:55
Mama Moonshine,Thursday,Lunched Out Lizards,0,0,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
The Scribes,Thursday,Mandala Stage,0,0,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
Drifty B2B Kesh,Thursday,Mez Yard,0,0,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
Booty Bass X Popola: Garoess X Thai Chi,Thursday,Nomad,0,0,23:00 - 23:30,23:00,23:30,27/06/2024,27/06/2024,27/06/2024 23:00,27/06/2024 23:30
Mista Trick,Thursday,Peace Stage,0,0,23:00 - 23:30,23:00,23:30,27/06/2024,27/06/2024,27/06/2024 23:00,27/06/2024 23:30
This Is Spinal Tap 40Th Anniversary + Video Intro With Rob Reiner 15,Thursday,Pilton Palais Cinema,64,36,23:00 - 00:25,23:00,00:25,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:25
Amancai,Thursday,Platform 23,0,0,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
Dixon,Thursday,San Remo,45,47,23:00 - 01:00,23:00,01:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 01:00
Fat Dog,Thursday,Strummerville,48,12,23:00 - 23:40,23:00,23:40,27/06/2024,27/06/2024,27/06/2024 23:00,27/06/2024 23:40
Hiveborn,Thursday,The Hive,0,0,23:00 - 03:00,23:00,03:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 03:00
Twice Shy,Thursday,The Meatrack,0,0,23:00 - 01:00,23:00,01:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 01:00
Guns Of Navarone,Thursday,The Rocket Lounge,64,16,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
Mc Chunky,Thursday,The Rum Shack,0,0,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
Ivy,Thursday,The Salon Carousel,0,0,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
"10 Yrs Of Jungle Cakes - Burt Cope, Deekline, Ed Solo & Maddy V",Thursday,The Temple,0,0,23:00 - 00:30,23:00,00:30,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:30
Mihail,Thursday,Toad Hall,0,0,23:00 - 00:00,23:00,00:00,27/06/2024,28/06/2024,27/06/2024 23:00,28/06/2024 00:00
Fairy Godmother And The Tooth Fairy,Thursday,Walkabouts,60,33,23:00 - 23:45,23:00,23:45,27/06/2024,27/06/2024,27/06/2024 23:00,27/06/2024 23:45
Giant Egret,Thursday,Walkabouts,60,33,23:00 - 23:45,23:00,23:45,27/06/2024,27/06/2024,27/06/2024 23:00,27/06/2024 23:45
High Flyers,Thursday,Walkabouts,60,33,23:00 - 23:45,23:00,23:45,27/06/2024,27/06/2024,27/06/2024 23:00,27/06/2024 23:45
Neon Moon- Paradise Circus,Thursday,Sensation Seekers Stage,0,0,23:05 - 23:50,23:05,23:50,27/06/2024,27/06/2024,27/06/2024 23:05,27/06/2024 23:50
Berthrands Toys,Thursday,The Astrolabe Theatre,0,0,23:10 - 00:10,23:10,00:10,27/06/2024,28/06/2024,27/06/2024 23:10,28/06/2024 00:10
Feeding The Fish,Thursday,Circus Big Top,57,34,23:14 - 23:22,23:14,23:22,27/06/2024,27/06/2024,27/06/2024 23:14,27/06/2024 23:22
Kanine,Thursday,Glade Dome,49,29,23:15 - 00:25,23:15,00:25,27/06/2024,28/06/2024,27/06/2024 23:15,28/06/2024 00:25
Blawan,Thursday,Iicon,66,21,23:15 - 01:15,23:15,01:15,27/06/2024,28/06/2024,27/06/2024 23:15,28/06/2024 01:15
Denham Audio,Thursday,Blind Tiger,0,0,23:30 - 00:15,23:30,00:15,27/06/2024,28/06/2024,27/06/2024 23:30,28/06/2024 00:15
Beatbox Collective (Blendid Takeover),Thursday,Cornish Arms,0,0,23:30 - 00:00,23:30,00:00,27/06/2024,28/06/2024,27/06/2024 23:30,28/06/2024 00:00
Ying (Eastern Margins),Thursday,Kinetic,0,0,23:30 - 00:30,23:30,00:30,27/06/2024,28/06/2024,27/06/2024 23:30,28/06/2024 00:30
Booty Bass X Popola: Cheza Lucina,Thursday,Nomad,0,0,23:30 - 00:00,23:30,00:00,27/06/2024,28/06/2024,27/06/2024 23:30,28/06/2024 00:00
An Dannaa Dub,Thursday,Peace Stage,0,0,23:30 - 00:15,23:30,00:15,27/06/2024,28/06/2024,27/06/2024 23:30,28/06/2024 00:15
Andy Hatman,Thursday,The Taphouse,0,0,23:30 - 01:00,23:30,01:00,27/06/2024,28/06/2024,27/06/2024 23:30,28/06/2024 01:00
Corvus Angelicus,Thursday,Walkabouts,60,33,23:30 - 00:15,23:30,00:15,27/06/2024,28/06/2024,27/06/2024 23:30,28/06/2024 00:15
Disco Turtle,Thursday,Walkabouts,60,33,23:30 - 01:00,23:30,01:00,27/06/2024,28/06/2024,27/06/2024 23:30,28/06/2024 01:00
Jayahadadream,Thursday,Wishing Well,42,20,23:30 - 00:30,23:30,00:30,27/06/2024,28/06/2024,27/06/2024 23:30,28/06/2024 00:30
Cirque Du Vulgar,Thursday,Circus Big Top,57,34,23:32 - 00:42,23:32,00:42,27/06/2024,28/06/2024,27/06/2024 23:32,28/06/2024 00:42
Greg Belson,Thursday,Nyc Downlow,0,0,23:40 - 00:55,23:40,00:55,27/06/2024,28/06/2024,27/06/2024 23:40,28/06/2024 00:55
Gracie T B2B Shivum Sharma [Dialled In Takeover],Thursday,Lonely Hearts Club,44,41,23:45 - 01:00,23:45,01:00,27/06/2024,28/06/2024,27/06/2024 23:45,28/06/2024 01:00
Dragiators,Thursday,Bread And Roses,0,0,23:50 - 01:30,23:50,01:30,27/06/2024,28/06/2024,27/06/2024 23:50,28/06/2024 01:30
The Orb,Thursday,Tree Stage,44,51,23:50 - 00:50,23:50,00:50,27/06/2024,28/06/2024,27/06/2024 23:50,28/06/2024 00:50
Dj Mimi B2B K. Monday,Friday,Arrivals,0,0,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Double O,Friday,Babylon Uprising,0,0,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Nick The Hedge,Friday,Blind Tiger,0,0,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Compère: Mc Onyx Fatale,Friday,Cabaret,62,26,00:00 - 02:00,00:00,02:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 02:00
The Cocoa Butter Club,Friday,Cabaret,62,26,00:00 - 02:00,00:00,02:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 02:00
Woody Cook X Truth Tribe (Blendid Takeover),Friday,Cornish Arms,0,0,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Noel Watson,Friday,Deluxe Diner,64,17,00:00 - 01:30,00:00,01:30,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:30
Apiento,Friday,Firmly Rooted,43,43,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Chris Stussy,Friday,Glade,51,29,00:00 - 01:30,00:00,01:30,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:30
Kilimanjaro,Friday,Glade Dome,49,29,00:00 - 01:30,00:00,01:30,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:30
Haila Y Su Orquesta,Friday,Glasto Latino,58,27,00:00 - 01:30,00:00,01:30,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:30
Charli Xcx,Friday,Levels,42,44,00:00 - 01:30,00:00,01:30,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:30
Pxssy Palace: Mya Mehmi,Friday,Nomad,0,0,00:00 - 01:10,00:00,01:10,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:10
Alex Mills,Friday,Nowhere,0,0,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Loominus,Friday,Sensation Seekers Stage,0,0,00:00 - 00:15,00:00,00:15,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 00:15
Dresden (Manfredas & Ivan Smagghe),Friday,Stonebridge Bar,42,18,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Mark Sinclair,Friday,Strummerville,48,12,00:00 - 01:20,00:00,01:20,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:20
Berthrands Toys,Friday,The Astrolabe Theatre,0,0,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Fülü,Friday,The Bandstand,56,38,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
N'Famady Kouyaté,Friday,The Hive,0,0,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
J.Aria,Friday,The Meatrack,0,0,00:00 - 01:30,00:00,01:30,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:30
Red Hot Riot,Friday,The Rocket Lounge,64,16,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Kaisha,Friday,The Salon Carousel,0,0,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Rinse 30Th Anniversary - Girls Don'T Sync,Friday,The Temple,0,0,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Tolstoy,Friday,Toad Hall,0,0,00:00 - 01:00,00:00,01:00,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 01:00
Kmru,Friday,Tree Stage,44,51,00:00 - 00:50,00:00,00:50,29/06/2024,29/06/2024,28/06/2024 00:00,29/06/2024 00:50
Just A Ride,Friday,Outside Circus Stage,59,33,00:07 - 00:19,00:07,00:19,29/06/2024,29/06/2024,28/06/2024 00:07,29/06/2024 00:19
United Queendom,Friday,Circus Big Top,57,34,00:10 - 01:10,00:10,01:10,29/06/2024,29/06/2024,28/06/2024 00:10,29/06/2024 01:10
Sleaze,Friday,Bimble Inn,41,16,00:15 - 01:15,00:15,01:15,29/06/2024,29/06/2024,28/06/2024 00:15,29/06/2024 01:15
Moonchild Sannelly,Friday,Peace Stage,0,0,00:15 - 01:00,00:15,01:00,29/06/2024,29/06/2024,28/06/2024 00:15,29/06/2024 01:00
Mercedes Benson,Friday,The Rum Shack,0,0,00:15 - 01:30,00:15,01:30,29/06/2024,29/06/2024,28/06/2024 00:15,29/06/2024 01:30
Brownton Abbey - Alex Fincher,Friday,The Sistxrhood,0,0,00:15 - 00:45,00:15,00:45,29/06/2024,29/06/2024,28/06/2024 00:15,29/06/2024 00:45
Aerial High Jinks,Friday,Outside Circus Stage,59,33,00:24 - 00:32,00:24,00:32,29/06/2024,29/06/2024,28/06/2024 00:24,29/06/2024 00:32
Wheel Of Four Tunes,Friday,Sensation Seekers Stage,0,0,00:25 - 01:10,00:25,01:10,29/06/2024,29/06/2024,28/06/2024 00:25,29/06/2024 01:10
6 Music Indie Forever With Nathan Shepherd & Emily Pilbeam,Friday,Bbc Music Introducing,45,44,00:30 - 02:30,00:30,02:30,29/06/2024,29/06/2024,28/06/2024 00:30,29/06/2024 02:30
Mellowmatic,Friday,Lunched Out Lizards,0,0,00:30 - 01:30,00:30,01:30,29/06/2024,29/06/2024,28/06/2024 00:30,29/06/2024 01:30
Baby Driver + Intro-Q&A With Director Edgar Wright 15,Friday,Pilton Palais Cinema,64,36,00:30 - 02:40,00:30,02:40,29/06/2024,29/06/2024,28/06/2024 00:30,29/06/2024 02:40
Porij,Friday,Scissors,42,21,00:30 - 01:30,00:30,01:30,29/06/2024,29/06/2024,28/06/2024 00:30,29/06/2024 01:30
Area 51,Friday,Outside Circus Stage,59,33,00:37 - 00:49,00:37,00:49,29/06/2024,29/06/2024,28/06/2024 00:37,29/06/2024 00:49
Haai B2B Ki/Ki,Friday,Arcadia,41,25,00:45 - 01:50,00:45,01:50,29/06/2024,29/06/2024,28/06/2024 00:45,29/06/2024 01:50
Brownton Abbey - Thempress,Friday,The Sistxrhood,0,0,00:45 - 01:15,00:45,01:15,29/06/2024,29/06/2024,28/06/2024 00:45,29/06/2024 01:15
Rebecca Vasmant,Friday,West Holts Bar,59,29,00:45 - 01:10,00:45,01:10,29/06/2024,29/06/2024,28/06/2024 00:45,29/06/2024 01:10
Max Cooper Ambient Live Av,Friday,Tree Stage,44,51,00:50 - 02:50,00:50,02:50,29/06/2024,29/06/2024,28/06/2024 00:50,29/06/2024 02:50
Raves R Us,Friday,Outside Circus Stage,59,33,00:54 - 01:39,00:54,01:39,29/06/2024,29/06/2024,28/06/2024 00:54,29/06/2024 01:39
Nabihah Iqbal ( Dj Set),Friday,Arrivals,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Palms Trax,Friday,Assembly,40,42,01:00 - 03:00,01:00,03:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 03:00
Teezle B2B Caption,Friday,Babylon Uprising,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Anna Prank,Friday,Blind Tiger,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Old Time Sailors,Friday,Bread And Roses,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Casper Gomez Presents Freedom,Friday,Cornish Arms,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Suntou Susso,Friday,Croissant Neuf,55,21,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Tba,Friday,Firmly Rooted,43,43,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Dyen,Friday,Flying Bus,0,0,01:00 - 02:30,01:00,02:30,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:30
Confidence Man Presents: Active Scenes. Confidence Man,Friday,Greenpeace,55,26,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Iicon Av:3D,Friday,Iicon,66,21,01:00 - 01:15,01:00,01:15,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 01:15
Gorgon City,Friday,Lonely Hearts Club,44,41,01:00 - 03:00,01:00,03:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 03:00
The Kaiden Noland Band,Friday,Mandala Stage,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Copperdollar: The Spirits Of Mezcal (Show),Friday,Mez Yard,0,0,01:00 - 03:00,01:00,03:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 03:00
Hagan,Friday,Nowhere,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Rush Davis,Friday,Nyc Downlow,0,0,01:00 - 02:45,01:00,02:45,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:45
Deaf Rave,Friday,Peace Stage,0,0,01:00 - 01:30,01:00,01:30,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 01:30
Dj Danifox,Friday,Platform 23,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Daphni,Friday,San Remo,45,47,01:00 - 03:00,01:00,03:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 03:00
Gene On Earth,Friday,Stonebridge Bar,42,18,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Flash Bang Brass,Friday,The Astrolabe Theatre,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Frank Harvey Trio,Friday,The Rocket Lounge,64,16,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Kelvin 373 B2B Selecta Jman,Friday,The Salon Carousel,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Andy Hatman,Friday,The Taphouse,0,0,01:00 - 03:00,01:00,03:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 03:00
Rinse 30Th Anniversary - Katy B Live,Friday,The Temple,0,0,01:00 - 01:30,01:00,01:30,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 01:30
My Mate Kate And Gentleman George Present ""Bangers And Mash"",Friday,Village Inn,0,0,01:00 - 02:00,01:00,02:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 02:00
Glowbros,Friday,Walkabouts,60,33,01:00 - 03:00,01:00,03:00,29/06/2024,29/06/2024,28/06/2024 01:00,29/06/2024 03:00
The Filthy Six,Friday,West Holts Bar,59,29,01:10 - 02:10,01:10,02:10,29/06/2024,29/06/2024,28/06/2024 01:10,29/06/2024 02:10
Bicep Pres Chroma (Av Dj Set),Friday,Iicon,66,21,01:15 - 02:45,01:15,02:45,29/06/2024,29/06/2024,28/06/2024 01:15,29/06/2024 02:45
Brownton Abbey - Ray Young,Friday,The Sistxrhood,0,0,01:15 - 01:30,01:15,01:30,29/06/2024,29/06/2024,28/06/2024 01:15,29/06/2024 01:30
Pxssy Palace: Ryan Lovell,Friday,Nomad,0,0,01:20 - 02:30,01:20,02:30,29/06/2024,29/06/2024,28/06/2024 01:20,29/06/2024 02:30
Loominus,Friday,Sensation Seekers Stage,0,0,01:20 - 01:35,01:20,01:35,29/06/2024,29/06/2024,28/06/2024 01:20,29/06/2024 01:35
Noble & Heath,Friday,Deluxe Diner,64,17,01:30 - 03:00,01:30,03:00,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 03:00
Bashkka,Friday,Genosys,0,0,01:30 - 03:30,01:30,03:30,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 03:30
Kolter,Friday,Glade,51,29,01:30 - 03:00,01:30,03:00,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 03:00
Charisse C,Friday,Glade Dome,49,29,01:30 - 02:55,01:30,02:55,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 02:55
Latin Party,Friday,Glasto Latino,58,27,01:30 - 03:00,01:30,03:00,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 03:00
Optimo [Espacio],Friday,Levels,42,44,01:30 - 03:00,01:30,03:00,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 03:00
Mista Trick,Friday,Lunched Out Lizards,0,0,01:30 - 02:30,01:30,02:30,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 02:30
Will Skillz,Friday,Strummerville,48,12,01:30 - 03:00,01:30,03:00,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 03:00
King Dinosaur,Friday,The Hive,0,0,01:30 - 02:30,01:30,02:30,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 02:30
Moxie,Friday,The Meatrack,0,0,01:30 - 03:00,01:30,03:00,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 03:00
Coco Em,Friday,The Rum Shack,0,0,01:30 - 02:30,01:30,02:30,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 02:30
Mela Sounds,Friday,The Sistxrhood,0,0,01:30 - 02:30,01:30,02:30,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 02:30
Rinse 30Th Anniversary - Jyoty,Friday,The Temple,0,0,01:30 - 02:30,01:30,02:30,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 02:30
Loonaloop,Friday,Toad Hall,0,0,01:30 - 02:30,01:30,02:30,29/06/2024,29/06/2024,28/06/2024 01:30,29/06/2024 02:30
Oh My God! It'S The Church,Friday,Sensation Seekers Stage,0,0,01:45 - 02:45,01:45,02:45,29/06/2024,29/06/2024,28/06/2024 01:45,29/06/2024 02:45
Amelie Lens,Friday,Arcadia,41,25,01:50 - 03:00,01:50,03:00,29/06/2024,29/06/2024,28/06/2024 01:50,29/06/2024 03:00
Manara,Friday,Arrivals,0,0,02:00 - 03:00,02:00,03:00,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:00
Kenneth,Friday,Babylon Uprising,0,0,02:00 - 02:45,02:00,02:45,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 02:45
Das Brass,Friday,Bimble Inn,41,16,02:00 - 03:00,02:00,03:00,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:00
Serkus,Friday,Blind Tiger,0,0,02:00 - 03:00,02:00,03:00,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:00
Andy Blake,Friday,Cornish Arms,0,0,02:00 - 03:00,02:00,03:00,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:00
Dreems & Jacoby,Friday,Firmly Rooted,43,43,02:00 - 03:00,02:00,03:00,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:00
Confidence Man Presents: Active Scenes. Confidence Man B2B O'Flynn,Friday,Greenpeace,55,26,02:00 - 03:00,02:00,03:00,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:00
Kitty Amor,Friday,Nowhere,0,0,02:00 - 03:00,02:00,03:00,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:00
Manuka Honey,Friday,Platform 23,0,0,02:00 - 03:00,02:00,03:00,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:00
Niks,Friday,Stonebridge Bar,42,18,02:00 - 03:00,02:00,03:00,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:00
The Trojans,Friday,The Rocket Lounge,64,16,02:00 - 03:45,02:00,03:45,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:45
Aries,Friday,The Salon Carousel,0,0,02:00 - 03:00,02:00,03:00,29/06/2024,29/06/2024,28/06/2024 02:00,29/06/2024 03:00
Guy.In.Glasses,Friday,Peace Stage,0,0,02:15 - 02:45,02:15,02:45,29/06/2024,29/06/2024,28/06/2024 02:15,29/06/2024 02:45
Azyr,Friday,Flying Bus,0,0,02:30 - 04:00,02:30,04:00,29/06/2024,29/06/2024,28/06/2024 02:30,29/06/2024 04:00
Hiveborn,Friday,The Hive,0,0,02:30 - 03:00,02:30,03:00,29/06/2024,29/06/2024,28/06/2024 02:30,29/06/2024 03:00
Dj Lag,Friday,The Rum Shack,0,0,02:30 - 03:30,02:30,03:30,29/06/2024,29/06/2024,28/06/2024 02:30,29/06/2024 03:30
Toya Delazy,Friday,The Sistxrhood,0,0,02:30 - 03:30,02:30,03:30,29/06/2024,29/06/2024,28/06/2024 02:30,29/06/2024 03:30
Rinse 30Th Anniversary - Dj Ez B2B Sammy Virji,Friday,The Temple,0,0,02:30 - 04:00,02:30,04:00,29/06/2024,29/06/2024,28/06/2024 02:30,29/06/2024 04:00
Afriquoi,Friday,Peace Stage,0,0,02:45 - 03:30,02:45,03:30,29/06/2024,29/06/2024,28/06/2024 02:45,29/06/2024 03:30
Dj Python,Friday,Iicon,66,21,02:50 - 04:20,02:50,04:20,29/06/2024,29/06/2024,28/06/2024 02:50,29/06/2024 04:20
Leeon,Friday,Nyc Downlow,0,0,02:50 - 04:15,02:50,04:15,29/06/2024,29/06/2024,28/06/2024 02:50,29/06/2024 04:15
Baalti,Friday,Arrivals,0,0,03:00 - 04:00,03:00,04:00,29/06/2024,29/06/2024,28/06/2024 03:00,29/06/2024 04:00
T Cuts,Friday,Blind Tiger,0,0,03:00 - 04:00,03:00,04:00,29/06/2024,29/06/2024,28/06/2024 03:00,29/06/2024 04:00
Roxanne Roll,Friday,Deluxe Diner,64,17,03:00 - 04:30,03:00,04:30,29/06/2024,29/06/2024,28/06/2024 03:00,29/06/2024 04:30
Village Cuts,Friday,Mez Yard,0,0,03:00 - 04:00,03:00,04:00,29/06/2024,29/06/2024,28/06/2024 03:00,29/06/2024 04:00
Camelphat B2B Tba,Friday,Nowhere,0,0,03:00 - 04:30,03:00,04:30,29/06/2024,29/06/2024,28/06/2024 03:00,29/06/2024 04:30
Rosa Pistola,Friday,Platform 23,0,0,03:00 - 04:00,03:00,04:00,29/06/2024,29/06/2024,28/06/2024 03:00,29/06/2024 04:00
Mella Dee B2B Saoirse,Friday,Stonebridge Bar,42,18,03:00 - 04:00,03:00,04:00,29/06/2024,29/06/2024,28/06/2024 03:00,29/06/2024 04:00
Grace B2B Andy Cato,Friday,The Meatrack,0,0,03:00 - 04:30,03:00,04:30,29/06/2024,29/06/2024,28/06/2024 03:00,29/06/2024 04:30
Mandidextrous,Friday,The Salon Carousel,0,0,03:00 - 04:00,03:00,04:00,29/06/2024,29/06/2024,28/06/2024 03:00,29/06/2024 04:00
Twisted Time Machines,Friday,Bimble Inn,41,16,03:30 - 05:00,03:30,05:00,29/06/2024,29/06/2024,28/06/2024 03:30,29/06/2024 05:00
Midland,Friday,Genosys,0,0,03:30 - 06:00,03:30,06:00,29/06/2024,29/06/2024,28/06/2024 03:30,29/06/2024 06:00
Fizzy Gillespie,Friday,Peace Stage,0,0,03:30 - 04:30,03:30,04:30,29/06/2024,29/06/2024,28/06/2024 03:30,29/06/2024 04:30
Anna Prior,Friday,Scissors,42,21,03:30 - 04:30,03:30,04:30,29/06/2024,29/06/2024,28/06/2024 03:30,29/06/2024 04:30
Izzi B2B Chandé (Daytimers),Friday,The Rum Shack,0,0,03:30 - 04:30,03:30,04:30,29/06/2024,29/06/2024,28/06/2024 03:30,29/06/2024 04:30
I Am Fya,Friday,The Sistxrhood,0,0,03:30 - 04:30,03:30,04:30,29/06/2024,29/06/2024,28/06/2024 03:30,29/06/2024 04:30
Pxssy Palace: Emma Korantema,Friday,Nomad,0,0,03:40 - 04:50,03:40,04:50,29/06/2024,29/06/2024,28/06/2024 03:40,29/06/2024 04:50
Old Time Sailors,Friday,The Rocket Lounge,64,16,03:45 - 05:00,03:45,05:00,29/06/2024,29/06/2024,28/06/2024 03:45,29/06/2024 05:00
Gracie T,Friday,Arrivals,0,0,04:00 - 05:00,04:00,05:00,29/06/2024,29/06/2024,28/06/2024 04:00,29/06/2024 05:00
Hardcore Energy Takeover: Origin8A & Propa B2B Hypershe,Friday,Blind Tiger,0,0,04:00 - 06:00,04:00,06:00,29/06/2024,29/06/2024,28/06/2024 04:00,29/06/2024 06:00
Ru Robinson,Friday,Mez Yard,0,0,04:00 - 06:00,04:00,06:00,29/06/2024,29/06/2024,28/06/2024 04:00,29/06/2024 06:00
Omega Nebula,Friday,Peace Stage,0,0,04:00 - 04:45,04:00,04:45,29/06/2024,29/06/2024,28/06/2024 04:00,29/06/2024 04:45
Benji B,Friday,Platform 23,0,0,04:00 - 05:00,04:00,05:00,29/06/2024,29/06/2024,28/06/2024 04:00,29/06/2024 05:00
Lukas Wigflex,Friday,Stonebridge Bar,42,18,04:00 - 05:00,04:00,05:00,29/06/2024,29/06/2024,28/06/2024 04:00,29/06/2024 05:00
Samurai Breaks,Friday,The Salon Carousel,0,0,04:00 - 05:00,04:00,05:00,29/06/2024,29/06/2024,28/06/2024 04:00,29/06/2024 05:00
Rinse 30Th Anniversary - Interplanetary Criminal,Friday,The Temple,0,0,04:00 - 05:00,04:00,05:00,29/06/2024,29/06/2024,28/06/2024 04:00,29/06/2024 05:00
Freakenstien,Friday,Iicon,66,21,04:20 - 06:00,04:20,06:00,29/06/2024,29/06/2024,28/06/2024 04:20,29/06/2024 06:00
James Hillard,Friday,Nyc Downlow,0,0,04:20 - 06:00,04:20,06:00,29/06/2024,29/06/2024,28/06/2024 04:20,29/06/2024 06:00
"Nicky,Nicky",Friday,Deluxe Diner,64,17,04:30 - 06:00,04:30,06:00,29/06/2024,29/06/2024,28/06/2024 04:30,29/06/2024 06:00
Friday Finale,Friday,Nowhere,0,0,04:30 - 06:00,04:30,06:00,29/06/2024,29/06/2024,28/06/2024 04:30,29/06/2024 06:00
Michelle Manetti,Friday,Scissors,42,21,04:30 - 06:00,04:30,06:00,29/06/2024,29/06/2024,28/06/2024 04:30,29/06/2024 06:00
Chris Cruse,Friday,The Meatrack,0,0,04:30 - 06:00,04:30,06:00,29/06/2024,29/06/2024,28/06/2024 04:30,29/06/2024 06:00
Daytimers Family,Friday,The Rum Shack,0,0,04:30 - 06:00,04:30,06:00,29/06/2024,29/06/2024,28/06/2024 04:30,29/06/2024 06:00
Sippin' T,Friday,The Sistxrhood,0,0,04:30 - 05:30,04:30,05:30,29/06/2024,29/06/2024,28/06/2024 04:30,29/06/2024 05:30
Mr Fitz,Friday,Peace Stage,0,0,04:45 - 05:15,04:45,05:15,29/06/2024,29/06/2024,28/06/2024 04:45,29/06/2024 05:15
Pxssy Palace: Nadine Noor,Friday,Nomad,0,0,04:50 - 06:00,04:50,06:00,29/06/2024,29/06/2024,28/06/2024 04:50,29/06/2024 06:00
Raji Rags,Friday,Arrivals,0,0,05:00 - 06:00,05:00,06:00,29/06/2024,29/06/2024,28/06/2024 05:00,29/06/2024 06:00
Nightmares On Wax (Dj Set),Friday,Platform 23,0,0,05:00 - 06:00,05:00,06:00,29/06/2024,29/06/2024,28/06/2024 05:00,29/06/2024 06:00
Downsetters,Friday,The Rocket Lounge,64,16,05:00 - 06:00,05:00,06:00,29/06/2024,29/06/2024,28/06/2024 05:00,29/06/2024 06:00
Monroller,Friday,The Salon Carousel,0,0,05:00 - 06:00,05:00,06:00,29/06/2024,29/06/2024,28/06/2024 05:00,29/06/2024 06:00
Rinse 30Th Anniversary - Hamdi,Friday,The Temple,0,0,05:00 - 06:00,05:00,06:00,29/06/2024,29/06/2024,28/06/2024 05:00,29/06/2024 06:00
Stone Cold Hustle,Friday,Peace Stage,0,0,05:15 - 06:00,05:15,06:00,29/06/2024,29/06/2024,28/06/2024 05:15,29/06/2024 06:00
Yoga Like Water With Dan Peppiatt,Friday,Humblewell Active Platform,42,21,08:30 - 09:30,08:30,09:30,28/06/2024,28/06/2024,28/06/2024 08:30,28/06/2024 09:30
Shakti Shake With Dina Cohen,Friday,Humblewell Retreat Yurt,42,21,08:45 - 09:30,08:45,09:30,28/06/2024,28/06/2024,28/06/2024 08:45,28/06/2024 09:30
Dna Puppetry Presents: Little Red & Other Tales,Friday,Kidzfield Big Top,0,0,09:30 - 10:00,09:30,10:00,28/06/2024,28/06/2024,28/06/2024 09:30,28/06/2024 10:00
Improv Voice Circle With Leti,Friday,Humblewell Active Platform,42,21,09:45 - 10:45,09:45,10:45,28/06/2024,28/06/2024,28/06/2024 09:45,28/06/2024 10:45
Crystal Singing Bowls With Yogic Sound,Friday,Humblewell Retreat Yurt,42,21,09:45 - 10:15,09:45,10:15,28/06/2024,28/06/2024,28/06/2024 09:45,28/06/2024 10:15
Nipsy,Friday,Cornish Arms,0,0,10:00 - 12:00,10:00,12:00,28/06/2024,28/06/2024,28/06/2024 10:00,28/06/2024 12:00
Power Ballad Yoga,Friday,Greenpeace,55,26,10:00 - 11:00,10:00,11:00,28/06/2024,28/06/2024,28/06/2024 10:00,28/06/2024 11:00
Emma-Jean Thackray,Friday,San Remo,45,47,10:00 - 11:30,10:00,11:30,28/06/2024,28/06/2024,28/06/2024 10:00,28/06/2024 11:30
Vulture Capitalism - Grace Blakely With Jack Symes,Friday,Speakers Forum,0,0,10:00 - 11:00,10:00,11:00,28/06/2024,28/06/2024,28/06/2024 10:00,28/06/2024 11:00
Andy And The Odd Socks,Friday,Kidzfield Big Top,0,0,10:15 - 10:50,10:15,10:50,28/06/2024,28/06/2024,28/06/2024 10:15,28/06/2024 10:50
Bell And Bullock,Friday,Walkabouts,60,33,10:20 - 10:50,10:20,10:50,28/06/2024,28/06/2024,28/06/2024 10:20,28/06/2024 10:50
Dodgy Boys,Friday,Walkabouts,60,33,10:20 - 11:05,10:20,11:05,28/06/2024,28/06/2024,28/06/2024 10:20,28/06/2024 11:05
Tented Talk,Friday,Circus Big Top,57,34,10:30 - 11:10,10:30,11:10,28/06/2024,28/06/2024,28/06/2024 10:30,28/06/2024 11:10
Compere: Chris Barltrop,Friday,Circus Big Top,57,34,10:30 - 12:30,10:30,12:30,28/06/2024,28/06/2024,28/06/2024 10:30,28/06/2024 12:30
Art & Activism,Friday,Greenpeace (Beam),54,26,10:30 - 11:15,10:30,11:15,28/06/2024,28/06/2024,28/06/2024 10:30,28/06/2024 11:15
"Discover The Power Of Intention: A Transformative Workshop On Consciousness, Water, And Breathwork",Friday,Humblewell Retreat Yurt,42,21,10:30 - 12:00,10:30,12:00,28/06/2024,28/06/2024,28/06/2024 10:30,28/06/2024 12:00
Sounds Of Science Dj Set,Friday,Laboratory Stage,0,0,10:30 - 11:00,10:30,11:00,28/06/2024,28/06/2024,28/06/2024 10:30,28/06/2024 11:00
The Crate Stack Challenge,Friday,Outside Circus Stage,59,33,10:30 - 11:30,10:30,11:30,28/06/2024,28/06/2024,28/06/2024 10:30,28/06/2024 11:30
Fire Fighters!,Friday,Walkabouts,60,33,10:30 - 11:00,10:30,11:00,28/06/2024,28/06/2024,28/06/2024 10:30,28/06/2024 11:00
Flamingos,Friday,Walkabouts,60,33,10:30 - 11:15,10:30,11:15,28/06/2024,28/06/2024,28/06/2024 10:30,28/06/2024 11:15
Clamour Of Bells,Friday,Walkabouts,60,33,10:35 - 11:20,10:35,11:20,28/06/2024,28/06/2024,28/06/2024 10:35,28/06/2024 11:20
The Newspaper Men,Friday,Walkabouts,60,33,10:35 - 11:20,10:35,11:20,28/06/2024,28/06/2024,28/06/2024 10:35,28/06/2024 11:20
The Fabularium - Carnival Of Animals,Friday,Walkabouts,60,33,10:45 - 11:30,10:45,11:30,28/06/2024,28/06/2024,28/06/2024 10:45,28/06/2024 11:30
The Smallest Race On Earth,Friday,Walkabouts,60,33,10:50 - 11:20,10:50,11:20,28/06/2024,28/06/2024,28/06/2024 10:50,28/06/2024 11:20
The Sky At Day,Friday,Walkabouts,60,33,10:50 - 11:35,10:50,11:35,28/06/2024,28/06/2024,28/06/2024 10:50,28/06/2024 11:35
Ukelele Thrash Mob,Friday,Walkabouts,60,33,10:50 - 11:35,10:50,11:35,28/06/2024,28/06/2024,28/06/2024 10:50,28/06/2024 11:35
Compère: Sally-Anne Hayward,Friday,The Astrolabe Theatre,0,0,10:55 - 15:30,10:55,15:30,28/06/2024,28/06/2024,28/06/2024 10:55,28/06/2024 15:30
The Crows,Friday,Walkabouts,60,33,10:55 - 11:25,10:55,11:25,28/06/2024,28/06/2024,28/06/2024 10:55,28/06/2024 11:25
The Midwives,Friday,Walkabouts,60,33,10:55 - 11:40,10:55,11:40,28/06/2024,28/06/2024,28/06/2024 10:55,28/06/2024 11:40
Films,Friday,Atchin Tan,0,0,11:00 - 12:30,11:00,12:30,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 12:30
Jo Bucket,Friday,Carhenge,58,36,11:00 - 12:00,11:00,12:00,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 12:00
Rab Duncan,Friday,Croissant Neuf Bandstand,55,21,11:00 - 11:45,11:00,11:45,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 11:45
Georgia Mann,Friday,Free University Of Glastonbury,42,21,11:00 - 12:00,11:00,12:00,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 12:00
Om And Bass Yoga With Dina Cohen,Friday,Humblewell Active Platform,42,21,11:00 - 11:50,11:00,11:50,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 11:50
Zoe Wren,Friday,Mandala Stage,0,0,11:00 - 11:45,11:00,11:45,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 11:45
Inside Out 2 Pg,Friday,Pilton Palais Cinema,64,36,11:00 - 12:40,11:00,12:40,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 12:40
Mending Our Broken Politics - Molly Scott Cato,Friday,Speakers Forum,0,0,11:00 - 12:00,11:00,12:00,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 12:00
St Paul'S Carnival: Windrush Library Talks - The Originators,Friday,Terminal 1,0,0,11:00 - 12:30,11:00,12:30,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 12:30
The Guardian Q & A,Friday,The Astrolabe Theatre,0,0,11:00 - 11:50,11:00,11:50,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 11:50
Graham Chilcott,Friday,The Hive,0,0,11:00 - 11:30,11:00,11:30,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 11:30
Sandy Yidaki Workshop,Friday,Toad Hall,0,0,11:00 - 11:45,11:00,11:45,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 11:45
Roo'D,Friday,Walkabouts,60,33,11:00 - 11:30,11:00,11:30,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 11:30
Magical Musical Time Machine,Friday,Walkabouts,60,33,11:00 - 11:45,11:00,11:45,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 11:45
Sofia Kourtesis,Friday,West Holts Stage,57,31,11:00 - 12:00,11:00,12:00,28/06/2024,28/06/2024,28/06/2024 11:00,28/06/2024 12:00
Giant Seagulls,Friday,Walkabouts,60,33,11:05 - 11:50,11:05,11:50,28/06/2024,28/06/2024,28/06/2024 11:05,28/06/2024 11:50
The Tea Ladies On Tour,Friday,Walkabouts,60,33,11:05 - 11:50,11:05,11:50,28/06/2024,28/06/2024,28/06/2024 11:05,28/06/2024 11:50
Anyone For Tennis,Friday,Walkabouts,60,33,11:10 - 11:55,11:10,11:55,28/06/2024,28/06/2024,28/06/2024 11:10,28/06/2024 11:55
Dapper Chaps,Friday,Walkabouts,60,33,11:10 - 11:55,11:10,11:55,28/06/2024,28/06/2024,28/06/2024 11:10,28/06/2024 11:55
Range Of Motion - Kim Wildbourne,Friday,Circus Big Top,57,34,11:15 - 12:00,11:15,12:00,28/06/2024,28/06/2024,28/06/2024 11:15,28/06/2024 12:00
Roger Mcgough'S 'The Sound Collector',Friday,Kidzfield Big Top,0,0,11:15 - 11:50,11:15,11:50,28/06/2024,28/06/2024,28/06/2024 11:15,28/06/2024 11:50
Science-Based Meditation,Friday,Laboratory Stage,0,0,11:15 - 11:45,11:15,11:45,28/06/2024,28/06/2024,28/06/2024 11:15,28/06/2024 11:45
Be Prepared,Friday,Walkabouts,60,33,11:15 - 12:00,11:15,12:00,28/06/2024,28/06/2024,28/06/2024 11:15,28/06/2024 12:00
The Bad Eggs,Friday,Walkabouts,60,33,11:15 - 12:00,11:15,12:00,28/06/2024,28/06/2024,28/06/2024 11:15,28/06/2024 12:00
The Burma,Friday,Acoustic Stage,66,38,11:30 - 12:00,11:30,12:00,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:00
Mighty Mighty J,Friday,Babylon Uprising,0,0,11:30 - 12:00,11:30,12:00,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:00
Coffee With Gok Wan,Friday,Croissant Neuf,55,21,11:30 - 12:30,11:30,12:30,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:30
Alucidnation,Friday,Glade Dome,49,29,11:30 - 12:45,11:30,12:45,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:45
Greenpeace Call To Action,Friday,Greenpeace,55,26,11:30 - 12:10,11:30,12:10,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:10
Tba,Friday,Greenpeace (Beam),54,26,11:30 - 12:15,11:30,12:15,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:15
Annie Mac,Friday,Other Stage,47,34,11:30 - 12:30,11:30,12:30,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:30
Compère: Famos Bramwells,Friday,Outside Circus Stage,59,33,11:30 - 16:00,11:30,16:00,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 16:00
Gecko,Friday,Poetry&Words,0,0,11:30 - 12:00,11:30,12:00,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:00
Deptford Northern Soul Club,Friday,San Remo,45,47,11:30 - 13:00,11:30,13:00,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 13:00
Jason Vegas Butler,Friday,The Hive,0,0,11:30 - 12:00,11:30,12:00,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:00
Lynks,Friday,The Park Stage,41,19,11:30 - 12:10,11:30,12:10,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:10
Ministry Of Happy,Friday,Walkabouts,60,33,11:30 - 12:15,11:30,12:15,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:15
Natural Diversions,Friday,Walkabouts,60,33,11:30 - 12:15,11:30,12:15,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:15
Voice Of Baceprot,Friday,Woodsies,43,52,11:30 - 12:15,11:30,12:15,28/06/2024,28/06/2024,28/06/2024 11:30,28/06/2024 12:15
Circus Raj And Rajasthan Heritage Brass Band,Friday,Outside Circus Stage,59,33,11:40 - 12:10,11:40,12:10,28/06/2024,28/06/2024,28/06/2024 11:40,28/06/2024 12:10
Fairly Fresh Fish Co,Friday,Walkabouts,60,33,11:40 - 12:25,11:40,12:25,28/06/2024,28/06/2024,28/06/2024 11:40,28/06/2024 12:25
Dick Pulses Morning Rise,Friday,Sensation Seekers Stage,0,0,11:45 - 12:10,11:45,12:10,28/06/2024,28/06/2024,28/06/2024 11:45,28/06/2024 12:10
Pasha Finn & The Ellipsis,Friday,The Bandstand,56,38,11:45 - 12:15,11:45,12:15,28/06/2024,28/06/2024,28/06/2024 11:45,28/06/2024 12:15
Space Cadets,Friday,Walkabouts,60,33,11:45 - 12:30,11:45,12:30,28/06/2024,28/06/2024,28/06/2024 11:45,28/06/2024 12:30
Swyron & Desaata,Friday,Walkabouts,60,33,11:45 - 12:30,11:45,12:30,28/06/2024,28/06/2024,28/06/2024 11:45,28/06/2024 12:30
Siegfried & Joy,Friday,The Astrolabe Theatre,0,0,11:50 - 13:00,11:50,13:00,28/06/2024,28/06/2024,28/06/2024 11:50,28/06/2024 13:00
Trifleenees,Friday,Walkabouts,60,33,11:50 - 12:35,11:50,12:35,28/06/2024,28/06/2024,28/06/2024 11:50,28/06/2024 12:35
Masters Of The Kazooniverse,Friday,Walkabouts,60,33,11:50 - 13:20,11:50,13:20,28/06/2024,28/06/2024,28/06/2024 11:50,28/06/2024 13:20
Tony And Ray,Friday,A Little More Sensation,0,0,12:00 - 12:15,12:00,12:15,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:15
Mle B2B Jerry [10 Years Of Rhythm Section],Friday,Assembly,40,42,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
Gutty,Friday,Babylon Uprising,0,0,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
Open,Friday,Bimble Inn,41,16,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
Steamy Bumplings Btb Vsvn,Friday,Blind Tiger,0,0,12:00 - 12:45,12:00,12:45,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:45
Thrill Collins,Friday,Bread And Roses,0,0,12:00 - 12:40,12:00,12:40,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:40
Compère: Ian Stone,Friday,Cabaret,62,26,12:00 - 16:00,12:00,16:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 16:00
Amy Alsop,Friday,Cornish Arms,0,0,12:00 - 14:00,12:00,14:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 14:00
Gracie Barry Tait,Friday,Crooner'S Corner,0,0,12:00 - 12:45,12:00,12:45,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:45
Chunky [15 Years Of Eglo],Friday,Firmly Rooted,43,43,12:00 - 14:00,12:00,14:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 14:00
Canon Fodder With Joe Dunthorne,Friday,Free University Of Glastonbury,42,21,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
Zero 7 Dj,Friday,Glade,51,29,12:00 - 13:55,12:00,13:55,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:55
Easy Tai Chi With Joe May,Friday,Humblewell Active Platform,42,21,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
"Feck, Arse, Carbon - An Interactive Climate Change Rant",Friday,Laboratory Stage,0,0,12:00 - 12:30,12:00,12:30,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:30
"Debates: Trans Liberation Now! With Hiba Noor, Noah Lonergan, Sabah Choudrey, Travis Alabanza, Shon Faye",Friday,Left Field,52,33,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
Nightmares On Wax [Dj],Friday,Levels,42,44,12:00 - 15:00,12:00,15:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 15:00
Olivia Nelson,Friday,Lonely Hearts Club,44,41,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
Daisy Chute,Friday,Mandala Stage,0,0,12:00 - 12:30,12:00,12:30,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:30
Compere: Jonny Fluffypunk,Friday,Poetry&Words,0,0,12:00 - 15:30,12:00,15:30,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 15:30
Squeeze,Friday,Pyramid Stage,51,43,12:00 - 12:45,12:00,12:45,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:45
Compères: George Orange / Grainne,Friday,Sensation Seekers Stage,0,0,12:00 - 17:55,12:00,17:55,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 17:55
The Blind Spot: The Climate Risks Government Missed,Friday,Speakers Forum,0,0,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
Rompas Reggae Shack,Friday,Strummerville,48,12,12:00 - 15:00,12:00,15:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 15:00
Land Of The Giants,Friday,The Gateway,0,0,12:00 - 12:30,12:00,12:30,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:30
Groovy Guy,Friday,The Glebe,60,33,12:00 - 12:30,12:00,12:30,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:30
"Shado Mag: The Power Of Boycott: Ahmed Alnaouq (We Are Not Numbers), Queer House Party, Venetia La Manna (Remember Who Made Them), Yiz (Novo), Hosted By Larissa Kennedy (Shado Mag)",Friday,The Information,41,41,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
Hilby,Friday,The Pavement,0,0,12:00 - 12:30,12:00,12:30,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:30
Rosa Hoop'S Rotation Motivation,Friday,Toad Hall,0,0,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
Jay Rawlings,Friday,Walkabouts,60,33,12:00 - 12:45,12:00,12:45,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:45
The Very Best Of Tommy Cooper,Friday,Walkabouts,60,33,12:00 - 12:45,12:00,12:45,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 12:45
The Explorers,Friday,Walkabouts,60,33,12:00 - 13:00,12:00,13:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 13:00
Worldroots Acapella,Friday,Walkabouts,60,33,12:00 - 14:00,12:00,14:00,28/06/2024,28/06/2024,28/06/2024 12:00,28/06/2024 14:00
R J Hunter,Friday,Poetry&Words,0,0,12:03 - 12:28,12:03,12:28,28/06/2024,28/06/2024,28/06/2024 12:03,28/06/2024 12:28
The Infinite Monkey Cage,Friday,Cabaret,62,26,12:05 - 13:00,12:05,13:00,28/06/2024,28/06/2024,28/06/2024 12:05,28/06/2024 13:00
Wookey Hole Circus,Friday,Circus Big Top,57,34,12:05 - 12:30,12:05,12:30,28/06/2024,28/06/2024,28/06/2024 12:05,28/06/2024 12:30
Maddie Moate'S Science Showdown!,Friday,Kidzfield Big Top,0,0,12:05 - 12:30,12:05,12:30,28/06/2024,28/06/2024,28/06/2024 12:05,28/06/2024 12:30
Flamingos,Friday,Walkabouts,60,33,12:05 - 12:50,12:05,12:50,28/06/2024,28/06/2024,28/06/2024 12:05,28/06/2024 12:50
John Smith,Friday,Acoustic Stage,66,38,12:10 - 12:40,12:10,12:40,28/06/2024,28/06/2024,28/06/2024 12:10,28/06/2024 12:40
Dr. Jane Goodall,Friday,Greenpeace,55,26,12:10 - 12:30,12:10,12:30,28/06/2024,28/06/2024,28/06/2024 12:10,28/06/2024 12:30
Jon Parry,Friday,The Hive,0,0,12:10 - 12:55,12:10,12:55,28/06/2024,28/06/2024,28/06/2024 12:10,28/06/2024 12:55
Football Crazy,Friday,Walkabouts,60,33,12:10 - 12:55,12:10,12:55,28/06/2024,28/06/2024,28/06/2024 12:10,28/06/2024 12:55
The Magnifient Kevens,Friday,Walkabouts,60,33,12:10 - 12:55,12:10,12:55,28/06/2024,28/06/2024,28/06/2024 12:10,28/06/2024 12:55
Compere: Bunny Morethan,Friday,Circus Big Top,57,34,12:15 - 16:45,12:15,16:45,28/06/2024,28/06/2024,28/06/2024 12:15,28/06/2024 16:45
Rob Roy Collins,Friday,Outside Circus Stage,59,33,12:15 - 12:45,12:15,12:45,28/06/2024,28/06/2024,28/06/2024 12:15,28/06/2024 12:45
Harvey Juggling,Friday,Sensation Seekers Stage,0,0,12:15 - 12:45,12:15,12:45,28/06/2024,28/06/2024,28/06/2024 12:15,28/06/2024 12:45
Natural Theatre Company,Friday,Walkabouts,60,33,12:15 - 13:00,12:15,13:00,28/06/2024,28/06/2024,28/06/2024 12:15,28/06/2024 13:00
Blockbuster Factory,Friday,Walkabouts,60,33,12:15 - 13:10,12:15,13:10,28/06/2024,28/06/2024,28/06/2024 12:15,28/06/2024 13:10
Tba,Friday,A Little More Sensation,0,0,12:20 - 12:50,12:20,12:50,28/06/2024,28/06/2024,28/06/2024 12:20,28/06/2024 12:50
"Thomas Mccarthy, Bob Knight, Damian Le Bas, Nikki James, Talk: Significance And Use Of Language",Friday,Atchin Tan,0,0,12:30 - 13:15,12:30,13:15,28/06/2024,28/06/2024,28/06/2024 12:30,28/06/2024 13:15
The Parallels,Friday,Bbc Music Introducing,45,44,12:30 - 13:00,12:30,13:00,28/06/2024,28/06/2024,28/06/2024 12:30,28/06/2024 13:00
Josh Hazelden,Friday,Croissant Neuf Bandstand,55,21,12:30 - 13:00,12:30,13:00,28/06/2024,28/06/2024,28/06/2024 12:30,28/06/2024 13:00
Carnival,Friday,Glasto Latino,58,27,12:30 - 13:00,12:30,13:00,28/06/2024,28/06/2024,28/06/2024 12:30,28/06/2024 13:00
Shamanic Drum Circle With Tracy Turnell,Friday,Humblewell Retreat Yurt,42,21,12:30 - 13:30,12:30,13:30,28/06/2024,28/06/2024,28/06/2024 12:30,28/06/2024 13:30
Dismantle The War Machine With Palestine Action,Friday,Temple Uprising,0,0,12:30 - 13:15,12:30,13:15,28/06/2024,28/06/2024,28/06/2024 12:30,28/06/2024 13:15
Mishra,Friday,The Bandstand,56,38,12:30 - 13:00,12:30,13:00,28/06/2024,28/06/2024,28/06/2024 12:30,28/06/2024 13:00
The Fabularium - Carnival Of Animals,Friday,Walkabouts,60,33,12:30 - 13:15,12:30,13:15,28/06/2024,28/06/2024,28/06/2024 12:30,28/06/2024 13:15
Asha Puthli,Friday,West Holts Stage,57,31,12:30 - 13:30,12:30,13:30,28/06/2024,28/06/2024,28/06/2024 12:30,28/06/2024 13:30
Kayleigh Jayshree,Friday,Poetry&Words,0,0,12:31 - 12:56,12:31,12:56,28/06/2024,28/06/2024,28/06/2024 12:31,28/06/2024 12:56
Head Over Wheels,Friday,Circus Big Top,57,34,12:35 - 12:43,12:35,12:43,28/06/2024,28/06/2024,28/06/2024 12:35,28/06/2024 12:43
The Old Time Rags,Friday,The Gateway,0,0,12:35 - 13:05,12:35,13:05,28/06/2024,28/06/2024,28/06/2024 12:35,28/06/2024 13:05
Mark Bruce Dance Company,Friday,The Glebe,60,33,12:35 - 12:45,12:35,12:45,28/06/2024,28/06/2024,28/06/2024 12:35,28/06/2024 12:45
Chinnen,Friday,The Pavement,0,0,12:35 - 13:05,12:35,13:05,28/06/2024,28/06/2024,28/06/2024 12:35,28/06/2024 13:05
The Newspaper Men,Friday,Walkabouts,60,33,12:35 - 13:20,12:35,13:20,28/06/2024,28/06/2024,28/06/2024 12:35,28/06/2024 13:20
Lil Miss Motown,Friday,Blind Tiger,0,0,12:45 - 13:45,12:45,13:45,28/06/2024,28/06/2024,28/06/2024 12:45,28/06/2024 13:45
Keeq,Friday,Glade Dome,49,29,12:45 - 14:00,12:45,14:00,28/06/2024,28/06/2024,28/06/2024 12:45,28/06/2024 14:00
The Flying Seagull Project,Friday,Kidzfield Big Top,0,0,12:45 - 13:20,12:45,13:20,28/06/2024,28/06/2024,28/06/2024 12:45,28/06/2024 13:20
Cow (Film Screening) / Q&A With Producer Kat Mansoor,Friday,Laboratory Stage,0,0,12:45 - 14:00,12:45,14:00,28/06/2024,28/06/2024,28/06/2024 12:45,28/06/2024 14:00
Holly Carter,Friday,Mandala Stage,0,0,12:45 - 13:30,12:45,13:30,28/06/2024,28/06/2024,28/06/2024 12:45,28/06/2024 13:30
Moonchild Sanelly,Friday,The Park Stage,41,19,12:45 - 13:30,12:45,13:30,28/06/2024,28/06/2024,28/06/2024 12:45,28/06/2024 13:30
The Bigheads,Friday,Walkabouts,60,33,12:45 - 13:25,12:45,13:25,28/06/2024,28/06/2024,28/06/2024 12:45,28/06/2024 13:25
Gnomes,Friday,Walkabouts,60,33,12:45 - 13:30,12:45,13:30,28/06/2024,28/06/2024,28/06/2024 12:45,28/06/2024 13:30
Lambrini Girls,Friday,Woodsies,43,52,12:45 - 13:30,12:45,13:30,28/06/2024,28/06/2024,28/06/2024 12:45,28/06/2024 13:30
Cirk Hes Presents Jaia And Malia,Friday,Circus Big Top,57,34,12:48 - 12:58,12:48,12:58,28/06/2024,28/06/2024,28/06/2024 12:48,28/06/2024 12:58
Goldie Fiasco,Friday,Outside Circus Stage,59,33,12:50 - 13:20,12:50,13:20,28/06/2024,28/06/2024,28/06/2024 12:50,28/06/2024 13:20
Billy Kidd Show,Friday,Sensation Seekers Stage,0,0,12:50 - 13:20,12:50,13:20,28/06/2024,28/06/2024,28/06/2024 12:50,28/06/2024 13:20
Faces Of Disco,Friday,The Glebe,60,33,12:50 - 13:20,12:50,13:20,28/06/2024,28/06/2024,28/06/2024 12:50,28/06/2024 13:20
The Sky At Day,Friday,Walkabouts,60,33,12:50 - 13:35,12:50,13:35,28/06/2024,28/06/2024,28/06/2024 12:50,28/06/2024 13:35
The Doogans,Friday,A Little More Sensation,0,0,12:55 - 13:25,12:55,13:25,28/06/2024,28/06/2024,28/06/2024 12:55,28/06/2024 13:25
Otamere Guobadia,Friday,Poetry&Words,0,0,12:59 - 13:24,12:59,13:24,28/06/2024,28/06/2024,28/06/2024 12:59,28/06/2024 13:24
Cocoa Butter Club Cabaret,Friday,10 Aces,0,0,13:00 - 13:30,13:00,13:30,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 13:30
Angie Mcmahon,Friday,Acoustic Stage,66,38,13:00 - 13:40,13:00,13:40,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 13:40
Cc:Disco [10 Years Of Rhythm Section],Friday,Assembly,40,42,13:00 - 14:30,13:00,14:30,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 14:30
The Bar-Steward Sons Of Val Doonican,Friday,Avalon Stage,66,38,13:00 - 13:50,13:00,13:50,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 13:50
Mish Mash,Friday,Babylon Uprising,0,0,13:00 - 14:00,13:00,14:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 14:00
Kid 12,Friday,Bread And Roses,0,0,13:00 - 13:40,13:00,13:40,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 13:40
Fulu Miziki,Friday,Carhenge,58,36,13:00 - 14:00,13:00,14:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 14:00
Max Rad,Friday,Croissant Neuf,55,21,13:00 - 14:00,13:00,14:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 14:00
Shaun Keaveny,Friday,Free University Of Glastonbury,42,21,13:00 - 14:00,13:00,14:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 14:00
Dance Class: Salsa,Friday,Glasto Latino,58,27,13:00 - 14:00,13:00,14:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 14:00
Skate Ramp Pro Session,Friday,Greenpeace,55,26,13:00 - 14:00,13:00,14:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 14:00
Action Skills Workshops,Friday,Greenpeace (Beam),54,26,13:00 - 15:00,13:00,15:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 15:00
Life Drawing With Fra Beecher,Friday,Humblewell Active Platform,42,21,13:00 - 13:30,13:00,13:30,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 13:30
The Snuts,Friday,Other Stage,47,34,13:00 - 13:45,13:00,13:45,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 13:45
Craig Charles Funk & Sound With Neillie Charles And Friends,Friday,Peace Stage,0,0,13:00 - 16:00,13:00,16:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 16:00
The Greatest Showman Sing-A-Long Pg,Friday,Pilton Palais Cinema,64,36,13:00 - 14:45,13:00,14:45,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 14:45
"Back To Mine Takeover W/ Fat Tony, Sarah Story, Mas Que Nada Bros + Gucci Girl",Friday,Platform 23,0,0,13:00 - 17:00,13:00,17:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 17:00
Ella Knight,Friday,San Remo,45,47,13:00 - 14:30,13:00,14:30,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 14:30
"Carbon Markets, Big Business And Net Zero - Patrick Greenfield",Friday,Speakers Forum,0,0,13:00 - 14:00,13:00,14:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 14:00
Jarvis Cocker + Alexis Taylor,Friday,Stonebridge Bar,42,18,13:00 - 15:00,13:00,15:00,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 15:00
Gecko,Friday,The Astrolabe Theatre,0,0,13:00 - 13:10,13:00,13:10,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 13:10
Mafia Wedding,Friday,Walkabouts,60,33,13:00 - 13:45,13:00,13:45,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 13:45
Steve Faulkner,Friday,Walkabouts,60,33,13:00 - 13:45,13:00,13:45,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 13:45
Psycho-Acoustic Goat,Friday,Wishing Well,42,20,13:00 - 13:30,13:00,13:30,28/06/2024,28/06/2024,28/06/2024 13:00,28/06/2024 13:30
Jon Udry,Friday,Circus Big Top,57,34,13:03 - 13:28,13:03,13:28,28/06/2024,28/06/2024,28/06/2024 13:03,28/06/2024 13:28
Spencer Jones,Friday,Cabaret,62,26,13:05 - 13:25,13:05,13:25,28/06/2024,28/06/2024,28/06/2024 13:05,28/06/2024 13:25
Paul Lambourne,Friday,Crooner'S Corner,0,0,13:05 - 13:35,13:05,13:35,28/06/2024,28/06/2024,28/06/2024 13:05,28/06/2024 13:35
Trash Test Dummies,Friday,The Astrolabe Theatre,0,0,13:10 - 14:10,13:10,14:10,28/06/2024,28/06/2024,28/06/2024 13:10,28/06/2024 14:10
The Beatbox Collective & Rogue Wave,Friday,The Hive,0,0,13:10 - 13:55,13:10,13:55,28/06/2024,28/06/2024,28/06/2024 13:10,28/06/2024 13:55
Ekleido Dance - Splice,Friday,The Pavement,0,0,13:10 - 13:25,13:10,13:25,28/06/2024,28/06/2024,28/06/2024 13:10,28/06/2024 13:25
Liver Cottage,Friday,Walkabouts,60,33,13:10 - 13:55,13:10,13:55,28/06/2024,28/06/2024,28/06/2024 13:10,28/06/2024 13:55
Martin Furey: Music,Friday,Atchin Tan,0,0,13:15 - 14:00,13:15,14:00,28/06/2024,28/06/2024,28/06/2024 13:15,28/06/2024 14:00
Olivia Dean,Friday,Pyramid Stage,51,43,13:15 - 14:15,13:15,14:15,28/06/2024,28/06/2024,28/06/2024 13:15,28/06/2024 14:15
Mal Webb & Kylie Morrigan,Friday,The Bandstand,56,38,13:15 - 13:45,13:15,13:45,28/06/2024,28/06/2024,28/06/2024 13:15,28/06/2024 13:45
"Waterbear: 'Nature’S Anthem - Environmentalism Meets Creativity': Jayda G (Dj, Music Producer, Environmental Toxicologist), Maria Correa (Waterbear Network) Hosted By Andrea Zara (Radio Broadcaster & Dj)",Friday,The Information,41,41,13:15 - 14:15,13:15,14:15,28/06/2024,28/06/2024,28/06/2024 13:15,28/06/2024 14:15
Sounds Of Space,Friday,Toad Hall,0,0,13:15 - 14:00,13:15,14:00,28/06/2024,28/06/2024,28/06/2024 13:15,28/06/2024 14:00
The Smallest Race On Earth,Friday,Walkabouts,60,33,13:15 - 13:45,13:15,13:45,28/06/2024,28/06/2024,28/06/2024 13:15,28/06/2024 13:45
Be Prepared,Friday,Walkabouts,60,33,13:15 - 14:00,13:15,14:00,28/06/2024,28/06/2024,28/06/2024 13:15,28/06/2024 14:00
The 2 Lisas,Friday,Outside Circus Stage,59,33,13:25 - 13:33,13:25,13:33,28/06/2024,28/06/2024,28/06/2024 13:25,28/06/2024 13:33
Akira,Friday,Sensation Seekers Stage,0,0,13:25 - 13:55,13:25,13:55,28/06/2024,28/06/2024,28/06/2024 13:25,28/06/2024 13:55
Old Time Sailors,Friday,The Gateway,0,0,13:25 - 14:25,13:25,14:25,28/06/2024,28/06/2024,28/06/2024 13:25,28/06/2024 14:25
Otto And Astrid - Die Roten Punkte,Friday,The Glebe,60,33,13:25 - 14:05,13:25,14:05,28/06/2024,28/06/2024,28/06/2024 13:25,28/06/2024 14:05
Imogen Stirling,Friday,Poetry&Words,0,0,13:27 - 13:52,13:27,13:52,28/06/2024,28/06/2024,28/06/2024 13:27,28/06/2024 13:52
Primary School Assembly Bangers,Friday,A Little More Sensation,0,0,13:30 - 14:00,13:30,14:00,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 14:00
Letisha Gordon,Friday,Bbc Music Introducing,45,44,13:30 - 14:00,13:30,14:00,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 14:00
Luisa Omielan,Friday,Cabaret,62,26,13:30 - 14:00,13:30,14:00,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 14:00
"Debates: Israel Palestine: Hope And Solidarity In Action With Ahmed Alnaouq, Na'Amod, Rachel Shabi, Shaista Aziz, John Harris",Friday,Left Field,52,33,13:30 - 14:30,13:30,14:30,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 14:30
Flowerovlove,Friday,Lonely Hearts Club,44,41,13:30 - 14:30,13:30,14:30,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 14:30
"Talk: Chris Fitchew, Joy Alchemy",Friday,Scissors,42,21,13:30 - 14:30,13:30,14:30,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 14:30
"Ancient Sounds & Modern Techno - Performance And Discussion (Jj Middleway, Danica Boyce, Alex Nunnes)",Friday,Temple Uprising,0,0,13:30 - 14:15,13:30,14:15,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 14:15
Harvey Juggling,Friday,The Pavement,0,0,13:30 - 14:00,13:30,14:00,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 14:00
Fire Fighters!,Friday,Walkabouts,60,33,13:30 - 14:00,13:30,14:00,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 14:00
The Jukeboxes,Friday,Walkabouts,60,33,13:30 - 15:00,13:30,15:00,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 15:00
Alex B And Gas Man (Dj Set),Friday,Wishing Well,42,20,13:30 - 14:15,13:30,14:15,28/06/2024,28/06/2024,28/06/2024 13:30,28/06/2024 14:15
Eloise & Jack,Friday,Circus Big Top,57,34,13:33 - 13:39,13:33,13:39,28/06/2024,28/06/2024,28/06/2024 13:33,28/06/2024 13:39
Cbbc'S Laura & Alex,Friday,Kidzfield Big Top,0,0,13:35 - 14:05,13:35,14:05,28/06/2024,28/06/2024,28/06/2024 13:35,28/06/2024 14:05
Dan The Hat,Friday,Outside Circus Stage,59,33,13:38 - 14:08,13:38,14:08,28/06/2024,28/06/2024,28/06/2024 13:38,28/06/2024 14:08
Rezon8 Artist Showcase,Friday,10 Aces,0,0,13:40 - 14:10,13:40,14:10,28/06/2024,28/06/2024,28/06/2024 13:40,28/06/2024 14:10
Cirk Hes - Ground Group Act,Friday,Circus Big Top,57,34,13:44 - 13:56,13:44,13:56,28/06/2024,28/06/2024,28/06/2024 13:44,28/06/2024 13:56
Mistafire,Friday,Blind Tiger,0,0,13:45 - 14:30,13:45,14:30,28/06/2024,28/06/2024,28/06/2024 13:45,28/06/2024 14:30
Life Drawing With Fra Beecher,Friday,Humblewell Active Platform,42,21,13:45 - 14:15,13:45,14:15,28/06/2024,28/06/2024,28/06/2024 13:45,28/06/2024 14:15
Meditation For Busy Minds With Dan Peppiat,Friday,Humblewell Retreat Yurt,42,21,13:45 - 14:45,13:45,14:45,28/06/2024,28/06/2024,28/06/2024 13:45,28/06/2024 14:45
Enchanted Flower Show Globe,Friday,Walkabouts,60,33,13:45 - 14:30,13:45,14:30,28/06/2024,28/06/2024,28/06/2024 13:45,28/06/2024 14:30
Scary & Spooky Skeletons,Friday,Walkabouts,60,33,13:50 - 14:35,13:50,14:35,28/06/2024,28/06/2024,28/06/2024 13:50,28/06/2024 14:35
Charlotte May,Friday,Crooner'S Corner,0,0,13:55 - 14:40,13:55,14:40,28/06/2024,28/06/2024,28/06/2024 13:55,28/06/2024 14:40
Iona Lee,Friday,Poetry&Words,0,0,13:55 - 14:20,13:55,14:20,28/06/2024,28/06/2024,28/06/2024 13:55,28/06/2024 14:20
Josh Rouse,Friday,Acoustic Stage,66,38,14:00 - 14:40,14:00,14:40,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 14:40
R.E.D,Friday,Babylon Uprising,0,0,14:00 - 15:00,14:00,15:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 15:00
New York Brass Band,Friday,Bread And Roses,0,0,14:00 - 14:40,14:00,14:40,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 14:40
Curt & Andy,Friday,Cornish Arms,0,0,14:00 - 16:00,14:00,16:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 16:00
Gateway Girl,Friday,Croissant Neuf Bandstand,55,21,14:00 - 14:30,14:00,14:30,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 14:30
Shy One [15 Years Of Eglo],Friday,Firmly Rooted,43,43,14:00 - 16:00,14:00,16:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 16:00
Dj Paulette,Friday,Free University Of Glastonbury,42,21,14:00 - 15:00,14:00,15:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 15:00
Don Letts,Friday,Glade Dome,49,29,14:00 - 15:00,14:00,15:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 15:00
Dance Class: Samba,Friday,Glasto Latino,58,27,14:00 - 15:00,14:00,15:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 15:00
Mr. T (Acoustic),Friday,Greenpeace,55,26,14:00 - 14:45,14:00,14:45,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 14:45
Anima Bloom,Friday,Mandala Stage,0,0,14:00 - 15:00,14:00,15:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 15:00
Novara Media Presents: Radical Connections,Friday,Nomad,0,0,14:00 - 15:00,14:00,15:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 15:00
Tony & Ray,Friday,Sensation Seekers Stage,0,0,14:00 - 14:15,14:00,14:15,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 14:15
"New North Sea Oil Or Not ? - Dale Vince, Molly Scott Cato, Tamasin Cave, Will Mccullen Justin Rowlatt",Friday,Speakers Forum,0,0,14:00 - 15:00,14:00,15:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 15:00
Maclean Colston & Saul Rose,Friday,The Bandstand,56,38,14:00 - 14:40,14:00,14:40,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 14:40
Congo Iain,Friday,The Hive,0,0,14:00 - 15:00,14:00,15:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 15:00
Barry Can'T Swim,Friday,The Park Stage,41,19,14:00 - 14:45,14:00,14:45,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 14:45
Fbr,Friday,Village Inn,0,0,14:00 - 16:00,14:00,16:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 16:00
Circus Raj,Friday,Walkabouts,60,33,14:00 - 14:45,14:00,14:45,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 14:45
Bowjangles,Friday,Walkabouts,60,33,14:00 - 15:00,14:00,15:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 15:00
Squid,Friday,West Holts Stage,57,31,14:00 - 15:00,14:00,15:00,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 15:00
Remi Wolf,Friday,Woodsies,43,52,14:00 - 14:45,14:00,14:45,28/06/2024,28/06/2024,28/06/2024 14:00,28/06/2024 14:45
Molly Whitehouse,Friday,Circus Big Top,57,34,14:01 - 14:07,14:01,14:07,28/06/2024,28/06/2024,28/06/2024 14:01,28/06/2024 14:07
Freddieno Show,Friday,A Little More Sensation,0,0,14:05 - 14:35,14:05,14:35,28/06/2024,28/06/2024,28/06/2024 14:05,28/06/2024 14:35
Rsvp - Dance Workshop,Friday,Cabaret,62,26,14:05 - 14:30,14:05,14:30,28/06/2024,28/06/2024,28/06/2024 14:05,28/06/2024 14:30
Bel Cobain,Friday,Glade,51,29,14:05 - 15:05,14:05,15:05,28/06/2024,28/06/2024,28/06/2024 14:05,28/06/2024 15:05
Rob Roy Collins,Friday,The Pavement,0,0,14:05 - 14:35,14:05,14:35,28/06/2024,28/06/2024,28/06/2024 14:05,28/06/2024 14:35
The Suitcase Escape Game,Friday,Walkabouts,60,33,14:05 - 14:50,14:05,14:50,28/06/2024,28/06/2024,28/06/2024 14:05,28/06/2024 14:50
The Explorers,Friday,Walkabouts,60,33,14:05 - 15:05,14:05,15:05,28/06/2024,28/06/2024,28/06/2024 14:05,28/06/2024 15:05
Marcus Du Sautoy And The School Of Hard Sums,Friday,The Astrolabe Theatre,0,0,14:10 - 15:05,14:10,15:05,28/06/2024,28/06/2024,28/06/2024 14:10,28/06/2024 15:05
Jack Defrost - Traceworks Dance,Friday,The Glebe,60,33,14:10 - 14:25,14:10,14:25,28/06/2024,28/06/2024,28/06/2024 14:10,28/06/2024 14:25
Rose Popay & Sidekick Saffy,Friday,Walkabouts,60,33,14:10 - 14:55,14:10,14:55,28/06/2024,28/06/2024,28/06/2024 14:10,28/06/2024 14:55
Fraser Hooper,Friday,Circus Big Top,57,34,14:12 - 14:37,14:12,14:37,28/06/2024,28/06/2024,28/06/2024 14:12,28/06/2024 14:37
Venus,Friday,Outside Circus Stage,59,33,14:13 - 14:43,14:13,14:43,28/06/2024,28/06/2024,28/06/2024 14:13,28/06/2024 14:43
Rhubarb Theatre Presents: Collection Day,Friday,Kidzfield Big Top,0,0,14:15 - 14:45,14:15,14:45,28/06/2024,28/06/2024,28/06/2024 14:15,28/06/2024 14:45
Bbc Natural History Unit,Friday,Laboratory Stage,0,0,14:15 - 14:45,14:15,14:45,28/06/2024,28/06/2024,28/06/2024 14:15,28/06/2024 14:45
Headie One,Friday,Other Stage,47,34,14:15 - 15:15,14:15,15:15,28/06/2024,28/06/2024,28/06/2024 14:15,28/06/2024 15:15
Ukelele Thrash Mob,Friday,Walkabouts,60,33,14:15 - 15:00,14:15,15:00,28/06/2024,28/06/2024,28/06/2024 14:15,28/06/2024 15:00
Dead Pages,Friday,Wishing Well,42,20,14:15 - 15:15,14:15,15:15,28/06/2024,28/06/2024,28/06/2024 14:15,28/06/2024 15:15
Sandpiper,Friday,10 Aces,0,0,14:20 - 15:20,14:20,15:20,28/06/2024,28/06/2024,28/06/2024 14:20,28/06/2024 15:20
The Deep Blue,Friday,Avalon Stage,66,38,14:20 - 15:10,14:20,15:10,28/06/2024,28/06/2024,28/06/2024 14:20,28/06/2024 15:10
Taiko Meantime,Friday,Sensation Seekers Stage,0,0,14:20 - 15:20,14:20,15:20,28/06/2024,28/06/2024,28/06/2024 14:20,28/06/2024 15:20
Kate Ireland,Friday,Poetry&Words,0,0,14:23 - 14:48,14:23,14:48,28/06/2024,28/06/2024,28/06/2024 14:23,28/06/2024 14:48
Sally C [10 Years Of Rhythm Section],Friday,Assembly,40,42,14:30 - 16:00,14:30,16:00,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 16:00
Maruja,Friday,Bbc Music Introducing,45,44,14:30 - 15:00,14:30,15:00,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 15:00
Why Tyrone & Double Vision,Friday,Blind Tiger,0,0,14:30 - 15:15,14:30,15:15,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 15:15
"Moya Brennan, The Voice Of Clannad",Friday,Croissant Neuf,55,21,14:30 - 15:30,14:30,15:30,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 15:30
African Dance With Penny Avery,Friday,Humblewell Active Platform,42,21,14:30 - 15:00,14:30,15:00,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 15:00
Retro Cassetta,Friday,San Remo,45,47,14:30 - 16:00,14:30,16:00,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 16:00
Grounding Our Activism Is Sacred - Panel Discussion,Friday,Temple Uprising,0,0,14:30 - 15:15,14:30,15:15,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 15:15
Lekiddo Lord Of The Lobsters,Friday,The Glebe,60,33,14:30 - 15:00,14:30,15:00,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 15:00
"Gaps In The Dial - The History Of Pirate Radio: Frankie Wells (Foundation Fm), Geeneus (Rinse Fm), Hosted By Tayo Popoola (Radio Producer)",Friday,The Information,41,41,14:30 - 15:30,14:30,15:30,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 15:30
The Zawose Queens,Friday,Toad Hall,0,0,14:30 - 15:30,14:30,15:30,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 15:30
Magical Musical Time Machine,Friday,Walkabouts,60,33,14:30 - 15:15,14:30,15:15,28/06/2024,28/06/2024,28/06/2024 14:30,28/06/2024 15:15
Andy Parsons,Friday,Cabaret,62,26,14:35 - 15:15,14:35,15:15,28/06/2024,28/06/2024,28/06/2024 14:35,28/06/2024 15:15
Hilby,Friday,A Little More Sensation,0,0,14:40 - 15:10,14:40,15:10,28/06/2024,28/06/2024,28/06/2024 14:40,28/06/2024 15:10
Billy Kidd Show,Friday,The Pavement,0,0,14:40 - 15:10,14:40,15:10,28/06/2024,28/06/2024,28/06/2024 14:40,28/06/2024 15:10
Vertigo Stilts,Friday,Walkabouts,60,33,14:40 - 15:25,14:40,15:25,28/06/2024,28/06/2024,28/06/2024 14:40,28/06/2024 15:25
Darius Magic,Friday,Walkabouts,60,33,14:40 - 15:40,14:40,15:40,28/06/2024,28/06/2024,28/06/2024 14:40,28/06/2024 15:40
Head Over Wheels,Friday,Circus Big Top,57,34,14:42 - 14:50,14:42,14:50,28/06/2024,28/06/2024,28/06/2024 14:42,28/06/2024 14:50
Seventeen,Friday,Pyramid Stage,51,43,14:45 - 15:45,14:45,15:45,28/06/2024,28/06/2024,28/06/2024 14:45,28/06/2024 15:45
Atchin Tan,Friday,The Gateway,0,0,14:45 - 15:25,14:45,15:25,28/06/2024,28/06/2024,28/06/2024 14:45,28/06/2024 15:25
The Bigheads,Friday,Walkabouts,60,33,14:45 - 15:25,14:45,15:25,28/06/2024,28/06/2024,28/06/2024 14:45,28/06/2024 15:25
Dodgy Boys,Friday,Walkabouts,60,33,14:45 - 15:30,14:45,15:30,28/06/2024,28/06/2024,28/06/2024 14:45,28/06/2024 15:30
Natural Diversions,Friday,Walkabouts,60,33,14:45 - 15:30,14:45,15:30,28/06/2024,28/06/2024,28/06/2024 14:45,28/06/2024 15:30
Wookey Hole Circus,Friday,Outside Circus Stage,59,33,14:48 - 15:13,14:48,15:13,28/06/2024,28/06/2024,28/06/2024 14:48,28/06/2024 15:13
Blip,Friday,Walkabouts,60,33,14:50 - 15:35,14:50,15:35,28/06/2024,28/06/2024,28/06/2024 14:50,28/06/2024 15:35
Ellerose The Unicorn,Friday,Poetry&Words,0,0,14:51 - 15:16,14:51,15:16,28/06/2024,28/06/2024,28/06/2024 14:51,28/06/2024 15:16
Cirk Hes Presents Rosenwyn,Friday,Circus Big Top,57,34,14:55 - 15:01,14:55,15:01,28/06/2024,28/06/2024,28/06/2024 14:55,28/06/2024 15:01
Red Hot Chilli Pipers,Friday,Acoustic Stage,66,38,15:00 - 15:40,15:00,15:40,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 15:40
Control Freak,Friday,Babylon Uprising,0,0,15:00 - 16:00,15:00,16:00,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:00
Hetta Falzon,Friday,Bread And Roses,0,0,15:00 - 15:40,15:00,15:40,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 15:40
Georgia D'Arcy Roden,Friday,Crooner'S Corner,0,0,15:00 - 15:45,15:00,15:45,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 15:45
Yemz,Friday,Glade Dome,49,29,15:00 - 16:30,15:00,16:30,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:30
Dance Class: Salsa,Friday,Glasto Latino,58,27,15:00 - 16:00,15:00,16:00,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:00
Yin + Restorative Yoga With Sasha Gabbe,Friday,Humblewell Retreat Yurt,42,21,15:00 - 16:00,15:00,16:00,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:00
Eco-Anxiety (Q&A With Justin Rowlatt & Dr Trudi Edgerton),Friday,Laboratory Stage,0,0,15:00 - 15:45,15:00,15:45,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 15:45
"Radical Round Up: Billy Bragg, Bow Anderson, Charlotte Church",Friday,Left Field,52,33,15:00 - 16:00,15:00,16:00,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:00
Midland,Friday,Levels,42,44,15:00 - 16:30,15:00,16:30,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:30
Grace Carter,Friday,Lonely Hearts Club,44,41,15:00 - 16:00,15:00,16:00,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:00
Kitty Steward,Friday,Lunched Out Lizards,0,0,15:00 - 16:00,15:00,16:00,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:00
The Movement Forward,Friday,Nomad,0,0,15:00 - 16:00,15:00,16:00,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:00
Dune: Part 2 + Intro-Q&A With Florence Pugh 12A,Friday,Pilton Palais Cinema,64,36,15:00 - 18:15,15:00,18:15,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 18:15
"Talk: Alexis Lee (Style Me Sunday), Embracing Rage",Friday,Scissors,42,21,15:00 - 15:45,15:00,15:45,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 15:45
Dale Vince,Friday,Speakers Forum,0,0,15:00 - 16:00,15:00,16:00,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:00
Club Ono,Friday,Stonebridge Bar,42,18,15:00 - 16:00,15:00,16:00,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:00
Paleblu,Friday,Strummerville,48,12,15:00 - 15:40,15:00,15:40,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 15:40
Red Carousel,Friday,The Bandstand,56,38,15:00 - 15:40,15:00,15:40,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 15:40
Rumble In The Jungle Takeover: Rumble Residents,Friday,The Hive,0,0,15:00 - 16:00,15:00,16:00,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:00
Sistxrhood Open House,Friday,The Sistxrhood,0,0,15:00 - 16:30,15:00,16:30,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 16:30
Anyone For Tennis,Friday,Walkabouts,60,33,15:00 - 15:45,15:00,15:45,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 15:45
Gliding Butterflies,Friday,Walkabouts,60,33,15:00 - 15:45,15:00,15:45,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 15:45
Jay Rawlings,Friday,Walkabouts,60,33,15:00 - 15:45,15:00,15:45,28/06/2024,28/06/2024,28/06/2024 15:00,28/06/2024 15:45
English Disco Lovers,Friday,Glade,51,29,15:05 - 15:35,15:05,15:35,28/06/2024,28/06/2024,28/06/2024 15:05,28/06/2024 15:35
The Basil Brush Show,Friday,Kidzfield Big Top,0,0,15:05 - 15:35,15:05,15:35,28/06/2024,28/06/2024,28/06/2024 15:05,28/06/2024 15:35
The Black Eagles,Friday,The Astrolabe Theatre,0,0,15:05 - 15:35,15:05,15:35,28/06/2024,28/06/2024,28/06/2024 15:05,28/06/2024 15:35
Go Bananas,Friday,The Glebe,60,33,15:05 - 15:35,15:05,15:35,28/06/2024,28/06/2024,28/06/2024 15:05,28/06/2024 15:35
Giant Seagulls,Friday,Walkabouts,60,33,15:05 - 15:50,15:05,15:50,28/06/2024,28/06/2024,28/06/2024 15:05,28/06/2024 15:50
Boom Circus,Friday,Circus Big Top,57,34,15:06 - 15:51,15:06,15:51,28/06/2024,28/06/2024,28/06/2024 15:06,28/06/2024 15:51
Dapper Chaps,Friday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,28/06/2024,28/06/2024,28/06/2024 15:10,28/06/2024 15:55
Hairy Hatter,Friday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,28/06/2024,28/06/2024,28/06/2024 15:10,28/06/2024 15:55
The Very Best Of Tommy Cooper,Friday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,28/06/2024,28/06/2024,28/06/2024 15:10,28/06/2024 15:55
Groovy Guy,Friday,A Little More Sensation,0,0,15:15 - 15:45,15:15,15:45,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 15:45
Natty Lou,Friday,Blind Tiger,0,0,15:15 - 16:30,15:15,16:30,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 16:30
The Pansy Boys,Friday,Cabaret,62,26,15:15 - 15:45,15:15,15:45,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 15:45
Cosmo Sheldrake,Friday,Greenpeace,55,26,15:15 - 16:10,15:15,16:10,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 16:10
Disco Fit With Helen Rooney,Friday,Humblewell Active Platform,42,21,15:15 - 15:45,15:15,15:45,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 15:45
The Mary Wallopers,Friday,The Park Stage,41,19,15:15 - 16:00,15:15,16:00,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 16:00
Mr Peewee The Drumming Puppet,Friday,The Pavement,0,0,15:15 - 15:45,15:15,15:45,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 15:45
The Crows,Friday,Walkabouts,60,33,15:15 - 15:45,15:15,15:45,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 15:45
The Natural Theatre Company,Friday,Walkabouts,60,33,15:15 - 16:00,15:15,16:00,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 16:00
Just A Couple Of Mums (Dj Set),Friday,Wishing Well,42,20,15:15 - 16:15,15:15,16:15,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 16:15
Kenya Grace,Friday,Woodsies,43,52,15:15 - 16:00,15:15,16:00,28/06/2024,28/06/2024,28/06/2024 15:15,28/06/2024 16:00
Duo Santus,Friday,Outside Circus Stage,59,33,15:18 - 15:25,15:18,15:25,28/06/2024,28/06/2024,28/06/2024 15:18,28/06/2024 15:25
Aflo,Friday,Poetry&Words,0,0,15:19 - 15:44,15:19,15:44,28/06/2024,28/06/2024,28/06/2024 15:19,28/06/2024 15:44
Fat Barry'S Bingo Bango Bongo,Friday,Sensation Seekers Stage,0,0,15:25 - 15:55,15:25,15:55,28/06/2024,28/06/2024,28/06/2024 15:25,28/06/2024 15:55
Figs In Wigs - Astrology Bingo!,Friday,10 Aces,0,0,15:30 - 16:20,15:30,16:20,28/06/2024,28/06/2024,28/06/2024 15:30,28/06/2024 16:20
"Traveller Pride, Talk: Lgbtq+ Traveller Rights",Friday,Atchin Tan,0,0,15:30 - 16:15,15:30,16:15,28/06/2024,28/06/2024,28/06/2024 15:30,28/06/2024 16:15
Olivia Nelson,Friday,Bbc Music Introducing,45,44,15:30 - 16:00,15:30,16:00,28/06/2024,28/06/2024,28/06/2024 15:30,28/06/2024 16:00
Joanna & The Dropouts,Friday,Croissant Neuf Bandstand,55,21,15:30 - 16:00,15:30,16:00,28/06/2024,28/06/2024,28/06/2024 15:30,28/06/2024 16:00
The Doogans,Friday,Outside Circus Stage,59,33,15:30 - 16:00,15:30,16:00,28/06/2024,28/06/2024,28/06/2024 15:30,28/06/2024 16:00
Prophecy Of The New Fire With Convergencia Ancestral,Friday,Temple Uprising,0,0,15:30 - 16:15,15:30,16:15,28/06/2024,28/06/2024,28/06/2024 15:30,28/06/2024 16:15
Compère: Dan Evans,Friday,The Astrolabe Theatre,0,0,15:30 - 19:00,15:30,19:00,28/06/2024,28/06/2024,28/06/2024 15:30,28/06/2024 19:00
Fortuni And Fae,Friday,Walkabouts,60,33,15:30 - 16:15,15:30,16:15,28/06/2024,28/06/2024,28/06/2024 15:30,28/06/2024 16:15
Ministry Of Happy,Friday,Walkabouts,60,33,15:30 - 16:15,15:30,16:15,28/06/2024,28/06/2024,28/06/2024 15:30,28/06/2024 16:15
Noname,Friday,West Holts Stage,57,31,15:30 - 16:25,15:30,16:25,28/06/2024,28/06/2024,28/06/2024 15:30,28/06/2024 16:25
Liam Bailey,Friday,Glade,51,29,15:35 - 16:35,15:35,16:35,28/06/2024,28/06/2024,28/06/2024 15:35,28/06/2024 16:35
Rod Laver,Friday,The Astrolabe Theatre,0,0,15:35 - 15:50,15:35,15:50,28/06/2024,28/06/2024,28/06/2024 15:35,28/06/2024 15:50
Kane And Abel Magic,Friday,Walkabouts,60,33,15:35 - 16:05,15:35,16:05,28/06/2024,28/06/2024,28/06/2024 15:35,28/06/2024 16:05
Clamour Of Bells,Friday,Walkabouts,60,33,15:35 - 16:20,15:35,16:20,28/06/2024,28/06/2024,28/06/2024 15:35,28/06/2024 16:20
The Bad Eggs,Friday,Walkabouts,60,33,15:35 - 16:20,15:35,16:20,28/06/2024,28/06/2024,28/06/2024 15:35,28/06/2024 16:20
Billie Marten,Friday,Avalon Stage,66,38,15:40 - 16:40,15:40,16:40,28/06/2024,28/06/2024,28/06/2024 15:40,28/06/2024 16:40
Tony And Ray,Friday,The Glebe,60,33,15:40 - 15:55,15:40,15:55,28/06/2024,28/06/2024,28/06/2024 15:40,28/06/2024 15:55
The Midwives,Friday,Walkabouts,60,33,15:40 - 16:25,15:40,16:25,28/06/2024,28/06/2024,28/06/2024 15:40,28/06/2024 16:25
Trifleenees,Friday,Walkabouts,60,33,15:40 - 16:25,15:40,16:25,28/06/2024,28/06/2024,28/06/2024 15:40,28/06/2024 16:25
Sav - Head Of Magic,Friday,Walkabouts,60,33,15:40 - 17:40,15:40,17:40,28/06/2024,28/06/2024,28/06/2024 15:40,28/06/2024 17:40
Compere: Rosy Carrick,Friday,Poetry&Words,0,0,15:44 - 19:00,15:44,19:00,28/06/2024,28/06/2024,28/06/2024 15:44,28/06/2024 19:00
Starkidz Superhero Vs Princess Show,Friday,Kidzfield Big Top,0,0,15:45 - 16:15,15:45,16:15,28/06/2024,28/06/2024,28/06/2024 15:45,28/06/2024 16:15
Confidence Man,Friday,Other Stage,47,34,15:45 - 16:45,15:45,16:45,28/06/2024,28/06/2024,28/06/2024 15:45,28/06/2024 16:45
Mellowmatic,Friday,The Gateway,0,0,15:45 - 16:25,15:45,16:25,28/06/2024,28/06/2024,28/06/2024 15:45,28/06/2024 16:25
"Art, Activism And Accountability: Led By Donkey’S, Hosted By Tayo Popoola",Friday,The Information,41,41,15:45 - 16:45,15:45,16:45,28/06/2024,28/06/2024,28/06/2024 15:45,28/06/2024 16:45
Louvre On The Move,Friday,Walkabouts,60,33,15:45 - 16:15,15:45,16:15,28/06/2024,28/06/2024,28/06/2024 15:45,28/06/2024 16:15
Bell And Bullock,Friday,Walkabouts,60,33,15:45 - 16:30,15:45,16:30,28/06/2024,28/06/2024,28/06/2024 15:45,28/06/2024 16:30
Football Crazy,Friday,Walkabouts,60,33,15:45 - 16:30,15:45,16:30,28/06/2024,28/06/2024,28/06/2024 15:45,28/06/2024 16:30
Culain Wood,Friday,Poetry&Words,0,0,15:47 - 16:12,15:47,16:12,28/06/2024,28/06/2024,28/06/2024 15:47,28/06/2024 16:12
Akira,Friday,A Little More Sensation,0,0,15:50 - 16:20,15:50,16:20,28/06/2024,28/06/2024,28/06/2024 15:50,28/06/2024 16:20
Tamar Katten,Friday,Cabaret,62,26,15:50 - 16:20,15:50,16:20,28/06/2024,28/06/2024,28/06/2024 15:50,28/06/2024 16:20
Mark Bruce Dance Company,Friday,The Astrolabe Theatre,0,0,15:50 - 16:00,15:50,16:00,28/06/2024,28/06/2024,28/06/2024 15:50,28/06/2024 16:00
Ekleido Dance - Splice,Friday,The Pavement,0,0,15:50 - 16:05,15:50,16:05,28/06/2024,28/06/2024,28/06/2024 15:50,28/06/2024 16:05
Gnomes,Friday,Walkabouts,60,33,15:50 - 16:35,15:50,16:35,28/06/2024,28/06/2024,28/06/2024 15:50,28/06/2024 16:35
The Tea Ladies On Tour,Friday,Walkabouts,60,33,15:50 - 16:35,15:50,16:35,28/06/2024,28/06/2024,28/06/2024 15:50,28/06/2024 16:35
Cirk Hes Presents Lizzie,Friday,Circus Big Top,57,34,15:56 - 16:02,15:56,16:02,28/06/2024,28/06/2024,28/06/2024 15:56,28/06/2024 16:02
Stornoway,Friday,Acoustic Stage,66,38,16:00 - 16:40,16:00,16:40,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 16:40
Chaos In The Cbd [10 Years Of Rhythm Section],Friday,Assembly,40,42,16:00 - 18:00,16:00,18:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 18:00
She Will Provide,Friday,Babylon Uprising,0,0,16:00 - 17:00,16:00,17:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:00
Sam Scherdel,Friday,Bread And Roses,0,0,16:00 - 16:30,16:00,16:30,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 16:30
Compère: Alister Barrie,Friday,Cabaret,62,26,16:00 - 20:00,16:00,20:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 20:00
Jo Bucket,Friday,Carhenge,58,36,16:00 - 17:00,16:00,17:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:00
Rompa'S Reggae Shack: Uncle Dugs/Daddy Nature/Sj Dansey (Blendid Takeover),Friday,Cornish Arms,0,0,16:00 - 18:00,16:00,18:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 18:00
Jesca Hoop,Friday,Croissant Neuf,55,21,16:00 - 17:00,16:00,17:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:00
Alex Nut [15 Years Of Eglo],Friday,Firmly Rooted,43,43,16:00 - 18:00,16:00,18:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 18:00
Dance Class: Samba,Friday,Glasto Latino,58,27,16:00 - 17:00,16:00,17:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:00
Hula Hoops With Helen Rooney,Friday,Humblewell Active Platform,42,21,16:00 - 16:45,16:00,16:45,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 16:45
Foodopoly - A Game Of Global Food Sustainability,Friday,Laboratory Stage,0,0,16:00 - 16:45,16:00,16:45,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 16:45
The Trouble Notes,Friday,Mandala Stage,0,0,16:00 - 17:00,16:00,17:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:00
Build Your Own (Trans) Protest,Friday,Nomad,0,0,16:00 - 17:00,16:00,17:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:00
Compères: Tamara And Dave,Friday,Outside Circus Stage,59,33,16:00 - 20:54,16:00,20:54,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 20:54
Stone Cold Hustle,Friday,Peace Stage,0,0,16:00 - 17:00,16:00,17:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:00
Heels & Souls,Friday,San Remo,45,47,16:00 - 17:30,16:00,17:30,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:30
Faces Of Disco,Friday,Sensation Seekers Stage,0,0,16:00 - 16:30,16:00,16:30,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 16:30
"Jso, Xr, Gndr Where Now? - Clare Farrell, Sarah Lunnon, Mel Kee",Friday,Speakers Forum,0,0,16:00 - 17:00,16:00,17:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:00
Fleetmac Wood,Friday,Stonebridge Bar,42,18,16:00 - 17:30,16:00,17:30,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:30
The Page Of Cups,Friday,Strummerville,48,12,16:00 - 16:40,16:00,16:40,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 16:40
George Egg'S Set Menu,Friday,The Astrolabe Theatre,0,0,16:00 - 17:05,16:00,17:05,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:05
Daisy Chapman,Friday,The Bandstand,56,38,16:00 - 16:40,16:00,16:40,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 16:40
Primary School Assembly Bangers,Friday,The Glebe,60,33,16:00 - 16:30,16:00,16:30,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 16:30
Rumble In The Jungle Takeover: Frenetic B2B Katalyst,Friday,The Hive,0,0,16:00 - 17:00,16:00,17:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:00
Ren Harvieu,Friday,Toad Hall,0,0,16:00 - 16:40,16:00,16:40,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 16:40
Love Come Down,Friday,Village Inn,0,0,16:00 - 18:00,16:00,18:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 18:00
Steve Faulkner,Friday,Walkabouts,60,33,16:00 - 16:45,16:00,16:45,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 16:45
The Last Of The Mohicans,Friday,Walkabouts,60,33,16:00 - 17:00,16:00,17:00,28/06/2024,28/06/2024,28/06/2024 16:00,28/06/2024 17:00
Mama Tokus,Friday,Crooner'S Corner,0,0,16:05 - 16:50,16:05,16:50,28/06/2024,28/06/2024,28/06/2024 16:05,28/06/2024 16:50
Cirk Hes Presents Sorrel,Friday,Outside Circus Stage,59,33,16:05 - 16:11,16:05,16:11,28/06/2024,28/06/2024,28/06/2024 16:05,28/06/2024 16:11
Roo'D,Friday,Walkabouts,60,33,16:05 - 16:35,16:05,16:35,28/06/2024,28/06/2024,28/06/2024 16:05,28/06/2024 16:35
The Explorers,Friday,Walkabouts,60,33,16:05 - 17:05,16:05,17:05,28/06/2024,28/06/2024,28/06/2024 16:05,28/06/2024 17:05
Nofit Howie,Friday,Circus Big Top,57,34,16:07 - 16:15,16:07,16:15,28/06/2024,28/06/2024,28/06/2024 16:07,28/06/2024 16:15
Venus,Friday,The Pavement,0,0,16:10 - 16:40,16:10,16:40,28/06/2024,28/06/2024,28/06/2024 16:10,28/06/2024 16:40
Trish Reilly: Music,Friday,Atchin Tan,0,0,16:15 - 17:00,16:15,17:00,28/06/2024,28/06/2024,28/06/2024 16:15,28/06/2024 17:00
Gong Bath With Yogic Sound,Friday,Humblewell Retreat Yurt,42,21,16:15 - 17:00,16:15,17:00,28/06/2024,28/06/2024,28/06/2024 16:15,28/06/2024 17:00
Kojaque,Friday,Lonely Hearts Club,44,41,16:15 - 16:15,16:15,16:15,28/06/2024,28/06/2024,28/06/2024 16:15,28/06/2024 16:15
Molly Walker,Friday,Poetry&Words,0,0,16:15 - 16:40,16:15,16:40,28/06/2024,28/06/2024,28/06/2024 16:15,28/06/2024 16:40
Paul Heaton,Friday,Pyramid Stage,51,43,16:15 - 17:15,16:15,17:15,28/06/2024,28/06/2024,28/06/2024 16:15,28/06/2024 17:15
Panel: Letting Your Heart Out Hosted By Otamere,Friday,Scissors,42,21,16:15 - 17:00,16:15,17:00,28/06/2024,28/06/2024,28/06/2024 16:15,28/06/2024 17:00
Enchanted Flower Show Globe,Friday,Walkabouts,60,33,16:15 - 17:00,16:15,17:00,28/06/2024,28/06/2024,28/06/2024 16:15,28/06/2024 17:00
The Cloudmen,Friday,Walkabouts,60,33,16:15 - 17:15,16:15,17:15,28/06/2024,28/06/2024,28/06/2024 16:15,28/06/2024 17:15
Enjoyable Listens,Friday,Wishing Well,42,20,16:15 - 16:45,16:15,16:45,28/06/2024,28/06/2024,28/06/2024 16:15,28/06/2024 16:45
Jon Udry,Friday,Outside Circus Stage,59,33,16:16 - 16:46,16:16,16:46,28/06/2024,28/06/2024,28/06/2024 16:16,28/06/2024 16:46
Duo Santus,Friday,Circus Big Top,57,34,16:20 - 16:26,16:20,16:26,28/06/2024,28/06/2024,28/06/2024 16:20,28/06/2024 16:26
The Jukeboxes,Friday,Walkabouts,60,33,16:20 - 17:50,16:20,17:50,28/06/2024,28/06/2024,28/06/2024 16:20,28/06/2024 17:50
Frank Harvey Trio,Friday,10 Aces,0,0,16:25 - 16:55,16:25,16:55,28/06/2024,28/06/2024,28/06/2024 16:25,28/06/2024 16:55
Mario Morris Magic,Friday,A Little More Sensation,0,0,16:25 - 16:55,16:25,16:55,28/06/2024,28/06/2024,28/06/2024 16:25,28/06/2024 16:55
Mawaan Rizwan & Band,Friday,Cabaret,62,26,16:25 - 17:05,16:25,17:05,28/06/2024,28/06/2024,28/06/2024 16:25,28/06/2024 17:05
Arxx,Friday,Bbc Music Introducing,45,44,16:30 - 17:00,16:30,17:00,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 17:00
G-Class B2B Rjd,Friday,Blind Tiger,0,0,16:30 - 17:15,16:30,17:15,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 17:15
Compere: Annabelle Holland,Friday,Circus Big Top,57,34,16:30 - 21:00,16:30,21:00,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 21:00
Wilfy D,Friday,Glade Dome,49,29,16:30 - 18:00,16:30,18:00,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 18:00
Bodger'S Badger,Friday,Kidzfield Big Top,0,0,16:30 - 16:05,16:30,16:05,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 16:05
Trampolene,Friday,Left Field,52,33,16:30 - 17:05,16:30,17:05,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 17:05
Romy [Dj],Friday,Levels,42,44,16:30 - 18:00,16:30,18:00,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 18:00
From Page To Rave With Mc Inja,Friday,Temple Uprising,0,0,16:30 - 17:15,16:30,17:15,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 17:15
This Is The Kit,Friday,The Park Stage,41,19,16:30 - 17:30,16:30,17:30,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 17:30
Brownton Abbey Talk Shop,Friday,The Sistxrhood,0,0,16:30 - 18:00,16:30,18:00,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 18:00
Circus Raj,Friday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 17:15
Fairly Fresh Fish Co,Friday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 17:15
The Suitcase Escape Game,Friday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 17:15
The Vaccines,Friday,Woodsies,43,52,16:30 - 17:30,16:30,17:30,28/06/2024,28/06/2024,28/06/2024 16:30,28/06/2024 17:30
Molly Whitehouse,Friday,Circus Big Top,57,34,16:31 - 16:37,16:31,16:37,28/06/2024,28/06/2024,28/06/2024 16:31,28/06/2024 16:37
English Disco Lovers,Friday,Glade,51,29,16:35 - 17:05,16:35,17:05,28/06/2024,28/06/2024,28/06/2024 16:35,28/06/2024 17:05
Ellis Grover,Friday,Sensation Seekers Stage,0,0,16:35 - 16:45,16:35,16:45,28/06/2024,28/06/2024,28/06/2024 16:35,28/06/2024 16:45
Jack Defrost - Traceworks Dance,Friday,The Glebe,60,33,16:35 - 16:50,16:35,16:50,28/06/2024,28/06/2024,28/06/2024 16:35,28/06/2024 16:50
Nabihah Iqbal,Friday,Greenpeace,55,26,16:40 - 17:30,16:40,17:30,28/06/2024,28/06/2024,28/06/2024 16:40,28/06/2024 17:30
New York Brass Band,Friday,The Gateway,0,0,16:40 - 17:10,16:40,17:10,28/06/2024,28/06/2024,28/06/2024 16:40,28/06/2024 17:10
Vertigo Stilts,Friday,Walkabouts,60,33,16:40 - 17:25,16:40,17:25,28/06/2024,28/06/2024,28/06/2024 16:40,28/06/2024 17:25
Steve Rawlings,Friday,Circus Big Top,57,34,16:42 - 17:02,16:42,17:02,28/06/2024,28/06/2024,28/06/2024 16:42,28/06/2024 17:02
Dominic Berry,Friday,Poetry&Words,0,0,16:43 - 17:08,16:43,17:08,28/06/2024,28/06/2024,28/06/2024 16:43,28/06/2024 17:08
Dan The Hat,Friday,The Pavement,0,0,16:45 - 17:15,16:45,17:15,28/06/2024,28/06/2024,28/06/2024 16:45,28/06/2024 17:15
Bigheads,Friday,Walkabouts,60,33,16:45 - 17:25,16:45,17:25,28/06/2024,28/06/2024,28/06/2024 16:45,28/06/2024 17:25
Alice And Alice,Friday,Walkabouts,60,33,16:45 - 17:30,16:45,17:30,28/06/2024,28/06/2024,28/06/2024 16:45,28/06/2024 17:30
Blip,Friday,Walkabouts,60,33,16:45 - 17:30,16:45,17:30,28/06/2024,28/06/2024,28/06/2024 16:45,28/06/2024 17:30
Leroy Thornhill (Dj Set),Friday,Wishing Well,42,20,16:45 - 18:00,16:45,18:00,28/06/2024,28/06/2024,28/06/2024 16:45,28/06/2024 18:00
Caleb Kunle,Friday,Bread And Roses,0,0,16:50 - 17:30,16:50,17:30,28/06/2024,28/06/2024,28/06/2024 16:50,28/06/2024 17:30
Scary & Spooky Skeletons,Friday,Walkabouts,60,33,16:50 - 17:35,16:50,17:35,28/06/2024,28/06/2024,28/06/2024 16:50,28/06/2024 17:35
Fraser Hooper,Friday,Outside Circus Stage,59,33,16:51 - 17:21,16:51,17:21,28/06/2024,28/06/2024,28/06/2024 16:51,28/06/2024 17:21
Old Time Sailors,Friday,Sensation Seekers Stage,0,0,16:55 - 17:55,16:55,17:55,28/06/2024,28/06/2024,28/06/2024 16:55,28/06/2024 17:55
Blockbuster Factory,Friday,The Glebe,60,33,16:55 - 17:50,16:55,17:50,28/06/2024,28/06/2024,28/06/2024 16:55,28/06/2024 17:50
Sugababes,Friday,West Holts Stage,57,31,16:55 - 17:55,16:55,17:55,28/06/2024,28/06/2024,28/06/2024 16:55,28/06/2024 17:55
Milkshed,Friday,10 Aces,0,0,17:00 - 17:30,17:00,17:30,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 17:30
Go Bananas,Friday,A Little More Sensation,0,0,17:00 - 17:30,17:00,17:30,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 17:30
Dervish,Friday,Acoustic Stage,66,38,17:00 - 18:00,17:00,18:00,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 18:00
Farrell - Introspect Takeover,Friday,Babylon Uprising,0,0,17:00 - 18:00,17:00,18:00,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 18:00
Alex Harding,Friday,Croissant Neuf Bandstand,55,21,17:00 - 17:30,17:00,17:30,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 17:30
Dance Class: Salsa,Friday,Glasto Latino,58,27,17:00 - 18:00,17:00,18:00,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 18:00
"Mind Of Another Kind: Ai Vs. Flesh (Q&A With Robin Ince, Prof. Gilly & Eric Drass)",Friday,Laboratory Stage,0,0,17:00 - 17:45,17:00,17:45,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 17:45
Taliesin,Friday,Lunched Out Lizards,0,0,17:00 - 18:00,17:00,18:00,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 18:00
"If I Speak, Live…",Friday,Nomad,0,0,17:00 - 18:00,17:00,18:00,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 18:00
Approaching Tipping Points - Prof Tim Lenton With Justin Rowlatt,Friday,Speakers Forum,0,0,17:00 - 18:00,17:00,18:00,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 18:00
The Jonny Halifax Invocation,Friday,Strummerville,48,12,17:00 - 17:40,17:00,17:40,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 17:40
Extra Medium,Friday,The Bug,41,25,17:00 - 18:00,17:00,18:00,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 18:00
Rumble In The Jungle Takeover: Haych,Friday,The Hive,0,0,17:00 - 18:00,17:00,18:00,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 18:00
"The Movement Forward: ‘ A Political Takeover’ - Marina Purkis (Political Commentator), Jemma Forte (Broadcast Journalist, Writer & Presenter), Asif Kapadia (Director), Josh Russell, Carol Vorderman (Broadcaster, Media Personality), Hosted By Danny Price (Dfp)",Friday,The Information,41,41,17:00 - 18:00,17:00,18:00,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 18:00
Fortuni And Fae,Friday,Walkabouts,60,33,17:00 - 17:45,17:00,17:45,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 17:45
Gliding Butterflies,Friday,Walkabouts,60,33,17:00 - 17:45,17:00,17:45,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 17:45
Swyron & Desaata,Friday,Walkabouts,60,33,17:00 - 17:45,17:00,17:45,28/06/2024,28/06/2024,28/06/2024 17:00,28/06/2024 17:45
Frank Turner,Friday,Avalon Stage,66,38,17:05 - 18:05,17:05,18:05,28/06/2024,28/06/2024,28/06/2024 17:05,28/06/2024 18:05
D:Ream,Friday,Glade,51,29,17:05 - 18:05,17:05,18:05,28/06/2024,28/06/2024,28/06/2024 17:05,28/06/2024 18:05
Dan Rhodes,Friday,Kidzfield Big Top,0,0,17:05 - 17:35,17:05,17:35,28/06/2024,28/06/2024,28/06/2024 17:05,28/06/2024 17:35
Stephen Frost Impro Allstars,Friday,The Astrolabe Theatre,0,0,17:05 - 18:10,17:05,18:10,28/06/2024,28/06/2024,28/06/2024 17:05,28/06/2024 18:10
Joli Blon,Friday,The Bandstand,56,38,17:05 - 17:50,17:05,17:50,28/06/2024,28/06/2024,28/06/2024 17:05,28/06/2024 17:50
3 Daft Monkeys,Friday,Toad Hall,0,0,17:05 - 17:50,17:05,17:50,28/06/2024,28/06/2024,28/06/2024 17:05,28/06/2024 17:50
High Society,Friday,Circus Big Top,57,34,17:07 - 17:52,17:07,17:52,28/06/2024,28/06/2024,28/06/2024 17:07,28/06/2024 17:52
Nish Kumar,Friday,Cabaret,62,26,17:10 - 17:40,17:10,17:40,28/06/2024,28/06/2024,28/06/2024 17:10,28/06/2024 17:40
Paul Lambourne,Friday,Crooner'S Corner,0,0,17:10 - 17:40,17:10,17:40,28/06/2024,28/06/2024,28/06/2024 17:10,28/06/2024 17:40
Rose Popay & Sidekick Saffy,Friday,Walkabouts,60,33,17:10 - 17:55,17:10,17:55,28/06/2024,28/06/2024,28/06/2024 17:10,28/06/2024 17:55
Princess Arinola Adegbite,Friday,Poetry&Words,0,0,17:11 - 17:36,17:11,17:36,28/06/2024,28/06/2024,28/06/2024 17:11,28/06/2024 17:36
Brewer'S Daughter: Music,Friday,Atchin Tan,0,0,17:15 - 18:00,17:15,18:00,28/06/2024,28/06/2024,28/06/2024 17:15,28/06/2024 18:00
Enerki,Friday,Blind Tiger,0,0,17:15 - 18:00,17:15,18:00,28/06/2024,28/06/2024,28/06/2024 17:15,28/06/2024 18:00
Ceildh With Kevin Campbell Davidson,Friday,Humblewell Active Platform,42,21,17:15 - 18:15,17:15,18:15,28/06/2024,28/06/2024,28/06/2024 17:15,28/06/2024 18:15
Gong Bath With Yogic Sound,Friday,Humblewell Retreat Yurt,42,21,17:15 - 18:00,17:15,18:00,28/06/2024,28/06/2024,28/06/2024 17:15,28/06/2024 18:00
Bombay Bicycle Club,Friday,Other Stage,47,34,17:15 - 18:15,17:15,18:15,28/06/2024,28/06/2024,28/06/2024 17:15,28/06/2024 18:15
Liver Cottage,Friday,Walkabouts,60,33,17:15 - 18:00,17:15,18:00,28/06/2024,28/06/2024,28/06/2024 17:15,28/06/2024 18:00
Magnificent Kevens,Friday,The Gateway,0,0,17:20 - 17:50,17:20,17:50,28/06/2024,28/06/2024,28/06/2024 17:20,28/06/2024 17:50
A Day At The Beach,Friday,The Pavement,0,0,17:20 - 17:50,17:20,17:50,28/06/2024,28/06/2024,28/06/2024 17:20,28/06/2024 17:50
Cirk Hes Presents Aerial Sensation,Friday,Outside Circus Stage,59,33,17:26 - 17:38,17:26,17:38,28/06/2024,28/06/2024,28/06/2024 17:26,28/06/2024 17:38
Tors,Friday,Bbc Music Introducing,45,44,17:30 - 18:00,17:30,18:00,28/06/2024,28/06/2024,28/06/2024 17:30,28/06/2024 18:00
Beans On Toast,Friday,Croissant Neuf,55,21,17:30 - 18:30,17:30,18:30,28/06/2024,28/06/2024,28/06/2024 17:30,28/06/2024 18:30
Here Come The Crows,Friday,Mandala Stage,0,0,17:30 - 18:30,17:30,18:30,28/06/2024,28/06/2024,28/06/2024 17:30,28/06/2024 18:30
Jayda G,Friday,San Remo,45,47,17:30 - 19:00,17:30,19:00,28/06/2024,28/06/2024,28/06/2024 17:30,28/06/2024 19:00
"Talk: Dj Paulette, Life Lessons Of A Black Woman Dj",Friday,Scissors,42,21,17:30 - 18:15,17:30,18:15,28/06/2024,28/06/2024,28/06/2024 17:30,28/06/2024 18:15
Fish56Octagon (Garage Set),Friday,Stonebridge Bar,42,18,17:30 - 19:00,17:30,19:00,28/06/2024,28/06/2024,28/06/2024 17:30,28/06/2024 19:00
Breath & Bass With Alex Harper Nunes And Kerry Veitch,Friday,Temple Uprising,0,0,17:30 - 18:30,17:30,18:30,28/06/2024,28/06/2024,28/06/2024 17:30,28/06/2024 18:30
Space Cadets,Friday,Walkabouts,60,33,17:30 - 18:15,17:30,18:15,28/06/2024,28/06/2024,28/06/2024 17:30,28/06/2024 18:15
Beatbox Collective,Friday,10 Aces,0,0,17:35 - 18:00,17:35,18:00,28/06/2024,28/06/2024,28/06/2024 17:35,28/06/2024 18:00
Tba,Friday,A Little More Sensation,0,0,17:35 - 18:05,17:35,18:05,28/06/2024,28/06/2024,28/06/2024 17:35,28/06/2024 18:05
Big Special,Friday,Left Field,52,33,17:35 - 18:10,17:35,18:10,28/06/2024,28/06/2024,28/06/2024 17:35,28/06/2024 18:10
Bsl Poet Laureate - Ismael Mansoor,Friday,Poetry&Words,0,0,17:39 - 18:09,17:39,18:09,28/06/2024,28/06/2024,28/06/2024 17:39,28/06/2024 18:09
Hairy Hatter,Friday,Walkabouts,60,33,17:40 - 18:25,17:40,18:25,28/06/2024,28/06/2024,28/06/2024 17:40,28/06/2024 18:25
Chinnen,Friday,Outside Circus Stage,59,33,17:43 - 18:13,17:43,18:13,28/06/2024,28/06/2024,28/06/2024 17:43,28/06/2024 18:13
An Audience With Doc Brown,Friday,Cabaret,62,26,17:45 - 18:25,17:45,18:25,28/06/2024,28/06/2024,28/06/2024 17:45,28/06/2024 18:25
The Silhouettes Project,Friday,Lonely Hearts Club,44,41,17:45 - 18:45,17:45,18:45,28/06/2024,28/06/2024,28/06/2024 17:45,28/06/2024 18:45
Caxxianne,Friday,Bread And Roses,0,0,17:50 - 18:30,17:50,18:30,28/06/2024,28/06/2024,28/06/2024 17:50,28/06/2024 18:30
The Buzztastic Bee-Balancing Blundershow,Friday,Kidzfield Big Top,0,0,17:55 - 18:25,17:55,18:25,28/06/2024,28/06/2024,28/06/2024 17:55,28/06/2024 18:25
Close,Friday,Sensation Seekers Stage,0,0,17:55 - 22:00,17:55,22:00,28/06/2024,28/06/2024,28/06/2024 17:55,28/06/2024 22:00
Lekiddo Lord Of The Lobsters,Friday,The Gateway,0,0,17:55 - 18:25,17:55,18:25,28/06/2024,28/06/2024,28/06/2024 17:55,28/06/2024 18:25
Kane & Abel,Friday,The Glebe,60,33,17:55 - 18:15,17:55,18:15,28/06/2024,28/06/2024,28/06/2024 17:55,28/06/2024 18:15
Tony And Ray,Friday,The Pavement,0,0,17:55 - 18:10,17:55,18:10,28/06/2024,28/06/2024,28/06/2024 17:55,28/06/2024 18:10
Toby Walker,Friday,Circus Big Top,57,34,17:57 - 18:05,17:57,18:05,28/06/2024,28/06/2024,28/06/2024 17:57,28/06/2024 18:05
Bradley Zero [10 Years Of Rhythm Section],Friday,Assembly,40,42,18:00 - 20:00,18:00,20:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 20:00
Yushh - Introspect Takeover,Friday,Babylon Uprising,0,0,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Sonwah,Friday,Blind Tiger,0,0,18:00 - 18:50,18:00,18:50,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 18:50
Dj Shorty & Mister Lees (Blendid Takeover),Friday,Cornish Arms,0,0,18:00 - 20:00,18:00,20:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 20:00
Charlotte May,Friday,Crooner'S Corner,0,0,18:00 - 18:45,18:00,18:45,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 18:45
Dj Milo [É Soul Cultura Takeover],Friday,Firmly Rooted,43,43,18:00 - 20:00,18:00,20:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 20:00
Charlie Porter (Chapter 10),Friday,Genosys,0,0,18:00 - 20:00,18:00,20:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 20:00
Ella Knight B2B Jeremy Slyvester,Friday,Glade Dome,49,29,18:00 - 19:30,18:00,19:30,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:30
Dance Class: Reggaeton,Friday,Glasto Latino,58,27,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Kiss Nuka (Live),Friday,Greenpeace,55,26,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Louis Vi,Friday,Laboratory Stage,0,0,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
I. Jordan,Friday,Levels,42,44,18:00 - 19:30,18:00,19:30,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:30
Novara Media Panel Event: Can Humanity Sort Its Shit Out?,Friday,Nomad,0,0,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Pj Harvey,Friday,Pyramid Stage,51,43,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Some Animals Are More Equal Than Others - Jolyon Rubinstein,Friday,Speakers Forum,0,0,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Us,Friday,Strummerville,48,12,18:00 - 18:40,18:00,18:40,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 18:40
Tom Tucker B2B Dave Trotter,Friday,The Bug,41,25,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Rumble In The Jungle Takeover: Zimma B2B Esme Banks,Friday,The Hive,0,0,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Dexys,Friday,The Park Stage,41,19,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Chris Arnold'S Wedding Disco,Friday,Village Inn,0,0,18:00 - 20:00,18:00,20:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 20:00
Jack Valero,Friday,Wishing Well,42,20,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Arlo Parks,Friday,Woodsies,43,52,18:00 - 19:00,18:00,19:00,28/06/2024,28/06/2024,28/06/2024 18:00,28/06/2024 19:00
Close,Friday,A Little More Sensation,0,0,18:05 - 23:30,18:05,23:30,28/06/2024,28/06/2024,28/06/2024 18:05,28/06/2024 23:30
English Disco Lovers,Friday,Glade,51,29,18:05 - 18:35,18:05,18:35,28/06/2024,28/06/2024,28/06/2024 18:05,28/06/2024 18:35
Eloise & Jack,Friday,Circus Big Top,57,34,18:10 - 18:16,18:10,18:16,28/06/2024,28/06/2024,28/06/2024 18:10,28/06/2024 18:16
Beyond Repair Dance,Friday,The Astrolabe Theatre,0,0,18:10 - 18:40,18:10,18:40,28/06/2024,28/06/2024,28/06/2024 18:10,28/06/2024 18:40
John Hegley,Friday,Poetry&Words,0,0,18:12 - 18:57,18:12,18:57,28/06/2024,28/06/2024,28/06/2024 18:12,28/06/2024 18:57
Dead Horse Bay,Friday,The Bandstand,56,38,18:15 - 19:00,18:15,19:00,28/06/2024,28/06/2024,28/06/2024 18:15,28/06/2024 19:00
Kwabana Lindsay Show,Friday,The Pavement,0,0,18:15 - 18:45,18:15,18:45,28/06/2024,28/06/2024,28/06/2024 18:15,28/06/2024 18:45
Sam Lee,Friday,Toad Hall,0,0,18:15 - 19:05,18:15,19:05,28/06/2024,28/06/2024,28/06/2024 18:15,28/06/2024 19:05
Stone Jets,Friday,West Holts Bar,59,29,18:15 - 18:45,18:15,18:45,28/06/2024,28/06/2024,28/06/2024 18:15,28/06/2024 18:45
Charlie Bicknell Is Holding Out For A Hero,Friday,Outside Circus Stage,59,33,18:18 - 18:30,18:18,18:30,28/06/2024,28/06/2024,28/06/2024 18:18,28/06/2024 18:30
Close,Friday,The Glebe,60,33,18:20 - 18:50,18:20,18:50,28/06/2024,28/06/2024,28/06/2024 18:20,28/06/2024 18:50
The Black Eagles,Friday,Circus Big Top,57,34,18:21 - 18:46,18:21,18:46,28/06/2024,28/06/2024,28/06/2024 18:21,28/06/2024 18:46
Tanita Tikaram,Friday,Acoustic Stage,66,38,18:30 - 19:30,18:30,19:30,28/06/2024,28/06/2024,28/06/2024 18:30,28/06/2024 19:30
Chloe Slater,Friday,Bbc Music Introducing,45,44,18:30 - 19:00,18:30,19:00,28/06/2024,28/06/2024,28/06/2024 18:30,28/06/2024 19:00
Nina Conti,Friday,Cabaret,62,26,18:30 - 19:00,18:30,19:00,28/06/2024,28/06/2024,28/06/2024 18:30,28/06/2024 19:00
Mike Dennis,Friday,Croissant Neuf Bandstand,55,21,18:30 - 19:30,18:30,19:30,28/06/2024,28/06/2024,28/06/2024 18:30,28/06/2024 19:30
"All Of Us Strangers + Q&A With Paul Mescal, Andrew Scott & Director Andrew Haigh 15",Friday,Pilton Palais Cinema,64,36,18:30 - 20:45,18:30,20:45,28/06/2024,28/06/2024,28/06/2024 18:30,28/06/2024 20:45
Louvre On The Move,Friday,Walkabouts,60,33,18:30 - 19:00,18:30,19:00,28/06/2024,28/06/2024,28/06/2024 18:30,28/06/2024 19:00
Danny Brown,Friday,West Holts Stage,57,31,18:30 - 19:30,18:30,19:30,28/06/2024,28/06/2024,28/06/2024 18:30,28/06/2024 19:30
Lulu,Friday,Avalon Stage,66,38,18:35 - 19:35,18:35,19:35,28/06/2024,28/06/2024,28/06/2024 18:35,28/06/2024 19:35
K Klass,Friday,Glade,51,29,18:35 - 19:35,18:35,19:35,28/06/2024,28/06/2024,28/06/2024 18:35,28/06/2024 19:35
The 2 Lisas,Friday,Outside Circus Stage,59,33,18:35 - 18:43,18:35,18:43,28/06/2024,28/06/2024,28/06/2024 18:35,28/06/2024 18:43
Seb Lowe,Friday,Left Field,52,33,18:40 - 19:20,18:40,19:20,28/06/2024,28/06/2024,28/06/2024 18:40,28/06/2024 19:20
Jonathan Pie,Friday,The Astrolabe Theatre,0,0,18:40 - 19:45,18:40,19:45,28/06/2024,28/06/2024,28/06/2024 18:40,28/06/2024 19:45
Matthew One Man,Friday,The Gateway,0,0,18:40 - 19:25,18:40,19:25,28/06/2024,28/06/2024,28/06/2024 18:40,28/06/2024 19:25
Anne-Marie,Friday,Other Stage,47,34,18:45 - 19:45,18:45,19:45,28/06/2024,28/06/2024,28/06/2024 18:45,28/06/2024 19:45
The Space Cowboy,Friday,Outside Circus Stage,59,33,18:48 - 19:18,18:48,19:18,28/06/2024,28/06/2024,28/06/2024 18:48,28/06/2024 19:18
Toby Spin,Friday,Blind Tiger,0,0,18:50 - 19:40,18:50,19:40,28/06/2024,28/06/2024,28/06/2024 18:50,28/06/2024 19:40
Tina Segner,Friday,Circus Big Top,57,34,18:51 - 18:56,18:51,18:56,28/06/2024,28/06/2024,28/06/2024 18:51,28/06/2024 18:56
Guns Of Navarone,Friday,The Glebe,60,33,18:55 - 19:25,18:55,19:25,28/06/2024,28/06/2024,28/06/2024 18:55,28/06/2024 19:25
Ro-G1 & Lesula - Introspect Takeover,Friday,Babylon Uprising,0,0,19:00 - 20:00,19:00,20:00,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 20:00
Jayahadadream,Friday,Bread And Roses,0,0,19:00 - 19:40,19:00,19:40,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 19:40
Feel It: Jaguar,Friday,Greenpeace,55,26,19:00 - 20:00,19:00,20:00,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 20:00
Eva Scott,Friday,Lunched Out Lizards,0,0,19:00 - 20:00,19:00,20:00,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 20:00
Tba,Friday,Mandala Stage,0,0,19:00 - 20:00,19:00,20:00,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 20:00
Swoose,Friday,San Remo,45,47,19:00 - 20:30,19:00,20:30,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 20:30
Annie Mac - Before Midnight W/ Bestley + Scarlett O’Malley,Friday,Stonebridge Bar,42,18,19:00 - 00:00,19:00,00:00,28/06/2024,29/06/2024,28/06/2024 19:00,29/06/2024 00:00
The Royston Club,Friday,Strummerville,48,12,19:00 - 19:40,19:00,19:40,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 19:40
Maha Quest,Friday,The Bug,41,25,19:00 - 20:00,19:00,20:00,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 20:00
Rumble In The Jungle Takeover: Monroller B2B Noisy Antics,Friday,The Hive,0,0,19:00 - 20:00,19:00,20:00,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 20:00
Mae Challis Live!,Friday,The Taphouse,0,0,19:00 - 21:00,19:00,21:00,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 21:00
Love Life Disco (Dj Set),Friday,Wishing Well,42,20,19:00 - 19:45,19:00,19:45,28/06/2024,28/06/2024,28/06/2024 19:00,28/06/2024 19:45
Laura Smyth,Friday,Cabaret,62,26,19:05 - 19:35,19:05,19:35,28/06/2024,28/06/2024,28/06/2024 19:05,28/06/2024 19:35
Circus Funtasia,Friday,Circus Big Top,57,34,19:06 - 20:16,19:06,20:16,28/06/2024,28/06/2024,28/06/2024 19:06,28/06/2024 20:16
Sam Danson 'Bi-Topia',Friday,Poetry&Words,0,0,19:10 - 20:00,19:10,20:00,28/06/2024,28/06/2024,28/06/2024 19:10,28/06/2024 20:00
Crazy P [Live],Friday,Lonely Hearts Club,44,41,19:15 - 20:15,19:15,20:15,28/06/2024,28/06/2024,28/06/2024 19:15,28/06/2024 20:15
Ballerinas,Friday,Outside Circus Stage,59,33,19:23 - 19:53,19:23,19:53,28/06/2024,28/06/2024,28/06/2024 19:23,28/06/2024 19:53
Pixey,Friday,Bbc Music Introducing,45,44,19:30 - 20:00,19:30,20:00,28/06/2024,28/06/2024,28/06/2024 19:30,28/06/2024 20:00
Izco + Liam Bailey (Live),Friday,Glade Dome,49,29,19:30 - 21:00,19:30,21:00,28/06/2024,28/06/2024,28/06/2024 19:30,28/06/2024 21:00
Bonobo [Dj],Friday,Levels,42,44,19:30 - 21:00,19:30,21:00,28/06/2024,28/06/2024,28/06/2024 19:30,28/06/2024 21:00
Mohawkestra,Friday,The Bandstand,56,38,19:30 - 20:30,19:30,20:30,28/06/2024,28/06/2024,28/06/2024 19:30,28/06/2024 20:30
Aurora,Friday,The Park Stage,41,19,19:30 - 20:30,19:30,20:30,28/06/2024,28/06/2024,28/06/2024 19:30,28/06/2024 20:30
Sam Scherdel,Friday,Toad Hall,0,0,19:30 - 20:20,19:30,20:20,28/06/2024,28/06/2024,28/06/2024 19:30,28/06/2024 20:20
Declan Mckenna,Friday,Woodsies,43,52,19:30 - 20:30,19:30,20:30,28/06/2024,28/06/2024,28/06/2024 19:30,28/06/2024 20:30
Fonzie,Friday,Blind Tiger,0,0,19:40 - 20:30,19:40,20:30,28/06/2024,28/06/2024,28/06/2024 19:40,28/06/2024 20:30
Talal Kartouti,Friday,Cabaret,62,26,19:40 - 20:10,19:40,20:10,28/06/2024,28/06/2024,28/06/2024 19:40,28/06/2024 20:10
Gok Wan,Friday,Glade,51,29,19:45 - 20:55,19:45,20:55,28/06/2024,28/06/2024,28/06/2024 19:45,28/06/2024 20:55
Lcd Soundsystem,Friday,Pyramid Stage,51,43,19:45 - 21:00,19:45,21:00,28/06/2024,28/06/2024,28/06/2024 19:45,28/06/2024 21:00
Closedown,Friday,The Astrolabe Theatre,0,0,19:45 - 00:00,19:45,00:00,28/06/2024,29/06/2024,28/06/2024 19:45,29/06/2024 00:00
She'S Got Brass,Friday,West Holts Bar,59,29,19:45 - 20:15,19:45,20:15,28/06/2024,28/06/2024,28/06/2024 19:45,28/06/2024 20:15
Stornoway,Friday,Wishing Well,42,20,19:45 - 20:45,19:45,20:45,28/06/2024,28/06/2024,28/06/2024 19:45,28/06/2024 20:45
Sprints,Friday,Left Field,52,33,19:50 - 20:30,19:50,20:30,28/06/2024,28/06/2024,28/06/2024 19:50,28/06/2024 20:30
Cirk Hes Presents Rosenwyn,Friday,Outside Circus Stage,59,33,19:58 - 20:04,19:58,20:04,28/06/2024,28/06/2024,28/06/2024 19:58,28/06/2024 20:04
Scouting For Girls,Friday,Acoustic Stage,66,38,20:00 - 21:00,20:00,21:00,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 21:00
Coast 2 Coast [Gene & The Ghost],Friday,Assembly,40,42,20:00 - 22:00,20:00,22:00,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 22:00
Charles Greene,Friday,Babylon Uprising,0,0,20:00 - 21:00,20:00,21:00,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 21:00
Ushti Baba,Friday,Bimble Inn,41,16,20:00 - 21:00,20:00,21:00,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 21:00
Compère: Cerys Nelmes,Friday,Cabaret,62,26,20:00 - 00:00,20:00,00:00,28/06/2024,29/06/2024,28/06/2024 20:00,29/06/2024 00:00
Natty Lou (Blendid Takeover),Friday,Cornish Arms,0,0,20:00 - 21:00,20:00,21:00,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 21:00
Nigel Shaw + Bethan Lloyd,Friday,Croissant Neuf Bandstand,55,21,20:00 - 20:45,20:00,20:45,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 20:45
Jamz Supernova [É Soul Cultura Takeover],Friday,Firmly Rooted,43,43,20:00 - 22:00,20:00,22:00,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 22:00
Wes Baggaley,Friday,Genosys,0,0,20:00 - 21:30,20:00,21:30,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 21:30
Feel It: Dj Boring B2B Joshua James,Friday,Greenpeace,55,26,20:00 - 21:30,20:00,21:30,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 21:30
Disco And Cinema,Friday,Humblewell Active Platform,42,21,20:00 - 01:00,20:00,01:00,28/06/2024,29/06/2024,28/06/2024 20:00,29/06/2024 01:00
Mia Koden,Friday,Iicon,66,21,20:00 - 22:30,20:00,22:30,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 22:30
T Sounds,Friday,Lunched Out Lizards,0,0,20:00 - 21:00,20:00,21:00,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 21:00
Giya,Friday,Strummerville,48,12,20:00 - 20:40,20:00,20:40,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 20:40
"Notting Hill Carnival Presents: Gladdy Wax, Mark Professor, David Hill, Mr Fix It",Friday,Terminal 1,0,0,20:00 - 03:00,20:00,03:00,28/06/2024,29/06/2024,28/06/2024 20:00,29/06/2024 03:00
Krafty Kuts,Friday,The Bug,41,25,20:00 - 21:00,20:00,21:00,28/06/2024,28/06/2024,28/06/2024 20:00,28/06/2024 21:00
Haircut 100,Friday,Avalon Stage,66,38,20:05 - 21:05,20:05,21:05,28/06/2024,28/06/2024,28/06/2024 20:05,28/06/2024 21:05
New York Brass Band,Friday,Outside Circus Stage,59,33,20:09 - 20:54,20:09,20:54,28/06/2024,28/06/2024,28/06/2024 20:09,28/06/2024 20:54
Sikisa,Friday,Cabaret,62,26,20:15 - 20:45,20:15,20:45,28/06/2024,28/06/2024,28/06/2024 20:15,28/06/2024 20:45
Heilung,Friday,West Holts Stage,57,31,20:15 - 21:30,20:15,21:30,28/06/2024,28/06/2024,28/06/2024 20:15,28/06/2024 21:30
Cirk Hes Presents Charlotte And Nadine,Friday,Circus Big Top,57,34,20:21 - 20:31,20:21,20:31,28/06/2024,28/06/2024,28/06/2024 20:21,28/06/2024 20:31
Fizz,Friday,Bbc Music Introducing,45,44,20:30 - 21:00,20:30,21:00,28/06/2024,28/06/2024,28/06/2024 20:30,28/06/2024 21:00
My-R,Friday,Blind Tiger,0,0,20:30 - 21:20,20:30,21:20,28/06/2024,28/06/2024,28/06/2024 20:30,28/06/2024 21:20
Eliza Rose [Live],Friday,Lonely Hearts Club,44,41,20:30 - 21:30,20:30,21:30,28/06/2024,28/06/2024,28/06/2024 20:30,28/06/2024 21:30
Plumm,Friday,Mandala Stage,0,0,20:30 - 21:30,20:30,21:30,28/06/2024,28/06/2024,28/06/2024 20:30,28/06/2024 21:30
D-Block Europe,Friday,Other Stage,47,34,20:30 - 21:30,20:30,21:30,28/06/2024,28/06/2024,28/06/2024 20:30,28/06/2024 21:30
Ross From Friends,Friday,San Remo,45,47,20:30 - 22:00,20:30,22:00,28/06/2024,28/06/2024,28/06/2024 20:30,28/06/2024 22:00
The Barefoot Bandit,Friday,The Hive,0,0,20:30 - 21:30,20:30,21:30,28/06/2024,28/06/2024,28/06/2024 20:30,28/06/2024 21:30
Leo,Friday,Circus Big Top,57,34,20:36 - 20:42,20:36,20:42,28/06/2024,28/06/2024,28/06/2024 20:36,28/06/2024 20:42
Compere: Dave Chameleon,Friday,Circus Big Top,57,34,20:45 - 01:30,20:45,01:30,28/06/2024,29/06/2024,28/06/2024 20:45,29/06/2024 01:30
Edwin James Pope,Friday,Toad Hall,0,0,20:45 - 21:30,20:45,21:30,28/06/2024,28/06/2024,28/06/2024 20:45,28/06/2024 21:30
Tba,Friday,Wishing Well,42,20,20:45 - 21:45,20:45,21:45,28/06/2024,28/06/2024,28/06/2024 20:45,28/06/2024 21:45
Duo Santus,Friday,Circus Big Top,57,34,20:47 - 20:53,20:47,20:53,28/06/2024,28/06/2024,28/06/2024 20:47,28/06/2024 20:53
Doc Brown,Friday,Cabaret,62,26,20:50 - 21:20,20:50,21:20,28/06/2024,28/06/2024,28/06/2024 20:50,28/06/2024 21:20
The Birds,Friday,Walkabouts,60,33,20:50 - 21:35,20:50,21:35,28/06/2024,28/06/2024,28/06/2024 20:50,28/06/2024 21:35
Close,Friday,Outside Circus Stage,59,33,20:54 - 23:30,20:54,23:30,28/06/2024,28/06/2024,28/06/2024 20:54,28/06/2024 23:30
English Disco Lovers,Friday,Glade,51,29,20:55 - 21:25,20:55,21:25,28/06/2024,28/06/2024,28/06/2024 20:55,28/06/2024 21:25
Ellis Grover,Friday,Circus Big Top,57,34,20:58 - 21:08,20:58,21:08,28/06/2024,28/06/2024,28/06/2024 20:58,28/06/2024 21:08
Yemz,Friday,Babylon Uprising,0,0,21:00 - 22:00,21:00,22:00,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:00
Carly Wilford (Blendid Takeover),Friday,Cornish Arms,0,0,21:00 - 22:00,21:00,22:00,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:00
Acoustic Open Mic,Friday,Croissant Neuf Bandstand,55,21,21:00 - 21:45,21:00,21:45,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 21:45
Guest Dj,Friday,Deluxe Diner,64,17,21:00 - 22:30,21:00,22:30,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:30
Keyrah,Friday,Glade Dome,49,29,21:00 - 22:30,21:00,22:30,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:30
Billy Bragg,Friday,Left Field,52,33,21:00 - 22:00,21:00,22:00,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:00
Anotr,Friday,Levels,42,44,21:00 - 22:30,21:00,22:30,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:30
Earmilk,Friday,Lunched Out Lizards,0,0,21:00 - 22:00,21:00,22:00,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:00
25 Years Of Defected Records,Friday,Nowhere,0,0,21:00 - 00:00,21:00,00:00,28/06/2024,29/06/2024,28/06/2024 21:00,29/06/2024 00:00
Sam Divine B2B Gorgon City B2B Arielle Free,Friday,Nowhere,0,0,21:00 - 00:00,21:00,00:00,28/06/2024,29/06/2024,28/06/2024 21:00,29/06/2024 00:00
Rishi,Friday,Platform 23,0,0,21:00 - 23:30,21:00,23:30,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 23:30
Wonderment Presents: Elevate,Friday,Scissors,42,21,21:00 - 22:30,21:00,22:30,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:30
Mr Key,Friday,Strummerville,48,12,21:00 - 21:40,21:00,21:40,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 21:40
Kangaroo Moon,Friday,The Bandstand,56,38,21:00 - 22:00,21:00,22:00,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:00
Badger,Friday,The Bug,41,25,21:00 - 22:00,21:00,22:00,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:00
Rum Shack Wild Card,Friday,The Rum Shack,0,0,21:00 - 22:45,21:00,22:45,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:45
Mark Miller,Friday,The Taphouse,0,0,21:00 - 23:00,21:00,23:00,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 23:00
The Runaway Christmas Tree Fairy,Friday,Walkabouts,60,33,21:00 - 21:45,21:00,21:45,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 21:45
Sampha,Friday,Woodsies,43,52,21:00 - 22:00,21:00,22:00,28/06/2024,28/06/2024,28/06/2024 21:00,28/06/2024 22:00
Toby Walker,Friday,Circus Big Top,57,34,21:13 - 21:21,21:13,21:21,28/06/2024,28/06/2024,28/06/2024 21:13,28/06/2024 21:21
King Krule,Friday,The Park Stage,41,19,21:15 - 22:15,21:15,22:15,28/06/2024,28/06/2024,28/06/2024 21:15,28/06/2024 22:15
Bustawidemove,Friday,Blind Tiger,0,0,21:20 - 22:10,21:20,22:10,28/06/2024,28/06/2024,28/06/2024 21:20,28/06/2024 22:10
Jen Brister,Friday,Cabaret,62,26,21:25 - 21:55,21:25,21:55,28/06/2024,28/06/2024,28/06/2024 21:25,28/06/2024 21:55
Faithless,Friday,Glade,51,29,21:25 - 22:40,21:25,22:40,28/06/2024,28/06/2024,28/06/2024 21:25,28/06/2024 22:40
Charlie Bicknell - Supersonic Woman,Friday,Circus Big Top,57,34,21:26 - 21:38,21:26,21:38,28/06/2024,28/06/2024,28/06/2024 21:26,28/06/2024 21:38
The Bootleg Beatles,Friday,Acoustic Stage,66,38,21:30 - 22:45,21:30,22:45,28/06/2024,28/06/2024,28/06/2024 21:30,28/06/2024 22:45
Ahadadream,Friday,Genosys,0,0,21:30 - 23:30,21:30,23:30,28/06/2024,28/06/2024,28/06/2024 21:30,28/06/2024 23:30
Feel It: Cormac,Friday,Greenpeace,55,26,21:30 - 22:45,21:30,22:45,28/06/2024,28/06/2024,28/06/2024 21:30,28/06/2024 22:45
Sg Lewis + Tove Lo: Club Heat,Friday,Lonely Hearts Club,44,41,21:30 - 23:30,21:30,23:30,28/06/2024,28/06/2024,28/06/2024 21:30,28/06/2024 23:30
The Cloudmen,Friday,Walkabouts,60,33,21:30 - 22:30,21:30,22:30,28/06/2024,28/06/2024,28/06/2024 21:30,28/06/2024 22:30
Tarju Le’Sano,Friday,West Holts Bar,59,29,21:30 - 22:15,21:30,22:15,28/06/2024,28/06/2024,28/06/2024 21:30,28/06/2024 22:15
Kate Nash,Friday,Avalon Stage,66,38,21:35 - 22:35,21:35,22:35,28/06/2024,28/06/2024,28/06/2024 21:35,28/06/2024 22:35
Ballerinas,Friday,Circus Big Top,57,34,21:43 - 21:53,21:43,21:53,28/06/2024,28/06/2024,28/06/2024 21:43,28/06/2024 21:53
Vulva Voce,Friday,The Hive,0,0,21:45 - 22:15,21:45,22:15,28/06/2024,28/06/2024,28/06/2024 21:45,28/06/2024 22:15
Mystic Mirror Show Globe,Friday,Walkabouts,60,33,21:45 - 22:45,21:45,22:45,28/06/2024,28/06/2024,28/06/2024 21:45,28/06/2024 22:45
Pumarosa,Friday,Wishing Well,42,20,21:45 - 23:00,21:45,23:00,28/06/2024,28/06/2024,28/06/2024 21:45,28/06/2024 23:00
Bexi - Barbarella,Friday,Circus Big Top,57,34,21:58 - 22:04,21:58,22:04,28/06/2024,28/06/2024,28/06/2024 21:58,28/06/2024 22:04
Fatboy Slim,Friday,Arcadia,41,25,22:00 - 23:30,22:00,23:30,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:30
Jumbi Soundsystem,Friday,Arrivals,0,0,22:00 - 23:00,22:00,23:00,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:00
Kt,Friday,Assembly,40,42,22:00 - 23:30,22:00,23:30,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:30
Neffa-T,Friday,Babylon Uprising,0,0,22:00 - 23:00,22:00,23:00,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:00
Emmanuel Sonubi,Friday,Cabaret,62,26,22:00 - 22:30,22:00,22:30,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 22:30
Fulu Miziki,Friday,Carhenge,58,36,22:00 - 23:00,22:00,23:00,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:00
Oliver Sudden (Blendid Takeover),Friday,Cornish Arms,0,0,22:00 - 23:00,22:00,23:00,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:00
Acoustic Open Mic,Friday,Croissant Neuf Bandstand,55,21,22:00 - 22:45,22:00,22:45,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 22:45
Luke Una [É Soul Cultura Takeover],Friday,Firmly Rooted,43,43,22:00 - 00:00,22:00,00:00,28/06/2024,29/06/2024,28/06/2024 22:00,29/06/2024 00:00
The Muffin Man,Friday,Flying Bus,0,0,22:00 - 23:30,22:00,23:30,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:30
Dj Polly Crow,Friday,Lunched Out Lizards,0,0,22:00 - 23:00,22:00,23:00,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:00
Farhannah,Friday,Mandala Stage,0,0,22:00 - 23:00,22:00,23:00,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:00
Mez Yard Guests,Friday,Mez Yard,0,0,22:00 - 23:00,22:00,23:00,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:00
Queer House Party: Harry Gay And Passer,Friday,Nomad,0,0,22:00 - 00:00,22:00,00:00,28/06/2024,29/06/2024,28/06/2024 22:00,29/06/2024 00:00
Luke Solomon,Friday,Nyc Downlow,0,0,22:00 - 23:25,22:00,23:25,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:25
Dua Lipa,Friday,Pyramid Stage,51,43,22:00 - 23:45,22:00,23:45,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:45
Theo Kottis,Friday,San Remo,45,47,22:00 - 23:30,22:00,23:30,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:30
Mad Apple Circus,Friday,Sensation Seekers Stage,0,0,22:00 - 22:45,22:00,22:45,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 22:45
Sabiyha,Friday,Strummerville,48,12,22:00 - 22:40,22:00,22:40,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 22:40
Maze,Friday,The Meatrack,0,0,22:00 - 00:00,22:00,00:00,28/06/2024,29/06/2024,28/06/2024 22:00,29/06/2024 00:00
Dj Baby Soul,Friday,The Rocket Lounge,64,16,22:00 - 06:00,22:00,06:00,28/06/2024,29/06/2024,28/06/2024 22:00,29/06/2024 06:00
Persistance,Friday,The Salon Carousel,0,0,22:00 - 23:00,22:00,23:00,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:00
Brownton Abbey - Laud Brownton,Friday,The Sistxrhood,0,0,22:00 - 22:30,22:00,22:30,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 22:30
Rinse 30Th Anniversary - Arthi,Friday,The Temple,0,0,22:00 - 23:00,22:00,23:00,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 23:00
Glowbros,Friday,Walkabouts,60,33,22:00 - 00:00,22:00,00:00,28/06/2024,29/06/2024,28/06/2024 22:00,29/06/2024 00:00
Corvus Angelicus,Friday,Walkabouts,60,33,22:00 - 22:45,22:00,22:45,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 22:45
High Flyers,Friday,Walkabouts,60,33,22:00 - 22:45,22:00,22:45,28/06/2024,28/06/2024,28/06/2024 22:00,28/06/2024 22:45
The Space Cowboy,Friday,Circus Big Top,57,34,22:09 - 22:34,22:09,22:34,28/06/2024,28/06/2024,28/06/2024 22:09,28/06/2024 22:34
Lucy Lee,Friday,Blind Tiger,0,0,22:10 - 23:00,22:10,23:00,28/06/2024,28/06/2024,28/06/2024 22:10,28/06/2024 23:00
Idles,Friday,Other Stage,47,34,22:15 - 23:30,22:15,23:30,28/06/2024,28/06/2024,28/06/2024 22:15,28/06/2024 23:30
Jungle,Friday,West Holts Stage,57,31,22:15 - 23:45,22:15,23:45,28/06/2024,28/06/2024,28/06/2024 22:15,28/06/2024 23:45
Chris Holt,Friday,Deluxe Diner,64,17,22:30 - 00:00,22:30,00:00,28/06/2024,29/06/2024,28/06/2024 22:30,29/06/2024 00:00
P-Rallel,Friday,Glade Dome,49,29,22:30 - 00:00,22:30,00:00,28/06/2024,29/06/2024,28/06/2024 22:30,29/06/2024 00:00
Introspekt,Friday,Iicon,66,21,22:30 - 01:00,22:30,01:00,28/06/2024,29/06/2024,28/06/2024 22:30,29/06/2024 01:00
Kelly Lee Owens [Dj],Friday,Levels,42,44,22:30 - 00:00,22:30,00:00,28/06/2024,29/06/2024,28/06/2024 22:30,29/06/2024 00:00
Rumba De Bodas,Friday,The Bandstand,56,38,22:30 - 23:30,22:30,23:30,28/06/2024,28/06/2024,28/06/2024 22:30,28/06/2024 23:30
Jfb,Friday,The Hive,0,0,22:30 - 23:30,22:30,23:30,28/06/2024,28/06/2024,28/06/2024 22:30,28/06/2024 23:30
Brownton Abbey - Bones Tan Jones,Friday,The Sistxrhood,0,0,22:30 - 22:55,22:30,22:55,28/06/2024,28/06/2024,28/06/2024 22:30,28/06/2024 22:55
The Primitives,Friday,Toad Hall,0,0,22:30 - 23:30,22:30,23:30,28/06/2024,28/06/2024,28/06/2024 22:30,28/06/2024 23:30
The Birds,Friday,Walkabouts,60,33,22:30 - 23:15,22:30,23:15,28/06/2024,28/06/2024,28/06/2024 22:30,28/06/2024 23:15
Jamie Xx,Friday,Woodsies,43,52,22:30 - 23:45,22:30,23:45,28/06/2024,28/06/2024,28/06/2024 22:30,28/06/2024 23:45
Alexandra Haddow,Friday,Cabaret,62,26,22:35 - 23:05,22:35,23:05,28/06/2024,28/06/2024,28/06/2024 22:35,28/06/2024 23:05
Leo,Friday,Circus Big Top,57,34,22:39 - 22:45,22:39,22:45,28/06/2024,28/06/2024,28/06/2024 22:39,28/06/2024 22:45
Feel It: I Jordan,Friday,Greenpeace,55,26,22:45 - 23:45,22:45,23:45,28/06/2024,28/06/2024,28/06/2024 22:45,28/06/2024 23:45
Guy.In.Glasses,Friday,Peace Stage,0,0,22:45 - 23:45,22:45,23:45,28/06/2024,28/06/2024,28/06/2024 22:45,28/06/2024 23:45
Enzo Siragusa,Friday,Glade,51,29,22:50 - 00:00,22:50,00:00,28/06/2024,29/06/2024,28/06/2024 22:50,29/06/2024 00:00
Cirque Du Vulgar,Friday,Circus Big Top,57,34,22:55 - 00:05,22:55,00:05,28/06/2024,29/06/2024,28/06/2024 22:55,29/06/2024 00:05
Feeding The Fish,Friday,Sensation Seekers Stage,0,0,22:55 - 23:03,22:55,23:03,28/06/2024,28/06/2024,28/06/2024 22:55,28/06/2024 23:03
Brownton Abbey - Laud Brownton,Friday,The Sistxrhood,0,0,22:55 - 23:25,22:55,23:25,28/06/2024,28/06/2024,28/06/2024 22:55,28/06/2024 23:25
Vedic Roots Soundsystem,Friday,Arrivals,0,0,23:00 - 00:00,23:00,00:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:00
Dj Adhd & Nikki Nair,Friday,Babylon Uprising,0,0,23:00 - 00:00,23:00,00:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:00
Mk,Friday,Blind Tiger,0,0,23:00 - 00:00,23:00,00:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:00
Beatbox Collective Takeover (Blendid Takeover),Friday,Cornish Arms,0,0,23:00 - 00:00,23:00,00:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:00
Dj And Dancing,Friday,Glasto Latino,58,27,23:00 - 00:00,23:00,00:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:00
Edie Blue,Friday,Laboratory Stage,0,0,23:00 - 23:55,23:00,23:55,28/06/2024,28/06/2024,28/06/2024 23:00,28/06/2024 23:55
She'S Got Brass,Friday,Lunched Out Lizards,0,0,23:00 - 00:00,23:00,00:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:00
Russ Ryan & Mo Fingaz,Friday,Meeting Place Bar,0,0,23:00 - 03:00,23:00,03:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 03:00
Amancai & Arias,Friday,Mez Yard,0,0,23:00 - 01:00,23:00,01:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 01:00
Fontaines D.C.,Friday,The Park Stage,41,19,23:00 - 00:15,23:00,00:15,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:15
Sister Suzie,Friday,The Rocket Lounge,64,16,23:00 - 00:00,23:00,00:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:00
Chiminyo,Friday,The Rum Shack,0,0,23:00 - 00:00,23:00,00:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:00
Rudi,Friday,The Salon Carousel,0,0,23:00 - 00:00,23:00,00:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:00
Jimmy Lopez,Friday,The Taphouse,0,0,23:00 - 01:00,23:00,01:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 01:00
Rinse 30Th Anniversary - Bakey B2B Izco,Friday,The Temple,0,0,23:00 - 00:00,23:00,00:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 00:00
Transgressive Takeover (Line Up Tba),Friday,Wishing Well,42,20,23:00 - 06:00,23:00,06:00,28/06/2024,29/06/2024,28/06/2024 23:00,29/06/2024 06:00
Skindred,Friday,Avalon Stage,66,38,23:05 - 00:20,23:05,00:20,28/06/2024,29/06/2024,28/06/2024 23:05,29/06/2024 00:20
Les Ooh La Las,Friday,Cabaret,62,26,23:05 - 23:10,23:05,23:10,28/06/2024,28/06/2024,28/06/2024 23:05,28/06/2024 23:10
Dj J9,Friday,Cabaret,62,26,23:10 - 23:40,23:10,23:40,28/06/2024,28/06/2024,28/06/2024 23:10,28/06/2024 23:40
Leather Lungs + Master Reblasters,Friday,Sensation Seekers Stage,0,0,23:10 - 23:55,23:10,23:55,28/06/2024,28/06/2024,28/06/2024 23:10,28/06/2024 23:55
Brownton Abbey - Rhys' Pieces,Friday,The Sistxrhood,0,0,23:25 - 23:45,23:25,23:45,28/06/2024,28/06/2024,28/06/2024 23:25,28/06/2024 23:45
Caravan Of Lost Souls,Friday,A Little More Sensation,0,0,23:30 - 01:30,23:30,01:30,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 01:30
Arcadia And The Wadjuk Noongar - Warraloo Ceremony,Friday,Arcadia,41,25,23:30 - 23:40,23:30,23:40,28/06/2024,28/06/2024,28/06/2024 23:30,28/06/2024 23:40
Fantastic Man B2B Tornado Wallace,Friday,Assembly,40,42,23:30 - 01:00,23:30,01:00,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 01:00
Mad Dog Mcrea,Friday,Croissant Neuf,55,21,23:30 - 00:30,23:30,00:30,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 00:30
Korse,Friday,Flying Bus,0,0,23:30 - 01:00,23:30,01:00,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 01:00
Honey Dijon,Friday,Genosys,0,0,23:30 - 01:30,23:30,01:30,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 01:30
Sonny Fodera,Friday,Lonely Hearts Club,44,41,23:30 - 01:00,23:30,01:00,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 01:00
Joli Blon Cajun Band,Friday,Mandala Stage,0,0,23:30 - 00:30,23:30,00:30,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 00:30
Makadsi,Friday,Nyc Downlow,0,0,23:30 - 00:55,23:30,00:55,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 00:55
Eyes Wide Shut Duo Trapeze,Friday,Outside Circus Stage,59,33,23:30 - 23:36,23:30,23:36,28/06/2024,28/06/2024,28/06/2024 23:30,28/06/2024 23:36
"Prestige Pak W/ Lil C, Lagoon Femshayma, Architect + Handsome Rob",Friday,Platform 23,0,0,23:30 - 01:00,23:30,01:00,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 01:00
Sofia Kourtesis (Dj),Friday,San Remo,45,47,23:30 - 01:00,23:30,01:00,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 01:00
Kate Hutchinson,Friday,Scissors,42,21,23:30 - 00:30,23:30,00:30,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 00:30
Corvus Angelicus,Friday,Walkabouts,60,33,23:30 - 00:15,23:30,00:15,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 00:15
High Flyers,Friday,Walkabouts,60,33,23:30 - 00:15,23:30,00:15,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 00:15
The Runaway Christmas Tree Fairy,Friday,Walkabouts,60,33,23:30 - 00:15,23:30,00:15,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 00:15
Disco Turtle,Friday,Walkabouts,60,33,23:30 - 01:00,23:30,01:00,28/06/2024,29/06/2024,28/06/2024 23:30,29/06/2024 01:00
Joy Orbison,Friday,Arcadia,41,25,23:40 - 00:40,23:40,00:40,28/06/2024,29/06/2024,28/06/2024 23:40,29/06/2024 00:40
Fiery Jack Family,Friday,Outside Circus Stage,59,33,23:41 - 23:51,23:41,23:51,28/06/2024,28/06/2024,28/06/2024 23:41,28/06/2024 23:51
Noah & The Loners,Friday,Bread And Roses,0,0,23:45 - 00:40,23:45,00:40,28/06/2024,29/06/2024,28/06/2024 23:45,29/06/2024 00:40
Feeding The Fish,Friday,Cabaret,62,26,23:45 - 00:00,23:45,00:00,28/06/2024,29/06/2024,28/06/2024 23:45,29/06/2024 00:00
Confidence Man Presents: Active Scenes. Carlita,Friday,Greenpeace,55,26,23:45 - 01:00,23:45,01:00,28/06/2024,29/06/2024,28/06/2024 23:45,29/06/2024 01:00
Brownton Abbey - Thempress,Friday,The Sistxrhood,0,0,23:45 - 00:15,23:45,00:15,28/06/2024,29/06/2024,28/06/2024 23:45,29/06/2024 00:15
Mat Collishaw - Even To The End,Friday,Tree Stage,44,51,23:45 - 00:00,23:45,00:00,28/06/2024,29/06/2024,28/06/2024 23:45,29/06/2024 00:00
Gentleman George,Friday,Village Inn,0,0,23:45 - 01:00,23:45,01:00,28/06/2024,29/06/2024,28/06/2024 23:45,29/06/2024 01:00
The Ben Jones Experience Feat Vula,Friday,West Holts Bar,59,29,23:45 - 00:45,23:45,00:45,28/06/2024,29/06/2024,28/06/2024 23:45,29/06/2024 00:45
Bexi - Barbarella,Friday,Outside Circus Stage,59,33,23:56 - 00:02,23:56,00:02,28/06/2024,29/06/2024,28/06/2024 23:56,29/06/2024 00:02
Almass Badat,Saturday,Arrivals,0,0,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Bluetoof B2B Mi-El,Saturday,Babylon Uprising,0,0,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Feeding The Fish,Saturday,Cabaret,62,26,00:00 - 00:15,00:00,00:15,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 00:15
Noel Watson,Saturday,Deluxe Diner,64,17,00:00 - 01:30,00:00,01:30,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:30
Ido Plumes [Sleep Felt Far Away Takeover],Saturday,Firmly Rooted,43,43,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Gene On Earth,Saturday,Glade Dome,49,29,00:00 - 01:30,00:00,01:30,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:30
Eliane Correa & La Evolución Orquesta,Saturday,Glasto Latino,58,27,00:00 - 01:30,00:00,01:30,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:30
Tba,Saturday,Levels,42,44,00:00 - 01:30,00:00,01:30,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:30
Dj Couscous,Saturday,Lunched Out Lizards,0,0,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
London Trans+ Pride X The Chateau: Ivicore,Saturday,Nomad,0,0,00:00 - 01:30,00:00,01:30,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:30
Delilah Bon,Saturday,Peace Stage,0,0,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Aisha Mirza X The Cocoa Butter Club,Saturday,Scissors,42,21,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Erol Alkan B2B Dj Paulette,Saturday,Stonebridge Bar,42,18,00:00 - 01:30,00:00,01:30,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:30
Andy Carroll House & Electro Set,Saturday,Strummerville,48,12,00:00 - 07:12,00:00,07:12,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 07:12
Berthrands Toys,Saturday,The Astrolabe Theatre,0,0,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Headmix,Saturday,The Bandstand,56,38,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Type One Community: Jayu B2B Kyle Parsley,Saturday,The Hive,0,0,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Deptford Northern Soul Club,Saturday,The Meatrack,0,0,00:00 - 01:30,00:00,01:30,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:30
Frank Harvey Trio,Saturday,The Rocket Lounge,64,16,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Oneda,Saturday,The Rum Shack,0,0,00:00 - 00:45,00:00,00:45,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 00:45
1Bdi,Saturday,The Salon Carousel,0,0,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Sherelle,Saturday,The Sistxrhood,0,0,00:00 - 02:00,00:00,02:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 02:00
Critical Soundsystem; Kasra B2B Qzb B2B Spectral,Saturday,The Temple,0,0,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Jon Hopkins - Ritual - Immersive Album Listening Experience,Saturday,Tree Stage,44,51,00:00 - 00:50,00:00,00:50,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 00:50
Rotate 38 (Dj Set),Saturday,Wishing Well,42,20,00:00 - 01:00,00:00,01:00,30/06/2024,30/06/2024,29/06/2024 00:00,30/06/2024 01:00
Incandescence Presents Trio Jolee,Saturday,Outside Circus Stage,59,33,00:03 - 00:11,00:03,00:11,30/06/2024,30/06/2024,29/06/2024 00:03,30/06/2024 00:11
Buffo'S Wake,Saturday,Bimble Inn,41,16,00:15 - 01:15,00:15,01:15,30/06/2024,30/06/2024,29/06/2024 00:15,30/06/2024 01:15
Dj'S James Acaster & Nish Kumar,Saturday,Cabaret,62,26,00:15 - 02:00,00:15,02:00,30/06/2024,30/06/2024,29/06/2024 00:15,30/06/2024 02:00
Layla Benitez,Saturday,Glade,51,29,00:15 - 01:25,00:15,01:25,30/06/2024,30/06/2024,29/06/2024 00:15,30/06/2024 01:25
Iicon Av:3D,Saturday,Iicon,66,21,00:15 - 00:30,00:15,00:30,30/06/2024,30/06/2024,29/06/2024 00:15,30/06/2024 00:30
Oh My God! It'S The Church,Saturday,Sensation Seekers Stage,0,0,00:15 - 01:15,00:15,01:15,30/06/2024,30/06/2024,29/06/2024 00:15,30/06/2024 01:15
Area 51,Saturday,Outside Circus Stage,59,33,00:16 - 00:26,00:16,00:26,30/06/2024,30/06/2024,29/06/2024 00:16,30/06/2024 00:26
Cirque Du Vulgar,Saturday,Circus Big Top,57,34,00:19 - 01:29,00:19,01:29,30/06/2024,30/06/2024,29/06/2024 00:19,30/06/2024 01:29
Kak Hatt,Saturday,Blind Tiger,0,0,00:20 - 01:00,00:20,01:00,30/06/2024,30/06/2024,29/06/2024 00:20,30/06/2024 01:00
Radio 2'S Alternative Sounds Of The 90S With Dermot O'Leary,Saturday,Bbc Music Introducing,45,44,00:30 - 02:30,00:30,02:30,30/06/2024,30/06/2024,29/06/2024 00:30,30/06/2024 02:30
Dr Meaker,Saturday,Croissant Neuf,55,21,00:30 - 01:30,00:30,01:30,30/06/2024,30/06/2024,29/06/2024 00:30,30/06/2024 01:30
Afrodeutsche,Saturday,Iicon,66,21,00:30 - 02:00,00:30,02:00,30/06/2024,30/06/2024,29/06/2024 00:30,30/06/2024 02:00
K Motionz B2B Friction,Saturday,Lonely Hearts Club,44,41,00:30 - 02:00,00:30,02:00,30/06/2024,30/06/2024,29/06/2024 00:30,30/06/2024 02:00
The Egg (Electronic Set),Saturday,Lunched Out Lizards,0,0,00:30 - 02:00,00:30,02:00,30/06/2024,30/06/2024,29/06/2024 00:30,30/06/2024 02:00
Only Lovers Left Alive + Intro-Q&A With Tilda Swinton 15,Saturday,Pilton Palais Cinema,64,36,00:30 - 03:00,00:30,03:00,30/06/2024,30/06/2024,29/06/2024 00:30,30/06/2024 03:00
Mina & Bryte,Saturday,Platform 23,0,0,00:30 - 01:45,00:30,01:45,30/06/2024,30/06/2024,29/06/2024 00:30,30/06/2024 01:45
Antikvariniai Kaspirovskio Dantys,Saturday,Toad Hall,0,0,00:30 - 01:30,00:30,01:30,30/06/2024,30/06/2024,29/06/2024 00:30,30/06/2024 01:30
Aerial High Jinks,Saturday,Outside Circus Stage,59,33,00:31 - 00:39,00:31,00:39,30/06/2024,30/06/2024,29/06/2024 00:31,30/06/2024 00:39
Area 51,Saturday,Outside Circus Stage,59,33,00:44 - 00:54,00:44,00:54,30/06/2024,30/06/2024,29/06/2024 00:44,30/06/2024 00:54
Hot Chip (Dj Set),Saturday,Arcadia,41,25,00:45 - 02:00,00:45,02:00,30/06/2024,30/06/2024,29/06/2024 00:45,30/06/2024 02:00
Lubiana,Saturday,West Holts Bar,59,29,00:45 - 01:10,00:45,01:10,30/06/2024,30/06/2024,29/06/2024 00:45,30/06/2024 01:10
James Burton (Warp Records) Warp Beatless Mix,Saturday,Tree Stage,44,51,00:50 - 02:00,00:50,02:00,30/06/2024,30/06/2024,29/06/2024 00:50,30/06/2024 02:00
Raves R Us,Saturday,Outside Circus Stage,59,33,00:59 - 01:44,00:59,01:44,30/06/2024,30/06/2024,29/06/2024 00:59,30/06/2024 01:44
Zeemuffin,Saturday,Arrivals,0,0,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
Craig Richards,Saturday,Assembly,40,42,01:00 - 03:00,01:00,03:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 03:00
Max Gurn Vs Drippy Chin,Saturday,Babylon Uprising,0,0,01:00 - 02:45,01:00,02:45,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:45
Zero Hosted By Local,Saturday,Blind Tiger,0,0,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
Old Time Sailors,Saturday,Bread And Roses,0,0,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
Dj Lag [Sleep Felt Far Away Takeover],Saturday,Firmly Rooted,43,43,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
Hannah Holland,Saturday,Genosys,0,0,01:00 - 02:30,01:00,02:30,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:30
Ahadadream,Saturday,Greenpeace,55,26,01:00 - 03:00,01:00,03:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 03:00
Tom Mcq,Saturday,Mandala Stage,0,0,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
Jonny Henfrey,Saturday,Meeting Place Bar,0,0,01:00 - 03:00,01:00,03:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 03:00
Copperdollar: The Spirits Of Mezcal (Show),Saturday,Mez Yard,0,0,01:00 - 03:00,01:00,03:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 03:00
Dj Spen,Saturday,Nyc Downlow,0,0,01:00 - 02:25,01:00,02:25,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:25
Young Marco,Saturday,San Remo,45,47,01:00 - 03:00,01:00,03:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 03:00
Type One Community: Daisy B2B Sophia Violet (Girls Don'T Sync),Saturday,The Hive,0,0,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
The Marching Skaletons,Saturday,The Rocket Lounge,64,16,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
Pengshui,Saturday,The Rum Shack,0,0,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
Dj Cant Say No,Saturday,The Salon Carousel,0,0,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
Break Ft. Carasel,Saturday,The Temple,0,0,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
Glowbros,Saturday,Walkabouts,60,33,01:00 - 03:00,01:00,03:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 03:00
An Dannsa Dub,Saturday,Wishing Well,42,20,01:00 - 02:00,01:00,02:00,30/06/2024,30/06/2024,29/06/2024 01:00,30/06/2024 02:00
Intervention,Saturday,West Holts Bar,59,29,01:10 - 02:00,01:10,02:00,30/06/2024,30/06/2024,29/06/2024 01:10,30/06/2024 02:00
Flash Bang Brass,Saturday,The Astrolabe Theatre,0,0,01:15 - 02:00,01:15,02:00,30/06/2024,30/06/2024,29/06/2024 01:15,30/06/2024 02:00
Loominus,Saturday,Sensation Seekers Stage,0,0,01:25 - 01:40,01:25,01:40,30/06/2024,30/06/2024,29/06/2024 01:25,30/06/2024 01:40
Altern 8 / Mark Archer (Blendid Takeover),Saturday,Cornish Arms,0,0,01:30 - 03:00,01:30,03:00,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 03:00
Andy P,Saturday,Deluxe Diner,64,17,01:30 - 03:00,01:30,03:00,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 03:00
Chris Stussy B2B Rossi,Saturday,Flying Bus,0,0,01:30 - 04:00,01:30,04:00,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 04:00
Fatboy Slim,Saturday,Glade,51,29,01:30 - 03:00,01:30,03:00,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 03:00
Chaos In The Cbd,Saturday,Glade Dome,49,29,01:30 - 02:55,01:30,02:55,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 02:55
Latin Party,Saturday,Glasto Latino,58,27,01:30 - 03:00,01:30,03:00,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 03:00
Ben Hemsley,Saturday,Levels,42,44,01:30 - 03:00,01:30,03:00,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 03:00
London Trans+ Pride X The Chateau: Sippin T,Saturday,Nomad,0,0,01:30 - 03:00,01:30,03:00,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 03:00
Kneecap,Saturday,Peace Stage,0,0,01:30 - 02:15,01:30,02:15,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 02:15
Pxssy Palace X The Cocoa Butter Club,Saturday,Scissors,42,21,01:30 - 02:30,01:30,02:30,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 02:30
Jamz Supernova,Saturday,Stonebridge Bar,42,18,01:30 - 02:30,01:30,02:30,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 02:30
Dave Beer House & Electro Set,Saturday,Strummerville,48,12,01:30 - 03:00,01:30,03:00,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 03:00
Mandel Turner,Saturday,The Meatrack,0,0,01:30 - 03:00,01:30,03:00,30/06/2024,30/06/2024,29/06/2024 01:30,30/06/2024 03:00
Blanco (Live),Saturday,Platform 23,0,0,01:45 - 02:30,01:45,02:30,30/06/2024,30/06/2024,29/06/2024 01:45,30/06/2024 02:30
Wheel Of Four Tunes,Saturday,Sensation Seekers Stage,0,0,01:50 - 02:50,01:50,02:50,30/06/2024,30/06/2024,29/06/2024 01:50,30/06/2024 02:50
Eric Prydz,Saturday,Arcadia,41,25,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Surya Sen,Saturday,Arrivals,0,0,02:00 - 02:30,02:00,02:30,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 02:30
Fat Dog,Saturday,Bimble Inn,41,16,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Frenetic Hosted By Y Dott,Saturday,Blind Tiger,0,0,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Yushh [Sleep Felt Far Away Takeover],Saturday,Firmly Rooted,43,43,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Dj Stingray 313,Saturday,Iicon,66,21,02:00 - 04:00,02:00,04:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 04:00
Charlie Tee B2B Sota,Saturday,Lonely Hearts Club,44,41,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Dj Couscous,Saturday,Lunched Out Lizards,0,0,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Mr West (Westival),Saturday,The Hive,0,0,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
The Trojans,Saturday,The Rocket Lounge,64,16,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Bianca Oblivion,Saturday,The Rum Shack,0,0,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Hixxy,Saturday,The Salon Carousel,0,0,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Dj Flight,Saturday,The Sistxrhood,0,0,02:00 - 04:00,02:00,04:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 04:00
Dillinja,Saturday,The Temple,0,0,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Mihail,Saturday,Toad Hall,0,0,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
The Quadalakalaka Club,Saturday,Tree Stage,44,51,02:00 - 02:50,02:00,02:50,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 02:50
Steamy Bumplings B2B Vsvn,Saturday,West Holts Bar,59,29,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Isaac Ferry (Dj Set),Saturday,Wishing Well,42,20,02:00 - 03:00,02:00,03:00,30/06/2024,30/06/2024,29/06/2024 02:00,30/06/2024 03:00
Dj Cue,Saturday,Peace Stage,0,0,02:15 - 02:45,02:15,02:45,30/06/2024,30/06/2024,29/06/2024 02:15,30/06/2024 02:45
Dialled In Soundsystem,Saturday,Arrivals,0,0,02:30 - 03:00,02:30,03:00,30/06/2024,30/06/2024,29/06/2024 02:30,30/06/2024 03:00
Madison Moore,Saturday,Genosys,0,0,02:30 - 04:30,02:30,04:30,30/06/2024,30/06/2024,29/06/2024 02:30,30/06/2024 04:30
Gideön,Saturday,Nyc Downlow,0,0,02:30 - 04:25,02:30,04:25,30/06/2024,30/06/2024,29/06/2024 02:30,30/06/2024 04:25
Chimpo,Saturday,Platform 23,0,0,02:30 - 03:15,02:30,03:15,30/06/2024,30/06/2024,29/06/2024 02:30,30/06/2024 03:15
Queer House Party,Saturday,Scissors,42,21,02:30 - 03:30,02:30,03:30,30/06/2024,30/06/2024,29/06/2024 02:30,30/06/2024 03:30
Idris Elba,Saturday,Stonebridge Bar,42,18,02:30 - 03:30,02:30,03:30,30/06/2024,30/06/2024,29/06/2024 02:30,30/06/2024 03:30
Casisdead,Saturday,Peace Stage,0,0,02:45 - 03:30,02:45,03:30,30/06/2024,30/06/2024,29/06/2024 02:45,30/06/2024 03:30
Nadī B2B Shivum,Saturday,Arrivals,0,0,03:00 - 04:00,03:00,04:00,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 04:00
"10 Years Of Vibena Jungle: Uncle Dugs, Leeroy Thornhill (Jungle Set) Daddy Nature, Mc Boxer Banton",Saturday,Blind Tiger,0,0,03:00 - 05:00,03:00,05:00,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 05:00
"Nicky,Nicky",Saturday,Deluxe Diner,64,17,03:00 - 04:30,03:00,04:30,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 04:30
Ru Robinson,Saturday,Mez Yard,0,0,03:00 - 04:00,03:00,04:00,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 04:00
London Trans+ Pride X The Chateau: Planningtorock,Saturday,Nomad,0,0,03:00 - 04:30,03:00,04:30,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 04:30
Booty Bass,Saturday,Nowhere,0,0,03:00 - 04:30,03:00,04:30,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 04:30
Peach,Saturday,The Meatrack,0,0,03:00 - 04:30,03:00,04:30,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 04:30
Chimpo,Saturday,The Rum Shack,0,0,03:00 - 04:00,03:00,04:00,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 04:00
Mollie Rush,Saturday,The Salon Carousel,0,0,03:00 - 04:00,03:00,04:00,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 04:00
Simula,Saturday,The Temple,0,0,03:00 - 04:00,03:00,04:00,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 04:00
Thee Ones,Saturday,Wishing Well,42,20,03:00 - 04:00,03:00,04:00,30/06/2024,30/06/2024,29/06/2024 03:00,30/06/2024 04:00
Samurai Breaks,Saturday,Platform 23,0,0,03:15 - 04:00,03:15,04:00,30/06/2024,30/06/2024,29/06/2024 03:15,30/06/2024 04:00
Jimbitch,Saturday,Bimble Inn,41,16,03:30 - 05:00,03:30,05:00,30/06/2024,30/06/2024,29/06/2024 03:30,30/06/2024 05:00
Lou Hayter,Saturday,Scissors,42,21,03:30 - 04:30,03:30,04:30,30/06/2024,30/06/2024,29/06/2024 03:30,30/06/2024 04:30
Rudimental B2B Todd Edwards,Saturday,Stonebridge Bar,42,18,03:30 - 05:00,03:30,05:00,30/06/2024,30/06/2024,29/06/2024 03:30,30/06/2024 05:00
The Downsetters,Saturday,The Rocket Lounge,64,16,03:45 - 05:00,03:45,05:00,30/06/2024,30/06/2024,29/06/2024 03:45,30/06/2024 05:00
Angel D’Lite,Saturday,Arrivals,0,0,04:00 - 05:00,04:00,05:00,30/06/2024,30/06/2024,29/06/2024 04:00,30/06/2024 05:00
Deena Abdelwahed,Saturday,Iicon,66,21,04:00 - 06:00,04:00,06:00,30/06/2024,30/06/2024,29/06/2024 04:00,30/06/2024 06:00
Chicha Morada,Saturday,Mez Yard,0,0,04:00 - 06:00,04:00,06:00,30/06/2024,30/06/2024,29/06/2024 04:00,30/06/2024 06:00
A Guy Called Gerald,Saturday,Platform 23,0,0,04:00 - 05:00,04:00,05:00,30/06/2024,30/06/2024,29/06/2024 04:00,30/06/2024 05:00
Saint Ludo,Saturday,The Rum Shack,0,0,04:00 - 05:00,04:00,05:00,30/06/2024,30/06/2024,29/06/2024 04:00,30/06/2024 05:00
Matt Scratch,Saturday,The Salon Carousel,0,0,04:00 - 05:00,04:00,05:00,30/06/2024,30/06/2024,29/06/2024 04:00,30/06/2024 05:00
Mantra,Saturday,The Sistxrhood,0,0,04:00 - 06:00,04:00,06:00,30/06/2024,30/06/2024,29/06/2024 04:00,30/06/2024 06:00
S.P.Y Ft. Lowqui,Saturday,The Temple,0,0,04:00 - 05:00,04:00,05:00,30/06/2024,30/06/2024,29/06/2024 04:00,30/06/2024 05:00
Discolypso Crew (Dj Set),Saturday,Wishing Well,42,20,04:00 - 06:00,04:00,06:00,30/06/2024,30/06/2024,29/06/2024 04:00,30/06/2024 06:00
"Louie,Louie",Saturday,Deluxe Diner,64,17,04:30 - 06:00,04:30,06:00,30/06/2024,30/06/2024,29/06/2024 04:30,30/06/2024 06:00
Partok,Saturday,Genosys,0,0,04:30 - 06:00,04:30,06:00,30/06/2024,30/06/2024,29/06/2024 04:30,30/06/2024 06:00
London Trans+ Pride X The Chateau: Faff,Saturday,Nomad,0,0,04:30 - 06:00,04:30,06:00,30/06/2024,30/06/2024,29/06/2024 04:30,30/06/2024 06:00
Lady Shaka,Saturday,Nowhere,0,0,04:30 - 06:00,04:30,06:00,30/06/2024,30/06/2024,29/06/2024 04:30,30/06/2024 06:00
Kings Of Tomorrow,Saturday,Nyc Downlow,0,0,04:30 - 06:00,04:30,06:00,30/06/2024,30/06/2024,29/06/2024 04:30,30/06/2024 06:00
Will 'Shakedown' Read,Saturday,Scissors,42,21,04:30 - 06:00,04:30,06:00,30/06/2024,30/06/2024,29/06/2024 04:30,30/06/2024 06:00
Ninebob And Sugarbear,Saturday,The Meatrack,0,0,04:30 - 06:00,04:30,06:00,30/06/2024,30/06/2024,29/06/2024 04:30,30/06/2024 06:00
Dj Chris Tofu & Debbralee Wells,Saturday,Peace Stage,0,0,04:45 - 05:15,04:45,05:15,30/06/2024,30/06/2024,29/06/2024 04:45,30/06/2024 05:15
Nikki Nair,Saturday,Arrivals,0,0,05:00 - 06:00,05:00,06:00,30/06/2024,30/06/2024,29/06/2024 05:00,30/06/2024 06:00
Benny L,Saturday,Blind Tiger,0,0,05:00 - 06:00,05:00,06:00,30/06/2024,30/06/2024,29/06/2024 05:00,30/06/2024 06:00
Bianca Oblivion,Saturday,Platform 23,0,0,05:00 - 06:00,05:00,06:00,30/06/2024,30/06/2024,29/06/2024 05:00,30/06/2024 06:00
Us,Saturday,The Rocket Lounge,64,16,05:00 - 06:00,05:00,06:00,30/06/2024,30/06/2024,29/06/2024 05:00,30/06/2024 06:00
Fizzy Gillespie,Saturday,The Rum Shack,0,0,05:00 - 06:00,05:00,06:00,30/06/2024,30/06/2024,29/06/2024 05:00,30/06/2024 06:00
Ecoli,Saturday,The Salon Carousel,0,0,05:00 - 06:00,05:00,06:00,30/06/2024,30/06/2024,29/06/2024 05:00,30/06/2024 06:00
4Am Kru,Saturday,The Temple,0,0,05:00 - 06:00,05:00,06:00,30/06/2024,30/06/2024,29/06/2024 05:00,30/06/2024 06:00
Fülü Electobrass,Saturday,Peace Stage,0,0,05:15 - 06:00,05:15,06:00,30/06/2024,30/06/2024,29/06/2024 05:15,30/06/2024 06:00
Yoga Like Water With Dan Peppiatt,Saturday,Humblewell Active Platform,42,21,08:30 - 09:30,08:30,09:30,29/06/2024,29/06/2024,29/06/2024 08:30,29/06/2024 09:30
Shakti Shake With Dina Cohen,Saturday,Humblewell Retreat Yurt,42,21,08:45 - 09:45,08:45,09:45,29/06/2024,29/06/2024,29/06/2024 08:45,29/06/2024 09:45
Music With Mike - The Big Gig,Saturday,Kidzfield Big Top,0,0,09:30 - 10:05,09:30,10:05,29/06/2024,29/06/2024,29/06/2024 09:30,29/06/2024 10:05
Singing Circle With Leti,Saturday,Humblewell Active Platform,42,21,09:45 - 10:45,09:45,10:45,29/06/2024,29/06/2024,29/06/2024 09:45,29/06/2024 10:45
Crystal Singing Bowls With Yogic Sound,Saturday,Humblewell Retreat Yurt,42,21,09:45 - 10:15,09:45,10:15,29/06/2024,29/06/2024,29/06/2024 09:45,29/06/2024 10:15
Nipsy,Saturday,Cornish Arms,0,0,10:00 - 12:00,10:00,12:00,29/06/2024,29/06/2024,29/06/2024 10:00,29/06/2024 12:00
Power Ballad Yoga,Saturday,Greenpeace,55,26,10:00 - 11:00,10:00,11:00,29/06/2024,29/06/2024,29/06/2024 10:00,29/06/2024 11:00
Prah Recordings,Saturday,San Remo,45,47,10:00 - 11:30,10:00,11:30,29/06/2024,29/06/2024,29/06/2024 10:00,29/06/2024 11:30
Badvertising- How To Stop Adverts Fuelling Climate Chaos - Andrew Simms,Saturday,Speakers Forum,0,0,10:00 - 11:00,10:00,11:00,29/06/2024,29/06/2024,29/06/2024 10:00,29/06/2024 11:00
Bell And Bullock,Saturday,Walkabouts,60,33,10:20 - 10:50,10:20,10:50,29/06/2024,29/06/2024,29/06/2024 10:20,29/06/2024 10:50
Dodgy Boys,Saturday,Walkabouts,60,33,10:20 - 11:05,10:20,11:05,29/06/2024,29/06/2024,29/06/2024 10:20,29/06/2024 11:05
Bodger'S Badger,Saturday,Kidzfield Big Top,0,0,10:25 - 10:45,10:25,10:45,29/06/2024,29/06/2024,29/06/2024 10:25,29/06/2024 10:45
Tented Talk,Saturday,Circus Big Top,57,34,10:30 - 11:10,10:30,11:10,29/06/2024,29/06/2024,29/06/2024 10:30,29/06/2024 11:10
Compere: Chris Barltrop,Saturday,Circus Big Top,57,34,10:30 - 12:30,10:30,12:30,29/06/2024,29/06/2024,29/06/2024 10:30,29/06/2024 12:30
Know Your Rights,Saturday,Greenpeace (Beam),54,26,10:30 - 11:15,10:30,11:15,29/06/2024,29/06/2024,29/06/2024 10:30,29/06/2024 11:15
Shamanic Drum Circle With Tracy Turnell,Saturday,Humblewell Retreat Yurt,42,21,10:30 - 11:30,10:30,11:30,29/06/2024,29/06/2024,29/06/2024 10:30,29/06/2024 11:30
Sounds Of Science Dj Set,Saturday,Laboratory Stage,0,0,10:30 - 11:00,10:30,11:00,29/06/2024,29/06/2024,29/06/2024 10:30,29/06/2024 11:00
Tba,Saturday,Mandala Stage,0,0,10:30 - 11:30,10:30,11:30,29/06/2024,29/06/2024,29/06/2024 10:30,29/06/2024 11:30
The Crate Stack Challenge,Saturday,Outside Circus Stage,59,33,10:30 - 11:30,10:30,11:30,29/06/2024,29/06/2024,29/06/2024 10:30,29/06/2024 11:30
Fire Fighters!,Saturday,Walkabouts,60,33,10:30 - 11:00,10:30,11:00,29/06/2024,29/06/2024,29/06/2024 10:30,29/06/2024 11:00
Jersey Girls,Saturday,Walkabouts,60,33,10:30 - 11:00,10:30,11:00,29/06/2024,29/06/2024,29/06/2024 10:30,29/06/2024 11:00
Flamingos,Saturday,Walkabouts,60,33,10:30 - 11:15,10:30,11:15,29/06/2024,29/06/2024,29/06/2024 10:30,29/06/2024 11:15
Clamour Of Bells,Saturday,Walkabouts,60,33,10:35 - 11:20,10:35,11:20,29/06/2024,29/06/2024,29/06/2024 10:35,29/06/2024 11:20
The Newspaper Men,Saturday,Walkabouts,60,33,10:35 - 11:20,10:35,11:20,29/06/2024,29/06/2024,29/06/2024 10:35,29/06/2024 11:20
Rishi Gordon,Saturday,Walkabouts,60,33,10:45 - 11:30,10:45,11:30,29/06/2024,29/06/2024,29/06/2024 10:45,29/06/2024 11:30
The Fabularium - Carnival Of Animals,Saturday,Walkabouts,60,33,10:45 - 11:30,10:45,11:30,29/06/2024,29/06/2024,29/06/2024 10:45,29/06/2024 11:30
The Smallest Race On Earth,Saturday,Walkabouts,60,33,10:50 - 11:20,10:50,11:20,29/06/2024,29/06/2024,29/06/2024 10:50,29/06/2024 11:20
Ukelele Thrash Mob,Saturday,Walkabouts,60,33,10:50 - 11:35,10:50,11:35,29/06/2024,29/06/2024,29/06/2024 10:50,29/06/2024 11:35
Compère: Dan Evans,Saturday,The Astrolabe Theatre,0,0,10:55 - 15:30,10:55,15:30,29/06/2024,29/06/2024,29/06/2024 10:55,29/06/2024 15:30
The Crows,Saturday,Walkabouts,60,33,10:55 - 11:25,10:55,11:25,29/06/2024,29/06/2024,29/06/2024 10:55,29/06/2024 11:25
The Midwives,Saturday,Walkabouts,60,33,10:55 - 11:40,10:55,11:40,29/06/2024,29/06/2024,29/06/2024 10:55,29/06/2024 11:40
Films,Saturday,Atchin Tan,0,0,11:00 - 12:30,11:00,12:30,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 12:30
Jo Bucket,Saturday,Carhenge,58,36,11:00 - 12:00,11:00,12:00,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 12:00
Acoustic Open Mic,Saturday,Croissant Neuf Bandstand,55,21,11:00 - 11:30,11:00,11:30,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 11:30
Robin Ince,Saturday,Free University Of Glastonbury,42,21,11:00 - 12:00,11:00,12:00,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 12:00
Skate Ramp Pro Session,Saturday,Greenpeace,55,26,11:00 - 12:00,11:00,12:00,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 12:00
Om And Bass Yoga With Dina Cohen,Saturday,Humblewell Active Platform,42,21,11:00 - 11:50,11:00,11:50,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 11:50
Roger Mcgough'S Poetry,Saturday,Kidzfield Big Top,0,0,11:00 - 11:30,11:00,11:30,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 11:30
Despicable Me 4,Saturday,Pilton Palais Cinema,64,36,11:00 - 12:25,11:00,12:25,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 12:25
Andy Burnham With John Harris,Saturday,Speakers Forum,0,0,11:00 - 12:00,11:00,12:00,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 12:00
Ged Lever,Saturday,Strummerville,48,12,11:00 - 12:00,11:00,12:00,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 12:00
St Paul'S Carnival: Windrush Library Talks - Fusion & Activism,Saturday,Terminal 1,0,0,11:00 - 12:30,11:00,12:30,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 12:30
The Guardian Q & A,Saturday,The Astrolabe Theatre,0,0,11:00 - 11:50,11:00,11:50,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 11:50
Dirk Landish,Saturday,The Hive,0,0,11:00 - 11:30,11:00,11:30,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 11:30
Sandy Yidaki Workshop,Saturday,Toad Hall,0,0,11:00 - 11:45,11:00,11:45,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 11:45
Jasmin Harsono - Immersive Ambient Live Sounds And Visuals,Saturday,Tree Stage,44,51,11:00 - 11:30,11:00,11:30,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 11:30
Roo'D,Saturday,Walkabouts,60,33,11:00 - 11:30,11:00,11:30,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 11:30
The Family Tree,Saturday,Walkabouts,60,33,11:00 - 11:45,11:00,11:45,29/06/2024,29/06/2024,29/06/2024 11:00,29/06/2024 11:45
Giant Seagulls,Saturday,Walkabouts,60,33,11:05 - 11:05,11:05,11:05,29/06/2024,29/06/2024,29/06/2024 11:05,29/06/2024 11:05
The Tea Ladies On Tour,Saturday,Walkabouts,60,33,11:05 - 11:50,11:05,11:50,29/06/2024,29/06/2024,29/06/2024 11:05,29/06/2024 11:50
Johnny Flynn,Saturday,The Park Stage,41,19,11:10 - 12:10,11:10,12:10,29/06/2024,29/06/2024,29/06/2024 11:10,29/06/2024 12:10
Anyone For Tennis,Saturday,Walkabouts,60,33,11:10 - 11:55,11:10,11:55,29/06/2024,29/06/2024,29/06/2024 11:10,29/06/2024 11:55
Tented Talk - The Space Cowboy,Saturday,Circus Big Top,57,34,11:15 - 12:00,11:15,12:00,29/06/2024,29/06/2024,29/06/2024 11:15,29/06/2024 12:00
Reducing Barriers To Activism,Saturday,Greenpeace (Beam),54,26,11:15 - 12:00,11:15,12:00,29/06/2024,29/06/2024,29/06/2024 11:15,29/06/2024 12:00
Science-Based Meditation,Saturday,Laboratory Stage,0,0,11:15 - 11:45,11:15,11:45,29/06/2024,29/06/2024,29/06/2024 11:15,29/06/2024 11:45
The Bad Eggs,Saturday,Walkabouts,60,33,11:15 - 12:00,11:15,12:00,29/06/2024,29/06/2024,29/06/2024 11:15,29/06/2024 12:00
The Buzzing Bees,Saturday,Walkabouts,60,33,11:15 - 12:15,11:15,12:15,29/06/2024,29/06/2024,29/06/2024 11:15,29/06/2024 12:15
Jada Star,Saturday,Acoustic Stage,66,38,11:30 - 12:00,11:30,12:00,29/06/2024,29/06/2024,29/06/2024 11:30,29/06/2024 12:00
Old Time Sailors,Saturday,Avalon Stage,66,38,11:30 - 12:20,11:30,12:20,29/06/2024,29/06/2024,29/06/2024 11:30,29/06/2024 12:20
Mighty Mighty J,Saturday,Babylon Uprising,0,0,11:30 - 12:00,11:30,12:00,29/06/2024,29/06/2024,29/06/2024 11:30,29/06/2024 12:00
Compères: Tamara And Dave,Saturday,Outside Circus Stage,59,33,11:30 - 16:00,11:30,16:00,29/06/2024,29/06/2024,29/06/2024 11:30,29/06/2024 16:00
Gecko,Saturday,Poetry&Words,0,0,11:30 - 12:00,11:30,12:00,29/06/2024,29/06/2024,29/06/2024 11:30,29/06/2024 12:00
Amateurism,Saturday,San Remo,45,47,11:30 - 13:00,11:30,13:00,29/06/2024,29/06/2024,29/06/2024 11:30,29/06/2024 13:00
Natural Diversions,Saturday,Walkabouts,60,33,11:30 - 12:15,11:30,12:15,29/06/2024,29/06/2024,29/06/2024 11:30,29/06/2024 12:15
47Soul,Saturday,West Holts Stage,57,31,11:30 - 12:30,11:30,12:30,29/06/2024,29/06/2024,29/06/2024 11:30,29/06/2024 12:30
Kneecap,Saturday,Woodsies,43,52,11:30 - 12:15,11:30,12:15,29/06/2024,29/06/2024,29/06/2024 11:30,29/06/2024 12:15
Circus Raj And Rajasthan Heritage Brass Band,Saturday,Outside Circus Stage,59,33,11:40 - 12:10,11:40,12:10,29/06/2024,29/06/2024,29/06/2024 11:40,29/06/2024 12:10
Bethany Humphries,Saturday,The Hive,0,0,11:40 - 12:20,11:40,12:20,29/06/2024,29/06/2024,29/06/2024 11:40,29/06/2024 12:20
Fairly Fresh Fish Co,Saturday,Walkabouts,60,33,11:40 - 12:25,11:40,12:25,29/06/2024,29/06/2024,29/06/2024 11:40,29/06/2024 12:25
Rhubarb Theatre Presents: Collection Day,Saturday,Kidzfield Big Top,0,0,11:45 - 12:20,11:45,12:20,29/06/2024,29/06/2024,29/06/2024 11:45,29/06/2024 12:20
Jamie Webster,Saturday,Other Stage,47,34,11:45 - 12:30,11:45,12:30,29/06/2024,29/06/2024,29/06/2024 11:45,29/06/2024 12:30
David Celia,Saturday,The Bandstand,56,38,11:45 - 12:15,11:45,12:15,29/06/2024,29/06/2024,29/06/2024 11:45,29/06/2024 12:15
Swyron & Desaata,Saturday,Walkabouts,60,33,11:45 - 12:30,11:45,12:30,29/06/2024,29/06/2024,29/06/2024 11:45,29/06/2024 12:30
Trifleenees,Saturday,Walkabouts,60,33,11:50 - 12:35,11:50,12:35,29/06/2024,29/06/2024,29/06/2024 11:50,29/06/2024 12:35
Masters Of The Kazooniverse,Saturday,Walkabouts,60,33,11:50 - 13:20,11:50,13:20,29/06/2024,29/06/2024,29/06/2024 11:50,29/06/2024 13:20
The Doogans,Saturday,A Little More Sensation,0,0,12:00 - 12:30,12:00,12:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:30
Faff [Bodymovements Takeover],Saturday,Assembly,40,42,12:00 - 14:00,12:00,14:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 14:00
Reason Sound B2B Miss Chilly,Saturday,Babylon Uprising,0,0,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
Beatles Dub Club,Saturday,Bimble Inn,41,16,12:00 - 14:00,12:00,14:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 14:00
Blind Tiger Residents,Saturday,Blind Tiger,0,0,12:00 - 12:30,12:00,12:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:30
Cara Hammond,Saturday,Bread And Roses,0,0,12:00 - 12:40,12:00,12:40,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:40
Compère: Sikisa,Saturday,Cabaret,62,26,12:00 - 16:00,12:00,16:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 16:00
Curt & Andy,Saturday,Cornish Arms,0,0,12:00 - 14:00,12:00,14:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 14:00
Kat Pither + Jessie Marcella,Saturday,Croissant Neuf,55,21,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
Paul Lambourne,Saturday,Crooner'S Corner,0,0,12:00 - 12:30,12:00,12:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:30
Qualitex Roots Vibration [Teachings In Dub Takeover],Saturday,Firmly Rooted,43,43,12:00 - 13:30,12:00,13:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:30
Nihal Arthanayake,Saturday,Free University Of Glastonbury,42,21,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
Guy.In.Glasses,Saturday,Glade,51,29,12:00 - 12:30,12:00,12:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:30
Carly Wilford,Saturday,Glade Dome,49,29,12:00 - 13:30,12:00,13:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:30
Miss (Burning) World With Sophie Duker And Joe Sutherland,Saturday,Greenpeace,55,26,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
Easy Tai Chi With Joe May,Saturday,Humblewell Active Platform,42,21,12:00 - 12:45,12:00,12:45,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:45
Life Drawing With Fra Beecher,Saturday,Humblewell Retreat Yurt,42,21,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
Wildlife Kate - Your Wild Neighbours,Saturday,Laboratory Stage,0,0,12:00 - 12:30,12:00,12:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:30
"Debates: Post Office Scandal: Reimagining Justice With Christopher Head Former Postmaster, Kate Osborne Mp, Kojo Koram, Why Me? Minnie Rahman",Saturday,Left Field,52,33,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
Arlo B2B Lulah Francs,Saturday,Levels,42,44,12:00 - 13:30,12:00,13:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:30
Tba,Saturday,Mandala Stage,0,0,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
Compere: Rosy Carrick,Saturday,Poetry&Words,0,0,12:00 - 15:30,12:00,15:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 15:30
Femi Kuti,Saturday,Pyramid Stage,51,43,12:00 - 12:45,12:00,12:45,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:45
Dick Pulses Morning Rise,Saturday,Sensation Seekers Stage,0,0,12:00 - 12:25,12:00,12:25,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:25
Compères: George Orange / Grainne,Saturday,Sensation Seekers Stage,0,0,12:00 - 18:45,12:00,18:45,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 18:45
The Gaza War: Media Reporting And Activism - Mike Berry,Saturday,Speakers Forum,0,0,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
Daphni,Saturday,Stonebridge Bar,42,18,12:00 - 14:00,12:00,14:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 14:00
Anna Campeau Dj,Saturday,Strummerville,48,12,12:00 - 14:00,12:00,14:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 14:00
Siegfried & Joy,Saturday,The Astrolabe Theatre,0,0,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
Land Of The Giants,Saturday,The Gateway,0,0,12:00 - 12:30,12:00,12:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:30
Kane & Abel,Saturday,The Glebe,60,33,12:00 - 12:30,12:00,12:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:30
"Big Team Cic: ‘Youth Exploitation - Road To Reform’: Faron Paul (Faz Amnesty), Leigh Mckenna, Ngozi Fulani (Ceo & Co-Founder - Sistah Space), Tba Hosted By: Tba",Saturday,The Information,41,41,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
Harvey Juggling,Saturday,The Pavement,0,0,12:00 - 12:30,12:00,12:30,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:30
Rosa Hoop'S Rotation Motivation,Saturday,Toad Hall,0,0,12:00 - 13:00,12:00,13:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 13:00
The Very Best Of Tommy Cooper,Saturday,Walkabouts,60,33,12:00 - 12:45,12:00,12:45,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 12:45
Worldroots Acapella,Saturday,Walkabouts,60,33,12:00 - 14:00,12:00,14:00,29/06/2024,29/06/2024,29/06/2024 12:00,29/06/2024 14:00
Naomi Wood 'Gobbess',Saturday,Poetry&Words,0,0,12:03 - 12:53,12:03,12:53,29/06/2024,29/06/2024,29/06/2024 12:03,29/06/2024 12:53
The Young Ones Panel Show,Saturday,Cabaret,62,26,12:05 - 13:00,12:05,13:00,29/06/2024,29/06/2024,29/06/2024 12:05,29/06/2024 13:00
Wookey Hole Circus,Saturday,Circus Big Top,57,34,12:05 - 12:30,12:05,12:30,29/06/2024,29/06/2024,29/06/2024 12:05,29/06/2024 12:30
Flamingos,Saturday,Walkabouts,60,33,12:05 - 12:50,12:05,12:50,29/06/2024,29/06/2024,29/06/2024 12:05,29/06/2024 12:50
Ryan Mcmullan,Saturday,Acoustic Stage,66,38,12:10 - 12:40,12:10,12:40,29/06/2024,29/06/2024,29/06/2024 12:10,29/06/2024 12:40
The Magnifient Kevens,Saturday,Walkabouts,60,33,12:10 - 12:55,12:10,12:55,29/06/2024,29/06/2024,29/06/2024 12:10,29/06/2024 12:55
Football Crazy,Saturday,Walkabouts,60,33,12:10 - 13:10,12:10,13:10,29/06/2024,29/06/2024,29/06/2024 12:10,29/06/2024 13:10
Compere: Annabelle Holland,Saturday,Circus Big Top,57,34,12:15 - 16:45,12:15,16:45,29/06/2024,29/06/2024,29/06/2024 12:15,29/06/2024 16:45
Rob Roy Collins,Saturday,Outside Circus Stage,59,33,12:15 - 12:45,12:15,12:45,29/06/2024,29/06/2024,29/06/2024 12:15,29/06/2024 12:45
Disco Robot Girlz,Saturday,Walkabouts,60,33,12:15 - 13:00,12:15,13:00,29/06/2024,29/06/2024,29/06/2024 12:15,29/06/2024 13:00
The Natural Theatre Company,Saturday,Walkabouts,60,33,12:15 - 13:00,12:15,13:00,29/06/2024,29/06/2024,29/06/2024 12:15,29/06/2024 13:00
Blockbuster Factory,Saturday,Walkabouts,60,33,12:15 - 13:10,12:15,13:10,29/06/2024,29/06/2024,29/06/2024 12:15,29/06/2024 13:10
"Damian Le Bas, Liza Mortimer, Talk: The Making Of The Realities Checked Film Series, Changing The Conversation Around Travellers And Crime",Saturday,Atchin Tan,0,0,12:30 - 13:15,12:30,13:15,29/06/2024,29/06/2024,29/06/2024 12:30,29/06/2024 13:15
Mary In The Junkyard,Saturday,Bbc Music Introducing,45,44,12:30 - 13:00,12:30,13:00,29/06/2024,29/06/2024,29/06/2024 12:30,29/06/2024 13:00
Blind Tiger Residents,Saturday,Blind Tiger,0,0,12:30 - 13:00,12:30,13:00,29/06/2024,29/06/2024,29/06/2024 12:30,29/06/2024 13:00
N'Famady Kouyaté,Saturday,Glade,51,29,12:30 - 13:30,12:30,13:30,29/06/2024,29/06/2024,29/06/2024 12:30,29/06/2024 13:30
Carnival,Saturday,Glasto Latino,58,27,12:30 - 13:00,12:30,13:00,29/06/2024,29/06/2024,29/06/2024 12:30,29/06/2024 13:00
Caleb Kunle,Saturday,Lonely Hearts Club,44,41,12:30 - 13:15,12:30,13:15,29/06/2024,29/06/2024,29/06/2024 12:30,29/06/2024 13:15
Freddieno,Saturday,Sensation Seekers Stage,0,0,12:30 - 13:00,12:30,13:00,29/06/2024,29/06/2024,29/06/2024 12:30,29/06/2024 13:00
Dusty Stray,Saturday,The Bandstand,56,38,12:30 - 13:00,12:30,13:00,29/06/2024,29/06/2024,29/06/2024 12:30,29/06/2024 13:00
Dan Ottewell,Saturday,The Hive,0,0,12:30 - 13:00,12:30,13:00,29/06/2024,29/06/2024,29/06/2024 12:30,29/06/2024 13:00
The Fabularium - Carnival Of Animals,Saturday,Walkabouts,60,33,12:30 - 13:15,12:30,13:15,29/06/2024,29/06/2024,29/06/2024 12:30,29/06/2024 13:15
Ballerinas,Saturday,A Little More Sensation,0,0,12:35 - 13:05,12:35,13:05,29/06/2024,29/06/2024,29/06/2024 12:35,29/06/2024 13:05
Head Over Wheels,Saturday,Circus Big Top,57,34,12:35 - 12:43,12:35,12:43,29/06/2024,29/06/2024,29/06/2024 12:35,29/06/2024 12:43
The Basil Brush Show,Saturday,Kidzfield Big Top,0,0,12:35 - 13:05,12:35,13:05,29/06/2024,29/06/2024,29/06/2024 12:35,29/06/2024 13:05
Faces Of Disco,Saturday,The Glebe,60,33,12:35 - 13:05,12:35,13:05,29/06/2024,29/06/2024,29/06/2024 12:35,29/06/2024 13:05
Hilby,Saturday,The Pavement,0,0,12:35 - 13:05,12:35,13:05,29/06/2024,29/06/2024,29/06/2024 12:35,29/06/2024 13:05
The Newspaper Men,Saturday,Walkabouts,60,33,12:35 - 13:20,12:35,13:20,29/06/2024,29/06/2024,29/06/2024 12:35,29/06/2024 13:20
Lost And Sound (Film Screening) / Q&A With Producer Kat Mansoor,Saturday,Laboratory Stage,0,0,12:45 - 14:00,12:45,14:00,29/06/2024,29/06/2024,29/06/2024 12:45,29/06/2024 14:00
The Old Time Rags,Saturday,The Gateway,0,0,12:45 - 13:15,12:45,13:15,29/06/2024,29/06/2024,29/06/2024 12:45,29/06/2024 13:15
Kara Jackson,Saturday,The Park Stage,41,19,12:45 - 13:30,12:45,13:30,29/06/2024,29/06/2024,29/06/2024 12:45,29/06/2024 13:30
The Bigheads,Saturday,Walkabouts,60,33,12:45 - 13:25,12:45,13:25,29/06/2024,29/06/2024,29/06/2024 12:45,29/06/2024 13:25
High Vis,Saturday,Woodsies,43,52,12:45 - 13:30,12:45,13:30,29/06/2024,29/06/2024,29/06/2024 12:45,29/06/2024 13:30
Toby Walker,Saturday,Circus Big Top,57,34,12:48 - 12:56,12:48,12:56,29/06/2024,29/06/2024,29/06/2024 12:48,29/06/2024 12:56
Elles Bailey,Saturday,Avalon Stage,66,38,12:50 - 13:45,12:50,13:45,29/06/2024,29/06/2024,29/06/2024 12:50,29/06/2024 13:45
Gracie Barry Tait,Saturday,Crooner'S Corner,0,0,12:50 - 13:35,12:50,13:35,29/06/2024,29/06/2024,29/06/2024 12:50,29/06/2024 13:35
Tba,Saturday,Outside Circus Stage,59,33,12:50 - 13:20,12:50,13:20,29/06/2024,29/06/2024,29/06/2024 12:50,29/06/2024 13:20
Riff Raff Kaberett,Saturday,10 Aces,0,0,13:00 - 13:30,13:00,13:30,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:30
Jessie Reid,Saturday,Acoustic Stage,66,38,13:00 - 13:40,13:00,13:40,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:40
Nj Carter,Saturday,Babylon Uprising,0,0,13:00 - 14:00,13:00,14:00,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 14:00
Charlie Rose,Saturday,Blind Tiger,0,0,13:00 - 14:00,13:00,14:00,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 14:00
Gusto Gusto,Saturday,Bread And Roses,0,0,13:00 - 13:40,13:00,13:40,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:40
Fulu Miziki,Saturday,Carhenge,58,36,13:00 - 14:00,13:00,14:00,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 14:00
Josh Roberts,Saturday,Croissant Neuf Bandstand,55,21,13:00 - 13:30,13:00,13:30,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:30
Luke Una,Saturday,Free University Of Glastonbury,42,21,13:00 - 14:00,13:00,14:00,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 14:00
Dance Class: Salsa,Saturday,Glasto Latino,58,27,13:00 - 14:00,13:00,14:00,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 14:00
Action Skills Workshops,Saturday,Greenpeace (Beam),54,26,13:00 - 15:00,13:00,15:00,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 15:00
African Dance With Penny Avery,Saturday,Humblewell Active Platform,42,21,13:00 - 13:30,13:00,13:30,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:30
The Staves,Saturday,Other Stage,47,34,13:00 - 13:45,13:00,13:45,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:45
Shaun Of The Dead 20Th Anniversary + Intro With Simon Pegg & Edgar Wright 15,Saturday,Pilton Palais Cinema,64,36,13:00 - 15:00,13:00,15:00,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 15:00
Sophie Mcalister,Saturday,San Remo,45,47,13:00 - 14:30,13:00,14:30,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 14:30
Community Activism - Frances Foley & Clive Lewis Mp,Saturday,Speakers Forum,0,0,13:00 - 14:00,13:00,14:00,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 14:00
Gecko,Saturday,The Astrolabe Theatre,0,0,13:00 - 13:10,13:00,13:10,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:10
Jersey Girls,Saturday,Walkabouts,60,33,13:00 - 13:30,13:00,13:30,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:30
Mafia Wedding,Saturday,Walkabouts,60,33,13:00 - 13:45,13:00,13:45,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:45
Steve Faulkner,Saturday,Walkabouts,60,33,13:00 - 13:45,13:00,13:45,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:45
The Skatalites,Saturday,West Holts Stage,57,31,13:00 - 14:00,13:00,14:00,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 14:00
Arrivals Takeover: Shivum Sharma,Saturday,Wishing Well,42,20,13:00 - 13:30,13:00,13:30,29/06/2024,29/06/2024,29/06/2024 13:00,29/06/2024 13:30
Cirk Hes Presents Sorrel,Saturday,Circus Big Top,57,34,13:01 - 13:07,13:01,13:07,29/06/2024,29/06/2024,29/06/2024 13:01,29/06/2024 13:07
Dj J9,Saturday,Cabaret,62,26,13:05 - 13:25,13:05,13:25,29/06/2024,29/06/2024,29/06/2024 13:05,29/06/2024 13:25
Open Mic Hosted By Aflo,Saturday,Poetry&Words,0,0,13:05 - 13:35,13:05,13:35,29/06/2024,29/06/2024,29/06/2024 13:05,29/06/2024 13:35
Akira,Saturday,A Little More Sensation,0,0,13:10 - 13:40,13:10,13:40,29/06/2024,29/06/2024,29/06/2024 13:10,29/06/2024 13:40
Ellis Grover,Saturday,Sensation Seekers Stage,0,0,13:10 - 13:20,13:10,13:20,29/06/2024,29/06/2024,29/06/2024 13:10,29/06/2024 13:20
Trash Test Dummies,Saturday,The Astrolabe Theatre,0,0,13:10 - 14:10,13:10,14:10,29/06/2024,29/06/2024,29/06/2024 13:10,29/06/2024 14:10
Mark Bruce Dance Company,Saturday,The Glebe,60,33,13:10 - 13:20,13:10,13:20,29/06/2024,29/06/2024,29/06/2024 13:10,29/06/2024 13:20
Georgie Boyd,Saturday,The Hive,0,0,13:10 - 13:40,13:10,13:40,29/06/2024,29/06/2024,29/06/2024 13:10,29/06/2024 13:40
Tony And Ray,Saturday,The Pavement,0,0,13:10 - 13:25,13:10,13:25,29/06/2024,29/06/2024,29/06/2024 13:10,29/06/2024 13:25
Liver Cottage,Saturday,Walkabouts,60,33,13:10 - 13:55,13:10,13:55,29/06/2024,29/06/2024,29/06/2024 13:10,29/06/2024 13:55
High Society,Saturday,Circus Big Top,57,34,13:12 - 13:57,13:12,13:57,29/06/2024,29/06/2024,29/06/2024 13:12,29/06/2024 13:57
Fftp: Music,Saturday,Atchin Tan,0,0,13:15 - 14:00,13:15,14:00,29/06/2024,29/06/2024,29/06/2024 13:15,29/06/2024 14:00
Laughter Yoga With Joe May,Saturday,Humblewell Retreat Yurt,42,21,13:15 - 14:15,13:15,14:15,29/06/2024,29/06/2024,29/06/2024 13:15,29/06/2024 14:15
Ayra Starr,Saturday,Pyramid Stage,51,43,13:15 - 14:00,13:15,14:00,29/06/2024,29/06/2024,29/06/2024 13:15,29/06/2024 14:00
Florence Knight,Saturday,The Bandstand,56,38,13:15 - 13:45,13:15,13:45,29/06/2024,29/06/2024,29/06/2024 13:15,29/06/2024 13:45
"Migrant Footprint: ‘Black British Mixtape’ - Reni Eddo-Lodge (Author, Journalist), Dj Milo (The Wild Bunch), Hosted By Tayo Popoola",Saturday,The Information,41,41,13:15 - 14:15,13:15,14:15,29/06/2024,29/06/2024,29/06/2024 13:15,29/06/2024 14:15
Julie Abbe,Saturday,Toad Hall,0,0,13:15 - 13:45,13:15,13:45,29/06/2024,29/06/2024,29/06/2024 13:15,29/06/2024 13:45
The Smallest Race On Earth,Saturday,Walkabouts,60,33,13:15 - 13:45,13:15,13:45,29/06/2024,29/06/2024,29/06/2024 13:15,29/06/2024 13:45
The Flying Seagull Project,Saturday,Kidzfield Big Top,0,0,13:20 - 14:00,13:20,14:00,29/06/2024,29/06/2024,29/06/2024 13:20,29/06/2024 14:00
Cirk Hes Presents Lizzie,Saturday,Outside Circus Stage,59,33,13:25 - 13:31,13:25,13:31,29/06/2024,29/06/2024,29/06/2024 13:25,29/06/2024 13:31
A Day At The Beach,Saturday,The Glebe,60,33,13:25 - 13:55,13:25,13:55,29/06/2024,29/06/2024,29/06/2024 13:25,29/06/2024 13:55
August Charles,Saturday,Bbc Music Introducing,45,44,13:30 - 14:00,13:30,14:00,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:00
Stuart Goldsmith,Saturday,Cabaret,62,26,13:30 - 14:00,13:30,14:00,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:00
She'S Got Brass,Saturday,Croissant Neuf,55,21,13:30 - 14:30,13:30,14:30,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:30
Sasha Steppa Feat Kiko Bun [Teachings In Dub Takeover],Saturday,Firmly Rooted,43,43,13:30 - 15:00,13:30,15:00,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 15:00
Guy.In.Glasses,Saturday,Glade,51,29,13:30 - 14:00,13:30,14:00,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:00
Marlie B2B Pach.,Saturday,Glade Dome,49,29,13:30 - 15:00,13:30,15:00,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 15:00
Holysseus Fly,Saturday,Greenpeace,55,26,13:30 - 14:15,13:30,14:15,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:15
"Debates: Election 2024: A Change Is Gonna Come With Angela Rayner Mp, Caroline Lucas Mp, Danny Sriskandarajah, Stephen Bush, John Harris",Saturday,Left Field,52,33,13:30 - 14:30,13:30,14:30,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:30
A For Alpha,Saturday,Levels,42,44,13:30 - 15:00,13:30,15:00,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 15:00
Ragz Originale,Saturday,Lonely Hearts Club,44,41,13:30 - 14:15,13:30,14:15,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:15
Paul Mortimer Jones,Saturday,Mandala Stage,0,0,13:30 - 14:30,13:30,14:30,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:30
"Talk: Mothership, Mother Energy",Saturday,Scissors,42,21,13:30 - 14:15,13:30,14:15,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:15
Taiko Meantime,Saturday,Sensation Seekers Stage,0,0,13:30 - 14:15,13:30,14:15,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:15
Otto And Astrid - Die Roten Punkte,Saturday,The Gateway,0,0,13:30 - 14:15,13:30,14:15,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:15
Chinnen,Saturday,The Pavement,0,0,13:30 - 14:00,13:30,14:00,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:00
Fire Fighters!,Saturday,Walkabouts,60,33,13:30 - 14:00,13:30,14:00,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 14:00
The Jukeboxes,Saturday,Walkabouts,60,33,13:30 - 15:00,13:30,15:00,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 15:00
Arrivals Takeover: Ri Mistry (Dj Set),Saturday,Wishing Well,42,20,13:30 - 13:45,13:30,13:45,29/06/2024,29/06/2024,29/06/2024 13:30,29/06/2024 13:45
Grant Goldie,Saturday,Outside Circus Stage,59,33,13:36 - 14:06,13:36,14:06,29/06/2024,29/06/2024,29/06/2024 13:36,29/06/2024 14:06
Roger Mcgough,Saturday,Poetry&Words,0,0,13:38 - 14:08,13:38,14:08,29/06/2024,29/06/2024,29/06/2024 13:38,29/06/2024 14:08
Rezon8 Artist Showcase,Saturday,10 Aces,0,0,13:40 - 14:10,13:40,14:10,29/06/2024,29/06/2024,29/06/2024 13:40,29/06/2024 14:10
Rishi Gordon,Saturday,Walkabouts,60,33,13:40 - 14:25,13:40,14:25,29/06/2024,29/06/2024,29/06/2024 13:40,29/06/2024 14:25
The Family Tree,Saturday,Walkabouts,60,33,13:40 - 14:25,13:40,14:25,29/06/2024,29/06/2024,29/06/2024 13:40,29/06/2024 14:25
Harvey Juggling,Saturday,A Little More Sensation,0,0,13:45 - 14:15,13:45,14:15,29/06/2024,29/06/2024,29/06/2024 13:45,29/06/2024 14:15
African Dance With Penny Avery,Saturday,Humblewell Active Platform,42,21,13:45 - 14:15,13:45,14:15,29/06/2024,29/06/2024,29/06/2024 13:45,29/06/2024 14:15
Enchanted Flower Show Globe,Saturday,Walkabouts,60,33,13:45 - 14:30,13:45,14:30,29/06/2024,29/06/2024,29/06/2024 13:45,29/06/2024 14:30
The Buzzing Bees,Saturday,Walkabouts,60,33,13:45 - 14:45,13:45,14:45,29/06/2024,29/06/2024,29/06/2024 13:45,29/06/2024 14:45
Arrivals Takeover: Shan Vincent De Paul,Saturday,Wishing Well,42,20,13:45 - 14:15,13:45,14:15,29/06/2024,29/06/2024,29/06/2024 13:45,29/06/2024 14:15
Georgia D'Arcy Roden,Saturday,Crooner'S Corner,0,0,13:55 - 14:40,13:55,14:40,29/06/2024,29/06/2024,29/06/2024 13:55,29/06/2024 14:40
Paul Casey,Saturday,Acoustic Stage,66,38,14:00 - 14:40,14:00,14:40,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 14:40
Gabrielle Kwarteng B2B Shanti Celeste [Bodymovements Takeover],Saturday,Assembly,40,42,14:00 - 16:00,14:00,16:00,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 16:00
Elvé - Ella Knight'S House Party,Saturday,Babylon Uprising,0,0,14:00 - 14:45,14:00,14:45,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 14:45
Bob Knight,Saturday,Blind Tiger,0,0,14:00 - 15:00,14:00,15:00,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 15:00
2 Indie Boys From Reading,Saturday,Bread And Roses,0,0,14:00 - 14:50,14:00,14:50,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 14:50
Kleptones,Saturday,Cornish Arms,0,0,14:00 - 16:00,14:00,16:00,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 16:00
The Social At 25,Saturday,Free University Of Glastonbury,42,21,14:00 - 15:00,14:00,15:00,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 15:00
Afriquoi,Saturday,Glade,51,29,14:00 - 15:00,14:00,15:00,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 15:00
Dance Class: Samba,Saturday,Glasto Latino,58,27,14:00 - 15:00,14:00,15:00,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 15:00
Sean Mccabe,Saturday,Nyc Downlow,0,0,14:00 - 15:30,14:00,15:30,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 15:30
"Revelations From The Spycops Inquiry - Tom Fowler, Baroness Jenny Jones",Saturday,Speakers Forum,0,0,14:00 - 15:00,14:00,15:00,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 15:00
Joe Goddard + Elkka,Saturday,Stonebridge Bar,42,18,14:00 - 15:30,14:00,15:30,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 15:30
Jennifer Crook,Saturday,The Bandstand,56,38,14:00 - 14:40,14:00,14:40,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 14:40
Lekiddo Lord Of The Lobsters,Saturday,The Glebe,60,33,14:00 - 14:30,14:00,14:30,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 14:30
Blaney,Saturday,The Hive,0,0,14:00 - 14:45,14:00,14:45,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 14:45
T. Jacques,Saturday,The Meatrack,0,0,14:00 - 15:30,14:00,15:30,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 15:30
Bar Italia,Saturday,The Park Stage,41,19,14:00 - 14:45,14:00,14:45,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 14:45
Tennyson King,Saturday,Toad Hall,0,0,14:00 - 14:45,14:00,14:45,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 14:45
Jfb,Saturday,Village Inn,0,0,14:00 - 16:00,14:00,16:00,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 16:00
Circus Raj,Saturday,Walkabouts,60,33,14:00 - 14:45,14:00,14:45,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 14:45
Mannequin Pussy,Saturday,Woodsies,43,52,14:00 - 14:45,14:00,14:45,29/06/2024,29/06/2024,29/06/2024 14:00,29/06/2024 14:45
Cirk Hes Ground Show,Saturday,Circus Big Top,57,34,14:02 - 14:14,14:02,14:14,29/06/2024,29/06/2024,29/06/2024 14:02,29/06/2024 14:14
Maisie Adam,Saturday,Cabaret,62,26,14:05 - 14:35,14:05,14:35,29/06/2024,29/06/2024,29/06/2024 14:05,29/06/2024 14:35
Ekleido Dance - Splice,Saturday,The Pavement,0,0,14:05 - 14:20,14:05,14:20,29/06/2024,29/06/2024,29/06/2024 14:05,29/06/2024 14:20
The Suitcase Escape Game,Saturday,Walkabouts,60,33,14:05 - 14:50,14:05,14:50,29/06/2024,29/06/2024,29/06/2024 14:05,29/06/2024 14:50
The Explorers,Saturday,Walkabouts,60,33,14:05 - 15:05,14:05,15:05,29/06/2024,29/06/2024,29/06/2024 14:05,29/06/2024 15:05
Rose Popay & Sidekick Saffy,Saturday,Walkabouts,60,33,14:10 - 14:55,14:10,14:55,29/06/2024,29/06/2024,29/06/2024 14:10,29/06/2024 14:55
Charlie Bicknell Is Holding Out For A Hero,Saturday,Outside Circus Stage,59,33,14:11 - 14:23,14:11,14:23,29/06/2024,29/06/2024,29/06/2024 14:11,29/06/2024 14:23
Molly Walker,Saturday,Poetry&Words,0,0,14:11 - 14:36,14:11,14:36,29/06/2024,29/06/2024,29/06/2024 14:11,29/06/2024 14:36
Cut Capers,Saturday,Avalon Stage,66,38,14:15 - 15:10,14:15,15:10,29/06/2024,29/06/2024,29/06/2024 14:15,29/06/2024 15:10
Old Time Sailors,Saturday,Bimble Inn,41,16,14:15 - 15:30,14:15,15:30,29/06/2024,29/06/2024,29/06/2024 14:15,29/06/2024 15:30
Cbbc'S Laura & Alex,Saturday,Kidzfield Big Top,0,0,14:15 - 14:45,14:15,14:45,29/06/2024,29/06/2024,29/06/2024 14:15,29/06/2024 14:45
Bbc Natural History Unit,Saturday,Laboratory Stage,0,0,14:15 - 14:45,14:15,14:45,29/06/2024,29/06/2024,29/06/2024 14:15,29/06/2024 14:45
Tems,Saturday,Other Stage,47,34,14:15 - 15:15,14:15,15:15,29/06/2024,29/06/2024,29/06/2024 14:15,29/06/2024 15:15
Marcus Du Sautoy And The School Of Hard Sums,Saturday,The Astrolabe Theatre,0,0,14:15 - 15:05,14:15,15:05,29/06/2024,29/06/2024,29/06/2024 14:15,29/06/2024 15:05
Disco Robot Girlz,Saturday,Walkabouts,60,33,14:15 - 15:00,14:15,15:00,29/06/2024,29/06/2024,29/06/2024 14:15,29/06/2024 15:00
Ukelele Thrash Mob,Saturday,Walkabouts,60,33,14:15 - 15:00,14:15,15:00,29/06/2024,29/06/2024,29/06/2024 14:15,29/06/2024 15:00
Arrivals Takeover: Ri Mistry (Dj Set),Saturday,Wishing Well,42,20,14:15 - 14:30,14:15,14:30,29/06/2024,29/06/2024,29/06/2024 14:15,29/06/2024 14:30
Nofit Howie,Saturday,Circus Big Top,57,34,14:19 - 14:27,14:19,14:27,29/06/2024,29/06/2024,29/06/2024 14:19,29/06/2024 14:27
Hilby,Saturday,A Little More Sensation,0,0,14:20 - 14:50,14:20,14:50,29/06/2024,29/06/2024,29/06/2024 14:20,29/06/2024 14:50
Fat Barry'S Bingo Bango Bongo,Saturday,Sensation Seekers Stage,0,0,14:25 - 14:55,14:25,14:55,29/06/2024,29/06/2024,29/06/2024 14:25,29/06/2024 14:55
Billy Kidd Show,Saturday,The Pavement,0,0,14:25 - 14:55,14:25,14:55,29/06/2024,29/06/2024,29/06/2024 14:25,29/06/2024 14:55
Wookey Hole Circus,Saturday,Outside Circus Stage,59,33,14:28 - 14:53,14:28,14:53,29/06/2024,29/06/2024,29/06/2024 14:28,29/06/2024 14:53
"Bela Veradi, Talk: Documenting The Lives Of Gypsy, Traveller And Roma Life Through Photography",Saturday,Atchin Tan,0,0,14:30 - 15:15,14:30,15:15,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:15
Kingfishr,Saturday,Bbc Music Introducing,45,44,14:30 - 15:00,14:30,15:00,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:00
Baskery,Saturday,Croissant Neuf,55,21,14:30 - 15:30,14:30,15:30,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:30
Chloe Leigh,Saturday,Croissant Neuf Bandstand,55,21,14:30 - 15:00,14:30,15:00,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:00
Disco Fit With Helen Rooney,Saturday,Humblewell Active Platform,42,21,14:30 - 15:00,14:30,15:00,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:00
Indian Head Massage Workshop With Lucy Sage,Saturday,Humblewell Retreat Yurt,42,21,14:30 - 15:30,14:30,15:30,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:30
Blanco,Saturday,Lonely Hearts Club,44,41,14:30 - 15:00,14:30,15:00,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:00
Cyndi Lauper,Saturday,Pyramid Stage,51,43,14:30 - 15:30,14:30,15:30,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:30
Macca,Saturday,San Remo,45,47,14:30 - 16:00,14:30,16:00,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 16:00
"Talk: Polyphilia, Threesomes: Communication & Consent",Saturday,Scissors,42,21,14:30 - 15:30,14:30,15:30,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:30
Rave New World: Acid House Cabaret,Saturday,Strummerville,48,12,14:30 - 15:15,14:30,15:15,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:15
"Soliphilia: ‘Music & Climate - Visions For The Future’: Frances Fox (Founder - Climate Live), Jack Mccutcheon (Director - World Wise Touring), Tori Tsui (Author, Activist), Hosted By Pauline Bourdon (Director - Soliphilia)",Saturday,The Information,41,41,14:30 - 15:30,14:30,15:30,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:30
Madame D'Orificio,Saturday,Walkabouts,60,33,14:30 - 16:00,14:30,16:00,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 16:00
Alogte Oho & His Sounds Of Joy,Saturday,West Holts Stage,57,31,14:30 - 15:30,14:30,15:30,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:30
Arrivals Takeover: Tara Lily,Saturday,Wishing Well,42,20,14:30 - 15:00,14:30,15:00,29/06/2024,29/06/2024,29/06/2024 14:30,29/06/2024 15:00
Bexi - Barbarella,Saturday,Circus Big Top,57,34,14:32 - 14:38,14:32,14:38,29/06/2024,29/06/2024,29/06/2024 14:32,29/06/2024 14:38
Matthew One Man,Saturday,The Gateway,0,0,14:35 - 15:05,14:35,15:05,29/06/2024,29/06/2024,29/06/2024 14:35,29/06/2024 15:05
Jack Defrost - Traceworks Dance,Saturday,The Glebe,60,33,14:35 - 14:50,14:35,14:50,29/06/2024,29/06/2024,29/06/2024 14:35,29/06/2024 14:50
Princess Arinola Adegbite,Saturday,Poetry&Words,0,0,14:39 - 15:04,14:39,15:04,29/06/2024,29/06/2024,29/06/2024 14:39,29/06/2024 15:04
Rsvp,Saturday,Cabaret,62,26,14:40 - 15:20,14:40,15:20,29/06/2024,29/06/2024,29/06/2024 14:40,29/06/2024 15:20
Vertigo Stilts,Saturday,Walkabouts,60,33,14:40 - 15:25,14:40,15:25,29/06/2024,29/06/2024,29/06/2024 14:40,29/06/2024 15:25
Darius Magic,Saturday,Walkabouts,60,33,14:40 - 15:40,14:40,15:40,29/06/2024,29/06/2024,29/06/2024 14:40,29/06/2024 15:40
Fraser Hooper,Saturday,Circus Big Top,57,34,14:43 - 15:08,14:43,15:08,29/06/2024,29/06/2024,29/06/2024 14:43,29/06/2024 15:08
Ella Knight - Ella Knight'S House Party,Saturday,Babylon Uprising,0,0,14:45 - 15:30,14:45,15:30,29/06/2024,29/06/2024,29/06/2024 14:45,29/06/2024 15:30
Liz Lawrence,Saturday,Greenpeace,55,26,14:45 - 15:30,14:45,15:30,29/06/2024,29/06/2024,29/06/2024 14:45,29/06/2024 15:30
The Bigheads,Saturday,Walkabouts,60,33,14:45 - 15:25,14:45,15:25,29/06/2024,29/06/2024,29/06/2024 14:45,29/06/2024 15:25
Dodgy Boys,Saturday,Walkabouts,60,33,14:45 - 15:30,14:45,15:30,29/06/2024,29/06/2024,29/06/2024 14:45,29/06/2024 15:30
Natural Diversions,Saturday,Walkabouts,60,33,14:45 - 15:30,14:45,15:30,29/06/2024,29/06/2024,29/06/2024 14:45,29/06/2024 15:30
Cash Cows,Saturday,10 Aces,0,0,14:50 - 13:30,14:50,13:30,29/06/2024,29/06/2024,29/06/2024 14:50,29/06/2024 13:30
Blip,Saturday,Walkabouts,60,33,14:50 - 15:35,14:50,15:35,29/06/2024,29/06/2024,29/06/2024 14:50,29/06/2024 15:35
Tba,Saturday,A Little More Sensation,0,0,14:55 - 15:25,14:55,15:25,29/06/2024,29/06/2024,29/06/2024 14:55,29/06/2024 15:25
Doc Brown'S Wordpower Hour,Saturday,Kidzfield Big Top,0,0,14:55 - 15:35,14:55,15:35,29/06/2024,29/06/2024,29/06/2024 14:55,29/06/2024 15:35
Tony And Ray,Saturday,The Glebe,60,33,14:55 - 15:10,14:55,15:10,29/06/2024,29/06/2024,29/06/2024 14:55,29/06/2024 15:10
Venus,Saturday,Outside Circus Stage,59,33,14:58 - 15:28,14:58,15:28,29/06/2024,29/06/2024,29/06/2024 14:58,29/06/2024 15:28
"Fun Lovin’ Crime Writers With Mark Billingham, Chris Brookmyre, Doug Johnstone, Val Mcdermid, Stuart Neville & Luca Veste",Saturday,Acoustic Stage,66,38,15:00 - 15:40,15:00,15:40,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:40
Trish Reilly,Saturday,Blind Tiger,0,0,15:00 - 16:00,15:00,16:00,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 16:00
Stanley Pratt,Saturday,Bread And Roses,0,0,15:00 - 15:30,15:00,15:30,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:30
Lily Lyons,Saturday,Croissant Neuf,55,21,15:00 - 16:00,15:00,16:00,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 16:00
Charlotte May,Saturday,Crooner'S Corner,0,0,15:00 - 15:45,15:00,15:45,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:45
Dubkasm Vs Gorgon Sound [Teachings In Dub Takeover],Saturday,Firmly Rooted,43,43,15:00 - 17:00,15:00,17:00,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 17:00
Guy.In.Glasses,Saturday,Glade,51,29,15:00 - 15:30,15:00,15:30,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:30
Wodda,Saturday,Glade Dome,49,29,15:00 - 16:30,15:00,16:30,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 16:30
Dance Class: Salsa,Saturday,Glasto Latino,58,27,15:00 - 16:00,15:00,16:00,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 16:00
Robin Ince & Special Guest,Saturday,Laboratory Stage,0,0,15:00 - 15:45,15:00,15:45,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:45
"Radical Round Up: Billy Bragg, Hank Wangford, Tamzene",Saturday,Left Field,52,33,15:00 - 16:00,15:00,16:00,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 16:00
Dan Shake B2B Lovefoxy,Saturday,Levels,42,44,15:00 - 16:30,15:00,16:30,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 16:30
Manilla Times,Saturday,Mandala Stage,0,0,15:00 - 16:00,15:00,16:00,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 16:00
Kneecap + Q&A With Band & Director,Saturday,Pilton Palais Cinema,64,36,15:00 - 17:15,15:00,17:15,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 17:15
Abandoman,Saturday,Sensation Seekers Stage,0,0,15:00 - 15:45,15:00,15:45,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:45
Biophobia - Jarvis Cocker,Saturday,Speakers Forum,0,0,15:00 - 16:00,15:00,16:00,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 16:00
Tom Moore & Archie Moss,Saturday,The Bandstand,56,38,15:00 - 15:40,15:00,15:40,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:40
Mr Peewee The Drumming Puppet,Saturday,The Pavement,0,0,15:00 - 15:30,15:00,15:30,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:30
Daisy Chute,Saturday,Toad Hall,0,0,15:00 - 15:45,15:00,15:45,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:45
Anyone For Tennis,Saturday,Walkabouts,60,33,15:00 - 15:45,15:00,15:45,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:45
Gliding Butterflies,Saturday,Walkabouts,60,33,15:00 - 15:45,15:00,15:45,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:45
Arrivals Takeover: Ri Mistry (Dj Set),Saturday,Wishing Well,42,20,15:00 - 15:15,15:00,15:15,29/06/2024,29/06/2024,29/06/2024 15:00,29/06/2024 15:15
Problem Patterns,Saturday,The Hive,0,0,15:05 - 15:50,15:05,15:50,29/06/2024,29/06/2024,29/06/2024 15:05,29/06/2024 15:50
Giant Seagulls,Saturday,Walkabouts,60,33,15:05 - 15:50,15:05,15:50,29/06/2024,29/06/2024,29/06/2024 15:05,29/06/2024 15:50
Laura London & Jake Francis,Saturday,Walkabouts,60,33,15:05 - 15:50,15:05,15:50,29/06/2024,29/06/2024,29/06/2024 15:05,29/06/2024 15:50
Lauren Mcnamara,Saturday,Poetry&Words,0,0,15:07 - 15:32,15:07,15:32,29/06/2024,29/06/2024,29/06/2024 15:07,29/06/2024 15:32
The Black Eagles,Saturday,The Astrolabe Theatre,0,0,15:10 - 15:35,15:10,15:35,29/06/2024,29/06/2024,29/06/2024 15:10,29/06/2024 15:35
Hairy Hatter,Saturday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,29/06/2024,29/06/2024,29/06/2024 15:10,29/06/2024 15:55
Jack Thomson,Saturday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,29/06/2024,29/06/2024,29/06/2024 15:10,29/06/2024 15:55
The Very Best Of Tommy Cooper,Saturday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,29/06/2024,29/06/2024,29/06/2024 15:10,29/06/2024 15:55
Head Over Wheels,Saturday,Circus Big Top,57,34,15:13 - 15:21,15:13,15:21,29/06/2024,29/06/2024,29/06/2024 15:13,29/06/2024 15:21
Hula Hoops With Helen Rooney,Saturday,Humblewell Active Platform,42,21,15:15 - 16:00,15:15,16:00,29/06/2024,29/06/2024,29/06/2024 15:15,29/06/2024 16:00
Dan The Hat,Saturday,The Glebe,60,33,15:15 - 15:45,15:15,15:45,29/06/2024,29/06/2024,29/06/2024 15:15,29/06/2024 15:45
Otoboke Beaver,Saturday,The Park Stage,41,19,15:15 - 16:00,15:15,16:00,29/06/2024,29/06/2024,29/06/2024 15:15,29/06/2024 16:00
The Crows,Saturday,Walkabouts,60,33,15:15 - 15:45,15:15,15:45,29/06/2024,29/06/2024,29/06/2024 15:15,29/06/2024 15:45
The Natural Theatre Company,Saturday,Walkabouts,60,33,15:15 - 16:00,15:15,16:00,29/06/2024,29/06/2024,29/06/2024 15:15,29/06/2024 16:00
Arrivals Takeover: Ustad Noor Bakhsh,Saturday,Wishing Well,42,20,15:15 - 16:45,15:15,16:45,29/06/2024,29/06/2024,29/06/2024 15:15,29/06/2024 16:45
Soccer Mommy,Saturday,Woodsies,43,52,15:15 - 16:00,15:15,16:00,29/06/2024,29/06/2024,29/06/2024 15:15,29/06/2024 16:00
The Wardens,Saturday,Walkabouts,60,33,15:20 - 15:50,15:20,15:50,29/06/2024,29/06/2024,29/06/2024 15:20,29/06/2024 15:50
Laura Lexx,Saturday,Cabaret,62,26,15:25 - 15:55,15:25,15:55,29/06/2024,29/06/2024,29/06/2024 15:25,29/06/2024 15:55
The Disappointments,Saturday,The Gateway,0,0,15:25 - 16:10,15:25,16:10,29/06/2024,29/06/2024,29/06/2024 15:25,29/06/2024 16:10
Toby Walker,Saturday,Circus Big Top,57,34,15:26 - 15:34,15:26,15:34,29/06/2024,29/06/2024,29/06/2024 15:26,29/06/2024 15:34
A Day At The Beach,Saturday,A Little More Sensation,0,0,15:30 - 16:00,15:30,16:00,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 16:00
Art Workshop,Saturday,Atchin Tan,0,0,15:30 - 17:00,15:30,17:00,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 17:00
Grace Sands - Ella Knight'S House Party,Saturday,Babylon Uprising,0,0,15:30 - 16:15,15:30,16:15,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 16:15
Tianna,Saturday,Bbc Music Introducing,45,44,15:30 - 16:00,15:30,16:00,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 16:00
Dele Sosimi Afrobeat Experience,Saturday,Glade,51,29,15:30 - 16:50,15:30,16:50,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 16:50
Caity Baser,Saturday,Lonely Hearts Club,44,41,15:30 - 16:15,15:30,16:15,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 16:15
Adam Scott Glaspool,Saturday,Lunched Out Lizards,0,0,15:30 - 16:30,15:30,16:30,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 16:30
François K,Saturday,Nyc Downlow,0,0,15:30 - 18:30,15:30,18:30,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 18:30
Ros Atkins,Saturday,Stonebridge Bar,42,18,15:30 - 17:00,15:30,17:00,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 17:00
Compère: Sally-Anne Hayward,Saturday,The Astrolabe Theatre,0,0,15:30 - 19:00,15:30,19:00,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 19:00
Junior Jungle,Saturday,The Bug,41,25,15:30 - 16:30,15:30,16:30,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 16:30
Maclo,Saturday,The Meatrack,0,0,15:30 - 17:00,15:30,17:00,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 17:00
Fortuni And Fae,Saturday,Walkabouts,60,33,15:30 - 16:15,15:30,16:15,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 16:15
Meanderthals,Saturday,Walkabouts,60,33,15:30 - 16:15,15:30,16:15,29/06/2024,29/06/2024,29/06/2024 15:30,29/06/2024 16:15
Compere: Jonny Fluffypunk,Saturday,Poetry&Words,0,0,15:32 - 19:00,15:32,19:00,29/06/2024,29/06/2024,29/06/2024 15:32,29/06/2024 19:00
Chinnen,Saturday,Outside Circus Stage,59,33,15:33 - 16:03,15:33,16:03,29/06/2024,29/06/2024,29/06/2024 15:33,29/06/2024 16:03
Kate Ireland,Saturday,Poetry&Words,0,0,15:35 - 16:00,15:35,16:00,29/06/2024,29/06/2024,29/06/2024 15:35,29/06/2024 16:00
Rod Laver,Saturday,The Astrolabe Theatre,0,0,15:35 - 15:50,15:35,15:50,29/06/2024,29/06/2024,29/06/2024 15:35,29/06/2024 15:50
Kwabana Lindsay Show,Saturday,The Pavement,0,0,15:35 - 16:05,15:35,16:05,29/06/2024,29/06/2024,29/06/2024 15:35,29/06/2024 16:05
Clamour Of Bells,Saturday,Walkabouts,60,33,15:35 - 16:20,15:35,16:20,29/06/2024,29/06/2024,29/06/2024 15:35,29/06/2024 16:20
The Bad Eggs,Saturday,Walkabouts,60,33,15:35 - 16:20,15:35,16:20,29/06/2024,29/06/2024,29/06/2024 15:35,29/06/2024 16:20
Cirk Hes Presents Jaia And Malia,Saturday,Circus Big Top,57,34,15:39 - 15:49,15:39,15:49,29/06/2024,29/06/2024,29/06/2024 15:39,29/06/2024 15:49
Riff Raff Kaberett,Saturday,10 Aces,0,0,15:40 - 16:10,15:40,16:10,29/06/2024,29/06/2024,29/06/2024 15:40,29/06/2024 16:10
Lucy Spraggan,Saturday,Avalon Stage,66,38,15:40 - 16:40,15:40,16:40,29/06/2024,29/06/2024,29/06/2024 15:40,29/06/2024 16:40
The Midwives,Saturday,Walkabouts,60,33,15:40 - 16:25,15:40,16:25,29/06/2024,29/06/2024,29/06/2024 15:40,29/06/2024 16:25
Trifleenees,Saturday,Walkabouts,60,33,15:40 - 16:25,15:40,16:25,29/06/2024,29/06/2024,29/06/2024 15:40,29/06/2024 16:25
Sav - Head Of Magic,Saturday,Walkabouts,60,33,15:40 - 17:40,15:40,17:40,29/06/2024,29/06/2024,29/06/2024 15:40,29/06/2024 17:40
The Royston Club,Saturday,Bread And Roses,0,0,15:45 - 16:45,15:45,16:45,29/06/2024,29/06/2024,29/06/2024 15:45,29/06/2024 16:45
Gong Bath With Yogic Sound,Saturday,Humblewell Retreat Yurt,42,21,15:45 - 16:30,15:45,16:30,29/06/2024,29/06/2024,29/06/2024 15:45,29/06/2024 16:30
Starkidz Superhero Vs Princess Show,Saturday,Kidzfield Big Top,0,0,15:45 - 16:15,15:45,16:15,29/06/2024,29/06/2024,29/06/2024 15:45,29/06/2024 16:15
The Last Dinner Party,Saturday,Other Stage,47,34,15:45 - 16:45,15:45,16:45,29/06/2024,29/06/2024,29/06/2024 15:45,29/06/2024 16:45
"Talk: Prof. Janina Ramirez, Warrior Women & Queer Nuns",Saturday,Scissors,42,21,15:45 - 16:45,15:45,16:45,29/06/2024,29/06/2024,29/06/2024 15:45,29/06/2024 16:45
"Versus: ‘The Future Of Football’: Blanco (Rapper), Ceylon Andi Hickman (Inmotion Collective & Football Beyond Borders), Maya Le Tissier (Manchester United & England Lioness) Hosted By Johnny Kay (Versus)",Saturday,The Information,41,41,15:45 - 16:45,15:45,16:45,29/06/2024,29/06/2024,29/06/2024 15:45,29/06/2024 16:45
Louvre On Th Move,Saturday,Walkabouts,60,33,15:45 - 16:15,15:45,16:15,29/06/2024,29/06/2024,29/06/2024 15:45,29/06/2024 16:15
Bell And Bullock,Saturday,Walkabouts,60,33,15:45 - 16:30,15:45,16:30,29/06/2024,29/06/2024,29/06/2024 15:45,29/06/2024 16:30
Football Crazy,Saturday,Walkabouts,60,33,15:45 - 16:30,15:45,16:30,29/06/2024,29/06/2024,29/06/2024 15:45,29/06/2024 16:30
Beans On Toast,Saturday,Sensation Seekers Stage,0,0,15:50 - 16:35,15:50,16:35,29/06/2024,29/06/2024,29/06/2024 15:50,29/06/2024 16:35
Mark Bruce Dance Company,Saturday,The Astrolabe Theatre,0,0,15:50 - 16:00,15:50,16:00,29/06/2024,29/06/2024,29/06/2024 15:50,29/06/2024 16:00
Primary School Assembly Bangers,Saturday,The Glebe,60,33,15:50 - 16:20,15:50,16:20,29/06/2024,29/06/2024,29/06/2024 15:50,29/06/2024 16:20
The Tea Ladies On Tour,Saturday,Walkabouts,60,33,15:50 - 16:35,15:50,16:35,29/06/2024,29/06/2024,29/06/2024 15:50,29/06/2024 16:35
Ellis Grover,Saturday,Circus Big Top,57,34,15:54 - 16:04,15:54,16:04,29/06/2024,29/06/2024,29/06/2024 15:54,29/06/2024 16:04
Albert Lee,Saturday,Acoustic Stage,66,38,16:00 - 16:40,16:00,16:40,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 16:40
Job Jobse [Bodymovements Takeover],Saturday,Assembly,40,42,16:00 - 18:00,16:00,18:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 18:00
Thomas Mccarthy,Saturday,Blind Tiger,0,0,16:00 - 17:00,16:00,17:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 17:00
Jen Brister,Saturday,Cabaret,62,26,16:00 - 16:30,16:00,16:30,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 16:30
Compère: Alister Barrie,Saturday,Cabaret,62,26,16:00 - 20:00,16:00,20:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 20:00
Jo Bucket,Saturday,Carhenge,58,36,16:00 - 17:00,16:00,17:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 17:00
O.P.Groover + Puttyrubber (Blendid Takeover),Saturday,Cornish Arms,0,0,16:00 - 17:00,16:00,17:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 17:00
Theo Warrington,Saturday,Croissant Neuf Bandstand,55,21,16:00 - 16:30,16:00,16:30,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 16:30
Dance Class: Samba,Saturday,Glasto Latino,58,27,16:00 - 17:00,16:00,17:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 17:00
Willie J Healey,Saturday,Greenpeace,55,26,16:00 - 16:45,16:00,16:45,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 16:45
Andrew O'Neill,Saturday,Laboratory Stage,0,0,16:00 - 16:45,16:00,16:45,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 16:45
Hitide,Saturday,Meeting Place Bar,0,0,16:00 - 19:00,16:00,19:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 19:00
Keane,Saturday,Pyramid Stage,51,43,16:00 - 17:00,16:00,17:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 17:00
Maddy Maia + Tottie,Saturday,San Remo,45,47,16:00 - 17:30,16:00,17:30,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 17:30
"Is Net Zero By 2050 Still Possible? - Clive Lewis Mp, Kevin Anderson, Molly Scott Cato, Rebecca Gibbs",Saturday,Speakers Forum,0,0,16:00 - 17:00,16:00,17:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 17:00
Supalung,Saturday,Strummerville,48,12,16:00 - 16:40,16:00,16:40,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 16:40
Gusto Gusto,Saturday,The Bandstand,56,38,16:00 - 16:40,16:00,16:40,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 16:40
Disco Freaks,Saturday,Village Inn,0,0,16:00 - 19:00,16:00,19:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 19:00
Steve Faulkner,Saturday,Walkabouts,60,33,16:00 - 16:45,16:00,16:45,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 16:45
The Last Of The Mohicans,Saturday,Walkabouts,60,33,16:00 - 17:00,16:00,17:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 17:00
Corinne Bailey Rae,Saturday,West Holts Stage,57,31,16:00 - 17:00,16:00,17:00,29/06/2024,29/06/2024,29/06/2024 16:00,29/06/2024 17:00
Compère: Famos Bramwells,Saturday,Outside Circus Stage,59,33,16:03 - 20:33,16:03,20:33,29/06/2024,29/06/2024,29/06/2024 16:03,29/06/2024 20:33
Kayleigh Jayshree,Saturday,Poetry&Words,0,0,16:03 - 16:28,16:03,16:28,29/06/2024,29/06/2024,29/06/2024 16:03,29/06/2024 16:28
Grant Goldie,Saturday,A Little More Sensation,0,0,16:05 - 16:35,16:05,16:35,29/06/2024,29/06/2024,29/06/2024 16:05,29/06/2024 16:35
Paul Lambourne,Saturday,Crooner'S Corner,0,0,16:05 - 16:35,16:05,16:35,29/06/2024,29/06/2024,29/06/2024 16:05,29/06/2024 16:35
George Egg'S Set Menu,Saturday,The Astrolabe Theatre,0,0,16:05 - 17:05,16:05,17:05,29/06/2024,29/06/2024,29/06/2024 16:05,29/06/2024 17:05
Roo'D,Saturday,Walkabouts,60,33,16:05 - 16:35,16:05,16:35,29/06/2024,29/06/2024,29/06/2024 16:05,29/06/2024 16:35
The Explorers,Saturday,Walkabouts,60,33,16:05 - 17:05,16:05,17:05,29/06/2024,29/06/2024,29/06/2024 16:05,29/06/2024 17:05
Bexi - Barbarella,Saturday,Outside Circus Stage,59,33,16:08 - 16:15,16:08,16:15,29/06/2024,29/06/2024,29/06/2024 16:08,29/06/2024 16:15
Charlie Bicknell - Supersonic Woman,Saturday,Circus Big Top,57,34,16:09 - 16:21,16:09,16:21,29/06/2024,29/06/2024,29/06/2024 16:09,29/06/2024 16:21
Boss Cass,Saturday,The Hive,0,0,16:10 - 16:55,16:10,16:55,29/06/2024,29/06/2024,29/06/2024 16:10,29/06/2024 16:55
Rob Roy Collins,Saturday,The Pavement,0,0,16:10 - 16:40,16:10,16:40,29/06/2024,29/06/2024,29/06/2024 16:10,29/06/2024 16:40
Garrett David - Ella Knight'S House Party,Saturday,Babylon Uprising,0,0,16:15 - 17:00,16:15,17:00,29/06/2024,29/06/2024,29/06/2024 16:15,29/06/2024 17:00
Feel Good Games With Kevin Campbell Davidson,Saturday,Humblewell Active Platform,42,21,16:15 - 17:00,16:15,17:00,29/06/2024,29/06/2024,29/06/2024 16:15,29/06/2024 17:00
David Ford Band,Saturday,Toad Hall,0,0,16:15 - 17:00,16:15,17:00,29/06/2024,29/06/2024,29/06/2024 16:15,29/06/2024 17:00
Enchanted Flower Show Globe,Saturday,Walkabouts,60,33,16:15 - 17:00,16:15,17:00,29/06/2024,29/06/2024,29/06/2024 16:15,29/06/2024 17:00
The Cloudmen,Saturday,Walkabouts,60,33,16:15 - 17:15,16:15,17:15,29/06/2024,29/06/2024,29/06/2024 16:15,29/06/2024 17:15
Red Hot Riot,Saturday,10 Aces,0,0,16:20 - 17:20,16:20,17:20,29/06/2024,29/06/2024,29/06/2024 16:20,29/06/2024 17:20
Cirk Hes Presents Acro Ensemble,Saturday,Outside Circus Stage,59,33,16:20 - 16:26,16:20,16:26,29/06/2024,29/06/2024,29/06/2024 16:20,29/06/2024 16:26
The Jukeboxes,Saturday,Walkabouts,60,33,16:20 - 17:50,16:20,17:50,29/06/2024,29/06/2024,29/06/2024 16:20,29/06/2024 17:50
Maddie Moate'S Science Showdown!,Saturday,Kidzfield Big Top,0,0,16:25 - 16:50,16:25,16:50,29/06/2024,29/06/2024,29/06/2024 16:25,29/06/2024 16:50
Faces Of Disco,Saturday,The Gateway,0,0,16:25 - 16:55,16:25,16:55,29/06/2024,29/06/2024,29/06/2024 16:25,29/06/2024 16:55
Billy Kidd Show,Saturday,The Glebe,60,33,16:25 - 16:55,16:25,16:55,29/06/2024,29/06/2024,29/06/2024 16:25,29/06/2024 16:55
Ballerinas,Saturday,Circus Big Top,57,34,16:26 - 16:36,16:26,16:36,29/06/2024,29/06/2024,29/06/2024 16:26,29/06/2024 16:36
Tba,Saturday,Bbc Music Introducing,45,44,16:30 - 17:00,16:30,17:00,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 17:00
Compere: Professor Elemental,Saturday,Circus Big Top,57,34,16:30 - 18:45,16:30,18:45,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 18:45
Admnti B2B Jack Ling,Saturday,Glade Dome,49,29,16:30 - 18:00,16:30,18:00,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 18:00
47Soul,Saturday,Left Field,52,33,16:30 - 17:05,16:30,17:05,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 17:05
Arielle Free,Saturday,Levels,42,44,16:30 - 18:00,16:30,18:00,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 18:00
Antony Szmierek,Saturday,Lonely Hearts Club,44,41,16:30 - 17:15,16:30,17:15,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 17:15
Arooj Aftab,Saturday,The Park Stage,41,19,16:30 - 17:30,16:30,17:30,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 17:30
Circus Raj,Saturday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 17:15
Fairly Fresh Fish Co,Saturday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 17:15
The Suitcase Escape Game,Saturday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 17:15
Fat White Family,Saturday,Woodsies,43,52,16:30 - 17:30,16:30,17:30,29/06/2024,29/06/2024,29/06/2024 16:30,29/06/2024 17:30
The Doogans,Saturday,Outside Circus Stage,59,33,16:31 - 17:01,16:31,17:01,29/06/2024,29/06/2024,29/06/2024 16:31,29/06/2024 17:01
Luke Wright,Saturday,Poetry&Words,0,0,16:31 - 17:01,16:31,17:01,29/06/2024,29/06/2024,29/06/2024 16:31,29/06/2024 17:01
Mawaan Rizwan & Band,Saturday,Cabaret,62,26,16:35 - 17:15,16:35,17:15,29/06/2024,29/06/2024,29/06/2024 16:35,29/06/2024 17:15
Kane And Abel Magic,Saturday,Walkabouts,60,33,16:35 - 17:05,16:35,17:05,29/06/2024,29/06/2024,29/06/2024 16:35,29/06/2024 17:05
Tba,Saturday,A Little More Sensation,0,0,16:40 - 17:10,16:40,17:10,29/06/2024,29/06/2024,29/06/2024 16:40,29/06/2024 17:10
Showhawk Duo,Saturday,Sensation Seekers Stage,0,0,16:40 - 17:40,16:40,17:40,29/06/2024,29/06/2024,29/06/2024 16:40,29/06/2024 17:40
Vertigo Stilts,Saturday,Walkabouts,60,33,16:40 - 17:25,16:40,17:25,29/06/2024,29/06/2024,29/06/2024 16:40,29/06/2024 17:25
Tina Segner,Saturday,Circus Big Top,57,34,16:41 - 16:46,16:41,16:46,29/06/2024,29/06/2024,29/06/2024 16:41,29/06/2024 16:46
Gong Bath With Yogic Sound,Saturday,Humblewell Retreat Yurt,42,21,16:45 - 17:30,16:45,17:30,29/06/2024,29/06/2024,29/06/2024 16:45,29/06/2024 17:30
Ekleido Dance - Splice,Saturday,The Pavement,0,0,16:45 - 17:00,16:45,17:00,29/06/2024,29/06/2024,29/06/2024 16:45,29/06/2024 17:00
Bigheads,Saturday,Walkabouts,60,33,16:45 - 17:25,16:45,17:25,29/06/2024,29/06/2024,29/06/2024 16:45,29/06/2024 17:25
Alice And Alice,Saturday,Walkabouts,60,33,16:45 - 17:30,16:45,17:30,29/06/2024,29/06/2024,29/06/2024 16:45,29/06/2024 17:30
Blip,Saturday,Walkabouts,60,33,16:45 - 17:30,16:45,17:30,29/06/2024,29/06/2024,29/06/2024 16:45,29/06/2024 17:30
Arrivals Takeover: Pia Collada (Dj Set),Saturday,Wishing Well,42,20,16:45 - 17:00,16:45,17:00,29/06/2024,29/06/2024,29/06/2024 16:45,29/06/2024 17:00
Guy.In.Glasses,Saturday,Glade,51,29,16:50 - 17:20,16:50,17:20,29/06/2024,29/06/2024,29/06/2024 16:50,29/06/2024 17:20
Duo Santus,Saturday,Circus Big Top,57,34,16:51 - 16:57,16:51,16:57,29/06/2024,29/06/2024,29/06/2024 16:51,29/06/2024 16:57
Gracie Barry Tait,Saturday,Crooner'S Corner,0,0,16:55 - 17:40,16:55,17:40,29/06/2024,29/06/2024,29/06/2024 16:55,29/06/2024 17:40
The Manfreds Featuring Paul Jones & Mike D’Abo,Saturday,Acoustic Stage,66,38,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
Safiye,Saturday,Babylon Uprising,0,0,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
Brewer'S Daughter,Saturday,Blind Tiger,0,0,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
Luke Gomm & The Works,Saturday,Bread And Roses,0,0,17:00 - 17:40,17:00,17:40,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:40
Puttyrubber + O.P.Groover (Blendid Takeover),Saturday,Cornish Arms,0,0,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
Manasseh Feat Likkle Minty [Teachings In Dub Takeover],Saturday,Firmly Rooted,43,43,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
Dance Class: Salsa,Saturday,Glasto Latino,58,27,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
Dinomania,Saturday,Kidzfield Big Top,0,0,17:00 - 17:25,17:00,17:25,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:25
Louis Vi,Saturday,Laboratory Stage,0,0,17:00 - 17:45,17:00,17:45,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:45
Eliza Oakes,Saturday,Lunched Out Lizards,0,0,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
The Burning Glass,Saturday,Mandala Stage,0,0,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
"Talk: Kate Hutchinson X Sam Lee, Nature Is Queer",Saturday,Scissors,42,21,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
"Parliament, Protest And Another England - Caroline Lucas Mp",Saturday,Speakers Forum,0,0,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
Yung Singh B2B Moktar,Saturday,Stonebridge Bar,42,18,17:00 - 19:00,17:00,19:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 19:00
Firouzeh,Saturday,Strummerville,48,12,17:00 - 17:40,17:00,17:40,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:40
The Barefoot Bandit,Saturday,The Bandstand,56,38,17:00 - 17:50,17:00,17:50,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:50
Rogue Wave,Saturday,The Bug,41,25,17:00 - 17:30,17:00,17:30,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:30
New York Brass Band,Saturday,The Gateway,0,0,17:00 - 17:30,17:00,17:30,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:30
Jack Defrost - Traceworks Dance,Saturday,The Glebe,60,33,17:00 - 17:15,17:00,17:15,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:15
"Party Lines: ‘Blues Dances To Free Parties - The Radical Roots Of Rave’ - Grace Sands (Diy Soundsystem), Phil Hartnoll (Orbital), Hosted By: Ed Gillett (Author - Party Lines)",Saturday,The Information,41,41,17:00 - 18:00,17:00,18:00,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:00
Husband,Saturday,The Meatrack,0,0,17:00 - 18:30,17:00,18:30,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 18:30
Fortuni And Fae,Saturday,Walkabouts,60,33,17:00 - 17:45,17:00,17:45,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:45
Gliding Butterflies,Saturday,Walkabouts,60,33,17:00 - 17:45,17:00,17:45,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:45
Swyron & Desaata,Saturday,Walkabouts,60,33,17:00 - 17:45,17:00,17:45,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:45
Dan Ottewell,Saturday,West Holts Bar,59,29,17:00 - 17:30,17:00,17:30,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:30
Arrivals Takeover: Baalti,Saturday,Wishing Well,42,20,17:00 - 17:45,17:00,17:45,29/06/2024,29/06/2024,29/06/2024 17:00,29/06/2024 17:45
Eloise & Jack,Saturday,Circus Big Top,57,34,17:02 - 17:08,17:02,17:08,29/06/2024,29/06/2024,29/06/2024 17:02,29/06/2024 17:08
Imogen Stirling,Saturday,Poetry&Words,0,0,17:04 - 17:29,17:04,17:29,29/06/2024,29/06/2024,29/06/2024 17:04,29/06/2024 17:29
Venus,Saturday,The Pavement,0,0,17:05 - 17:35,17:05,17:35,29/06/2024,29/06/2024,29/06/2024 17:05,29/06/2024 17:35
Fraser Hooper,Saturday,Outside Circus Stage,59,33,17:06 - 17:36,17:06,17:36,29/06/2024,29/06/2024,29/06/2024 17:06,29/06/2024 17:36
Flyte,Saturday,Avalon Stage,66,38,17:10 - 18:10,17:10,18:10,29/06/2024,29/06/2024,29/06/2024 17:10,29/06/2024 18:10
Stephen Frost Impro Allstars,Saturday,The Astrolabe Theatre,0,0,17:10 - 18:10,17:10,18:10,29/06/2024,29/06/2024,29/06/2024 17:10,29/06/2024 18:10
Jack Thomson,Saturday,Walkabouts,60,33,17:10 - 17:55,17:10,17:55,29/06/2024,29/06/2024,29/06/2024 17:10,29/06/2024 17:55
Rose Popay & Sidekick Saffy,Saturday,Walkabouts,60,33,17:10 - 17:55,17:10,17:55,29/06/2024,29/06/2024,29/06/2024 17:10,29/06/2024 17:55
Steve Rawlings,Saturday,Circus Big Top,57,34,17:13 - 17:33,17:13,17:33,29/06/2024,29/06/2024,29/06/2024 17:13,29/06/2024 17:33
Tony And Ray,Saturday,A Little More Sensation,0,0,17:15 - 17:30,17:15,17:30,29/06/2024,29/06/2024,29/06/2024 17:15,29/06/2024 17:30
Music: Vagz,Saturday,Atchin Tan,0,0,17:15 - 17:45,17:15,17:45,29/06/2024,29/06/2024,29/06/2024 17:15,29/06/2024 17:45
Jayahadadream,Saturday,Greenpeace,55,26,17:15 - 18:00,17:15,18:00,29/06/2024,29/06/2024,29/06/2024 17:15,29/06/2024 18:00
Ceildh With Kevin Campbell Davidson,Saturday,Humblewell Active Platform,42,21,17:15 - 18:15,17:15,18:15,29/06/2024,29/06/2024,29/06/2024 17:15,29/06/2024 18:15
Bloc Party,Saturday,Other Stage,47,34,17:15 - 18:15,17:15,18:15,29/06/2024,29/06/2024,29/06/2024 17:15,29/06/2024 18:15
Furiosa: A Mad Max Saga 15,Saturday,Pilton Palais Cinema,64,36,17:15 - 19:45,17:15,19:45,29/06/2024,29/06/2024,29/06/2024 17:15,29/06/2024 19:45
Jack Valero,Saturday,The Hive,0,0,17:15 - 18:00,17:15,18:00,29/06/2024,29/06/2024,29/06/2024 17:15,29/06/2024 18:00
Liver Cottage,Saturday,Walkabouts,60,33,17:15 - 18:00,17:15,18:00,29/06/2024,29/06/2024,29/06/2024 17:15,29/06/2024 18:00
The Fairy Godmother And The Tooth Fairy,Saturday,Walkabouts,60,33,17:15 - 18:00,17:15,18:00,29/06/2024,29/06/2024,29/06/2024 17:15,29/06/2024 18:00
Kerry Godliman,Saturday,Cabaret,62,26,17:20 - 17:50,17:20,17:50,29/06/2024,29/06/2024,29/06/2024 17:20,29/06/2024 17:50
Nubiyan Twist,Saturday,Glade,51,29,17:20 - 18:30,17:20,18:30,29/06/2024,29/06/2024,29/06/2024 17:20,29/06/2024 18:30
Blockbuster Factory,Saturday,The Glebe,60,33,17:20 - 18:15,17:20,18:15,29/06/2024,29/06/2024,29/06/2024 17:20,29/06/2024 18:15
Hairy Hatter,Saturday,Walkabouts,60,33,17:20 - 18:05,17:20,18:05,29/06/2024,29/06/2024,29/06/2024 17:20,29/06/2024 18:05
Beatbox Collective,Saturday,10 Aces,0,0,17:30 - 18:00,17:30,18:00,29/06/2024,29/06/2024,29/06/2024 17:30,29/06/2024 18:00
Lizzie Esau,Saturday,Bbc Music Introducing,45,44,17:30 - 18:00,17:30,18:00,29/06/2024,29/06/2024,29/06/2024 17:30,29/06/2024 18:00
Suntou Susso,Saturday,Croissant Neuf Bandstand,55,21,17:30 - 18:15,17:30,18:15,29/06/2024,29/06/2024,29/06/2024 17:30,29/06/2024 18:15
Lord Apex,Saturday,Lonely Hearts Club,44,41,17:30 - 18:15,17:30,18:15,29/06/2024,29/06/2024,29/06/2024 17:30,29/06/2024 18:15
Dar Disku,Saturday,San Remo,45,47,17:30 - 19:00,17:30,19:00,29/06/2024,29/06/2024,29/06/2024 17:30,29/06/2024 19:00
Loopdeeloop Sos Takeover,Saturday,The Bug,41,25,17:30 - 18:00,17:30,18:00,29/06/2024,29/06/2024,29/06/2024 17:30,29/06/2024 18:00
Meanderthals,Saturday,Walkabouts,60,33,17:30 - 18:15,17:30,18:15,29/06/2024,29/06/2024,29/06/2024 17:30,29/06/2024 18:15
Nitin Sawhney,Saturday,West Holts Stage,57,31,17:30 - 18:30,17:30,18:30,29/06/2024,29/06/2024,29/06/2024 17:30,29/06/2024 18:30
Otamere Guobadia,Saturday,Poetry&Words,0,0,17:32 - 17:57,17:32,17:57,29/06/2024,29/06/2024,29/06/2024 17:32,29/06/2024 17:57
Dan The Hat,Saturday,A Little More Sensation,0,0,17:35 - 18:05,17:35,18:05,29/06/2024,29/06/2024,29/06/2024 17:35,29/06/2024 18:05
Calum Bowie,Saturday,Left Field,52,33,17:35 - 18:10,17:35,18:10,29/06/2024,29/06/2024,29/06/2024 17:35,29/06/2024 18:10
Molly Whitehouse,Saturday,Circus Big Top,57,34,17:38 - 17:44,17:38,17:44,29/06/2024,29/06/2024,29/06/2024 17:38,29/06/2024 17:44
Magnificent Kevens,Saturday,The Gateway,0,0,17:40 - 18:10,17:40,18:10,29/06/2024,29/06/2024,29/06/2024 17:40,29/06/2024 18:10
Akira,Saturday,The Pavement,0,0,17:40 - 18:10,17:40,18:10,29/06/2024,29/06/2024,29/06/2024 17:40,29/06/2024 18:10
Cirk Hes Presents Rosenwyn,Saturday,Outside Circus Stage,59,33,17:41 - 17:53,17:41,17:53,29/06/2024,29/06/2024,29/06/2024 17:41,29/06/2024 17:53
Michael Kiwanuka,Saturday,Pyramid Stage,51,43,17:45 - 18:45,17:45,18:45,29/06/2024,29/06/2024,29/06/2024 17:45,29/06/2024 18:45
Old Time Sailors,Saturday,Sensation Seekers Stage,0,0,17:45 - 18:45,17:45,18:45,29/06/2024,29/06/2024,29/06/2024 17:45,29/06/2024 18:45
The Wardens,Saturday,Walkabouts,60,33,17:45 - 18:15,17:45,18:15,29/06/2024,29/06/2024,29/06/2024 17:45,29/06/2024 18:15
Laura London & Jake Francis,Saturday,Walkabouts,60,33,17:45 - 18:30,17:45,18:30,29/06/2024,29/06/2024,29/06/2024 17:45,29/06/2024 18:30
Arrivals Takeover: Pia Collada (Dj Set),Saturday,Wishing Well,42,20,17:45 - 18:15,17:45,18:15,29/06/2024,29/06/2024,29/06/2024 17:45,29/06/2024 18:15
The Black Eagles,Saturday,Circus Big Top,57,34,17:49 - 18:14,17:49,18:14,29/06/2024,29/06/2024,29/06/2024 17:49,29/06/2024 18:14
Andy And The Odd Socks,Saturday,Kidzfield Big Top,0,0,17:50 - 18:25,17:50,18:25,29/06/2024,29/06/2024,29/06/2024 17:50,29/06/2024 18:25
Mary Bourke,Saturday,Cabaret,62,26,17:55 - 18:25,17:55,18:25,29/06/2024,29/06/2024,29/06/2024 17:55,29/06/2024 18:25
The Space Cowboy,Saturday,Outside Circus Stage,59,33,17:58 - 18:28,17:58,18:28,29/06/2024,29/06/2024,29/06/2024 17:58,29/06/2024 18:28
Haai B2B Saoirse [Bodymovements Takeover],Saturday,Assembly,40,42,18:00 - 20:00,18:00,20:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 20:00
Rishi,Saturday,Babylon Uprising,0,0,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Martin Furey,Saturday,Blind Tiger,0,0,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Olivia Nelson,Saturday,Bread And Roses,0,0,18:00 - 18:40,18:00,18:40,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 18:40
King Killership Honkey Tonk Piano & A Little Rocknroll Singalong,Saturday,Cornish Arms,0,0,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Zawose Queens,Saturday,Croissant Neuf,55,21,18:00 - 17:00,18:00,17:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 17:00
Mama Tokus,Saturday,Crooner'S Corner,0,0,18:00 - 18:45,18:00,18:45,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 18:45
Think Tonk [Hold Tight Records Takeover],Saturday,Firmly Rooted,43,43,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Sixsixsixties,Saturday,Genosys,0,0,18:00 - 19:30,18:00,19:30,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:30
Melody,Saturday,Glade Dome,49,29,18:00 - 19:30,18:00,19:30,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:30
Dance Class: Reggaeton,Saturday,Glasto Latino,58,27,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Artificial Intelligence Wtf? (Q&A With Eric Drass),Saturday,Laboratory Stage,0,0,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Eats Everything B2B Groove Armada,Saturday,Levels,42,44,18:00 - 19:30,18:00,19:30,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:30
Tba,Saturday,Mandala Stage,0,0,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Iona Lee,Saturday,Poetry&Words,0,0,18:00 - 18:25,18:00,18:25,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 18:25
"Media And Climate Science - Justin Rowlatt, Kevin Anderson, Richard Betts, Roger Harrabin,",Saturday,Speakers Forum,0,0,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Zoe Devlin Love,Saturday,Strummerville,48,12,18:00 - 18:40,18:00,18:40,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 18:40
Dan Shake Sos Takeover,Saturday,The Bug,41,25,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Lankum,Saturday,The Park Stage,41,19,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Tba,Saturday,Woodsies,43,52,18:00 - 19:00,18:00,19:00,29/06/2024,29/06/2024,29/06/2024 18:00,29/06/2024 19:00
Close,Saturday,A Little More Sensation,0,0,18:10 - 23:30,18:10,23:30,29/06/2024,29/06/2024,29/06/2024 18:10,29/06/2024 23:30
Beyond Repair Dance,Saturday,The Astrolabe Theatre,0,0,18:10 - 18:40,18:10,18:40,29/06/2024,29/06/2024,29/06/2024 18:10,29/06/2024 18:40
Cabaret: Wife Material,Saturday,Scissors,42,21,18:15 - 19:00,18:15,19:00,29/06/2024,29/06/2024,29/06/2024 18:15,29/06/2024 19:00
Kirszenbaum,Saturday,The Bandstand,56,38,18:15 - 19:00,18:15,19:00,29/06/2024,29/06/2024,29/06/2024 18:15,29/06/2024 19:00
Arrivals Takeover: Bhangra All Stars,Saturday,Wishing Well,42,20,18:15 - 19:00,18:15,19:00,29/06/2024,29/06/2024,29/06/2024 18:15,29/06/2024 19:00
Charlie Bicknell - Supersonic Woman,Saturday,Circus Big Top,57,34,18:19 - 18:31,18:19,18:31,29/06/2024,29/06/2024,29/06/2024 18:19,29/06/2024 18:31
Close,Saturday,The Glebe,60,33,18:20 - 18:50,18:20,18:50,29/06/2024,29/06/2024,29/06/2024 18:20,29/06/2024 18:50
Imperial Wax,Saturday,The Hive,0,0,18:20 - 19:05,18:20,19:05,29/06/2024,29/06/2024,29/06/2024 18:20,29/06/2024 19:05
Degna Stone,Saturday,Poetry&Words,0,0,18:28 - 18:58,18:28,18:58,29/06/2024,29/06/2024,29/06/2024 18:28,29/06/2024 18:58
Russell Crowe'S Indoor Garden Party,Saturday,Acoustic Stage,66,38,18:30 - 19:30,18:30,19:30,29/06/2024,29/06/2024,29/06/2024 18:30,29/06/2024 19:30
Jonny Awsum,Saturday,Cabaret,62,26,18:30 - 18:50,18:30,18:50,29/06/2024,29/06/2024,29/06/2024 18:30,29/06/2024 18:50
Myles Smith,Saturday,Greenpeace,55,26,18:30 - 19:30,18:30,19:30,29/06/2024,29/06/2024,29/06/2024 18:30,29/06/2024 19:30
Casisdead,Saturday,Lonely Hearts Club,44,41,18:30 - 19:15,18:30,19:15,29/06/2024,29/06/2024,29/06/2024 18:30,29/06/2024 19:15
Dungeon Meat,Saturday,Nyc Downlow,0,0,18:30 - 20:00,18:30,20:00,29/06/2024,29/06/2024,29/06/2024 18:30,29/06/2024 20:00
Lekiddo Lord Of The Lobsters,Saturday,The Gateway,0,0,18:30 - 19:15,18:30,19:15,29/06/2024,29/06/2024,29/06/2024 18:30,29/06/2024 19:15
Guy Williams,Saturday,The Meatrack,0,0,18:30 - 22:00,18:30,22:00,29/06/2024,29/06/2024,29/06/2024 18:30,29/06/2024 22:00
Matt Owens (Noah & The Whale),Saturday,Toad Hall,0,0,18:30 - 19:15,18:30,19:15,29/06/2024,29/06/2024,29/06/2024 18:30,29/06/2024 19:15
Louvre On Th Move,Saturday,Walkabouts,60,33,18:30 - 19:00,18:30,19:00,29/06/2024,29/06/2024,29/06/2024 18:30,29/06/2024 19:00
Georgie Boyd,Saturday,West Holts Bar,59,29,18:30 - 19:00,18:30,19:00,29/06/2024,29/06/2024,29/06/2024 18:30,29/06/2024 19:00
Incandescence Presents Trio Jolee,Saturday,Outside Circus Stage,59,33,18:33 - 18:41,18:33,18:41,29/06/2024,29/06/2024,29/06/2024 18:33,29/06/2024 18:41
Bc Camplight,Saturday,Avalon Stage,66,38,18:40 - 19:40,18:40,19:40,29/06/2024,29/06/2024,29/06/2024 18:40,29/06/2024 19:40
Louis Dunford,Saturday,Left Field,52,33,18:40 - 19:20,18:40,19:20,29/06/2024,29/06/2024,29/06/2024 18:40,29/06/2024 19:20
Circus Funtasia,Saturday,Circus Big Top,57,34,18:41 - 19:51,18:41,19:51,29/06/2024,29/06/2024,29/06/2024 18:41,29/06/2024 19:51
Compere: Bunny Morethan,Saturday,Circus Big Top,57,34,18:45 - 01:45,18:45,01:45,29/06/2024,30/06/2024,29/06/2024 18:45,30/06/2024 01:45
Dan Shake,Saturday,Glade,51,29,18:45 - 19:45,18:45,19:45,29/06/2024,29/06/2024,29/06/2024 18:45,29/06/2024 19:45
Camila Cabello,Saturday,Other Stage,47,34,18:45 - 19:45,18:45,19:45,29/06/2024,29/06/2024,29/06/2024 18:45,29/06/2024 19:45
Close,Saturday,Sensation Seekers Stage,0,0,18:45 - 21:45,18:45,21:45,29/06/2024,29/06/2024,29/06/2024 18:45,29/06/2024 21:45
An Evening Without Kate Bush,Saturday,The Astrolabe Theatre,0,0,18:45 - 19:55,18:45,19:55,29/06/2024,29/06/2024,29/06/2024 18:45,29/06/2024 19:55
Jon Udry,Saturday,Outside Circus Stage,59,33,18:46 - 19:16,18:46,19:16,29/06/2024,29/06/2024,29/06/2024 18:46,29/06/2024 19:16
Luke Wright,Saturday,Cabaret,62,26,18:55 - 19:25,18:55,19:25,29/06/2024,29/06/2024,29/06/2024 18:55,29/06/2024 19:25
Guns Of Navarone,Saturday,The Glebe,60,33,18:55 - 19:25,18:55,19:25,29/06/2024,29/06/2024,29/06/2024 18:55,29/06/2024 19:25
In Dub We Trust,Saturday,Babylon Uprising,0,0,19:00 - 20:00,19:00,20:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 20:00
1Xtra Pre-Party Takeover With Dj Target,Saturday,Bbc Music Introducing,45,44,19:00 - 21:00,19:00,21:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 21:00
Fftp,Saturday,Blind Tiger,0,0,19:00 - 20:00,19:00,20:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 20:00
Airsine,Saturday,Cornish Arms,0,0,19:00 - 21:00,19:00,21:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 21:00
Mad Dog Mcrea,Saturday,Croissant Neuf Bandstand,55,21,19:00 - 20:00,19:00,20:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 20:00
"Hold Tight Records Ft Jman, Who Knew & Pab Mc",Saturday,Firmly Rooted,43,43,19:00 - 20:00,19:00,20:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 20:00
Jam Session,Saturday,Lunched Out Lizards,0,0,19:00 - 20:00,19:00,20:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 20:00
Bedfactory Records,Saturday,Meeting Place Bar,0,0,19:00 - 21:00,19:00,21:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 21:00
Alexander Nut,Saturday,San Remo,45,47,19:00 - 20:30,19:00,20:30,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 20:30
"Gutterfunk: Back At It W/ Dj Die, Randall, Dismantle, Addison Groove + Inja",Saturday,Stonebridge Bar,42,18,19:00 - 21:00,19:00,21:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 21:00
Just Like Honey,Saturday,Strummerville,48,12,19:00 - 19:40,19:00,19:40,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 19:40
Sim0Ne Sos Takeover,Saturday,The Bug,41,25,19:00 - 20:00,19:00,20:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 20:00
Mae Challis Live!,Saturday,The Taphouse,0,0,19:00 - 21:00,19:00,21:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 21:00
Black Pumas,Saturday,West Holts Stage,57,31,19:00 - 20:00,19:00,20:00,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 20:00
Grace (The Soulstice Collective) (Dj Set),Saturday,Wishing Well,42,20,19:00 - 20:30,19:00,20:30,29/06/2024,29/06/2024,29/06/2024 19:00,29/06/2024 20:30
Sam Danson 'Bi-Topia',Saturday,Poetry&Words,0,0,19:10 - 20:00,19:10,20:00,29/06/2024,29/06/2024,29/06/2024 19:10,29/06/2024 20:00
Poetry: Talitha Wing,Saturday,Scissors,42,21,19:15 - 19:30,19:15,19:30,29/06/2024,29/06/2024,29/06/2024 19:15,29/06/2024 19:30
Duo Santus,Saturday,Outside Circus Stage,59,33,19:21 - 19:28,19:21,19:28,29/06/2024,29/06/2024,29/06/2024 19:21,29/06/2024 19:28
The Petebox,Saturday,The Hive,0,0,19:25 - 20:10,19:25,20:10,29/06/2024,29/06/2024,29/06/2024 19:25,29/06/2024 20:10
Mike Garry,Saturday,Cabaret,62,26,19:30 - 20:00,19:30,20:00,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 20:00
Niks,Saturday,Genosys,0,0,19:30 - 21:00,19:30,21:00,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 21:00
Just Jam,Saturday,Glade Dome,49,29,19:30 - 21:00,19:30,21:00,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 21:00
Abbie Mccarthy (Dj Set),Saturday,Greenpeace,55,26,19:30 - 20:30,19:30,20:30,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 20:30
Alisha B2B Archie Hamilton,Saturday,Levels,42,44,19:30 - 21:00,19:30,21:00,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 21:00
Emz,Saturday,Lonely Hearts Club,44,41,19:30 - 20:00,19:30,20:00,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 20:00
Grant Showbiz,Saturday,Mandala Stage,0,0,19:30 - 20:30,19:30,20:30,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 20:30
Poetry: Rj Hunter,Saturday,Scissors,42,21,19:30 - 19:45,19:30,19:45,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 19:45
Ushti Baba,Saturday,The Bandstand,56,38,19:30 - 20:30,19:30,20:30,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 20:30
The Breeders,Saturday,The Park Stage,41,19,19:30 - 20:30,19:30,20:30,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 20:30
Yard Act,Saturday,Woodsies,43,52,19:30 - 20:30,19:30,20:30,29/06/2024,29/06/2024,29/06/2024 19:30,29/06/2024 20:30
Cirk Hes Presents Charlotte & Nadine,Saturday,Outside Circus Stage,59,33,19:33 - 19:43,19:33,19:43,29/06/2024,29/06/2024,29/06/2024 19:33,29/06/2024 19:43
Mellowmatic,Saturday,The Gateway,0,0,19:35 - 20:20,19:35,20:20,29/06/2024,29/06/2024,29/06/2024 19:35,29/06/2024 20:20
Jamz Supernova B2B Yung Singh,Saturday,Glade,51,29,19:45 - 21:15,19:45,21:15,29/06/2024,29/06/2024,29/06/2024 19:45,29/06/2024 21:15
Eno + Q&A With Director Gary Hustwit,Saturday,Pilton Palais Cinema,64,36,19:45 - 21:55,19:45,21:55,29/06/2024,29/06/2024,29/06/2024 19:45,29/06/2024 21:55
Little Simz,Saturday,Pyramid Stage,51,43,19:45 - 20:45,19:45,20:45,29/06/2024,29/06/2024,29/06/2024 19:45,29/06/2024 20:45
Kathryn Roberts & Sean Lakeman,Saturday,Toad Hall,0,0,19:45 - 20:30,19:45,20:30,29/06/2024,29/06/2024,29/06/2024 19:45,29/06/2024 20:30
New York Brass Band,Saturday,Outside Circus Stage,59,33,19:48 - 20:33,19:48,20:33,29/06/2024,29/06/2024,29/06/2024 19:48,29/06/2024 20:33
English Teacher,Saturday,Left Field,52,33,19:50 - 20:30,19:50,20:30,29/06/2024,29/06/2024,29/06/2024 19:50,29/06/2024 20:30
Closedown,Saturday,The Astrolabe Theatre,0,0,19:55 - 00:00,19:55,00:00,29/06/2024,30/06/2024,29/06/2024 19:55,30/06/2024 00:00
Circ Hes - Group Aerial,Saturday,Circus Big Top,57,34,19:56 - 20:08,19:56,20:08,29/06/2024,29/06/2024,29/06/2024 19:56,29/06/2024 20:08
Ralph Mctell,Saturday,Acoustic Stage,66,38,20:00 - 21:00,20:00,21:00,29/06/2024,29/06/2024,29/06/2024 20:00,29/06/2024 21:00
Amaliah B2B Danielle,Saturday,Assembly,40,42,20:00 - 22:00,20:00,22:00,29/06/2024,29/06/2024,29/06/2024 20:00,29/06/2024 22:00
Fliss Mayo,Saturday,Babylon Uprising,0,0,20:00 - 21:00,20:00,21:00,29/06/2024,29/06/2024,29/06/2024 20:00,29/06/2024 21:00
Silva Snipa B2B Chinese Daughter,Saturday,Blind Tiger,0,0,20:00 - 21:00,20:00,21:00,29/06/2024,29/06/2024,29/06/2024 20:00,29/06/2024 21:00
Compère: Alexandra Haddow,Saturday,Cabaret,62,26,20:00 - 00:00,20:00,00:00,29/06/2024,30/06/2024,29/06/2024 20:00,30/06/2024 00:00
Sis:Dem [Hold Tight Records Takeover],Saturday,Firmly Rooted,43,43,20:00 - 22:00,20:00,22:00,29/06/2024,29/06/2024,29/06/2024 20:00,29/06/2024 22:00
Disco And Cinema,Saturday,Humblewell Active Platform,42,21,20:00 - 01:00,20:00,01:00,29/06/2024,30/06/2024,29/06/2024 20:00,30/06/2024 01:00
A- Future,Saturday,Iicon,66,21,20:00 - 22:15,20:00,22:15,29/06/2024,29/06/2024,29/06/2024 20:00,29/06/2024 22:15
Scarsdale Fats,Saturday,Strummerville,48,12,20:00 - 20:40,20:00,20:40,29/06/2024,29/06/2024,29/06/2024 20:00,29/06/2024 20:40
"Notting Hill Carnival Presents: Gaz'S Rockin' Blues, Chris Peckings, Likkle Minty, David Hill, Mr Fix It",Saturday,Terminal 1,0,0,20:00 - 03:00,20:00,03:00,29/06/2024,30/06/2024,29/06/2024 20:00,30/06/2024 03:00
Dj Boring Sos Takeover,Saturday,The Bug,41,25,20:00 - 21:00,20:00,21:00,29/06/2024,29/06/2024,29/06/2024 20:00,29/06/2024 21:00
Noah And The Loners,Saturday,West Holts Bar,59,29,20:00 - 20:30,20:00,20:30,29/06/2024,29/06/2024,29/06/2024 20:00,29/06/2024 20:30
Dr. John Cooper Clarke,Saturday,Cabaret,62,26,20:05 - 21:00,20:05,21:00,29/06/2024,29/06/2024,29/06/2024 20:05,29/06/2024 21:00
Shaznay Lewis,Saturday,Avalon Stage,66,38,20:10 - 21:10,20:10,21:10,29/06/2024,29/06/2024,29/06/2024 20:10,29/06/2024 21:10
The Space Cowboy,Saturday,Circus Big Top,57,34,20:13 - 20:38,20:13,20:38,29/06/2024,29/06/2024,29/06/2024 20:13,29/06/2024 20:38
"20 Yrs Of Shogun Ft Monrroe, Pola & Bryson, Jaevon, Emiliy Makis, Duskee",Saturday,Lonely Hearts Club,44,41,20:15 - 22:15,20:15,22:15,29/06/2024,29/06/2024,29/06/2024 20:15,29/06/2024 22:15
Kitty Stewart,Saturday,Croissant Neuf Bandstand,55,21,20:30 - 21:15,20:30,21:15,29/06/2024,29/06/2024,29/06/2024 20:30,29/06/2024 21:15
Fleetmac Wood,Saturday,Greenpeace,55,26,20:30 - 22:00,20:30,22:00,29/06/2024,29/06/2024,29/06/2024 20:30,29/06/2024 22:00
The Streets,Saturday,Other Stage,47,34,20:30 - 21:30,20:30,21:30,29/06/2024,29/06/2024,29/06/2024 20:30,29/06/2024 21:30
Tarzsa,Saturday,San Remo,45,47,20:30 - 22:00,20:30,22:00,29/06/2024,29/06/2024,29/06/2024 20:30,29/06/2024 22:00
Shade Uk,Saturday,The Hive,0,0,20:30 - 21:15,20:30,21:15,29/06/2024,29/06/2024,29/06/2024 20:30,29/06/2024 21:15
Masego,Saturday,West Holts Stage,57,31,20:30 - 21:30,20:30,21:30,29/06/2024,29/06/2024,29/06/2024 20:30,29/06/2024 21:30
Sabiyha,Saturday,Wishing Well,42,20,20:30 - 21:15,20:30,21:15,29/06/2024,29/06/2024,29/06/2024 20:30,29/06/2024 21:15
Close,Saturday,Outside Circus Stage,59,33,20:33 - 23:35,20:33,23:35,29/06/2024,29/06/2024,29/06/2024 20:33,29/06/2024 23:35
Eloise & Jack,Saturday,Circus Big Top,57,34,20:43 - 20:49,20:43,20:49,29/06/2024,29/06/2024,29/06/2024 20:43,29/06/2024 20:49
The Birds,Saturday,Walkabouts,60,33,20:50 - 21:35,20:50,21:35,29/06/2024,29/06/2024,29/06/2024 20:50,29/06/2024 21:35
Cirk Hes Presents Edith,Saturday,Circus Big Top,57,34,20:54 - 21:00,20:54,21:00,29/06/2024,29/06/2024,29/06/2024 20:54,29/06/2024 21:00
Sarah Story,Saturday,Arcadia,41,25,21:00 - 21:45,21:00,21:45,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 21:45
Dr Dubplate,Saturday,Babylon Uprising,0,0,21:00 - 22:00,21:00,22:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:00
Bish 90S Dance Set,Saturday,Blind Tiger,0,0,21:00 - 22:00,21:00,22:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:00
Fulu Miziki & Notting Hill Carnival,Saturday,Carhenge,58,36,21:00 - 22:00,21:00,22:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:00
Boogaloo Dee (Blendid Takeover),Saturday,Cornish Arms,0,0,21:00 - 22:00,21:00,22:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:00
Garrett David (Live),Saturday,Genosys,0,0,21:00 - 22:00,21:00,22:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:00
Margaret Dygas,Saturday,Glade Dome,49,29,21:00 - 22:30,21:00,22:30,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:30
Billy Nomates,Saturday,Left Field,52,33,21:00 - 22:00,21:00,22:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:00
Carlita,Saturday,Levels,42,44,21:00 - 22:30,21:00,22:30,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:30
Alma Twist,Saturday,Lunched Out Lizards,0,0,21:00 - 22:00,21:00,22:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:00
Jon Xvm,Saturday,Meeting Place Bar,0,0,21:00 - 23:00,21:00,23:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 23:00
Jpeg,Saturday,Platform 23,0,0,21:00 - 23:00,21:00,23:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 23:00
Twisted Time Machine X Femm Again,Saturday,Scissors,42,21,21:00 - 23:15,21:00,23:15,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 23:15
Lau.Ra + Carl (The Social),Saturday,Stonebridge Bar,42,18,21:00 - 22:00,21:00,22:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:00
Fat White Family (Acoustic),Saturday,Strummerville,48,12,21:00 - 21:45,21:00,21:45,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 21:45
The Beatbox Collective,Saturday,The Bandstand,56,38,21:00 - 22:00,21:00,22:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:00
Rum Shack Wild Card,Saturday,The Rum Shack,0,0,21:00 - 22:45,21:00,22:45,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:45
Marc Miller,Saturday,The Taphouse,0,0,21:00 - 23:00,21:00,23:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 23:00
Steve Knightley,Saturday,Toad Hall,0,0,21:00 - 21:45,21:00,21:45,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 21:45
The Runaway Christmas Tree Fairy,Saturday,Walkabouts,60,33,21:00 - 21:45,21:00,21:45,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 21:45
Sleaford Mods,Saturday,Woodsies,43,52,21:00 - 22:00,21:00,22:00,29/06/2024,29/06/2024,29/06/2024 21:00,29/06/2024 22:00
Talal Karkouti - Songs With His Guitar,Saturday,Cabaret,62,26,21:05 - 21:35,21:05,21:35,29/06/2024,29/06/2024,29/06/2024 21:05,29/06/2024 21:35
Duo Santus,Saturday,Circus Big Top,57,34,21:05 - 21:11,21:05,21:11,29/06/2024,29/06/2024,29/06/2024 21:05,29/06/2024 21:11
Ltj Bukem With Mc Lowqui,Saturday,Glade,51,29,21:15 - 22:30,21:15,22:30,29/06/2024,29/06/2024,29/06/2024 21:15,29/06/2024 22:30
Orbital,Saturday,The Park Stage,41,19,21:15 - 22:15,21:15,22:15,29/06/2024,29/06/2024,29/06/2024 21:15,29/06/2024 22:15
Music To Make Your Ears Smile With Spikey (Dj Set),Saturday,Wishing Well,42,20,21:15 - 22:30,21:15,22:30,29/06/2024,29/06/2024,29/06/2024 21:15,29/06/2024 22:30
Leo,Saturday,Circus Big Top,57,34,21:16 - 21:22,21:16,21:22,29/06/2024,29/06/2024,29/06/2024 21:16,29/06/2024 21:22
Stay Hungry,Saturday,The Hive,0,0,21:20 - 22:20,21:20,22:20,29/06/2024,29/06/2024,29/06/2024 21:20,29/06/2024 22:20
Molly Whitehouse,Saturday,Circus Big Top,57,34,21:27 - 21:33,21:27,21:33,29/06/2024,29/06/2024,29/06/2024 21:27,29/06/2024 21:33
Ocean Colour Scene,Saturday,Acoustic Stage,66,38,21:30 - 22:45,21:30,22:45,29/06/2024,29/06/2024,29/06/2024 21:30,29/06/2024 22:45
Shemanic Dj,Saturday,Croissant Neuf Bandstand,55,21,21:30 - 22:45,21:30,22:45,29/06/2024,29/06/2024,29/06/2024 21:30,29/06/2024 22:45
Guest Dj,Saturday,Deluxe Diner,64,17,21:30 - 22:30,21:30,22:30,29/06/2024,29/06/2024,29/06/2024 21:30,29/06/2024 22:30
Little Miss Dj,Saturday,Mandala Stage,0,0,21:30 - 23:00,21:30,23:00,29/06/2024,29/06/2024,29/06/2024 21:30,29/06/2024 23:00
Pony Montana,Saturday,Peace Stage,0,0,21:30 - 22:30,21:30,22:30,29/06/2024,29/06/2024,29/06/2024 21:30,29/06/2024 22:30
The Cloudmen,Saturday,Walkabouts,60,33,21:30 - 22:30,21:30,22:30,29/06/2024,29/06/2024,29/06/2024 21:30,29/06/2024 22:30
Enjoyable Listens,Saturday,West Holts Bar,59,29,21:30 - 22:15,21:30,22:15,29/06/2024,29/06/2024,29/06/2024 21:30,29/06/2024 22:15
Jon Udry,Saturday,Circus Big Top,57,34,21:38 - 22:03,21:38,22:03,29/06/2024,29/06/2024,29/06/2024 21:38,29/06/2024 22:03
The Magic Numbers,Saturday,Avalon Stage,66,38,21:40 - 22:40,21:40,22:40,29/06/2024,29/06/2024,29/06/2024 21:40,29/06/2024 22:40
Luisa Omielan,Saturday,Cabaret,62,26,21:40 - 22:10,21:40,22:10,29/06/2024,29/06/2024,29/06/2024 21:40,29/06/2024 22:10
Shygirl Presents Club Shy,Saturday,Arcadia,41,25,21:45 - 22:30,21:45,22:30,29/06/2024,29/06/2024,29/06/2024 21:45,29/06/2024 22:30
Coldplay,Saturday,Pyramid Stage,51,43,21:45 - 23:45,21:45,23:45,29/06/2024,29/06/2024,29/06/2024 21:45,29/06/2024 23:45
Mad Apple Circus,Saturday,Sensation Seekers Stage,0,0,21:45 - 22:30,21:45,22:30,29/06/2024,29/06/2024,29/06/2024 21:45,29/06/2024 22:30
Mystic Mirror Show Globe,Saturday,Walkabouts,60,33,21:45 - 22:45,21:45,22:45,29/06/2024,29/06/2024,29/06/2024 21:45,29/06/2024 22:45
De Silva,Saturday,Arrivals,0,0,22:00 - 23:00,22:00,23:00,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:00
Unai Trotti,Saturday,Assembly,40,42,22:00 - 23:30,22:00,23:30,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:30
Ssbb: Samurai Breaks B2B Toby Ross,Saturday,Babylon Uprising,0,0,22:00 - 23:00,22:00,23:00,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:00
"10 Years Of Rumble In The Jungle Ft Randall & Carasel, Toby Ross B2B Rise B2B Oram B2B Zimma Ft Joe Burn",Saturday,Blind Tiger,0,0,22:00 - 00:20,22:00,00:20,29/06/2024,30/06/2024,29/06/2024 22:00,30/06/2024 00:20
Elrobo (Blendid Takeover),Saturday,Cornish Arms,0,0,22:00 - 23:00,22:00,23:00,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:00
Bakey Ft Who Knew [Hold Tight Records Takeover],Saturday,Firmly Rooted,43,43,22:00 - 23:00,22:00,23:00,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:00
Melody,Saturday,Flying Bus,0,0,22:00 - 23:00,22:00,23:00,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:00
Syreeta,Saturday,Genosys,0,0,22:00 - 23:30,22:00,23:30,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:30
Erol Alkan,Saturday,Greenpeace,55,26,22:00 - 23:30,22:00,23:30,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:30
Dj Tarloak,Saturday,Lunched Out Lizards,0,0,22:00 - 23:00,22:00,23:00,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:00
Wintz,Saturday,Mez Yard,0,0,22:00 - 23:30,22:00,23:30,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:30
Thempress And Friends,Saturday,Nomad,0,0,22:00 - 00:00,22:00,00:00,29/06/2024,30/06/2024,29/06/2024 22:00,30/06/2024 00:00
Heléna Star,Saturday,Nyc Downlow,0,0,22:00 - 23:20,22:00,23:20,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:20
Leon Vynehall,Saturday,San Remo,45,47,22:00 - 23:30,22:00,23:30,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:30
"Ransom Note W/ Optimo (Espacio) + Ally Tropical, Matt Cowell + Rosie Ama",Saturday,Stonebridge Bar,42,18,22:00 - 00:00,22:00,00:00,29/06/2024,30/06/2024,29/06/2024 22:00,30/06/2024 00:00
Lambrini Girls,Saturday,Strummerville,48,12,22:00 - 22:40,22:00,22:40,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 22:40
Wallace,Saturday,The Meatrack,0,0,22:00 - 00:00,22:00,00:00,29/06/2024,30/06/2024,29/06/2024 22:00,30/06/2024 00:00
Dj Mr Mass,Saturday,The Rocket Lounge,64,16,22:00 - 06:00,22:00,06:00,29/06/2024,30/06/2024,29/06/2024 22:00,30/06/2024 06:00
Dj Double L,Saturday,The Salon Carousel,0,0,22:00 - 23:00,22:00,23:00,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:00
Vxrgo,Saturday,The Sistxrhood,0,0,22:00 - 00:00,22:00,00:00,29/06/2024,30/06/2024,29/06/2024 22:00,30/06/2024 00:00
Unglued Ft. Carasel,Saturday,The Temple,0,0,22:00 - 23:00,22:00,23:00,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 23:00
The Bookshop Band,Saturday,Toad Hall,0,0,22:00 - 22:40,22:00,22:40,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 22:40
Glowbros,Saturday,Walkabouts,60,33,22:00 - 00:00,22:00,00:00,29/06/2024,30/06/2024,29/06/2024 22:00,30/06/2024 00:00
Corvus Angelicus,Saturday,Walkabouts,60,33,22:00 - 22:45,22:00,22:45,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 22:45
High Flyers,Saturday,Walkabouts,60,33,22:00 - 22:45,22:00,22:45,29/06/2024,29/06/2024,29/06/2024 22:00,29/06/2024 22:45
Boom Circus,Saturday,Circus Big Top,57,34,22:08 - 22:53,22:08,22:53,29/06/2024,29/06/2024,29/06/2024 22:08,29/06/2024 22:53
Emmanuel Sonubi,Saturday,Cabaret,62,26,22:15 - 22:45,22:15,22:45,29/06/2024,29/06/2024,29/06/2024 22:15,29/06/2024 22:45
Charisse C,Saturday,Iicon,66,21,22:15 - 00:15,22:15,00:15,29/06/2024,30/06/2024,29/06/2024 22:15,30/06/2024 00:15
Charlotte Plank,Saturday,Lonely Hearts Club,44,41,22:15 - 22:45,22:15,22:45,29/06/2024,29/06/2024,29/06/2024 22:15,29/06/2024 22:45
The Fairy Godmother And The Tooth Fairy,Saturday,Walkabouts,60,33,22:15 - 23:00,22:15,23:00,29/06/2024,29/06/2024,29/06/2024 22:15,29/06/2024 23:00
Jessie Ware,Saturday,West Holts Stage,57,31,22:15 - 23:45,22:15,23:45,29/06/2024,29/06/2024,29/06/2024 22:15,29/06/2024 23:45
Perri Kaye,Saturday,Deluxe Diner,64,17,22:30 - 00:00,22:30,00:00,29/06/2024,30/06/2024,29/06/2024 22:30,30/06/2024 00:00
Laidlaw,Saturday,Glade Dome,49,29,22:30 - 00:00,22:30,00:00,29/06/2024,30/06/2024,29/06/2024 22:30,30/06/2024 00:00
Jamie Jones,Saturday,Levels,42,44,22:30 - 00:00,22:30,00:00,29/06/2024,30/06/2024,29/06/2024 22:30,30/06/2024 00:00
Disclosure,Saturday,Other Stage,47,34,22:30 - 23:45,22:30,23:45,29/06/2024,29/06/2024,29/06/2024 22:30,29/06/2024 23:45
The Bhangra All Stars,Saturday,Peace Stage,0,0,22:30 - 23:30,22:30,23:30,29/06/2024,29/06/2024,29/06/2024 22:30,29/06/2024 23:30
The World Government,Saturday,The Bandstand,56,38,22:30 - 23:30,22:30,23:30,29/06/2024,29/06/2024,29/06/2024 22:30,29/06/2024 23:30
The Birds,Saturday,Walkabouts,60,33,22:30 - 23:15,22:30,23:15,29/06/2024,29/06/2024,29/06/2024 22:30,29/06/2024 23:15
The Ayoub Sisters,Saturday,Wishing Well,42,20,22:30 - 23:00,22:30,23:00,29/06/2024,29/06/2024,29/06/2024 22:30,29/06/2024 23:00
Gossip,Saturday,Woodsies,43,52,22:30 - 23:45,22:30,23:45,29/06/2024,29/06/2024,29/06/2024 22:30,29/06/2024 23:45
Barry Cant Swim,Saturday,Arcadia,41,25,22:35 - 23:35,22:35,23:35,29/06/2024,29/06/2024,29/06/2024 22:35,29/06/2024 23:35
Feeding The Fish,Saturday,Sensation Seekers Stage,0,0,22:40 - 22:50,22:40,22:50,29/06/2024,29/06/2024,29/06/2024 22:40,29/06/2024 22:50
Ri Mistry B2B Rohan Rakhit (Daytimers),Saturday,The Rum Shack,0,0,22:45 - 23:45,22:45,23:45,29/06/2024,29/06/2024,29/06/2024 22:45,29/06/2024 23:45
Frank Sanazi,Saturday,Cabaret,62,26,22:50 - 23:20,22:50,23:20,29/06/2024,29/06/2024,29/06/2024 22:50,29/06/2024 23:20
Mellowmatic,Saturday,The Hive,0,0,22:50 - 23:50,22:50,23:50,29/06/2024,29/06/2024,29/06/2024 22:50,29/06/2024 23:50
Issey Cross,Saturday,Lonely Hearts Club,44,41,22:55 - 23:25,22:55,23:25,29/06/2024,29/06/2024,29/06/2024 22:55,29/06/2024 23:25
Neon Moon - Paradise Circus,Saturday,Sensation Seekers Stage,0,0,22:55 - 23:40,22:55,23:40,29/06/2024,29/06/2024,29/06/2024 22:55,29/06/2024 23:40
Leo,Saturday,Circus Big Top,57,34,22:58 - 23:04,22:58,23:04,29/06/2024,29/06/2024,29/06/2024 22:58,29/06/2024 23:04
Yourboykiran,Saturday,Arrivals,0,0,23:00 - 00:00,23:00,00:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:00
Silva Bumpa,Saturday,Babylon Uprising,0,0,23:00 - 00:00,23:00,00:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:00
Rogue Wave (Blendid Takeover),Saturday,Cornish Arms,0,0,23:00 - 23:30,23:00,23:30,29/06/2024,29/06/2024,29/06/2024 23:00,29/06/2024 23:30
Freetown Collective,Saturday,Croissant Neuf,55,21,23:00 - 00:00,23:00,00:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:00
Minty B2B Sepia [Hold Tight Records Takeover],Saturday,Firmly Rooted,43,43,23:00 - 00:00,23:00,00:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:00
Tristan Da Cunha B2B His Friend,Saturday,Flying Bus,0,0,23:00 - 01:30,23:00,01:30,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 01:30
Goldie Live,Saturday,Glade,51,29,23:00 - 00:00,23:00,00:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:00
Drass,Saturday,Laboratory Stage,0,0,23:00 - 23:55,23:00,23:55,29/06/2024,29/06/2024,29/06/2024 23:00,29/06/2024 23:55
Barefoot Bandit,Saturday,Lunched Out Lizards,0,0,23:00 - 00:00,23:00,00:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:00
D*Lex,Saturday,Meeting Place Bar,0,0,23:00 - 01:00,23:00,01:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 01:00
Coco Em,Saturday,Platform 23,0,0,23:00 - 00:30,23:00,00:30,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:30
Uncle Brian'S Abattoir,Saturday,Strummerville,48,12,23:00 - 23:40,23:00,23:40,29/06/2024,29/06/2024,29/06/2024 23:00,29/06/2024 23:40
Peggy Gou,Saturday,The Park Stage,41,19,23:00 - 00:15,23:00,00:15,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:15
Sister Suzie,Saturday,The Rocket Lounge,64,16,23:00 - 00:00,23:00,00:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:00
Bosslady,Saturday,The Salon Carousel,0,0,23:00 - 00:00,23:00,00:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:00
Jack Osman B2B Danny Vito,Saturday,The Taphouse,0,0,23:00 - 03:00,23:00,03:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 03:00
Artemis Ft. Ruthless,Saturday,The Temple,0,0,23:00 - 00:00,23:00,00:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:00
Giant Egret,Saturday,Walkabouts,60,33,23:00 - 23:45,23:00,23:45,29/06/2024,29/06/2024,29/06/2024 23:00,29/06/2024 23:45
Love Latin Disco (Dj Set),Saturday,Wishing Well,42,20,23:00 - 00:00,23:00,00:00,29/06/2024,30/06/2024,29/06/2024 23:00,30/06/2024 00:00
United Queendom,Saturday,Circus Big Top,57,34,23:09 - 00:09,23:09,00:09,29/06/2024,30/06/2024,29/06/2024 23:09,30/06/2024 00:09
New Model Army,Saturday,Avalon Stage,66,38,23:10 - 00:20,23:10,00:20,29/06/2024,30/06/2024,29/06/2024 23:10,30/06/2024 00:20
Fulu,Saturday,Toad Hall,0,0,23:10 - 00:00,23:10,00:00,29/06/2024,30/06/2024,29/06/2024 23:10,30/06/2024 00:00
Les Ooh La Las,Saturday,Cabaret,62,26,23:25 - 23:30,23:25,23:30,29/06/2024,29/06/2024,29/06/2024 23:25,29/06/2024 23:30
Caravan Of Lost Souls,Saturday,A Little More Sensation,0,0,23:30 - 01:30,23:30,01:30,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 01:30
Chez De Milo B2B Ellie Stokes,Saturday,Assembly,40,42,23:30 - 01:00,23:30,01:00,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 01:00
Basil Brush - Unleashed,Saturday,Cabaret,62,26,23:30 - 00:00,23:30,00:00,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 00:00
Jfb (Blendid Takeover),Saturday,Cornish Arms,0,0,23:30 - 01:30,23:30,01:30,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 01:30
Ok Williams,Saturday,Genosys,0,0,23:30 - 01:00,23:30,01:00,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 01:00
Dj And Dancing,Saturday,Glasto Latino,58,27,23:30 - 00:00,23:30,00:00,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 00:00
Surusinghe,Saturday,Greenpeace,55,26,23:30 - 01:00,23:30,01:00,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 01:00
Wilkinson,Saturday,Lonely Hearts Club,44,41,23:30 - 00:30,23:30,00:30,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 00:30
Sacred Geometry Band,Saturday,Mandala Stage,0,0,23:30 - 00:30,23:30,00:30,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 00:30
Dj Dakilei,Saturday,Mez Yard,0,0,23:30 - 01:00,23:30,01:00,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 01:00
Jeff Mendoza (Soul Summit - Ny),Saturday,Nyc Downlow,0,0,23:30 - 00:55,23:30,00:55,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 00:55
Paree,Saturday,Peace Stage,0,0,23:30 - 00:00,23:30,00:00,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 00:00
Moxie,Saturday,San Remo,45,47,23:30 - 01:00,23:30,01:00,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 01:00
Corvus Angelicus,Saturday,Walkabouts,60,33,23:30 - 00:15,23:30,00:15,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 00:15
High Flyers,Saturday,Walkabouts,60,33,23:30 - 00:15,23:30,00:15,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 00:15
The Runaway Christmas Tree Fairy,Saturday,Walkabouts,60,33,23:30 - 00:15,23:30,00:15,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 00:15
Disco Turtle,Saturday,Walkabouts,60,33,23:30 - 01:00,23:30,01:00,29/06/2024,30/06/2024,29/06/2024 23:30,30/06/2024 01:00
Arcadia And The Wadjuk Noongar - Warraloo Ceremony,Saturday,Arcadia,41,25,23:35 - 23:45,23:35,23:45,29/06/2024,29/06/2024,29/06/2024 23:35,29/06/2024 23:45
Eyes Wide Shut Duo Trapeze,Saturday,Outside Circus Stage,59,33,23:35 - 23:43,23:35,23:43,29/06/2024,29/06/2024,29/06/2024 23:35,29/06/2024 23:43
Joy (Anonymous) B2B Salute,Saturday,Arcadia,41,25,23:45 - 00:45,23:45,00:45,29/06/2024,30/06/2024,29/06/2024 23:45,30/06/2024 00:45
Noah & The Loners,Saturday,Bread And Roses,0,0,23:45 - 00:40,23:45,00:40,29/06/2024,30/06/2024,29/06/2024 23:45,30/06/2024 00:40
Mat Collishaw - Even To The End,Saturday,Tree Stage,44,51,23:45 - 00:00,23:45,00:00,29/06/2024,30/06/2024,29/06/2024 23:45,30/06/2024 00:00
Stacky,Saturday,Village Inn,0,0,23:45 - 02:00,23:45,02:00,29/06/2024,30/06/2024,29/06/2024 23:45,30/06/2024 02:00
She'S Got Brass,Saturday,West Holts Bar,59,29,23:45 - 00:45,23:45,00:45,29/06/2024,30/06/2024,29/06/2024 23:45,30/06/2024 00:45
Fiery Jack Family,Saturday,Outside Circus Stage,59,33,23:48 - 23:58,23:48,23:58,29/06/2024,29/06/2024,29/06/2024 23:48,29/06/2024 23:58
Loominus,Saturday,Sensation Seekers Stage,0,0,23:50 - 00:05,23:50,00:05,29/06/2024,30/06/2024,29/06/2024 23:50,30/06/2024 00:05
Anish Kumar,Sunday,Arrivals,0,0,00:00 - 01:00,00:00,01:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:00
N4 Records & Singularity Bliind Tiger Takeover - Mixtress,Sunday,Blind Tiger,0,0,00:00 - 01:00,00:00,01:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:00
Duckworthsound & Dread [Duckplates Label Takeover],Sunday,Firmly Rooted,43,43,00:00 - 01:15,00:00,01:15,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:15
"25 Years Of Zed Bias And Friends Hosted By Specialist Moss, Chunky & Mc Bic",Sunday,Flying Bus,0,0,00:00 - 04:00,00:00,04:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 04:00
Feline,Sunday,Lunched Out Lizards,0,0,00:00 - 01:30,00:00,01:30,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:30
Dj Ez,Sunday,Nowhere,0,0,00:00 - 01:00,00:00,01:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:00
Tama Sumo & Lakuti,Sunday,Nyc Downlow,0,0,00:00 - 02:00,00:00,02:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 02:00
The Scratch,Sunday,Peace Stage,0,0,00:00 - 01:00,00:00,01:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:00
Darkstepper B2B A.G.,Sunday,Stonebridge Bar,42,18,00:00 - 01:00,00:00,01:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:00
"Strummerville Closing Party Ft Taleggio Nights, Lord Gid",Sunday,Strummerville,48,12,00:00 - 03:00,00:00,03:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 03:00
Mas Que Nada Takeover: Mas Que Nada Bros,Sunday,The Hive,0,0,00:00 - 01:30,00:00,01:30,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:30
Dave Harvey,Sunday,The Meatrack,0,0,00:00 - 01:30,00:00,01:30,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:30
Frank Harvey Trio,Sunday,The Rocket Lounge,64,16,00:00 - 01:00,00:00,01:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:00
Venbee,Sunday,The Rum Shack,0,0,00:00 - 00:45,00:00,00:45,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 00:45
Bish,Sunday,The Salon Carousel,0,0,00:00 - 01:00,00:00,01:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:00
Dj Ammi B2B Ladygrey,Sunday,The Sistxrhood,0,0,00:00 - 02:00,00:00,02:00,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 02:00
Daria Kolosova,Sunday,The Temple,0,0,00:00 - 01:30,00:00,01:30,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 01:30
Rodney Branigan,Sunday,Toad Hall,0,0,00:00 - 00:50,00:00,00:50,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 00:50
Dan Bean,Sunday,Tree Stage,44,51,00:00 - 00:10,00:00,00:10,01/07/2024,01/07/2024,30/06/2024 00:00,01/07/2024 00:10
Area 51,Sunday,Outside Circus Stage,59,33,00:10 - 00:22,00:10,00:22,01/07/2024,01/07/2024,30/06/2024 00:10,01/07/2024 00:22
Bea Brennan,Sunday,Tree Stage,44,51,00:10 - 01:10,00:10,01:10,01/07/2024,01/07/2024,30/06/2024 00:10,01/07/2024 01:10
Loominus,Sunday,Sensation Seekers Stage,0,0,00:25 - 00:40,00:25,00:40,01/07/2024,01/07/2024,30/06/2024 00:25,01/07/2024 00:40
Aerial High Jinks,Sunday,Outside Circus Stage,59,33,00:27 - 00:35,00:27,00:35,01/07/2024,01/07/2024,30/06/2024 00:27,01/07/2024 00:35
Hedex B2B Bou Ft B Live 247 & Eksman,Sunday,Arcadia,41,25,00:30 - 01:30,00:30,01:30,01/07/2024,01/07/2024,30/06/2024 00:30,01/07/2024 01:30
Fülü,Sunday,Croissant Neuf,55,21,00:30 - 01:30,00:30,01:30,01/07/2024,01/07/2024,30/06/2024 00:30,01/07/2024 01:30
Chris Holt,Sunday,Deluxe Diner,64,17,00:30 - 02:00,00:30,02:00,01/07/2024,01/07/2024,30/06/2024 00:30,01/07/2024 02:00
Camelphat,Sunday,Glade,51,29,00:30 - 02:00,00:30,02:00,01/07/2024,01/07/2024,30/06/2024 00:30,01/07/2024 02:00
Enzo Siragusa B2B Traumer [Fuse Takeover],Sunday,Lonely Hearts Club,44,41,00:30 - 02:30,00:30,02:30,01/07/2024,01/07/2024,30/06/2024 00:30,01/07/2024 02:30
Chicha Morada B2B Ru Robinson,Sunday,Mez Yard,0,0,00:30 - 02:00,00:30,02:00,01/07/2024,01/07/2024,30/06/2024 00:30,01/07/2024 02:00
A Girl Walks Home Alone At Night 15,Sunday,Pilton Palais Cinema,64,36,00:30 - 02:35,00:30,02:35,01/07/2024,01/07/2024,30/06/2024 00:30,01/07/2024 02:35
Village Underground Takeover: Moktar B2B Surusinghe,Sunday,Platform 23,0,0,00:30 - 02:00,00:30,02:00,01/07/2024,01/07/2024,30/06/2024 00:30,01/07/2024 02:00
Shanti Celeste B2B Peach,Sunday,San Remo,45,47,00:30 - 02:30,00:30,02:30,01/07/2024,01/07/2024,30/06/2024 00:30,01/07/2024 02:30
Abbie Mccarthy (Dj Set),Sunday,Wishing Well,42,20,00:30 - 01:30,00:30,01:30,01/07/2024,01/07/2024,30/06/2024 00:30,01/07/2024 01:30
Area 51,Sunday,Outside Circus Stage,59,33,00:40 - 00:52,00:40,00:52,01/07/2024,01/07/2024,30/06/2024 00:40,01/07/2024 00:52
Flash Bang Brass,Sunday,Bimble Inn,41,16,00:45 - 02:00,00:45,02:00,01/07/2024,01/07/2024,30/06/2024 00:45,01/07/2024 02:00
Daisy Doris May,Sunday,Scissors,42,21,00:45 - 01:00,00:45,01:00,01/07/2024,01/07/2024,30/06/2024 00:45,01/07/2024 01:00
Doreen Doreen,Sunday,Sensation Seekers Stage,0,0,00:45 - 01:45,00:45,01:45,01/07/2024,01/07/2024,30/06/2024 00:45,01/07/2024 01:45
Raves R Us,Sunday,Outside Circus Stage,59,33,00:57 - 01:42,00:57,01:42,01/07/2024,01/07/2024,30/06/2024 00:57,01/07/2024 01:42
Daytimers,Sunday,Arrivals,0,0,01:00 - 03:00,01:00,03:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 03:00
Dj Stingray 313,Sunday,Assembly,40,42,01:00 - 02:30,01:00,02:30,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:30
N4 Records & Singularity Blind Tiger Takeover - Janaway,Sunday,Blind Tiger,0,0,01:00 - 02:00,01:00,02:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:00
Raymonds Luxury Yacht Rock All-Stars,Sunday,Cornish Arms,0,0,01:00 - 03:00,01:00,03:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 03:00
Dj Tennis B2B Demi Riquísimo,Sunday,Glade Dome,49,29,01:00 - 02:30,01:00,02:30,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:30
Latin Party,Sunday,Glasto Latino,58,27,01:00 - 02:30,01:00,02:30,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:30
Dj Paulette,Sunday,Greenpeace,55,26,01:00 - 02:30,01:00,02:30,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:30
Dr Dubplate B2B Todd Edwards,Sunday,Levels,42,44,01:00 - 02:30,01:00,02:30,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:30
Jon Le Champignon,Sunday,Mandala Stage,0,0,01:00 - 02:00,01:00,02:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:00
Swana Takeover X Nazar Presents: Aran Cherkez,Sunday,Nomad,0,0,01:00 - 02:00,01:00,02:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:00
Conducta,Sunday,Nowhere,0,0,01:00 - 02:00,01:00,02:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:00
Neffa T B2B Oblig,Sunday,Stonebridge Bar,42,18,01:00 - 02:00,01:00,02:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:00
Us,Sunday,The Rocket Lounge,64,16,01:00 - 02:00,01:00,02:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:00
A Guy Called Gerald And The Jungle Drummer,Sunday,The Rum Shack,0,0,01:00 - 02:00,01:00,02:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:00
Skitz And Joe Burn,Sunday,The Salon Carousel,0,0,01:00 - 02:00,01:00,02:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:00
Russell Betts,Sunday,The Taphouse,0,0,01:00 - 02:30,01:00,02:30,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:30
Glowbros,Sunday,Walkabouts,60,33,01:00 - 03:00,01:00,03:00,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 03:00
Freddie And The Freeloaders,Sunday,West Holts Bar,59,29,01:00 - 02:30,01:00,02:30,01/07/2024,01/07/2024,30/06/2024 01:00,01/07/2024 02:30
Dan Bean,Sunday,Tree Stage,44,51,01:10 - 01:20,01:10,01:20,01/07/2024,01/07/2024,30/06/2024 01:10,01/07/2024 01:20
Michele & Romeo Stodart Magic Numbers & Friends,Sunday,Toad Hall,0,0,01:15 - 02:30,01:15,02:30,01/07/2024,01/07/2024,30/06/2024 01:15,01/07/2024 02:30
Konx-Om-Pax,Sunday,Tree Stage,44,51,01:20 - 02:20,01:20,02:20,01/07/2024,01/07/2024,30/06/2024 01:20,01/07/2024 02:20
Andy C Ft Tonn Piper,Sunday,Arcadia,41,25,01:30 - 02:30,01:30,02:30,01/07/2024,01/07/2024,30/06/2024 01:30,01/07/2024 02:30
Ushti Baba,Sunday,Lunched Out Lizards,0,0,01:30 - 02:30,01:30,02:30,01/07/2024,01/07/2024,30/06/2024 01:30,01/07/2024 02:30
Bob Vylan,Sunday,Peace Stage,0,0,01:30 - 02:30,01:30,02:30,01/07/2024,01/07/2024,30/06/2024 01:30,01/07/2024 02:30
Mas Que Nada Takeover: Tommy Tickle,Sunday,The Hive,0,0,01:30 - 02:30,01:30,02:30,01/07/2024,01/07/2024,30/06/2024 01:30,01/07/2024 02:30
Shay Malt,Sunday,The Meatrack,0,0,01:30 - 03:00,01:30,03:00,01/07/2024,01/07/2024,30/06/2024 01:30,01/07/2024 03:00
Kink,Sunday,The Temple,0,0,01:30 - 02:30,01:30,02:30,01/07/2024,01/07/2024,30/06/2024 01:30,01/07/2024 02:30
The Barefoot Bandit,Sunday,Wishing Well,42,20,01:30 - 03:00,01:30,03:00,01/07/2024,01/07/2024,30/06/2024 01:30,01/07/2024 03:00
N4 Records & Singularity Blind Tiger Takeover - Cheetah,Sunday,Blind Tiger,0,0,02:00 - 03:00,02:00,03:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 03:00
Whitts/ Andy P/ Chris Holt,Sunday,Deluxe Diner,64,17,02:00 - 05:00,02:00,05:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 05:00
Goldie (Dj Set),Sunday,Iicon,66,21,02:00 - 03:30,02:00,03:30,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 03:30
Marc Stylus,Sunday,Mez Yard,0,0,02:00 - 05:00,02:00,05:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 05:00
Swana Takeover X Nazar Presents: Ryan Lanji,Sunday,Nomad,0,0,02:00 - 03:00,02:00,03:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 03:00
Notion B2B Oppidan,Sunday,Nowhere,0,0,02:00 - 03:00,02:00,03:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 03:00
Village Underground Takeover,Sunday,Platform 23,0,0,02:00 - 03:00,02:00,03:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 03:00
Zerya,Sunday,Scissors,42,21,02:00 - 03:30,02:00,03:30,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 03:30
Chinese Daughter B2B Jamie Rodigan,Sunday,Stonebridge Bar,42,18,02:00 - 03:00,02:00,03:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 03:00
The Downsetters,Sunday,The Rocket Lounge,64,16,02:00 - 03:00,02:00,03:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 03:00
Kossov,Sunday,The Rum Shack,0,0,02:00 - 03:00,02:00,03:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 03:00
Osh Kosh,Sunday,The Salon Carousel,0,0,02:00 - 03:00,02:00,03:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 03:00
Sadsugar B2B Jamurai,Sunday,The Sistxrhood,0,0,02:00 - 04:00,02:00,04:00,01/07/2024,01/07/2024,30/06/2024 02:00,01/07/2024 04:00
Prosumer,Sunday,Nyc Downlow,0,0,02:05 - 03:30,02:05,03:30,01/07/2024,01/07/2024,30/06/2024 02:05,01/07/2024 03:30
Lsdj,Sunday,Bimble Inn,41,16,02:30 - 05:00,02:30,05:00,01/07/2024,01/07/2024,30/06/2024 02:30,01/07/2024 05:00
Madame Electrifie,Sunday,Peace Stage,0,0,02:30 - 03:00,02:30,03:00,01/07/2024,01/07/2024,30/06/2024 02:30,01/07/2024 03:00
Kettama,Sunday,The Temple,0,0,02:30 - 04:00,02:30,04:00,01/07/2024,01/07/2024,30/06/2024 02:30,01/07/2024 04:00
B2B2B2B2B2B2B,Sunday,Arrivals,0,0,03:00 - 04:00,03:00,04:00,01/07/2024,01/07/2024,30/06/2024 03:00,01/07/2024 04:00
Felix Dickinson,Sunday,Genosys,0,0,03:00 - 05:00,03:00,05:00,01/07/2024,01/07/2024,30/06/2024 03:00,01/07/2024 05:00
Swana Takeover X Nazar Presents: Aisha Mirza,Sunday,Nomad,0,0,03:00 - 05:00,03:00,05:00,01/07/2024,01/07/2024,30/06/2024 03:00,01/07/2024 05:00
Sam Divine B2B Cashonly,Sunday,Nowhere,0,0,03:00 - 04:00,03:00,04:00,01/07/2024,01/07/2024,30/06/2024 03:00,01/07/2024 04:00
High Fade,Sunday,Peace Stage,0,0,03:00 - 04:00,03:00,04:00,01/07/2024,01/07/2024,30/06/2024 03:00,01/07/2024 04:00
Caspar,Sunday,Stonebridge Bar,42,18,03:00 - 04:00,03:00,04:00,01/07/2024,01/07/2024,30/06/2024 03:00,01/07/2024 04:00
Ryan Hope (Gabriels),Sunday,The Meatrack,0,0,03:00 - 05:00,03:00,05:00,01/07/2024,01/07/2024,30/06/2024 03:00,01/07/2024 05:00
Old Time Sailors,Sunday,The Rocket Lounge,64,16,03:00 - 04:00,03:00,04:00,01/07/2024,01/07/2024,30/06/2024 03:00,01/07/2024 04:00
Aum,Sunday,The Rum Shack,0,0,03:00 - 04:00,03:00,04:00,01/07/2024,01/07/2024,30/06/2024 03:00,01/07/2024 04:00
Anna Prank,Sunday,The Salon Carousel,0,0,03:00 - 04:00,03:00,04:00,01/07/2024,01/07/2024,30/06/2024 03:00,01/07/2024 04:00
Dj Flight,Sunday,Iicon,66,21,03:30 - 05:00,03:30,05:00,01/07/2024,01/07/2024,30/06/2024 03:30,01/07/2024 05:00
Bad Cop Worse Cop,Sunday,Scissors,42,21,03:30 - 05:00,03:30,05:00,01/07/2024,01/07/2024,30/06/2024 03:30,01/07/2024 05:00
Luke Howard,Sunday,Nyc Downlow,0,0,03:35 - 05:00,03:35,05:00,01/07/2024,01/07/2024,30/06/2024 03:35,01/07/2024 05:00
N4 Records & Singularity Blind Tiger Takeover - Ivan Cargo,Sunday,Blind Tiger,0,0,04:00 - 05:00,04:00,05:00,01/07/2024,01/07/2024,30/06/2024 04:00,01/07/2024 05:00
Badger,Sunday,Nowhere,0,0,04:00 - 05:00,04:00,05:00,01/07/2024,01/07/2024,30/06/2024 04:00,01/07/2024 05:00
Dj Chris Tofu Vs Crew Boss,Sunday,Peace Stage,0,0,04:00 - 05:00,04:00,05:00,01/07/2024,01/07/2024,30/06/2024 04:00,01/07/2024 05:00
"Village Underground Takeover: Eastern Margins W/ Minna-No-Kimochi, Lumi & Jex Wang",Sunday,Platform 23,0,0,04:00 - 05:00,04:00,05:00,01/07/2024,01/07/2024,30/06/2024 04:00,01/07/2024 05:00
New York Brass Band,Sunday,The Rocket Lounge,64,16,04:00 - 05:00,04:00,05:00,01/07/2024,01/07/2024,30/06/2024 04:00,01/07/2024 05:00
Oh Annie Oh,Sunday,The Rum Shack,0,0,04:00 - 05:00,04:00,05:00,01/07/2024,01/07/2024,30/06/2024 04:00,01/07/2024 05:00
Jim Bitch And Stivs,Sunday,The Salon Carousel,0,0,04:00 - 05:00,04:00,05:00,01/07/2024,01/07/2024,30/06/2024 04:00,01/07/2024 05:00
Sherelle,Sunday,The Temple,0,0,04:00 - 05:00,04:00,05:00,01/07/2024,01/07/2024,30/06/2024 04:00,01/07/2024 05:00
Yoga Like Water With Dan Peppiatt,Sunday,Humblewell Active Platform,42,21,08:30 - 09:30,08:30,09:30,30/06/2024,30/06/2024,30/06/2024 08:30,30/06/2024 09:30
Dna Puppetry Presents: Little Red & Other Tales,Sunday,Kidzfield Big Top,0,0,09:30 - 10:00,09:30,10:00,30/06/2024,30/06/2024,30/06/2024 09:30,30/06/2024 10:00
Singing Circle With Leti,Sunday,Humblewell Active Platform,42,21,09:45 - 10:45,09:45,10:45,30/06/2024,30/06/2024,30/06/2024 09:45,30/06/2024 10:45
Nipsy,Sunday,Cornish Arms,0,0,10:00 - 11:45,10:00,11:45,30/06/2024,30/06/2024,30/06/2024 10:00,30/06/2024 11:45
Ravers 2 Runners (Stretch Session),Sunday,Greenpeace,55,26,10:00 - 10:30,10:00,10:30,30/06/2024,30/06/2024,30/06/2024 10:00,30/06/2024 10:30
Shamanic Drum Circle With Tracy Turnell,Sunday,Humblewell Retreat Yurt,42,21,10:00 - 11:00,10:00,11:00,30/06/2024,30/06/2024,30/06/2024 10:00,30/06/2024 11:00
Frederika,Sunday,San Remo,45,47,10:00 - 12:00,10:00,12:00,30/06/2024,30/06/2024,30/06/2024 10:00,30/06/2024 12:00
"Right To Food - Sarah Wooley, Fliss Premru",Sunday,Speakers Forum,0,0,10:00 - 11:00,10:00,11:00,30/06/2024,30/06/2024,30/06/2024 10:00,30/06/2024 11:00
Starkidz Superhero Vs Princess Show,Sunday,Kidzfield Big Top,0,0,10:10 - 10:40,10:10,10:40,30/06/2024,30/06/2024,30/06/2024 10:10,30/06/2024 10:40
Bell And Bullock,Sunday,Walkabouts,60,33,10:20 - 10:50,10:20,10:50,30/06/2024,30/06/2024,30/06/2024 10:20,30/06/2024 10:50
Dodgy Boys,Sunday,Walkabouts,60,33,10:20 - 11:05,10:20,11:05,30/06/2024,30/06/2024,30/06/2024 10:20,30/06/2024 11:05
Tented Talk - Tumble Circus,Sunday,Circus Big Top,57,34,10:30 - 11:10,10:30,11:10,30/06/2024,30/06/2024,30/06/2024 10:30,30/06/2024 11:10
Compère: Chris Barltrop,Sunday,Circus Big Top,57,34,10:30 - 12:30,10:30,12:30,30/06/2024,30/06/2024,30/06/2024 10:30,30/06/2024 12:30
Skate Ramp Pro Session,Sunday,Greenpeace,55,26,10:30 - 12:00,10:30,12:00,30/06/2024,30/06/2024,30/06/2024 10:30,30/06/2024 12:00
Activist Intersection,Sunday,Greenpeace (Beam),54,26,10:30 - 11:00,10:30,11:00,30/06/2024,30/06/2024,30/06/2024 10:30,30/06/2024 11:00
Sounds Of Science Dj Set,Sunday,Laboratory Stage,0,0,10:30 - 11:00,10:30,11:00,30/06/2024,30/06/2024,30/06/2024 10:30,30/06/2024 11:00
The Crate Stack Challenge,Sunday,Outside Circus Stage,59,33,10:30 - 11:30,10:30,11:30,30/06/2024,30/06/2024,30/06/2024 10:30,30/06/2024 11:30
Poetry Workshop With John Hegley,Sunday,Poetry&Words,0,0,10:30 - 11:25,10:30,11:25,30/06/2024,30/06/2024,30/06/2024 10:30,30/06/2024 11:25
Fire Fighters!,Sunday,Walkabouts,60,33,10:30 - 11:00,10:30,11:00,30/06/2024,30/06/2024,30/06/2024 10:30,30/06/2024 11:00
Jersey Girls,Sunday,Walkabouts,60,33,10:30 - 11:00,10:30,11:00,30/06/2024,30/06/2024,30/06/2024 10:30,30/06/2024 11:00
Flamingos,Sunday,Walkabouts,60,33,10:30 - 11:15,10:30,11:15,30/06/2024,30/06/2024,30/06/2024 10:30,30/06/2024 11:15
Clamour Of Bells,Sunday,Walkabouts,60,33,10:35 - 11:20,10:35,11:20,30/06/2024,30/06/2024,30/06/2024 10:35,30/06/2024 11:20
The Newspaper Men,Sunday,Walkabouts,60,33,10:35 - 11:20,10:35,11:20,30/06/2024,30/06/2024,30/06/2024 10:35,30/06/2024 11:20
Rishi Gordon,Sunday,Walkabouts,60,33,10:45 - 11:30,10:45,11:30,30/06/2024,30/06/2024,30/06/2024 10:45,30/06/2024 11:30
Maddie Moate'S Science Showdown!,Sunday,Kidzfield Big Top,0,0,10:50 - 11:15,10:50,11:15,30/06/2024,30/06/2024,30/06/2024 10:50,30/06/2024 11:15
The Smallest Race On Earth,Sunday,Walkabouts,60,33,10:50 - 11:20,10:50,11:20,30/06/2024,30/06/2024,30/06/2024 10:50,30/06/2024 11:20
Ukelele Thrash Mob,Sunday,Walkabouts,60,33,10:50 - 11:35,10:50,11:35,30/06/2024,30/06/2024,30/06/2024 10:50,30/06/2024 11:35
Compère: Sally-Anne Hayward,Sunday,The Astrolabe Theatre,0,0,10:55 - 15:30,10:55,15:30,30/06/2024,30/06/2024,30/06/2024 10:55,30/06/2024 15:30
The Crows,Sunday,Walkabouts,60,33,10:55 - 11:25,10:55,11:25,30/06/2024,30/06/2024,30/06/2024 10:55,30/06/2024 11:25
The Midwives,Sunday,Walkabouts,60,33,10:55 - 11:40,10:55,11:40,30/06/2024,30/06/2024,30/06/2024 10:55,30/06/2024 11:40
Films,Sunday,Atchin Tan,0,0,11:00 - 12:30,11:00,12:30,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 12:30
Jo Bucket,Sunday,Carhenge,58,36,11:00 - 12:00,11:00,12:00,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 12:00
Nigel Shaw + Bethan Lloyd,Sunday,Croissant Neuf Bandstand,55,21,11:00 - 11:45,11:00,11:45,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 11:45
Dance Against Deportation Takeover,Sunday,Greenpeace (Beam),54,26,11:00 - 12:00,11:00,12:00,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 12:00
Om And Bass Yoga With Dina Cohen,Sunday,Humblewell Active Platform,42,21,11:00 - 11:50,11:00,11:50,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 11:50
I'M Not There + Q&A With Cate Blanchett 15,Sunday,Pilton Palais Cinema,64,36,11:00 - 13:45,11:00,13:45,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 13:45
Taking On The Oil Industry And Winning - Tamasin Cave,Sunday,Speakers Forum,0,0,11:00 - 12:00,11:00,12:00,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 12:00
St Paul'S Carnival: Windrush Library Talks - Infinity & Beyond,Sunday,Terminal 1,0,0,11:00 - 12:30,11:00,12:30,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 12:30
The Guardian Q & A,Sunday,The Astrolabe Theatre,0,0,11:00 - 11:50,11:00,11:50,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 11:50
Mindful Movement With Laurie Clothier,Sunday,Toad Hall,0,0,11:00 - 11:40,11:00,11:40,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 11:40
Roo'D,Sunday,Walkabouts,60,33,11:00 - 11:30,11:00,11:30,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 11:30
The Family Tree,Sunday,Walkabouts,60,33,11:00 - 11:45,11:00,11:45,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 11:45
Matthew Halsall,Sunday,West Holts Stage,57,31,11:00 - 12:00,11:00,12:00,30/06/2024,30/06/2024,30/06/2024 11:00,30/06/2024 12:00
The Tea Ladies On Tour,Sunday,Walkabouts,60,33,11:05 - 11:50,11:05,11:50,30/06/2024,30/06/2024,30/06/2024 11:05,30/06/2024 11:50
Anyone For Tennis,Sunday,Walkabouts,60,33,11:10 - 11:55,11:10,11:55,30/06/2024,30/06/2024,30/06/2024 11:10,30/06/2024 11:55
Dapper Chaps,Sunday,Walkabouts,60,33,11:10 - 11:55,11:10,11:55,30/06/2024,30/06/2024,30/06/2024 11:10,30/06/2024 11:55
Tented Talk - Angel De Castro,Sunday,Circus Big Top,57,34,11:15 - 12:00,11:15,12:00,30/06/2024,30/06/2024,30/06/2024 11:15,30/06/2024 12:00
Crystal Singing Bowls With Yogic Sound,Sunday,Humblewell Retreat Yurt,42,21,11:15 - 11:45,11:15,11:45,30/06/2024,30/06/2024,30/06/2024 11:15,30/06/2024 11:45
Science-Based Meditation,Sunday,Laboratory Stage,0,0,11:15 - 11:45,11:15,11:45,30/06/2024,30/06/2024,30/06/2024 11:15,30/06/2024 11:45
The Zutons,Sunday,Other Stage,47,34,11:15 - 12:00,11:15,12:00,30/06/2024,30/06/2024,30/06/2024 11:15,30/06/2024 12:00
Be Prepared,Sunday,Walkabouts,60,33,11:15 - 12:00,11:15,12:00,30/06/2024,30/06/2024,30/06/2024 11:15,30/06/2024 12:00
The Bad Eggs,Sunday,Walkabouts,60,33,11:15 - 12:00,11:15,12:00,30/06/2024,30/06/2024,30/06/2024 11:15,30/06/2024 12:00
The Buzzing Bees,Sunday,Walkabouts,60,33,11:15 - 12:15,11:15,12:15,30/06/2024,30/06/2024,30/06/2024 11:15,30/06/2024 12:15
Jayahadadream,Sunday,Woodsies,43,52,11:15 - 12:00,11:15,12:00,30/06/2024,30/06/2024,30/06/2024 11:15,30/06/2024 12:00
Dan Rhodes,Sunday,Kidzfield Big Top,0,0,11:25 - 11:55,11:25,11:55,30/06/2024,30/06/2024,30/06/2024 11:25,30/06/2024 11:55
Toby Lee,Sunday,Acoustic Stage,66,38,11:30 - 12:00,11:30,12:00,30/06/2024,30/06/2024,30/06/2024 11:30,30/06/2024 12:00
The Ayoub Sisters,Sunday,Avalon Stage,66,38,11:30 - 12:10,11:30,12:10,30/06/2024,30/06/2024,30/06/2024 11:30,30/06/2024 12:10
Mighty Mighty J B2B Tilly B,Sunday,Babylon Uprising,0,0,11:30 - 12:00,11:30,12:00,30/06/2024,30/06/2024,30/06/2024 11:30,30/06/2024 12:00
Sustainability In Music Talks,Sunday,Croissant Neuf,55,21,11:30 - 12:45,11:30,12:45,30/06/2024,30/06/2024,30/06/2024 11:30,30/06/2024 12:45
Tba,Sunday,Mandala Stage,0,0,11:30 - 12:30,11:30,12:30,30/06/2024,30/06/2024,30/06/2024 11:30,30/06/2024 12:30
Compère: Famos Bramwells,Sunday,Outside Circus Stage,59,33,11:30 - 16:00,11:30,16:00,30/06/2024,30/06/2024,30/06/2024 11:30,30/06/2024 16:00
Gecko,Sunday,Poetry&Words,0,0,11:30 - 12:00,11:30,12:00,30/06/2024,30/06/2024,30/06/2024 11:30,30/06/2024 12:00
Interlinked Ballet,Sunday,Pyramid Stage,51,43,11:30 - 12:00,11:30,12:00,30/06/2024,30/06/2024,30/06/2024 11:30,30/06/2024 12:00
Alex Priddice,Sunday,The Hive,0,0,11:30 - 12:05,11:30,12:05,30/06/2024,30/06/2024,30/06/2024 11:30,30/06/2024 12:05
Problem Patterns,Sunday,The Park Stage,41,19,11:30 - 12:15,11:30,12:15,30/06/2024,30/06/2024,30/06/2024 11:30,30/06/2024 12:15
Circus Raj And Rajasthan Heritage Brass Band,Sunday,Outside Circus Stage,59,33,11:40 - 12:10,11:40,12:10,30/06/2024,30/06/2024,30/06/2024 11:40,30/06/2024 12:10
Lewis,Sunday,Cornish Arms,0,0,11:45 - 12:00,11:45,12:00,30/06/2024,30/06/2024,30/06/2024 11:45,30/06/2024 12:00
Good Habits,Sunday,The Bandstand,56,38,11:45 - 12:15,11:45,12:15,30/06/2024,30/06/2024,30/06/2024 11:45,30/06/2024 12:15
Space Cadets,Sunday,Walkabouts,60,33,11:45 - 12:30,11:45,12:30,30/06/2024,30/06/2024,30/06/2024 11:45,30/06/2024 12:30
Swyron & Desaata,Sunday,Walkabouts,60,33,11:45 - 12:30,11:45,12:30,30/06/2024,30/06/2024,30/06/2024 11:45,30/06/2024 12:30
The Trifleenees,Sunday,Walkabouts,60,33,11:50 - 12:35,11:50,12:35,30/06/2024,30/06/2024,30/06/2024 11:50,30/06/2024 12:35
Masters Of The Kazooniverse,Sunday,Walkabouts,60,33,11:50 - 13:20,11:50,13:20,30/06/2024,30/06/2024,30/06/2024 11:50,30/06/2024 13:20
Tba,Sunday,A Little More Sensation,0,0,12:00 - 12:35,12:00,12:35,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:35
Anna Wall B2B Bobby. [25 Years Of Fabric],Sunday,Assembly,40,42,12:00 - 14:00,12:00,14:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 14:00
Pixels,Sunday,Babylon Uprising,0,0,12:00 - 14:00,12:00,14:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 14:00
Open,Sunday,Bimble Inn,41,16,12:00 - 14:30,12:00,14:30,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 14:30
Jellzdnb,Sunday,Blind Tiger,0,0,12:00 - 12:40,12:00,12:40,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:40
Jack Valero,Sunday,Bread And Roses,0,0,12:00 - 12:40,12:00,12:40,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:40
An Audience With Alexei Sayle,Sunday,Cabaret,62,26,12:00 - 12:55,12:00,12:55,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:55
Compère: Cerys Nelms,Sunday,Cabaret,62,26,12:00 - 16:00,12:00,16:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 16:00
Curt & Andy,Sunday,Cornish Arms,0,0,12:00 - 13:00,12:00,13:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:00
Mama Tokus,Sunday,Crooner'S Corner,0,0,12:00 - 12:45,12:00,12:45,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:45
Bandyt [St Paul'S Carnival Takeover],Sunday,Firmly Rooted,43,43,12:00 - 13:00,12:00,13:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:00
Professor Alice Roberts,Sunday,Free University Of Glastonbury,42,21,12:00 - 13:00,12:00,13:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:00
Cassetteboy & Dj Rubbish,Sunday,Glade,51,29,12:00 - 12:50,12:00,12:50,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:50
Harri Pepper,Sunday,Glade Dome,49,29,12:00 - 13:20,12:00,13:20,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:20
Carnival,Sunday,Glasto Latino,58,27,12:00 - 12:30,12:00,12:30,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:30
Katya,Sunday,Greenpeace,55,26,12:00 - 12:45,12:00,12:45,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:45
Easy Tai Chi With Joe May,Sunday,Humblewell Active Platform,42,21,12:00 - 12:45,12:00,12:45,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:45
Katona Yoga And Breathwork With Lucy Wright,Sunday,Humblewell Retreat Yurt,42,21,12:00 - 13:00,12:00,13:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:00
Live Demo - Rocket Science!,Sunday,Laboratory Stage,0,0,12:00 - 12:30,12:00,12:30,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:30
"Debates: Small Boats: Safe Routes And Solidarity With Bibby Stockholm Campaigner, Nadia Whittome Mp, Rainbow Migration, Survivors Speak Out, Minnie Rahman",Sunday,Left Field,52,33,12:00 - 13:00,12:00,13:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:00
Aæe B2B Fonzo,Sunday,Levels,42,44,12:00 - 13:30,12:00,13:30,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:30
Compere: Jonny Fluffypunk,Sunday,Poetry&Words,0,0,12:00 - 14:20,12:00,14:20,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 14:20
Raw Silk,Sunday,San Remo,45,47,12:00 - 13:30,12:00,13:30,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:30
Dick Pulses Morning Rise,Sunday,Sensation Seekers Stage,0,0,12:00 - 12:25,12:00,12:25,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:25
Compères: George Orange / Grainne,Sunday,Sensation Seekers Stage,0,0,12:00 - 18:45,12:00,18:45,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 18:45
Are Climate Experts Part Of The Climate Problem ? - Kevin Anderson With Alice Larkin,Sunday,Speakers Forum,0,0,12:00 - 13:00,12:00,13:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:00
Greg Mahon Poetry,Sunday,Strummerville,48,12,12:00 - 12:20,12:00,12:20,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:20
Siegfried & Joy,Sunday,The Astrolabe Theatre,0,0,12:00 - 13:00,12:00,13:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:00
Land Of The Giants,Sunday,The Gateway,0,0,12:00 - 12:30,12:00,12:30,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:30
Groovy Guy,Sunday,The Glebe,60,33,12:00 - 12:30,12:00,12:30,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:30
Transition Network: 'Time Travel As A Tool For Activists': Rob Hopkins (Author - From What Is To What If),Sunday,The Information,41,41,12:00 - 13:00,12:00,13:00,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 13:00
Yann Elvis,Sunday,The Pavement,0,0,12:00 - 12:30,12:00,12:30,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:30
Aminadabu,Sunday,Toad Hall,0,0,12:00 - 12:40,12:00,12:40,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:40
The Very Best Of Tommy Cooper,Sunday,Walkabouts,60,33,12:00 - 12:30,12:00,12:30,30/06/2024,30/06/2024,30/06/2024 12:00,30/06/2024 12:30
Black Liver 'Miss Nobodies',Sunday,Poetry&Words,0,0,12:03 - 13:03,12:03,13:03,30/06/2024,30/06/2024,30/06/2024 12:03,30/06/2024 13:03
Wookey Hole Circus,Sunday,Circus Big Top,57,34,12:05 - 12:30,12:05,12:30,30/06/2024,30/06/2024,30/06/2024 12:05,30/06/2024 12:30
Flamingos,Sunday,Walkabouts,60,33,12:05 - 12:50,12:05,12:50,30/06/2024,30/06/2024,30/06/2024 12:05,30/06/2024 12:50
Frankie Archer,Sunday,Acoustic Stage,66,38,12:10 - 12:40,12:10,12:40,30/06/2024,30/06/2024,30/06/2024 12:10,30/06/2024 12:40
Football Crazy,Sunday,Walkabouts,60,33,12:10 - 12:55,12:10,12:55,30/06/2024,30/06/2024,30/06/2024 12:10,30/06/2024 12:55
The Magnifient Kevens,Sunday,Walkabouts,60,33,12:10 - 12:55,12:10,12:55,30/06/2024,30/06/2024,30/06/2024 12:10,30/06/2024 12:55
Compère: Ken Fanning,Sunday,Circus Big Top,57,34,12:15 - 14:45,12:15,14:45,30/06/2024,30/06/2024,30/06/2024 12:15,30/06/2024 14:45
Andy And The Odd Socks,Sunday,Kidzfield Big Top,0,0,12:15 - 12:50,12:15,12:50,30/06/2024,30/06/2024,30/06/2024 12:15,30/06/2024 12:50
Cirk Hes Presents Rosenwyn,Sunday,Outside Circus Stage,59,33,12:15 - 12:21,12:15,12:21,30/06/2024,30/06/2024,30/06/2024 12:15,30/06/2024 12:21
Walter Kocays,Sunday,The Hive,0,0,12:15 - 12:55,12:15,12:55,30/06/2024,30/06/2024,30/06/2024 12:15,30/06/2024 12:55
Disco Robot Girlz,Sunday,Walkabouts,60,33,12:15 - 13:00,12:15,13:00,30/06/2024,30/06/2024,30/06/2024 12:15,30/06/2024 13:00
The Natural Theatre Company,Sunday,Walkabouts,60,33,12:15 - 13:00,12:15,13:00,30/06/2024,30/06/2024,30/06/2024 12:15,30/06/2024 13:00
Tba,Sunday,Outside Circus Stage,59,33,12:26 - 12:56,12:26,12:56,30/06/2024,30/06/2024,30/06/2024 12:26,30/06/2024 12:56
"Delaine Le Bas, In Conversation With Liza Mortimer Travellers Times",Sunday,Atchin Tan,0,0,12:30 - 13:15,12:30,13:15,30/06/2024,30/06/2024,30/06/2024 12:30,30/06/2024 13:15
Girlband!,Sunday,Bbc Music Introducing,45,44,12:30 - 13:00,12:30,13:00,30/06/2024,30/06/2024,30/06/2024 12:30,30/06/2024 13:00
Dance Class: Salsa,Sunday,Glasto Latino,58,27,12:30 - 13:30,12:30,13:30,30/06/2024,30/06/2024,30/06/2024 12:30,30/06/2024 13:30
Rachel Chinouriri,Sunday,Other Stage,47,34,12:30 - 13:15,12:30,13:15,30/06/2024,30/06/2024,30/06/2024 12:30,30/06/2024 13:15
Seasick Steve,Sunday,Pyramid Stage,51,43,12:30 - 13:15,12:30,13:15,30/06/2024,30/06/2024,30/06/2024 12:30,30/06/2024 13:15
Sunday Service With Everyone'S Choir By Xoph,Sunday,Scissors,42,21,12:30 - 13:30,12:30,13:30,30/06/2024,30/06/2024,30/06/2024 12:30,30/06/2024 13:30
Otto & Astrid-Die Roten Punkte,Sunday,Sensation Seekers Stage,0,0,12:30 - 13:00,12:30,13:00,30/06/2024,30/06/2024,30/06/2024 12:30,30/06/2024 13:00
Morning Star,Sunday,The Bandstand,56,38,12:30 - 13:00,12:30,13:00,30/06/2024,30/06/2024,30/06/2024 12:30,30/06/2024 13:00
Jalen Ngonda,Sunday,West Holts Stage,57,31,12:30 - 13:30,12:30,13:30,30/06/2024,30/06/2024,30/06/2024 12:30,30/06/2024 13:30
The Ks,Sunday,Woodsies,43,52,12:30 - 13:30,12:30,13:30,30/06/2024,30/06/2024,30/06/2024 12:30,30/06/2024 13:30
Harvey Juggling,Sunday,A Little More Sensation,0,0,12:35 - 13:05,12:35,13:05,30/06/2024,30/06/2024,30/06/2024 12:35,30/06/2024 13:05
Kingfishr,Sunday,Avalon Stage,66,38,12:35 - 13:25,12:35,13:25,30/06/2024,30/06/2024,30/06/2024 12:35,30/06/2024 13:25
Nofit Howie,Sunday,Circus Big Top,57,34,12:35 - 12:43,12:35,12:43,30/06/2024,30/06/2024,30/06/2024 12:35,30/06/2024 12:43
Lekiddo Lord Of The Lobsters,Sunday,The Glebe,60,33,12:35 - 13:05,12:35,13:05,30/06/2024,30/06/2024,30/06/2024 12:35,30/06/2024 13:05
Billy Kidd Show,Sunday,The Pavement,0,0,12:35 - 13:05,12:35,13:05,30/06/2024,30/06/2024,30/06/2024 12:35,30/06/2024 13:05
The Newspaper Men,Sunday,Walkabouts,60,33,12:35 - 13:20,12:35,13:20,30/06/2024,30/06/2024,30/06/2024 12:35,30/06/2024 13:20
Mtbeats,Sunday,Blind Tiger,0,0,12:40 - 13:20,12:40,13:20,30/06/2024,30/06/2024,30/06/2024 12:40,30/06/2024 13:20
Jack Henry + Julie Abbe,Sunday,Croissant Neuf Bandstand,55,21,12:45 - 13:15,12:45,13:15,30/06/2024,30/06/2024,30/06/2024 12:45,30/06/2024 13:15
The Great Ape Challenge,Sunday,Laboratory Stage,0,0,12:45 - 13:15,12:45,13:15,30/06/2024,30/06/2024,30/06/2024 12:45,30/06/2024 13:15
Faces Of Disco,Sunday,The Gateway,0,0,12:45 - 13:15,12:45,13:15,30/06/2024,30/06/2024,30/06/2024 12:45,30/06/2024 13:15
Lime Garden,Sunday,The Park Stage,41,19,12:45 - 13:30,12:45,13:30,30/06/2024,30/06/2024,30/06/2024 12:45,30/06/2024 13:30
Gnomes,Sunday,Walkabouts,60,33,12:45 - 13:30,12:45,13:30,30/06/2024,30/06/2024,30/06/2024 12:45,30/06/2024 13:30
Steve Rawlings,Sunday,Circus Big Top,57,34,12:48 - 13:08,12:48,13:08,30/06/2024,30/06/2024,30/06/2024 12:48,30/06/2024 13:08
An Dannsa Dub,Sunday,Glade,51,29,12:55 - 13:55,12:55,13:55,30/06/2024,30/06/2024,30/06/2024 12:55,30/06/2024 13:55
Rezon8 Artist Showcase,Sunday,10 Aces,0,0,13:00 - 13:30,13:00,13:30,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 13:30
Nadia Kadek (Etc Finalist),Sunday,Acoustic Stage,66,38,13:00 - 13:40,13:00,13:40,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 13:40
Jonny Awsum,Sunday,Cabaret,62,26,13:00 - 13:20,13:00,13:20,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 13:20
Lazy Technician B2B Oliver Sudden,Sunday,Cornish Arms,0,0,13:00 - 14:00,13:00,14:00,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 14:00
St Pauls Carnival B2B Notting Hill Carnival [St Paul'S Carnival Takeover],Sunday,Firmly Rooted,43,43,13:00 - 15:00,13:00,15:00,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 15:00
Dr Janina Ramirez,Sunday,Free University Of Glastonbury,42,21,13:00 - 14:00,13:00,14:00,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 14:00
African Dance With Penny Avery,Sunday,Humblewell Active Platform,42,21,13:00 - 13:30,13:00,13:30,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 13:30
Faltsanger,Sunday,Mandala Stage,0,0,13:00 - 14:00,13:00,14:00,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 14:00
"Reform, Protest Or Resistance - Clare Farrell, Will Mccullen, Shane Collins, Sarah Lunnon, Mel Kee",Sunday,Speakers Forum,0,0,13:00 - 14:00,13:00,14:00,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 14:00
Luke Una,Sunday,Stonebridge Bar,42,18,13:00 - 15:00,13:00,15:00,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 15:00
Jack Chard,Sunday,Strummerville,48,12,13:00 - 13:20,13:00,13:20,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 13:20
The Black Eagles,Sunday,The Astrolabe Theatre,0,0,13:00 - 13:25,13:00,13:25,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 13:25
Jersey Girls,Sunday,Walkabouts,60,33,13:00 - 13:30,13:00,13:30,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 13:30
Mafia Wedding,Sunday,Walkabouts,60,33,13:00 - 13:45,13:00,13:45,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 13:45
Alma Twist,Sunday,Wishing Well,42,20,13:00 - 13:45,13:00,13:45,30/06/2024,30/06/2024,30/06/2024 13:00,30/06/2024 13:45
Cirk Hes Presents Jaia & Malia,Sunday,Outside Circus Stage,59,33,13:01 - 13:11,13:01,13:11,30/06/2024,30/06/2024,30/06/2024 13:01,30/06/2024 13:11
Ellerose The Unicorn,Sunday,Poetry&Words,0,0,13:08 - 13:33,13:08,13:33,30/06/2024,30/06/2024,30/06/2024 13:08,30/06/2024 13:33
The Doogans,Sunday,A Little More Sensation,0,0,13:10 - 13:40,13:10,13:40,30/06/2024,30/06/2024,30/06/2024 13:10,30/06/2024 13:40
Freddieno,Sunday,Sensation Seekers Stage,0,0,13:10 - 13:40,13:10,13:40,30/06/2024,30/06/2024,30/06/2024 13:10,30/06/2024 13:40
Mark Bruce Dance Company,Sunday,The Glebe,60,33,13:10 - 13:20,13:10,13:20,30/06/2024,30/06/2024,30/06/2024 13:10,30/06/2024 13:20
Grant Goldie,Sunday,The Pavement,0,0,13:10 - 13:40,13:10,13:40,30/06/2024,30/06/2024,30/06/2024 13:10,30/06/2024 13:40
Liver Cottage,Sunday,Walkabouts,60,33,13:10 - 13:55,13:10,13:55,30/06/2024,30/06/2024,30/06/2024 13:10,30/06/2024 13:55
Cirk Hes Presents Charlotte And Nadine,Sunday,Circus Big Top,57,34,13:13 - 13:23,13:13,13:23,30/06/2024,30/06/2024,30/06/2024 13:13,30/06/2024 13:23
Vulva Voce,Sunday,Croissant Neuf,55,21,13:15 - 14:00,13:15,14:00,30/06/2024,30/06/2024,30/06/2024 13:15,30/06/2024 14:00
Charlotte May,Sunday,Crooner'S Corner,0,0,13:15 - 14:00,13:15,14:00,30/06/2024,30/06/2024,30/06/2024 13:15,30/06/2024 14:00
The Zawose Queens,Sunday,Greenpeace,55,26,13:15 - 14:00,13:15,14:00,30/06/2024,30/06/2024,30/06/2024 13:15,30/06/2024 14:00
Life Drawing With Fra Beecher,Sunday,Humblewell Retreat Yurt,42,21,13:15 - 14:15,13:15,14:15,30/06/2024,30/06/2024,30/06/2024 13:15,30/06/2024 14:15
Doc Brown'S Wordpower Hour,Sunday,Kidzfield Big Top,0,0,13:15 - 13:55,13:15,13:55,30/06/2024,30/06/2024,30/06/2024 13:15,30/06/2024 13:55
Superlung,Sunday,The Bandstand,56,38,13:15 - 13:45,13:15,13:45,30/06/2024,30/06/2024,30/06/2024 13:15,30/06/2024 13:45
John E Vistic,Sunday,The Hive,0,0,13:15 - 13:45,13:15,13:45,30/06/2024,30/06/2024,30/06/2024 13:15,30/06/2024 13:45
"Team Canteen: ‘Fair Shares - Inequality On The High Street’: Emma Hopkins (Mothers Meeting), Xanthe Clay (Telegraph), Jo Ingleby (Feeding Bristol), Tba, Hosted By Josh Eggleton (The Pony & Trap)",Sunday,The Information,41,41,13:15 - 14:15,13:15,14:15,30/06/2024,30/06/2024,30/06/2024 13:15,30/06/2024 14:15
The Smallest Race On Earth,Sunday,Walkabouts,60,33,13:15 - 13:45,13:15,13:45,30/06/2024,30/06/2024,30/06/2024 13:15,30/06/2024 13:45
Be Prepared,Sunday,Walkabouts,60,33,13:15 - 14:00,13:15,14:00,30/06/2024,30/06/2024,30/06/2024 13:15,30/06/2024 14:00
Charlie Bicknell Is Holding Out For A Hero,Sunday,Outside Circus Stage,59,33,13:16 - 13:28,13:16,13:28,30/06/2024,30/06/2024,30/06/2024 13:16,30/06/2024 13:28
Sounds Of Fia,Sunday,Blind Tiger,0,0,13:20 - 14:00,13:20,14:00,30/06/2024,30/06/2024,30/06/2024 13:20,30/06/2024 14:00
Lucy Cook,Sunday,Glade Dome,49,29,13:20 - 14:40,13:20,14:40,30/06/2024,30/06/2024,30/06/2024 13:20,30/06/2024 14:40
Peppermint.,Sunday,Strummerville,48,12,13:20 - 13:40,13:20,13:40,30/06/2024,30/06/2024,30/06/2024 13:20,30/06/2024 13:40
Robin Ince,Sunday,Cabaret,62,26,13:25 - 13:55,13:25,13:55,30/06/2024,30/06/2024,30/06/2024 13:25,30/06/2024 13:55
Gecko,Sunday,The Astrolabe Theatre,0,0,13:25 - 13:35,13:25,13:35,30/06/2024,30/06/2024,30/06/2024 13:25,30/06/2024 13:35
Primary School Assembly Bangers,Sunday,The Glebe,60,33,13:25 - 13:55,13:25,13:55,30/06/2024,30/06/2024,30/06/2024 13:25,30/06/2024 13:55
Duo Santus,Sunday,Circus Big Top,57,34,13:28 - 13:34,13:28,13:34,30/06/2024,30/06/2024,30/06/2024 13:28,30/06/2024 13:34
Chiedu Oraka,Sunday,Bbc Music Introducing,45,44,13:30 - 14:00,13:30,14:00,30/06/2024,30/06/2024,30/06/2024 13:30,30/06/2024 14:00
Dance Class: Samba,Sunday,Glasto Latino,58,27,13:30 - 14:30,13:30,14:30,30/06/2024,30/06/2024,30/06/2024 13:30,30/06/2024 14:30
Science Shorts: Your Brain On Therapy/ You'Re On Neuron,Sunday,Laboratory Stage,0,0,13:30 - 14:00,13:30,14:00,30/06/2024,30/06/2024,30/06/2024 13:30,30/06/2024 14:00
"Debates: How To End The Housing Crisis With Andy Burnham, Kwajo Tweneboa, London Renter'S Union, Museum Of Homelessness, John Harris",Sunday,Left Field,52,33,13:30 - 14:30,13:30,14:30,30/06/2024,30/06/2024,30/06/2024 13:30,30/06/2024 14:30
Dismantle B2B Emerald,Sunday,Levels,42,44,13:30 - 15:00,13:30,15:00,30/06/2024,30/06/2024,30/06/2024 13:30,30/06/2024 15:00
Camilo Miranda,Sunday,San Remo,45,47,13:30 - 15:00,13:30,15:00,30/06/2024,30/06/2024,30/06/2024 13:30,30/06/2024 15:00
Sophie Ellis Bextor Q&A,Sunday,Scissors,42,21,13:30 - 14:15,13:30,14:15,30/06/2024,30/06/2024,30/06/2024 13:30,30/06/2024 14:15
Fire Fighters!,Sunday,Walkabouts,60,33,13:30 - 14:00,13:30,14:00,30/06/2024,30/06/2024,30/06/2024 13:30,30/06/2024 14:00
The Jukeboxes,Sunday,Walkabouts,60,33,13:30 - 15:00,13:30,15:00,30/06/2024,30/06/2024,30/06/2024 13:30,30/06/2024 15:00
Jon Udry,Sunday,Outside Circus Stage,59,33,13:33 - 14:03,13:33,14:03,30/06/2024,30/06/2024,30/06/2024 13:33,30/06/2024 14:03
Trash Test Dummies,Sunday,The Astrolabe Theatre,0,0,13:35 - 14:35,13:35,14:35,30/06/2024,30/06/2024,30/06/2024 13:35,30/06/2024 14:35
Old Time Sailors,Sunday,The Gateway,0,0,13:35 - 14:35,13:35,14:35,30/06/2024,30/06/2024,30/06/2024 13:35,30/06/2024 14:35
"Joe Sellman-Leava 'It'S The Economy, Stupid!'",Sunday,Poetry&Words,0,0,13:38 - 14:38,13:38,14:38,30/06/2024,30/06/2024,30/06/2024 13:38,30/06/2024 14:38
High Society,Sunday,Circus Big Top,57,34,13:39 - 14:24,13:39,14:24,30/06/2024,30/06/2024,30/06/2024 13:39,30/06/2024 14:24
Cocoa Butter Club Cabaret,Sunday,10 Aces,0,0,13:40 - 14:10,13:40,14:10,30/06/2024,30/06/2024,30/06/2024 13:40,30/06/2024 14:10
Bob Doyle,Sunday,Strummerville,48,12,13:40 - 14:00,13:40,14:00,30/06/2024,30/06/2024,30/06/2024 13:40,30/06/2024 14:00
Rishi Gordon,Sunday,Walkabouts,60,33,13:40 - 14:25,13:40,14:25,30/06/2024,30/06/2024,30/06/2024 13:40,30/06/2024 14:25
The Family Tree,Sunday,Walkabouts,60,33,13:40 - 14:25,13:40,14:25,30/06/2024,30/06/2024,30/06/2024 13:40,30/06/2024 14:25
Dan The Hat,Sunday,A Little More Sensation,0,0,13:45 - 14:15,13:45,14:15,30/06/2024,30/06/2024,30/06/2024 13:45,30/06/2024 14:15
African Dance With Penny Avery,Sunday,Humblewell Active Platform,42,21,13:45 - 14:15,13:45,14:15,30/06/2024,30/06/2024,30/06/2024 13:45,30/06/2024 14:15
Soft Play,Sunday,Other Stage,47,34,13:45 - 14:30,13:45,14:30,30/06/2024,30/06/2024,30/06/2024 13:45,30/06/2024 14:30
Paloma Faith,Sunday,Pyramid Stage,51,43,13:45 - 14:45,13:45,14:45,30/06/2024,30/06/2024,30/06/2024 13:45,30/06/2024 14:45
Ekleido Dance - Splice,Sunday,The Pavement,0,0,13:45 - 14:00,13:45,14:00,30/06/2024,30/06/2024,30/06/2024 13:45,30/06/2024 14:00
The Buzzing Bees,Sunday,Walkabouts,60,33,13:45 - 14:45,13:45,14:45,30/06/2024,30/06/2024,30/06/2024 13:45,30/06/2024 14:45
Rhythm Districk (Dj Set),Sunday,Wishing Well,42,20,13:45 - 14:45,13:45,14:45,30/06/2024,30/06/2024,30/06/2024 13:45,30/06/2024 14:45
Tony & Ray,Sunday,Sensation Seekers Stage,0,0,13:50 - 14:05,13:50,14:05,30/06/2024,30/06/2024,30/06/2024 13:50,30/06/2024 14:05
Scary & Spooky Skeletons,Sunday,Walkabouts,60,33,13:50 - 14:35,13:50,14:35,30/06/2024,30/06/2024,30/06/2024 13:50,30/06/2024 14:35
Toyah & Robert,Sunday,Avalon Stage,66,38,13:55 - 14:55,13:55,14:55,30/06/2024,30/06/2024,30/06/2024 13:55,30/06/2024 14:55
Grace Petrie,Sunday,Acoustic Stage,66,38,14:00 - 14:40,14:00,14:40,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 14:40
Or:La [25 Years Of Fabric],Sunday,Assembly,40,42,14:00 - 16:00,14:00,16:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 16:00
Traveller Acoustic Music Session,Sunday,Atchin Tan,0,0,14:00 - 18:00,14:00,18:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 18:00
Cardinal Sound - Origins Set,Sunday,Babylon Uprising,0,0,14:00 - 15:00,14:00,15:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 15:00
Anolah An Zee Bonez (Live),Sunday,Blind Tiger,0,0,14:00 - 15:00,14:00,15:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 15:00
Kerry Godliman,Sunday,Cabaret,62,26,14:00 - 14:30,14:00,14:30,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 14:30
Lewis,Sunday,Cornish Arms,0,0,14:00 - 14:15,14:00,14:15,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 14:15
Larabel,Sunday,Croissant Neuf Bandstand,55,21,14:00 - 14:30,14:00,14:30,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 14:30
Dame Dr Maggie Aderin,Sunday,Free University Of Glastonbury,42,21,14:00 - 15:00,14:00,15:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 15:00
Holysseus Fly,Sunday,Lonely Hearts Club,44,41,14:00 - 15:00,14:00,15:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 15:00
"Unicorns + Q&A With Ben Hardy, Jason Patel And Directors 15",Sunday,Pilton Palais Cinema,64,36,14:00 - 16:30,14:00,16:30,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 16:30
Up Shit Creek – Making Water Plc’S Pay - Carla Denyer,Sunday,Speakers Forum,0,0,14:00 - 15:00,14:00,15:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 15:00
Joli Blon Cajun Band,Sunday,Strummerville,48,12,14:00 - 14:40,14:00,14:40,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 14:40
The Ayoub Sisters,Sunday,The Bandstand,56,38,14:00 - 14:40,14:00,14:40,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 14:40
A Day At The Beach,Sunday,The Glebe,60,33,14:00 - 14:30,14:00,14:30,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 14:30
Psychedelic Porn Crumpets,Sunday,The Park Stage,41,19,14:00 - 14:45,14:00,14:45,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 14:45
Camkahla,Sunday,Village Inn,0,0,14:00 - 16:00,14:00,16:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 16:00
Circus Raj,Sunday,Walkabouts,60,33,14:00 - 14:45,14:00,14:45,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 14:45
Bowjangles,Sunday,Walkabouts,60,33,14:00 - 15:00,14:00,15:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 15:00
Balming Tiger,Sunday,West Holts Stage,57,31,14:00 - 15:00,14:00,15:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 15:00
Newdad,Sunday,Woodsies,43,52,14:00 - 15:00,14:00,15:00,30/06/2024,30/06/2024,30/06/2024 14:00,30/06/2024 15:00
Don Letts,Sunday,Glade,51,29,14:05 - 15:05,14:05,15:05,30/06/2024,30/06/2024,30/06/2024 14:05,30/06/2024 15:05
James Humphrys,Sunday,The Hive,0,0,14:05 - 14:50,14:05,14:50,30/06/2024,30/06/2024,30/06/2024 14:05,30/06/2024 14:50
Jack Defrost - Traceworks Dance,Sunday,The Pavement,0,0,14:05 - 14:20,14:05,14:20,30/06/2024,30/06/2024,30/06/2024 14:05,30/06/2024 14:20
The Explorers,Sunday,Walkabouts,60,33,14:05 - 15:05,14:05,15:05,30/06/2024,30/06/2024,30/06/2024 14:05,30/06/2024 15:05
Fraser Hooper,Sunday,Outside Circus Stage,59,33,14:08 - 14:38,14:08,14:38,30/06/2024,30/06/2024,30/06/2024 14:08,30/06/2024 14:38
Clown Zazz - Circus Pazaz,Sunday,Kidzfield Big Top,0,0,14:10 - 14:35,14:10,14:35,30/06/2024,30/06/2024,30/06/2024 14:10,30/06/2024 14:35
Abandoman,Sunday,Sensation Seekers Stage,0,0,14:10 - 14:55,14:10,14:55,30/06/2024,30/06/2024,30/06/2024 14:10,30/06/2024 14:55
Lazy Technician B2B Oliver Sudden,Sunday,Cornish Arms,0,0,14:15 - 15:00,14:15,15:00,30/06/2024,30/06/2024,30/06/2024 14:15,30/06/2024 15:00
Wildlife Kate - Get Wild In Your Space!,Sunday,Laboratory Stage,0,0,14:15 - 14:45,14:15,14:45,30/06/2024,30/06/2024,30/06/2024 14:15,30/06/2024 14:45
Jenny Colquitt,Sunday,Toad Hall,0,0,14:15 - 15:00,14:15,15:00,30/06/2024,30/06/2024,30/06/2024 14:15,30/06/2024 15:00
Disco Robot Girlz,Sunday,Walkabouts,60,33,14:15 - 15:00,14:15,15:00,30/06/2024,30/06/2024,30/06/2024 14:15,30/06/2024 15:00
Ukelele Thrash Mob,Sunday,Walkabouts,60,33,14:15 - 15:00,14:15,15:00,30/06/2024,30/06/2024,30/06/2024 14:15,30/06/2024 15:00
Cash Cows,Sunday,10 Aces,0,0,14:20 - 14:50,14:20,14:50,30/06/2024,30/06/2024,30/06/2024 14:20,30/06/2024 14:50
Akira,Sunday,A Little More Sensation,0,0,14:20 - 14:50,14:20,14:50,30/06/2024,30/06/2024,30/06/2024 14:20,30/06/2024 14:50
Harvey Juggling,Sunday,The Pavement,0,0,14:25 - 14:55,14:25,14:55,30/06/2024,30/06/2024,30/06/2024 14:25,30/06/2024 14:55
Molly Whitehouse,Sunday,Circus Big Top,57,34,14:29 - 14:35,14:29,14:35,30/06/2024,30/06/2024,30/06/2024 14:29,30/06/2024 14:35
Maya Lakhani,Sunday,Bbc Music Introducing,45,44,14:30 - 15:00,14:30,15:00,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 15:00
Luke Gomm & The Works,Sunday,Bread And Roses,0,0,14:30 - 15:30,14:30,15:30,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 15:30
Compère: Dave Chameleon,Sunday,Circus Big Top,57,34,14:30 - 18:30,14:30,18:30,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 18:30
Rainbow Girls,Sunday,Croissant Neuf,55,21,14:30 - 15:30,14:30,15:30,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 15:30
Georgis D'Arcy Roden,Sunday,Crooner'S Corner,0,0,14:30 - 15:15,14:30,15:15,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 15:15
Dance Class: Salsa,Sunday,Glasto Latino,58,27,14:30 - 15:30,14:30,15:30,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 15:30
Beans On Toast,Sunday,Greenpeace,55,26,14:30 - 15:30,14:30,15:30,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 15:30
Disco Fit With Helen Rooney,Sunday,Humblewell Active Platform,42,21,14:30 - 15:00,14:30,15:00,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 15:00
Yin And Restorative Yoga With Sasha Gabbe,Sunday,Humblewell Retreat Yurt,42,21,14:30 - 15:30,14:30,15:30,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 15:30
"Workshop: Booty Bass, Nicheren Buddhism",Sunday,Scissors,42,21,14:30 - 15:15,14:30,15:15,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 15:15
"Black British Book Festival: ‘Remembering Benjamin Zephaniah’ - David Springer (Benjamin'S Brother), Sophia Thakur (Poet), Moqapi Selassie (Poet), Hosted By Casey Bailey (Writer, Performer, Educator)",Sunday,The Information,41,41,14:30 - 15:30,14:30,15:30,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 15:30
Madame D'Orificio,Sunday,Walkabouts,60,33,14:30 - 16:00,14:30,16:00,30/06/2024,30/06/2024,30/06/2024 14:30,30/06/2024 16:00
Pam Ayres,Sunday,Cabaret,62,26,14:35 - 15:30,14:35,15:30,30/06/2024,30/06/2024,30/06/2024 14:35,30/06/2024 15:30
Billy Kidd Show,Sunday,The Glebe,60,33,14:35 - 15:05,14:35,15:05,30/06/2024,30/06/2024,30/06/2024 14:35,30/06/2024 15:05
Compere: Rosy Carrick,Sunday,Poetry&Words,0,0,14:38 - 16:55,14:38,16:55,30/06/2024,30/06/2024,30/06/2024 14:38,30/06/2024 16:55
Ellis Grover,Sunday,Circus Big Top,57,34,14:40 - 14:50,14:40,14:50,30/06/2024,30/06/2024,30/06/2024 14:40,30/06/2024 14:50
T.Jacques,Sunday,Glade Dome,49,29,14:40 - 16:00,14:40,16:00,30/06/2024,30/06/2024,30/06/2024 14:40,30/06/2024 16:00
Marcus Du Sautoy And The School Of Hard Sums,Sunday,The Astrolabe Theatre,0,0,14:40 - 15:30,14:40,15:30,30/06/2024,30/06/2024,30/06/2024 14:40,30/06/2024 15:30
Vertigo Stilts,Sunday,Walkabouts,60,33,14:40 - 15:25,14:40,15:25,30/06/2024,30/06/2024,30/06/2024 14:40,30/06/2024 15:25
Darius Magic,Sunday,Walkabouts,60,33,14:40 - 15:40,14:40,15:40,30/06/2024,30/06/2024,30/06/2024 14:40,30/06/2024 15:40
Wookey Hole Circus,Sunday,Outside Circus Stage,59,33,14:43 - 15:08,14:43,15:08,30/06/2024,30/06/2024,30/06/2024 14:43,30/06/2024 15:08
Sophia And Heleana Blackwell 'Wife Material',Sunday,Poetry&Words,0,0,14:44 - 15:44,14:44,15:44,30/06/2024,30/06/2024,30/06/2024 14:44,30/06/2024 15:44
Epic Story Quest,Sunday,The Gateway,0,0,14:45 - 15:15,14:45,15:15,30/06/2024,30/06/2024,30/06/2024 14:45,30/06/2024 15:15
Dodgy Boys,Sunday,Walkabouts,60,33,14:45 - 15:30,14:45,15:30,30/06/2024,30/06/2024,30/06/2024 14:45,30/06/2024 15:30
Daisy Veacock,Sunday,Wishing Well,42,20,14:45 - 15:30,14:45,15:30,30/06/2024,30/06/2024,30/06/2024 14:45,30/06/2024 15:30
Fladam Presents: Green Fingers,Sunday,Kidzfield Big Top,0,0,14:50 - 15:45,14:50,15:45,30/06/2024,30/06/2024,30/06/2024 14:50,30/06/2024 15:45
Yann Elvis,Sunday,A Little More Sensation,0,0,14:55 - 15:25,14:55,15:25,30/06/2024,30/06/2024,30/06/2024 14:55,30/06/2024 15:25
Cirk Hes Presents Edith,Sunday,Circus Big Top,57,34,14:55 - 15:01,14:55,15:01,30/06/2024,30/06/2024,30/06/2024 14:55,30/06/2024 15:01
Riff Raff Kaberett,Sunday,10 Aces,0,0,15:00 - 15:30,15:00,15:30,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 15:30
Michele Stodart,Sunday,Acoustic Stage,66,38,15:00 - 15:50,15:00,15:50,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 15:50
Symeon,Sunday,Babylon Uprising,0,0,15:00 - 16:00,15:00,16:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:00
"Wickednbad - A-Star, Kaisha, Rhys, N.E.D, Sensi",Sunday,Blind Tiger,0,0,15:00 - 17:00,15:00,17:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 17:00
Jo Bucket,Sunday,Carhenge,58,36,15:00 - 16:00,15:00,16:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:00
Johnny Cass Uncle Monty'S Party (Brighton),Sunday,Cornish Arms,0,0,15:00 - 17:00,15:00,17:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 17:00
Josephine Gyasi [St Paul'S Carnival Takeover],Sunday,Firmly Rooted,43,43,15:00 - 16:00,15:00,16:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:00
Bbc Natural History Unit,Sunday,Laboratory Stage,0,0,15:00 - 15:45,15:00,15:45,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 15:45
"Radical Round Up: Billy Bragg, Steve Knightley, Jack Jones",Sunday,Left Field,52,33,15:00 - 16:00,15:00,16:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:00
Shy Fx,Sunday,Levels,42,44,15:00 - 16:00,15:00,16:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:00
Plumm,Sunday,Lunched Out Lizards,0,0,15:00 - 16:00,15:00,16:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:00
Flogan,Sunday,Mandala Stage,0,0,15:00 - 16:00,15:00,16:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:00
James,Sunday,Other Stage,47,34,15:00 - 16:00,15:00,16:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:00
Scarlett O'Malley,Sunday,San Remo,45,47,15:00 - 16:30,15:00,16:30,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:30
Fat Barry'S Bingo Bango Bongo,Sunday,Sensation Seekers Stage,0,0,15:00 - 15:30,15:00,15:30,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 15:30
Every Struggle Writes A Song - Seize The Day,Sunday,Speakers Forum,0,0,15:00 - 16:00,15:00,16:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:00
Hagop Tchaparian + Anish Kumar,Sunday,Stonebridge Bar,42,18,15:00 - 17:00,15:00,17:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 17:00
Charles Hendy (Mary Wallopers),Sunday,Strummerville,48,12,15:00 - 16:00,15:00,16:00,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 16:00
Hawkeye & Hoe Band,Sunday,The Bandstand,56,38,15:00 - 15:40,15:00,15:40,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 15:40
Chinnen,Sunday,The Pavement,0,0,15:00 - 15:30,15:00,15:30,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 15:30
Anyone For Tennis,Sunday,Walkabouts,60,33,15:00 - 15:45,15:00,15:45,30/06/2024,30/06/2024,30/06/2024 15:00,30/06/2024 15:45
Laura London & Jake Francis,Sunday,Walkabouts,60,33,15:05 - 15:50,15:05,15:50,30/06/2024,30/06/2024,30/06/2024 15:05,30/06/2024 15:50
Head Over Wheels,Sunday,Circus Big Top,57,34,15:06 - 15:14,15:06,15:14,30/06/2024,30/06/2024,30/06/2024 15:06,30/06/2024 15:14
Tony And Ray,Sunday,The Glebe,60,33,15:10 - 15:25,15:10,15:25,30/06/2024,30/06/2024,30/06/2024 15:10,30/06/2024 15:25
The Ayoub Sisters,Sunday,The Hive,0,0,15:10 - 15:40,15:10,15:40,30/06/2024,30/06/2024,30/06/2024 15:10,30/06/2024 15:40
Dapper Chaps,Sunday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,30/06/2024,30/06/2024,30/06/2024 15:10,30/06/2024 15:55
Hairy Hatter,Sunday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,30/06/2024,30/06/2024,30/06/2024 15:10,30/06/2024 15:55
Jack Thomson,Sunday,Walkabouts,60,33,15:10 - 15:55,15:10,15:55,30/06/2024,30/06/2024,30/06/2024 15:10,30/06/2024 15:55
The Doogans,Sunday,Outside Circus Stage,59,33,15:13 - 15:43,15:13,15:43,30/06/2024,30/06/2024,30/06/2024 15:13,30/06/2024 15:43
Eva Lazarus Live Av,Sunday,Glade,51,29,15:15 - 16:05,15:15,16:05,30/06/2024,30/06/2024,30/06/2024 15:15,30/06/2024 16:05
Hula Hoops With Helen Rooney,Sunday,Humblewell Active Platform,42,21,15:15 - 16:00,15:15,16:00,30/06/2024,30/06/2024,30/06/2024 15:15,30/06/2024 16:00
Mdou Moctar,Sunday,The Park Stage,41,19,15:15 - 16:00,15:15,16:00,30/06/2024,30/06/2024,30/06/2024 15:15,30/06/2024 16:00
The Crows,Sunday,Walkabouts,60,33,15:15 - 15:45,15:15,15:45,30/06/2024,30/06/2024,30/06/2024 15:15,30/06/2024 15:45
The Black Eagles,Sunday,Circus Big Top,57,34,15:19 - 15:44,15:19,15:44,30/06/2024,30/06/2024,30/06/2024 15:19,30/06/2024 15:44
Via Trio,Sunday,Toad Hall,0,0,15:20 - 16:00,15:20,16:00,30/06/2024,30/06/2024,30/06/2024 15:20,30/06/2024 16:00
The Wardens,Sunday,Walkabouts,60,33,15:20 - 15:50,15:20,15:50,30/06/2024,30/06/2024,30/06/2024 15:20,30/06/2024 15:50
The Scratch,Sunday,Avalon Stage,66,38,15:25 - 16:20,15:25,16:20,30/06/2024,30/06/2024,30/06/2024 15:25,30/06/2024 16:20
Figs In Wigs - Astrology Bingo!,Sunday,10 Aces,0,0,15:30 - 16:10,15:30,16:10,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:10
Freddieno Show,Sunday,A Little More Sensation,0,0,15:30 - 16:00,15:30,16:00,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:00
Sabiyha,Sunday,Bbc Music Introducing,45,44,15:30 - 16:00,15:30,16:00,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:00
Ben Hemming,Sunday,Croissant Neuf Bandstand,55,21,15:30 - 16:00,15:30,16:00,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:00
Dance Class: Samba,Sunday,Glasto Latino,58,27,15:30 - 16:30,15:30,16:30,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:30
Porij,Sunday,Lonely Hearts Club,44,41,15:30 - 16:30,15:30,16:30,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:30
Hayley Wallace,Sunday,Nowhere,0,0,15:30 - 16:00,15:30,16:00,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:00
Compère: Dan Evans,Sunday,The Astrolabe Theatre,0,0,15:30 - 19:00,15:30,19:00,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 19:00
Faces Of Disco,Sunday,The Glebe,60,33,15:30 - 16:00,15:30,16:00,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:00
Fortuni And Fae,Sunday,Walkabouts,60,33,15:30 - 16:15,15:30,16:15,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:15
Meanderthals,Sunday,Walkabouts,60,33,15:30 - 16:15,15:30,16:15,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:15
Steel Pulse,Sunday,West Holts Stage,57,31,15:30 - 16:30,15:30,16:30,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:30
Midlife Crisis (Dj Set),Sunday,Wishing Well,42,20,15:30 - 16:00,15:30,16:00,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:00
Blondshell,Sunday,Woodsies,43,52,15:30 - 16:30,15:30,16:30,30/06/2024,30/06/2024,30/06/2024 15:30,30/06/2024 16:30
Ian Stone,Sunday,Cabaret,62,26,15:35 - 16:05,15:35,16:05,30/06/2024,30/06/2024,30/06/2024 15:35,30/06/2024 16:05
Taiko Meantime,Sunday,Sensation Seekers Stage,0,0,15:35 - 16:20,15:35,16:20,30/06/2024,30/06/2024,30/06/2024 15:35,30/06/2024 16:20
Rod Laver,Sunday,The Astrolabe Theatre,0,0,15:35 - 15:50,15:35,15:50,30/06/2024,30/06/2024,30/06/2024 15:35,30/06/2024 15:50
Mellowmatic,Sunday,The Gateway,0,0,15:35 - 16:20,15:35,16:20,30/06/2024,30/06/2024,30/06/2024 15:35,30/06/2024 16:20
Mr Peewee And His Drumming Puppet,Sunday,The Pavement,0,0,15:35 - 16:05,15:35,16:05,30/06/2024,30/06/2024,30/06/2024 15:35,30/06/2024 16:05
Clamour Of Bells,Sunday,Walkabouts,60,33,15:35 - 15:35,15:35,15:35,30/06/2024,30/06/2024,30/06/2024 15:35,30/06/2024 15:35
Kane And Abel Magic,Sunday,Walkabouts,60,33,15:35 - 16:05,15:35,16:05,30/06/2024,30/06/2024,30/06/2024 15:35,30/06/2024 16:05
The Bad Eggs,Sunday,Walkabouts,60,33,15:35 - 16:20,15:35,16:20,30/06/2024,30/06/2024,30/06/2024 15:35,30/06/2024 16:20
The Midwives,Sunday,Walkabouts,60,33,15:40 - 16:25,15:40,16:25,30/06/2024,30/06/2024,30/06/2024 15:40,30/06/2024 16:25
The Trifleenees,Sunday,Walkabouts,60,33,15:40 - 16:25,15:40,16:25,30/06/2024,30/06/2024,30/06/2024 15:40,30/06/2024 16:25
Sav - Head Of Magic,Sunday,Walkabouts,60,33,15:40 - 17:40,15:40,17:40,30/06/2024,30/06/2024,30/06/2024 15:40,30/06/2024 17:40
Mama Tokus,Sunday,Crooner'S Corner,0,0,15:45 - 16:30,15:45,16:30,30/06/2024,30/06/2024,30/06/2024 15:45,30/06/2024 16:30
Songer,Sunday,Greenpeace,55,26,15:45 - 16:30,15:45,16:30,30/06/2024,30/06/2024,30/06/2024 15:45,30/06/2024 16:30
Gong Bath With Yogic Sound,Sunday,Humblewell Retreat Yurt,42,21,15:45 - 16:45,15:45,16:45,30/06/2024,30/06/2024,30/06/2024 15:45,30/06/2024 16:45
Shania Twain,Sunday,Pyramid Stage,51,43,15:45 - 17:00,15:45,17:00,30/06/2024,30/06/2024,30/06/2024 15:45,30/06/2024 17:00
Ms Pink,Sunday,The Hive,0,0,15:45 - 16:45,15:45,16:45,30/06/2024,30/06/2024,30/06/2024 15:45,30/06/2024 16:45
Bell And Bullock,Sunday,Walkabouts,60,33,15:45 - 16:15,15:45,16:15,30/06/2024,30/06/2024,30/06/2024 15:45,30/06/2024 16:15
Louvre On The Move,Sunday,Walkabouts,60,33,15:45 - 16:15,15:45,16:15,30/06/2024,30/06/2024,30/06/2024 15:45,30/06/2024 16:15
Football Crazy,Sunday,Walkabouts,60,33,15:45 - 16:30,15:45,16:30,30/06/2024,30/06/2024,30/06/2024 15:45,30/06/2024 16:30
The Space Cowboy,Sunday,Outside Circus Stage,59,33,15:48 - 16:18,15:48,16:18,30/06/2024,30/06/2024,30/06/2024 15:48,30/06/2024 16:18
Cirk Hes Presents Sorrel,Sunday,Circus Big Top,57,34,15:49 - 15:55,15:49,15:55,30/06/2024,30/06/2024,30/06/2024 15:49,30/06/2024 15:55
R J Hunter,Sunday,Poetry&Words,0,0,15:49 - 16:14,15:49,16:14,30/06/2024,30/06/2024,30/06/2024 15:49,30/06/2024 16:14
Mark Bruce Dance Company,Sunday,The Astrolabe Theatre,0,0,15:50 - 16:00,15:50,16:00,30/06/2024,30/06/2024,30/06/2024 15:50,30/06/2024 16:00
Gnomes,Sunday,Walkabouts,60,33,15:50 - 16:35,15:50,16:35,30/06/2024,30/06/2024,30/06/2024 15:50,30/06/2024 16:35
The Tea Ladies On Tour,Sunday,Walkabouts,60,33,15:50 - 16:35,15:50,16:35,30/06/2024,30/06/2024,30/06/2024 15:50,30/06/2024 16:35
Nicola Cruz [25 Years Of Fabric],Sunday,Assembly,40,42,16:00 - 18:00,16:00,18:00,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 18:00
"Ying, Oh Annie Oh, Dj Cleanshirt & Mc Dandan",Sunday,Babylon Uprising,0,0,16:00 - 17:00,16:00,17:00,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 17:00
Compère: Laura Smyth,Sunday,Cabaret,62,26,16:00 - 20:00,16:00,20:00,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 20:00
Toby Walker,Sunday,Circus Big Top,57,34,16:00 - 16:08,16:00,16:08,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 16:08
The Barefoot Bandit,Sunday,Croissant Neuf,55,21,16:00 - 17:00,16:00,17:00,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 17:00
Booty Bass [St Paul'S Carnival Takeover],Sunday,Firmly Rooted,43,43,16:00 - 17:00,16:00,17:00,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 17:00
Harry Mccanna,Sunday,Glade Dome,49,29,16:00 - 17:30,16:00,17:30,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 17:30
Cbbc'S Laura & Alex,Sunday,Kidzfield Big Top,0,0,16:00 - 16:30,16:00,16:30,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 16:30
Sounds Of Space,Sunday,Laboratory Stage,0,0,16:00 - 16:45,16:00,16:45,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 16:45
Clipz,Sunday,Levels,42,44,16:00 - 17:00,16:00,17:00,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 17:00
"Workshop: Holly Roxanne, Open Your Voice",Sunday,Scissors,42,21,16:00 - 17:00,16:00,17:00,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 17:00
Green Beat (Dj),Sunday,Strummerville,48,12,16:00 - 16:45,16:00,16:45,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 16:45
Leburnicus,Sunday,The Bandstand,56,38,16:00 - 16:40,16:00,16:40,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 16:40
Asha Gold,Sunday,Wishing Well,42,20,16:00 - 16:30,16:00,16:30,30/06/2024,30/06/2024,30/06/2024 16:00,30/06/2024 16:30
Grant Goldie,Sunday,A Little More Sensation,0,0,16:05 - 16:35,16:05,16:35,30/06/2024,30/06/2024,30/06/2024 16:05,30/06/2024 16:35
George Egg'S Set Menu,Sunday,The Astrolabe Theatre,0,0,16:05 - 17:05,16:05,17:05,30/06/2024,30/06/2024,30/06/2024 16:05,30/06/2024 17:05
Go Bananas,Sunday,The Glebe,60,33,16:05 - 16:35,16:05,16:35,30/06/2024,30/06/2024,30/06/2024 16:05,30/06/2024 16:35
Roo'D,Sunday,Walkabouts,60,33,16:05 - 16:35,16:05,16:35,30/06/2024,30/06/2024,30/06/2024 16:05,30/06/2024 16:35
The Explorers,Sunday,Walkabouts,60,33,16:05 - 17:05,16:05,17:05,30/06/2024,30/06/2024,30/06/2024 16:05,30/06/2024 17:05
Bernard Butler,Sunday,Acoustic Stage,66,38,16:10 - 17:00,16:10,17:00,30/06/2024,30/06/2024,30/06/2024 16:10,30/06/2024 17:00
Maisie Adam,Sunday,Cabaret,62,26,16:10 - 16:40,16:10,16:40,30/06/2024,30/06/2024,30/06/2024 16:10,30/06/2024 16:40
Ekleido Dance - Splice,Sunday,The Pavement,0,0,16:10 - 16:25,16:10,16:25,30/06/2024,30/06/2024,30/06/2024 16:10,30/06/2024 16:25
Leo,Sunday,Circus Big Top,57,34,16:13 - 16:19,16:13,16:19,30/06/2024,30/06/2024,30/06/2024 16:13,30/06/2024 16:19
Gillie,Sunday,Toad Hall,0,0,16:15 - 17:00,16:15,17:00,30/06/2024,30/06/2024,30/06/2024 16:15,30/06/2024 17:00
Celestials,Sunday,Walkabouts,60,33,16:15 - 16:45,16:15,16:45,30/06/2024,30/06/2024,30/06/2024 16:15,30/06/2024 16:45
Malaika Kegode (Poet In Residence),Sunday,Poetry&Words,0,0,16:17 - 16:37,16:17,16:37,30/06/2024,30/06/2024,30/06/2024 16:17,30/06/2024 16:37
Compères: Tamara And Dave,Sunday,Outside Circus Stage,59,33,16:18 - 20:34,16:18,20:34,30/06/2024,30/06/2024,30/06/2024 16:18,30/06/2024 20:34
Cash Cows,Sunday,10 Aces,0,0,16:20 - 17:10,16:20,17:10,30/06/2024,30/06/2024,30/06/2024 16:20,30/06/2024 17:10
The Jukeboxes,Sunday,Walkabouts,60,33,16:20 - 17:50,16:20,17:50,30/06/2024,30/06/2024,30/06/2024 16:20,30/06/2024 17:50
Incandescence Presents Trio Jolee,Sunday,Outside Circus Stage,59,33,16:23 - 16:30,16:23,16:30,30/06/2024,30/06/2024,30/06/2024 16:23,30/06/2024 16:30
Jon Udry,Sunday,Circus Big Top,57,34,16:24 - 16:49,16:24,16:49,30/06/2024,30/06/2024,30/06/2024 16:24,30/06/2024 16:49
Paris Paloma,Sunday,Bbc Music Introducing,45,44,16:30 - 17:00,16:30,17:00,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:00
Dance Class: Salsa,Sunday,Glasto Latino,58,27,16:30 - 17:30,16:30,17:30,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:30
Pillow Queens,Sunday,Left Field,52,33,16:30 - 17:00,16:30,17:00,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:00
Georgia Duncan,Sunday,Lunched Out Lizards,0,0,16:30 - 17:30,16:30,17:30,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:30
Tba,Sunday,Mandala Stage,0,0,16:30 - 17:30,16:30,17:30,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:30
Nothing But Thieves,Sunday,Other Stage,47,34,16:30 - 17:30,16:30,17:30,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:30
Guardians Of The Galaxy Vol.3 12,Sunday,Pilton Palais Cinema,64,36,16:30 - 19:00,16:30,19:00,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 19:00
Kim Ann Foxman,Sunday,San Remo,45,47,16:30 - 18:00,16:30,18:00,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 18:00
Old Time Sailors,Sunday,Sensation Seekers Stage,0,0,16:30 - 17:30,16:30,17:30,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:30
Baxter Dury,Sunday,The Park Stage,41,19,16:30 - 17:30,16:30,17:30,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:30
Dan The Hat,Sunday,The Pavement,0,0,16:30 - 17:00,16:30,17:00,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:00
Circus Raj,Sunday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:15
The Suitcase Escape Game,Sunday,Walkabouts,60,33,16:30 - 17:15,16:30,17:15,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:15
Junior Jungle (Dj Set),Sunday,Wishing Well,42,20,16:30 - 17:15,16:30,17:15,30/06/2024,30/06/2024,30/06/2024 16:30,30/06/2024 17:15
Henge,Sunday,Glade,51,29,16:35 - 17:45,16:35,17:45,30/06/2024,30/06/2024,30/06/2024 16:35,30/06/2024 17:45
Duo Santus,Sunday,Outside Circus Stage,59,33,16:35 - 16:42,16:35,16:42,30/06/2024,30/06/2024,30/06/2024 16:35,30/06/2024 16:42
Lekiddo Lord Of The Lobsters,Sunday,The Gateway,0,0,16:35 - 17:05,16:35,17:05,30/06/2024,30/06/2024,30/06/2024 16:35,30/06/2024 17:05
Tony And Ray,Sunday,A Little More Sensation,0,0,16:40 - 17:10,16:40,17:10,30/06/2024,30/06/2024,30/06/2024 16:40,30/06/2024 17:10
Talitha Wing (2023 Slam Winner),Sunday,Poetry&Words,0,0,16:40 - 17:00,16:40,17:00,30/06/2024,30/06/2024,30/06/2024 16:40,30/06/2024 17:00
Jack Defrost - Traceworks Dance,Sunday,The Glebe,60,33,16:40 - 16:55,16:40,16:55,30/06/2024,30/06/2024,30/06/2024 16:40,30/06/2024 16:55
Vertigo Stilts,Sunday,Walkabouts,60,33,16:40 - 17:25,16:40,17:25,30/06/2024,30/06/2024,30/06/2024 16:40,30/06/2024 17:25
Bassey Bewitched,Sunday,Cabaret,62,26,16:45 - 17:05,16:45,17:05,30/06/2024,30/06/2024,30/06/2024 16:45,30/06/2024 17:05
The Basil Brush Show,Sunday,Kidzfield Big Top,0,0,16:45 - 17:15,16:45,17:15,30/06/2024,30/06/2024,30/06/2024 16:45,30/06/2024 17:15
Elkka [Live],Sunday,Lonely Hearts Club,44,41,16:45 - 17:45,16:45,17:45,30/06/2024,30/06/2024,30/06/2024 16:45,30/06/2024 17:45
Gentleman George,Sunday,The Hive,0,0,16:45 - 17:45,16:45,17:45,30/06/2024,30/06/2024,30/06/2024 16:45,30/06/2024 17:45
Alice And Alice,Sunday,Walkabouts,60,33,16:45 - 17:30,16:45,17:30,30/06/2024,30/06/2024,30/06/2024 16:45,30/06/2024 17:30
Venus,Sunday,Outside Circus Stage,59,33,16:47 - 17:17,16:47,17:17,30/06/2024,30/06/2024,30/06/2024 16:47,30/06/2024 17:17
The Go! Team,Sunday,Avalon Stage,66,38,16:50 - 17:50,16:50,17:50,30/06/2024,30/06/2024,30/06/2024 16:50,30/06/2024 17:50
Scary & Spooky Skeletons,Sunday,Walkabouts,60,33,16:50 - 17:35,16:50,17:35,30/06/2024,30/06/2024,30/06/2024 16:50,30/06/2024 17:35
Circus Funtasia,Sunday,Circus Big Top,57,34,16:59 - 18:09,16:59,18:09,30/06/2024,30/06/2024,30/06/2024 16:59,30/06/2024 18:09
"Songwriters Arc Chris Difford With Beth Nielsen Chapman, Guy Chambers, Sid Griffin & Jessie Reid",Sunday,Acoustic Stage,66,38,17:00 - 18:00,17:00,18:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 18:00
"Atki2, Dub Boy & Jonesy Wales",Sunday,Babylon Uprising,0,0,17:00 - 19:00,17:00,19:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 19:00
Kelvin 373,Sunday,Blind Tiger,0,0,17:00 - 17:40,17:00,17:40,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 17:40
Dj Iona,Sunday,Cornish Arms,0,0,17:00 - 19:00,17:00,19:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 19:00
Gracie Barry Tait,Sunday,Crooner'S Corner,0,0,17:00 - 17:45,17:00,17:45,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 17:45
Grove [Dj] [St Paul'S Carnival Takeover],Sunday,Firmly Rooted,43,43,17:00 - 18:00,17:00,18:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 18:00
Funke And The Two Tone Baby,Sunday,Greenpeace,55,26,17:00 - 17:45,17:00,17:45,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 17:45
Y U Qt,Sunday,Levels,42,44,17:00 - 18:30,17:00,18:30,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 18:30
Phill Welch & Maslow Unknown,Sunday,Meeting Place Bar,0,0,17:00 - 20:00,17:00,20:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 20:00
Slam (Hosted By Dominic Berry And Culain Wood),Sunday,Poetry&Words,0,0,17:00 - 19:00,17:00,19:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 19:00
Trippin Takeover,Sunday,Stonebridge Bar,42,18,17:00 - 18:00,17:00,18:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 18:00
Lizzie Esau,Sunday,Strummerville,48,12,17:00 - 17:40,17:00,17:40,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 17:40
Shamanism & Civilisation With Graham Hancock,Sunday,Temple Uprising,0,0,17:00 - 18:00,17:00,18:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 18:00
King Dinosaur,Sunday,The Bandstand,56,38,17:00 - 17:40,17:00,17:40,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 17:40
Andy Cato B2B Spooky Cash Cash,Sunday,The Bug,41,25,17:00 - 18:00,17:00,18:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 18:00
Kane & Abel,Sunday,The Glebe,60,33,17:00 - 17:30,17:00,17:30,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 17:30
Swyron & Desaata,Sunday,Walkabouts,60,33,17:00 - 17:45,17:00,17:45,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 17:45
Jordan Rakei,Sunday,West Holts Stage,57,31,17:00 - 18:00,17:00,18:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 18:00
Alvvays,Sunday,Woodsies,43,52,17:00 - 18:00,17:00,18:00,30/06/2024,30/06/2024,30/06/2024 17:00,30/06/2024 18:00
Akira,Sunday,The Pavement,0,0,17:05 - 17:35,17:05,17:35,30/06/2024,30/06/2024,30/06/2024 17:05,30/06/2024 17:35
Frank Sanazi & Dean Stalin,Sunday,Cabaret,62,26,17:10 - 17:40,17:10,17:40,30/06/2024,30/06/2024,30/06/2024 17:10,30/06/2024 17:40
The Very Best Of Tommy Cooper,Sunday,The Astrolabe Theatre,0,0,17:10 - 18:10,17:10,18:10,30/06/2024,30/06/2024,30/06/2024 17:10,30/06/2024 18:10
Jack Thomson,Sunday,Walkabouts,60,33,17:10 - 17:55,17:10,17:55,30/06/2024,30/06/2024,30/06/2024 17:10,30/06/2024 17:55
"Workshop: Daisy Doris May, Developing Your Drag King",Sunday,Scissors,42,21,17:15 - 18:00,17:15,18:00,30/06/2024,30/06/2024,30/06/2024 17:15,30/06/2024 18:00
New York Brass Band,Sunday,The Gateway,0,0,17:15 - 17:45,17:15,17:45,30/06/2024,30/06/2024,30/06/2024 17:15,30/06/2024 17:45
Hodamadoddery,Sunday,Toad Hall,0,0,17:15 - 18:00,17:15,18:00,30/06/2024,30/06/2024,30/06/2024 17:15,30/06/2024 18:00
Stacky,Sunday,Village Inn,0,0,17:15 - 19:15,17:15,19:15,30/06/2024,30/06/2024,30/06/2024 17:15,30/06/2024 19:15
Liver Cottage,Sunday,Walkabouts,60,33,17:15 - 18:00,17:15,18:00,30/06/2024,30/06/2024,30/06/2024 17:15,30/06/2024 18:00
The Fairy Godmother And The Tooth Fairy,Sunday,Walkabouts,60,33,17:15 - 18:00,17:15,18:00,30/06/2024,30/06/2024,30/06/2024 17:15,30/06/2024 18:00
Moonchild Sanelly,Sunday,Wishing Well,42,20,17:15 - 18:00,17:15,18:00,30/06/2024,30/06/2024,30/06/2024 17:15,30/06/2024 18:00
Red Hot Riot,Sunday,10 Aces,0,0,17:20 - 18:00,17:20,18:00,30/06/2024,30/06/2024,30/06/2024 17:20,30/06/2024 18:00
Hairy Hatter,Sunday,Walkabouts,60,33,17:20 - 18:05,17:20,18:05,30/06/2024,30/06/2024,30/06/2024 17:20,30/06/2024 18:05
Cirk Hes Presents Aerial Sensation,Sunday,Outside Circus Stage,59,33,17:22 - 17:34,17:22,17:34,30/06/2024,30/06/2024,30/06/2024 17:22,30/06/2024 17:34
Antony Szmierek,Sunday,Bbc Music Introducing,45,44,17:30 - 18:00,17:30,18:00,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 18:00
Problem Patterns,Sunday,Bread And Roses,0,0,17:30 - 18:30,17:30,18:30,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 18:30
Blackberry Wood,Sunday,Croissant Neuf,55,21,17:30 - 18:30,17:30,18:30,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 18:30
Casey Spillman B2B Julian Anthony,Sunday,Glade Dome,49,29,17:30 - 19:00,17:30,19:00,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 19:00
Dance Class: Reggaeton,Sunday,Glasto Latino,58,27,17:30 - 18:30,17:30,18:30,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 18:30
Roger Mcgough'S 'The Sound Collector',Sunday,Kidzfield Big Top,0,0,17:30 - 18:00,17:30,18:00,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 18:00
Will Varley,Sunday,Left Field,52,33,17:30 - 18:10,17:30,18:10,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 18:10
Lizard Djs,Sunday,Lunched Out Lizards,0,0,17:30 - 19:00,17:30,19:00,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 19:00
Close,Sunday,Sensation Seekers Stage,0,0,17:30 - 22:15,17:30,22:15,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 22:15
Meanderthals,Sunday,Walkabouts,60,33,17:30 - 18:15,17:30,18:15,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 18:15
Space Cadets,Sunday,Walkabouts,60,33,17:30 - 18:15,17:30,18:15,30/06/2024,30/06/2024,30/06/2024 17:30,30/06/2024 18:15
Chinnen,Sunday,Outside Circus Stage,59,33,17:39 - 18:09,17:39,18:09,30/06/2024,30/06/2024,30/06/2024 17:39,30/06/2024 18:09
Gwyn Selector,Sunday,Blind Tiger,0,0,17:40 - 18:20,17:40,18:20,30/06/2024,30/06/2024,30/06/2024 17:40,30/06/2024 18:20
Spencer Jones,Sunday,Cabaret,62,26,17:45 - 18:05,17:45,18:05,30/06/2024,30/06/2024,30/06/2024 17:45,30/06/2024 18:05
Danny Howard And Friends,Sunday,Greenpeace,55,26,17:45 - 19:30,17:45,19:30,30/06/2024,30/06/2024,30/06/2024 17:45,30/06/2024 19:30
Janelle Monae,Sunday,Pyramid Stage,51,43,17:45 - 18:45,17:45,18:45,30/06/2024,30/06/2024,30/06/2024 17:45,30/06/2024 18:45
Celestials,Sunday,Walkabouts,60,33,17:45 - 18:15,17:45,18:15,30/06/2024,30/06/2024,30/06/2024 17:45,30/06/2024 18:15
The Wardens,Sunday,Walkabouts,60,33,17:45 - 18:15,17:45,18:15,30/06/2024,30/06/2024,30/06/2024 17:45,30/06/2024 18:15
Laura London & Jake Francis,Sunday,Walkabouts,60,33,17:45 - 18:30,17:45,18:30,30/06/2024,30/06/2024,30/06/2024 17:45,30/06/2024 18:30
Session Victim,Sunday,Glade,51,29,17:55 - 18:55,17:55,18:55,30/06/2024,30/06/2024,30/06/2024 17:55,30/06/2024 18:55
Craig Richards B2B Francesco Del Garda [25 Years Of Fabric],Sunday,Assembly,40,42,18:00 - 20:00,18:00,20:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 20:00
Silver Snipa B2B Vxrgo [30 Years Of Metalheadz],Sunday,Firmly Rooted,43,43,18:00 - 19:00,18:00,19:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 19:00
L-Vis 1990,Sunday,Genosys,0,0,18:00 - 21:00,18:00,21:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 21:00
Hak Baker,Sunday,Lonely Hearts Club,44,41,18:00 - 19:00,18:00,19:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 19:00
Dj Basil B,Sunday,Mandala Stage,0,0,18:00 - 19:00,18:00,19:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 19:00
Syreeta *Ukg Special,Sunday,Nowhere,0,0,18:00 - 19:00,18:00,19:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 19:00
Avril Lavigne,Sunday,Other Stage,47,34,18:00 - 19:00,18:00,19:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 19:00
Erol Alkan B2B Palms Trax,Sunday,San Remo,45,47,18:00 - 20:00,18:00,20:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 20:00
Bradley Zero B2B Batu,Sunday,Stonebridge Bar,42,18,18:00 - 19:00,18:00,19:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 19:00
Miss Beans,Sunday,Strummerville,48,12,18:00 - 18:45,18:00,18:45,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 18:45
Phil Hartnoll B2B Conradical,Sunday,The Bug,41,25,18:00 - 19:00,18:00,19:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 19:00
Mas Que Nada Takeover: Kiimi (Live),Sunday,The Hive,0,0,18:00 - 19:00,18:00,19:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 19:00
Mount Kimbie,Sunday,The Park Stage,41,19,18:00 - 19:00,18:00,19:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 19:00
Ruby Cross,Sunday,West Holts Bar,59,29,18:00 - 18:30,18:00,18:30,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 18:30
Woody Cook (Dj Set),Sunday,Wishing Well,42,20,18:00 - 19:00,18:00,19:00,30/06/2024,30/06/2024,30/06/2024 18:00,30/06/2024 19:00
Paul Foot - Dissolve,Sunday,Cabaret,62,26,18:10 - 19:05,18:10,19:05,30/06/2024,30/06/2024,30/06/2024 18:10,30/06/2024 19:05
Rob Roy Collins,Sunday,Outside Circus Stage,59,33,18:14 - 18:44,18:14,18:44,30/06/2024,30/06/2024,30/06/2024 18:14,30/06/2024 18:44
The Flying Seagull Project,Sunday,Kidzfield Big Top,0,0,18:15 - 18:45,18:15,18:45,30/06/2024,30/06/2024,30/06/2024 18:15,30/06/2024 18:45
Beyond Repair Dance,Sunday,The Astrolabe Theatre,0,0,18:15 - 18:45,18:15,18:45,30/06/2024,30/06/2024,30/06/2024 18:15,30/06/2024 18:45
The Marching Skaletons,Sunday,The Bandstand,56,38,18:15 - 19:00,18:15,19:00,30/06/2024,30/06/2024,30/06/2024 18:15,30/06/2024 19:00
Bethan Lloyd,Sunday,Toad Hall,0,0,18:15 - 19:05,18:15,19:05,30/06/2024,30/06/2024,30/06/2024 18:15,30/06/2024 19:05
Baby Queen,Sunday,Avalon Stage,66,38,18:20 - 19:20,18:20,19:20,30/06/2024,30/06/2024,30/06/2024 18:20,30/06/2024 19:20
Chezney,Sunday,Blind Tiger,0,0,18:20 - 19:00,18:20,19:00,30/06/2024,30/06/2024,30/06/2024 18:20,30/06/2024 19:00
London Community Gospel Choir,Sunday,Acoustic Stage,66,38,18:30 - 19:30,18:30,19:30,30/06/2024,30/06/2024,30/06/2024 18:30,30/06/2024 19:30
Deja,Sunday,Bbc Music Introducing,45,44,18:30 - 19:00,18:30,19:00,30/06/2024,30/06/2024,30/06/2024 18:30,30/06/2024 19:00
Interplanetary Criminal,Sunday,Levels,42,44,18:30 - 20:00,18:30,20:00,30/06/2024,30/06/2024,30/06/2024 18:30,30/06/2024 20:00
Louvre On The Move,Sunday,Walkabouts,60,33,18:30 - 19:00,18:30,19:00,30/06/2024,30/06/2024,30/06/2024 18:30,30/06/2024 19:00
Brittany Howard,Sunday,West Holts Stage,57,31,18:30 - 18:30,18:30,18:30,30/06/2024,30/06/2024,30/06/2024 18:30,30/06/2024 18:30
Kim Gordon,Sunday,Woodsies,43,52,18:30 - 19:30,18:30,19:30,30/06/2024,30/06/2024,30/06/2024 18:30,30/06/2024 19:30
Lottery Winners,Sunday,Left Field,52,33,18:35 - 19:15,18:35,19:15,30/06/2024,30/06/2024,30/06/2024 18:35,30/06/2024 19:15
Nature Is Noisy,Sunday,Croissant Neuf Bandstand,55,21,18:45 - 21:45,18:45,21:45,30/06/2024,30/06/2024,30/06/2024 18:45,30/06/2024 21:45
Incandescence Presents Trio Jolee,Sunday,Outside Circus Stage,59,33,18:49 - 18:57,18:49,18:57,30/06/2024,30/06/2024,30/06/2024 18:49,30/06/2024 18:57
An Evening Without Kate Bush,Sunday,The Astrolabe Theatre,0,0,18:50 - 20:00,18:50,20:00,30/06/2024,30/06/2024,30/06/2024 18:50,30/06/2024 20:00
Gridlock In Parliament,Sunday,Babylon Uprising,0,0,19:00 - 02:45,19:00,02:45,30/06/2024,01/07/2024,30/06/2024 19:00,01/07/2024 02:45
Oliver Sudden,Sunday,Blind Tiger,0,0,19:00 - 20:00,19:00,20:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:00
Jo Bucket,Sunday,Carhenge,58,36,19:00 - 20:00,19:00,20:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:00
Kooki (Positive Sound System),Sunday,Cornish Arms,0,0,19:00 - 20:00,19:00,20:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:00
Submotive [30 Yrs Of Metalheadz],Sunday,Firmly Rooted,43,43,19:00 - 20:00,19:00,20:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:00
Syreeta,Sunday,Glade Dome,49,29,19:00 - 20:30,19:00,20:30,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:30
Dolly Mavies,Sunday,Lunched Out Lizards,0,0,19:00 - 20:00,19:00,20:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:00
Rio B2B Randall,Sunday,Nowhere,0,0,19:00 - 20:00,19:00,20:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:00
Saliah,Sunday,Stonebridge Bar,42,18,19:00 - 20:00,19:00,20:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:00
Bel Cobain,Sunday,Strummerville,48,12,19:00 - 19:40,19:00,19:40,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 19:40
Woody Cook,Sunday,The Bug,41,25,19:00 - 20:00,19:00,20:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:00
Mas Que Nada Takeover: Osmaan,Sunday,The Hive,0,0,19:00 - 20:00,19:00,20:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:00
Mae Challis Live!,Sunday,The Taphouse,0,0,19:00 - 21:00,19:00,21:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 21:00
Stone Jets,Sunday,Wishing Well,42,20,19:00 - 20:00,19:00,20:00,30/06/2024,30/06/2024,30/06/2024 19:00,30/06/2024 20:00
Tba,Sunday,Outside Circus Stage,59,33,19:02 - 19:32,19:02,19:32,30/06/2024,30/06/2024,30/06/2024 19:02,30/06/2024 19:32
Logic1000,Sunday,Glade,51,29,19:05 - 20:20,19:05,20:20,30/06/2024,30/06/2024,30/06/2024 19:05,30/06/2024 20:20
The Pansy Boys,Sunday,Cabaret,62,26,19:10 - 19:40,19:10,19:40,30/06/2024,30/06/2024,30/06/2024 19:10,30/06/2024 19:40
Tolstoys,Sunday,The Bandstand,56,38,19:20 - 20:00,19:20,20:00,30/06/2024,30/06/2024,30/06/2024 19:20,30/06/2024 20:00
Tba,Sunday,Bbc Music Introducing,45,44,19:30 - 20:00,19:30,20:00,30/06/2024,30/06/2024,30/06/2024 19:30,30/06/2024 20:00
Hold A Corner,Sunday,Greenpeace,55,26,19:30 - 20:30,19:30,20:30,30/06/2024,30/06/2024,30/06/2024 19:30,30/06/2024 20:30
Fat Dog,Sunday,Lonely Hearts Club,44,41,19:30 - 20:30,19:30,20:30,30/06/2024,30/06/2024,30/06/2024 19:30,30/06/2024 20:30
Nosferatu (1922) + Intro With Dan Smith And Live Score By Chris Green Pg,Sunday,Pilton Palais Cinema,64,36,19:30 - 21:10,19:30,21:10,30/06/2024,30/06/2024,30/06/2024 19:30,30/06/2024 21:10
Burna Boy,Sunday,Pyramid Stage,51,43,19:30 - 20:30,19:30,20:30,30/06/2024,30/06/2024,30/06/2024 19:30,30/06/2024 20:30
Ghetts,Sunday,The Park Stage,41,19,19:30 - 20:30,19:30,20:30,30/06/2024,30/06/2024,30/06/2024 19:30,30/06/2024 20:30
Dean King,Sunday,West Holts Bar,59,29,19:30 - 20:00,19:30,20:00,30/06/2024,30/06/2024,30/06/2024 19:30,30/06/2024 20:00
Bexi - Barbarella,Sunday,Outside Circus Stage,59,33,19:37 - 19:44,19:37,19:44,30/06/2024,30/06/2024,30/06/2024 19:37,30/06/2024 19:44
Spliff Richard,Sunday,Cabaret,62,26,19:45 - 20:15,19:45,20:15,30/06/2024,30/06/2024,30/06/2024 19:45,30/06/2024 20:15
The Farm,Sunday,Left Field,52,33,19:45 - 20:30,19:45,20:30,30/06/2024,30/06/2024,30/06/2024 19:45,30/06/2024 20:30
Two Door Cinema Club,Sunday,Other Stage,47,34,19:45 - 20:45,19:45,20:45,30/06/2024,30/06/2024,30/06/2024 19:45,30/06/2024 20:45
New York Brass Band,Sunday,Outside Circus Stage,59,33,19:49 - 20:34,19:49,20:34,30/06/2024,30/06/2024,30/06/2024 19:49,30/06/2024 20:34
The Cat Empire,Sunday,Avalon Stage,66,38,19:55 - 20:55,19:55,20:55,30/06/2024,30/06/2024,30/06/2024 19:55,30/06/2024 20:55
Judy Collins,Sunday,Acoustic Stage,66,38,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Hospital Showcase Ft Anais B2B Hoax B2B Unglued Ft Ruthless,Sunday,Arcadia,41,25,20:00 - 21:30,20:00,21:30,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:30
Facta & K Lone,Sunday,Assembly,40,42,20:00 - 22:00,20:00,22:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 22:00
N4 Records & Singularity Blind Tiger Takeover - Kotei,Sunday,Blind Tiger,0,0,20:00 - 20:30,20:00,20:30,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 20:30
Compère: Joe Rooney,Sunday,Cabaret,62,26,20:00 - 00:00,20:00,00:00,30/06/2024,01/07/2024,30/06/2024 20:00,01/07/2024 00:00
Emergency Steve,Sunday,Cornish Arms,0,0,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Benny L [30 Years Of Metalheadz],Sunday,Firmly Rooted,43,43,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Disco And Cinema,Sunday,Humblewell Active Platform,42,21,20:00 - 01:00,20:00,01:00,30/06/2024,01/07/2024,30/06/2024 20:00,01/07/2024 01:00
Raggs,Sunday,Iicon,66,21,20:00 - 21:30,20:00,21:30,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:30
Sammy Virji,Sunday,Levels,42,44,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Dj Earl Rafferty,Sunday,Lunched Out Lizards,0,0,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Room Two,Sunday,Meeting Place Bar,0,0,20:00 - 22:00,20:00,22:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 22:00
Chinese Daughter,Sunday,Nowhere,0,0,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Confidence Man (Dj),Sunday,San Remo,45,47,20:00 - 21:30,20:00,21:30,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:30
Dialled In Soundsystem,Sunday,Stonebridge Bar,42,18,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Underdog Presents: Se.V.En,Sunday,Strummerville,48,12,20:00 - 20:30,20:00,20:30,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 20:30
"Notting Hill Carnival Presents: Seduction City, Smokey Joe, David Hill, Mr Fix It",Sunday,Terminal 1,0,0,20:00 - 02:30,20:00,02:30,30/06/2024,01/07/2024,30/06/2024 20:00,01/07/2024 02:30
Mas Que Nada Takeover: Mitch Nunn B2B Josh Parkinson,Sunday,The Hive,0,0,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Gotsome,Sunday,The Temple,0,0,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Nia Archives,Sunday,West Holts Stage,57,31,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Wishing Well Djs,Sunday,Wishing Well,42,20,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Romy,Sunday,Woodsies,43,52,20:00 - 21:00,20:00,21:00,30/06/2024,30/06/2024,30/06/2024 20:00,30/06/2024 21:00
Acoustic Open Mic,Sunday,Croissant Neuf Bandstand,55,21,20:15 - 21:00,20:15,21:00,30/06/2024,30/06/2024,30/06/2024 20:15,30/06/2024 21:00
Laura Lexx,Sunday,Cabaret,62,26,20:20 - 20:50,20:20,20:50,30/06/2024,30/06/2024,30/06/2024 20:20,30/06/2024 20:50
Jordan Mackampa,Sunday,Bbc Music Introducing,45,44,20:30 - 21:00,20:30,21:00,30/06/2024,30/06/2024,30/06/2024 20:30,30/06/2024 21:00
N4 Records & Singularity Blind Tiger Takeover - Reo,Sunday,Blind Tiger,0,0,20:30 - 21:00,20:30,21:00,30/06/2024,30/06/2024,30/06/2024 20:30,30/06/2024 21:00
Groove Armada Dj,Sunday,Glade,51,29,20:30 - 22:00,20:30,22:00,30/06/2024,30/06/2024,30/06/2024 20:30,30/06/2024 22:00
Effy,Sunday,Glade Dome,49,29,20:30 - 22:00,20:30,22:00,30/06/2024,30/06/2024,30/06/2024 20:30,30/06/2024 22:00
Matt Jam Lamont,Sunday,Greenpeace,55,26,20:30 - 22:00,20:30,22:00,30/06/2024,30/06/2024,30/06/2024 20:30,30/06/2024 22:00
Underdog Presents: Dream Mclean,Sunday,Strummerville,48,12,20:30 - 21:00,20:30,21:00,30/06/2024,30/06/2024,30/06/2024 20:30,30/06/2024 21:00
The Shingalings,Sunday,The Bandstand,56,38,20:30 - 21:15,20:30,21:15,30/06/2024,30/06/2024,30/06/2024 20:30,30/06/2024 21:15
The Runaway Christmas Tree Fairy,Sunday,Walkabouts,60,33,20:30 - 21:15,20:30,21:15,30/06/2024,30/06/2024,30/06/2024 20:30,30/06/2024 21:15
Close,Sunday,Outside Circus Stage,59,33,20:34 - 23:31,20:34,23:31,30/06/2024,30/06/2024,30/06/2024 20:34,30/06/2024 23:31
Mary Bourke,Sunday,Cabaret,62,26,20:55 - 21:25,20:55,21:25,30/06/2024,30/06/2024,30/06/2024 20:55,30/06/2024 21:25
N4 Records & Singularity Blind Tiger Takeover - The Bass Injector,Sunday,Blind Tiger,0,0,21:00 - 22:00,21:00,22:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:00
Ed Eldridge,Sunday,Cornish Arms,0,0,21:00 - 23:00,21:00,23:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 23:00
Goldie X Doc Scott X Randall [30 Years Of Metalheadz],Sunday,Firmly Rooted,43,43,21:00 - 00:00,21:00,00:00,30/06/2024,01/07/2024,30/06/2024 21:00,01/07/2024 00:00
A Guy Called Gerald,Sunday,Genosys,0,0,21:00 - 23:00,21:00,23:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 23:00
Bob Vylan,Sunday,Left Field,52,33,21:00 - 22:00,21:00,22:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:00
Jyoty X Lil Silva X Sampha [Dj],Sunday,Levels,42,44,21:00 - 23:30,21:00,23:30,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 23:30
Paranoid London [Live],Sunday,Lonely Hearts Club,44,41,21:00 - 22:00,21:00,22:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:00
Antikvariniai Kaspirovskio Dantys,Sunday,Lunched Out Lizards,0,0,21:00 - 22:00,21:00,22:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:00
Mandala Folk Jam,Sunday,Mandala Stage,0,0,21:00 - 23:00,21:00,23:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 23:00
Uncommon Records And Dope Ammo Records,Sunday,Nowhere,0,0,21:00 - 00:00,21:00,00:00,30/06/2024,01/07/2024,30/06/2024 21:00,01/07/2024 00:00
Retromigration,Sunday,Nyc Downlow,0,0,21:00 - 22:25,21:00,22:25,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:25
Village Underground Takeover: Mi-El,Sunday,Platform 23,0,0,21:00 - 23:00,21:00,23:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 23:00
Wonderment Presents: Elevate,Sunday,Scissors,42,21,21:00 - 23:45,21:00,23:45,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 23:45
Blumitsu,Sunday,Stonebridge Bar,42,18,21:00 - 22:00,21:00,22:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:00
Underdog Presents: Peter Xan,Sunday,Strummerville,48,12,21:00 - 21:30,21:00,21:30,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 21:30
Mas Que Nada Takeover: Jess Iszatt,Sunday,The Hive,0,0,21:00 - 22:00,21:00,22:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:00
Scarlet O'Malley,Sunday,The Meatrack,0,0,21:00 - 22:30,21:00,22:30,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:30
Rum Shack Wild Card,Sunday,The Rum Shack,0,0,21:00 - 21:45,21:00,21:45,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 21:45
Jimmy Lopez,Sunday,The Taphouse,0,0,21:00 - 23:00,21:00,23:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 23:00
East End Dubs,Sunday,The Temple,0,0,21:00 - 22:30,21:00,22:30,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:30
Bau Cat,Sunday,Toad Hall,0,0,21:00 - 22:00,21:00,22:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:00
Natalie Williams Soul Family,Sunday,West Holts Bar,59,29,21:00 - 22:00,21:00,22:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:00
Tba,Sunday,Wishing Well,42,20,21:00 - 22:00,21:00,22:00,30/06/2024,30/06/2024,30/06/2024 21:00,30/06/2024 22:00
Alex Harding,Sunday,Croissant Neuf Bandstand,55,21,21:15 - 17:30,21:15,17:30,30/06/2024,30/06/2024,30/06/2024 21:15,30/06/2024 17:30
Acoustic Open Mic,Sunday,Croissant Neuf Bandstand,55,21,21:15 - 22:00,21:15,22:00,30/06/2024,30/06/2024,30/06/2024 21:15,30/06/2024 22:00
London Grammar,Sunday,The Park Stage,41,19,21:15 - 22:30,21:15,22:30,30/06/2024,30/06/2024,30/06/2024 21:15,30/06/2024 22:30
Caity Baser,Sunday,Avalon Stage,66,38,21:20 - 22:20,21:20,22:20,30/06/2024,30/06/2024,30/06/2024 21:20,30/06/2024 22:20
Gipsy Kings Featuring Tonino Baliardo,Sunday,Acoustic Stage,66,38,21:30 - 22:45,21:30,22:45,30/06/2024,30/06/2024,30/06/2024 21:30,30/06/2024 22:45
Lens,Sunday,Arcadia,41,25,21:30 - 22:30,21:30,22:30,30/06/2024,30/06/2024,30/06/2024 21:30,30/06/2024 22:30
Tamar Katten,Sunday,Cabaret,62,26,21:30 - 22:00,21:30,22:00,30/06/2024,30/06/2024,30/06/2024 21:30,30/06/2024 22:00
Guest Dj,Sunday,Deluxe Diner,64,17,21:30 - 23:00,21:30,23:00,30/06/2024,30/06/2024,30/06/2024 21:30,30/06/2024 23:00
Tim Reaper,Sunday,Iicon,66,21,21:30 - 23:00,21:30,23:00,30/06/2024,30/06/2024,30/06/2024 21:30,30/06/2024 23:00
Sza,Sunday,Pyramid Stage,51,43,21:30 - 23:15,21:30,23:15,30/06/2024,30/06/2024,30/06/2024 21:30,30/06/2024 23:15
Dj Tennis,Sunday,San Remo,45,47,21:30 - 23:00,21:30,23:00,30/06/2024,30/06/2024,30/06/2024 21:30,30/06/2024 23:00
James Blake,Sunday,Woodsies,43,52,21:30 - 22:45,21:30,22:45,30/06/2024,30/06/2024,30/06/2024 21:30,30/06/2024 22:45
The National,Sunday,Other Stage,47,34,21:45 - 23:15,21:45,23:15,30/06/2024,30/06/2024,30/06/2024 21:45,30/06/2024 23:15
Buffo'S Wake,Sunday,The Bandstand,56,38,21:45 - 22:45,21:45,22:45,30/06/2024,30/06/2024,30/06/2024 21:45,30/06/2024 22:45
Ulula Roots,Sunday,The Rum Shack,0,0,21:45 - 22:30,21:45,22:30,30/06/2024,30/06/2024,30/06/2024 21:45,30/06/2024 22:30
4Resh + Shir.In,Sunday,Arrivals,0,0,22:00 - 23:00,22:00,23:00,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:00
Pangaea B2B Tasha,Sunday,Assembly,40,42,22:00 - 23:30,22:00,23:30,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:30
N4 Records & Singularity Blind Tiger Takeover - Pete Cannon,Sunday,Blind Tiger,0,0,22:00 - 23:00,22:00,23:00,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:00
Suns Of Acid,Sunday,Flying Bus,0,0,22:00 - 00:00,22:00,00:00,30/06/2024,01/07/2024,30/06/2024 22:00,01/07/2024 00:00
Carlita,Sunday,Glade,51,29,22:00 - 23:15,22:00,23:15,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:15
Samba Boys (Kettama + Tommy Holohan),Sunday,Glade Dome,49,29,22:00 - 23:30,22:00,23:30,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:30
Girls Of The Internet (Dj Set),Sunday,Greenpeace,55,26,22:00 - 23:30,22:00,23:30,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:30
Rossi. [Fuse Takeover],Sunday,Lonely Hearts Club,44,41,22:00 - 23:15,22:00,23:15,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:15
Mez Yard Guests,Sunday,Mez Yard,0,0,22:00 - 23:00,22:00,23:00,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:00
Swana Takeover X Nazar Presents: Saliah,Sunday,Nomad,0,0,22:00 - 00:00,22:00,00:00,30/06/2024,01/07/2024,30/06/2024 22:00,01/07/2024 00:00
Andy Blake,Sunday,Stonebridge Bar,42,18,22:00 - 23:00,22:00,23:00,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:00
Bastard Love,Sunday,Strummerville,48,12,22:00 - 00:00,22:00,00:00,30/06/2024,01/07/2024,30/06/2024 22:00,01/07/2024 00:00
Mas Que Nada Takeover: Charlie Boon B2B Meg Ward,Sunday,The Hive,0,0,22:00 - 23:00,22:00,23:00,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:00
Dj Gaz,Sunday,The Rocket Lounge,64,16,22:00 - 05:00,22:00,05:00,30/06/2024,01/07/2024,30/06/2024 22:00,01/07/2024 05:00
Tor Da Force,Sunday,The Sistxrhood,0,0,22:00 - 23:00,22:00,23:00,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:00
Glowbros,Sunday,Walkabouts,60,33,22:00 - 00:00,22:00,00:00,30/06/2024,01/07/2024,30/06/2024 22:00,01/07/2024 00:00
Justice,Sunday,West Holts Stage,57,31,22:00 - 23:15,22:00,23:15,30/06/2024,30/06/2024,30/06/2024 22:00,30/06/2024 23:15
Love Life Disco (Dj Set),Sunday,Wishing Well,42,20,22:00 - 00:30,22:00,00:30,30/06/2024,01/07/2024,30/06/2024 22:00,01/07/2024 00:30
Andrew O'Neill - The History Of Heavy Metal,Sunday,Cabaret,62,26,22:05 - 22:45,22:05,22:45,30/06/2024,30/06/2024,30/06/2024 22:05,30/06/2024 22:45
Mad Apple Circus,Sunday,Sensation Seekers Stage,0,0,22:15 - 23:00,22:15,23:00,30/06/2024,30/06/2024,30/06/2024 22:15,30/06/2024 23:00
The Fairy Godmother And The Tooth Fairy,Sunday,Walkabouts,60,33,22:15 - 23:00,22:15,23:00,30/06/2024,30/06/2024,30/06/2024 22:15,30/06/2024 23:00
Mandidextrous B2B Ivy,Sunday,Arcadia,41,25,22:30 - 23:30,22:30,23:30,30/06/2024,30/06/2024,30/06/2024 22:30,30/06/2024 23:30
Matt Jam Lamont B2B Scott Diaz,Sunday,Nyc Downlow,0,0,22:30 - 23:55,22:30,23:55,30/06/2024,30/06/2024,30/06/2024 22:30,30/06/2024 23:55
Cam Cole,Sunday,Peace Stage,0,0,22:30 - 23:30,22:30,23:30,30/06/2024,30/06/2024,30/06/2024 22:30,30/06/2024 23:30
Mr. Redley,Sunday,The Meatrack,0,0,22:30 - 00:00,22:30,00:00,30/06/2024,01/07/2024,30/06/2024 22:30,01/07/2024 00:00
Manni Dee,Sunday,The Temple,0,0,22:30 - 00:00,22:30,00:00,30/06/2024,01/07/2024,30/06/2024 22:30,01/07/2024 00:00
Kirszenbaum,Sunday,Toad Hall,0,0,22:30 - 23:30,22:30,23:30,30/06/2024,30/06/2024,30/06/2024 22:30,30/06/2024 23:30
Disco Turtle,Sunday,Walkabouts,60,33,22:30 - 00:00,22:30,00:00,30/06/2024,01/07/2024,30/06/2024 22:30,01/07/2024 00:00
Giant Egret,Sunday,Walkabouts,60,33,22:30 - 23:15,22:30,23:15,30/06/2024,30/06/2024,30/06/2024 22:30,30/06/2024 23:15
Mat Collishaw - Even To The End,Sunday,Tree Stage,44,51,22:45 - 23:00,22:45,23:00,30/06/2024,30/06/2024,30/06/2024 22:45,30/06/2024 23:00
The Feeling,Sunday,Avalon Stage,66,38,22:50 - 23:50,22:50,23:50,30/06/2024,30/06/2024,30/06/2024 22:50,30/06/2024 23:50
Cash & Diamond,Sunday,Cabaret,62,26,22:50 - 23:20,22:50,23:20,30/06/2024,30/06/2024,30/06/2024 22:50,30/06/2024 23:20
Vedic Roots Soundsystem,Sunday,Arrivals,0,0,23:00 - 00:00,23:00,00:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:00
N4 Records & Singularity Bliind Tiger Takeover - 4Am Kru,Sunday,Blind Tiger,0,0,23:00 - 00:00,23:00,00:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:00
Twin Sun (Blendid Takeover),Sunday,Cornish Arms,0,0,23:00 - 01:00,23:00,01:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 01:00
Raz + Afla,Sunday,Croissant Neuf,55,21,23:00 - 00:00,23:00,00:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:00
Perri Kaye,Sunday,Deluxe Diner,64,17,23:00 - 00:30,23:00,00:30,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:30
Diy 35Th Anniversary Party,Sunday,Genosys,0,0,23:00 - 03:00,23:00,03:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 03:00
Dj And Dancing,Sunday,Glasto Latino,58,27,23:00 - 23:30,23:00,23:30,30/06/2024,30/06/2024,30/06/2024 23:00,30/06/2024 23:30
Iicon Av:3D,Sunday,Iicon,66,21,23:00 - 23:15,23:00,23:15,30/06/2024,30/06/2024,30/06/2024 23:00,30/06/2024 23:15
Loonaloop,Sunday,Lunched Out Lizards,0,0,23:00 - 00:00,23:00,00:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:00
Wild Fantasy,Sunday,Meeting Place Bar,0,0,23:00 - 02:30,23:00,02:30,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 02:30
Paul'S Mobile Disco,Sunday,Mez Yard,0,0,23:00 - 00:30,23:00,00:30,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:30
Village Underground Takeover: Blumitsu,Sunday,Platform 23,0,0,23:00 - 00:30,23:00,00:30,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:30
Axel Boman,Sunday,San Remo,45,47,23:00 - 00:30,23:00,00:30,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:30
Priscilla B2B H3L3Na,Sunday,Stonebridge Bar,42,18,23:00 - 00:00,23:00,00:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:00
Mas Que Nada Takeover: Elliot Schooling & Liam Palmer,Sunday,The Hive,0,0,23:00 - 00:00,23:00,00:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:00
Red Hot Riot,Sunday,The Rocket Lounge,64,16,23:00 - 00:00,23:00,00:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:00
Jessica Wilde,Sunday,The Rum Shack,0,0,23:00 - 23:45,23:00,23:45,30/06/2024,30/06/2024,30/06/2024 23:00,30/06/2024 23:45
Kaptain,Sunday,The Salon Carousel,0,0,23:00 - 00:00,23:00,00:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:00
Marla Kether,Sunday,The Sistxrhood,0,0,23:00 - 00:00,23:00,00:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:00
Andy Hatman,Sunday,The Taphouse,0,0,23:00 - 01:00,23:00,01:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 01:00
Rrose,Sunday,Tree Stage,44,51,23:00 - 00:00,23:00,00:00,30/06/2024,01/07/2024,30/06/2024 23:00,01/07/2024 00:00
Loominus,Sunday,Sensation Seekers Stage,0,0,23:10 - 23:25,23:10,23:25,30/06/2024,30/06/2024,30/06/2024 23:10,30/06/2024 23:25
Daniel Avery,Sunday,Glade,51,29,23:15 - 00:30,23:15,00:30,30/06/2024,01/07/2024,30/06/2024 23:15,01/07/2024 00:30
Roni Size,Sunday,Iicon,66,21,23:15 - 02:00,23:15,02:00,30/06/2024,01/07/2024,30/06/2024 23:15,01/07/2024 02:00
Lauren Lo Sung [Fuse Takeover],Sunday,Lonely Hearts Club,44,41,23:15 - 00:30,23:15,00:30,30/06/2024,01/07/2024,30/06/2024 23:15,01/07/2024 00:30
Suntou Susso,Sunday,The Bandstand,56,38,23:15 - 00:15,23:15,00:15,30/06/2024,01/07/2024,30/06/2024 23:15,01/07/2024 00:15
J Spynx,Sunday,West Holts Bar,59,29,23:15 - 00:45,23:15,00:45,30/06/2024,01/07/2024,30/06/2024 23:15,01/07/2024 00:45
Basil Brush - Unleashed,Sunday,Cabaret,62,26,23:25 - 23:55,23:25,23:55,30/06/2024,30/06/2024,30/06/2024 23:25,30/06/2024 23:55
Arcadia And The Wadjuk Noongar - Warraloo Ceremony,Sunday,Arcadia,41,25,23:30 - 23:40,23:30,23:40,30/06/2024,30/06/2024,30/06/2024 23:30,30/06/2024 23:40
Aurora Halal,Sunday,Assembly,40,42,23:30 - 01:00,23:30,01:00,30/06/2024,01/07/2024,30/06/2024 23:30,01/07/2024 01:00
Daisy Veacock,Sunday,Bread And Roses,0,0,23:30 - 00:30,23:30,00:30,30/06/2024,01/07/2024,30/06/2024 23:30,01/07/2024 00:30
Leon Vynehall,Sunday,Glade Dome,49,29,23:30 - 01:00,23:30,01:00,30/06/2024,01/07/2024,30/06/2024 23:30,01/07/2024 01:00
Timba Britanica Ft Mayito Rivera,Sunday,Glasto Latino,58,27,23:30 - 01:00,23:30,01:00,30/06/2024,01/07/2024,30/06/2024 23:30,01/07/2024 01:00
Prospa,Sunday,Greenpeace,55,26,23:30 - 01:00,23:30,01:00,30/06/2024,01/07/2024,30/06/2024 23:30,01/07/2024 01:00
Girls Don'T Sync,Sunday,Levels,42,44,23:30 - 01:00,23:30,01:00,30/06/2024,01/07/2024,30/06/2024 23:30,01/07/2024 01:00
Replete,Sunday,Mandala Stage,0,0,23:30 - 00:30,23:30,00:30,30/06/2024,01/07/2024,30/06/2024 23:30,01/07/2024 00:30
Mista Trick,Sunday,Peace Stage,0,0,23:30 - 00:00,23:30,00:00,30/06/2024,01/07/2024,30/06/2024 23:30,01/07/2024 00:00
Leather Lungs + Master Reblasters,Sunday,Sensation Seekers Stage,0,0,23:30 - 00:15,23:30,00:15,30/06/2024,01/07/2024,30/06/2024 23:30,01/07/2024 00:15
Disco Freaks,Sunday,Village Inn,0,0,23:30 - 02:00,23:30,02:00,30/06/2024,01/07/2024,30/06/2024 23:30,01/07/2024 02:00
Aerial High Jinks,Sunday,Outside Circus Stage,59,33,23:31 - 23:37,23:31,23:37,30/06/2024,30/06/2024,30/06/2024 23:31,30/06/2024 23:37
A Little Sound,Sunday,Arcadia,41,25,23:40 - 00:30,23:40,00:30,30/06/2024,01/07/2024,30/06/2024 23:40,01/07/2024 00:30
Fiery Jack Family,Sunday,Outside Circus Stage,59,33,23:42 - 23:57,23:42,23:57,30/06/2024,30/06/2024,30/06/2024 23:42,30/06/2024 23:57
Sippin' T,Sunday,Scissors,42,21,23:45 - 00:45,23:45,00:45,30/06/2024,01/07/2024,30/06/2024 23:45,01/07/2024 00:45
Eyes Wide Shut Duo Trapeze,Sunday,Outside Circus Stage,59,33,23:57 - 00:05,23:57,00:05,30/06/2024,01/07/2024,30/06/2024 23:57,01/07/2024 00:05
""")