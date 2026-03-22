class Channel:
    def __init__(self, name, description, subscribers):
        self.name = name
        self.description = description
        self.subscribers = subscribers
        self.videos = []
        self.playlists: list[Playlist] = []
    
    def subscribe(self, quantity=1):
        self.subscribers += quantity
    
    def post(self, video):
        if video in self.videos:
            print("This video already exists!")
            return
        self.videos.append(video)
    
    def playlist_info(self):
        for playlist in self.playlists:
            print(playlist.name)
            playlist.video_info()
    
    def add_playlist(self, playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)
        else:
            print("This playlist has already been added!")
    
    def remove_playlist(self, playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)
        else:
            print("This playlist does not exist.")

class BusinessChannel(Channel):
    def __init__(self, name, description, subscribers):
        super().__init__(name, description, subscribers)
        self._team = []
    
    @property
    def team(self):
        return self._team
    
    def add_team_member(self, member):
        if member not in self._team:
            self._team.append(member)
        else:
            print(f"The member {member} is already in the team!")
    
    def remove_team_member(self, member):
        if member in self._team:
            self._team.remove(member)
        else:
            print(f"The member {member} is not in the team!")

class Video:
    def __init__(self, title, description):
        self.title = title
        self.description = description

        self.views = 0
        self.likes = 0
        self.dislikes = 0
        self.comments = []

    def __repr__(self):
        return f"<{self.title}>"

    def watch(self):
        self.views += 1
    
    def like(self):
        self.likes += 1
    
    def dislike(self):
        self.dislikes += 1
    
    def comment(self, comment_text):
        self.comments.append(comment_text)
    
    def info(self):
        print(f"""Title: {self.title}
Description: {self.description}
{self.views} Views
{self.likes} Likes {self.dislikes} Dislikes
{self.comments}\n""")

class Playlist:
    def __init__(self, name):
        self.name = name
        self.videos: list[Video] = []
    
    def add_video(self, video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print(f"This video is already in the playlist!")
    
    def remove_video(self, video):
        if video in self.videos:
            self.videos.remove(video)
        else:
            print(f"This video is not in the playlist.")

    def video_info(self):
        for video in self.videos:
            video.info()

# --- Testing the code ---

lan_code_channel = Channel('Lan Code', 'Codes and cats', 34000)
guanabara_channel = Channel('Curso em Vídeo', 'Passion for teaching', 2500000)
duolingo_channel = BusinessChannel('Duolingo', 'English', 500000)

poo_video = Video('Python Objects', 'Learn now')
discordpy_video = Video('Learn Discord.py', 'squarecloud')

programming_playlist = Playlist('Programming')
programming_playlist.add_video(poo_video)
programming_playlist.add_video(discordpy_video)

minecraft_video = Video('Playing Minecraft', 'Mine')
deltarune_video = Video('Playing Deltarune', 'Deltarune')

games_playlist = Playlist('Games')
games_playlist.add_video(minecraft_video)
games_playlist.add_video(deltarune_video)

lan_code_channel.add_playlist(programming_playlist)
lan_code_channel.add_playlist(games_playlist)

lan_code_channel.post(poo_video)
lan_code_channel.post(discordpy_video)

lan_code_channel.playlist_info()