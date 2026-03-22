# OOP

Object-Oriented Programming works with entities that we create in order to replicate their properties and methods into instances.

## Source

> This content was created based on the following video:\
> 👉 [Watch on
> YouTube](https://youtu.be/QAwNvlEd1aM?si=xpbyHqNZwUQQq7cR)
>
> 📺 Channel:\
> 👉 [Lan Code](https://www.youtube.com/@lan_code)

## Classes

A class is nothing more than a mold used to create objects. Let's use a YouTube channel as an example:

1. We use the keyword `class` and then define the name of our class, for example `Channel`:

```python
class Channel:
    pass
```

2. After creating the class, we define its attributes, which are the information that compose the class:

```python
class Channel:
    def __init__(self, name, description, subscribers):
        self.name = name
        self.description = description
        self.subscribers = subscribers
```

- The `__init__` function is called the constructor method. It is executed when instantiating the object.  
- The `self` parameter refers to the instance itself. When we instantiate a class, `self` represents the specific object being created, not the class.  
- Every method inside a class receives `self`.

3. After defining the class and its attributes, the next step is to create the objects.

## Objects

To create objects, we use the class as a mold. Based on this mold, the object must respect the attributes defined in that class.

1. The `Channel` class has 3 attributes: name, description, and subscribers. Therefore, the object we create must have these same 3 attributes:

- Name: "Lan Code"
- Description: "Programming Channel"
- Subscribers: 34,000

2. Usage Example:

```python
canal_lancode = Channel("Lan Code", "Programming Channel", 34000)
print(canal_lancode.description)
```

- In this example, `self` represents `canal_lancode`.

---

## Methods

In the previous example, we used the `__init__` method. This is a special Python method used as a constructor. However, we can also create our own custom methods.

1. Inside the class, but outside `__init__`, we create a new method:

```python
class Channel:
    def __init__(self, name, description, subscribers):
        self.name = name
        self.description = description
        self.subscribers = subscribers

    def subscribe(self, quantity=1):
        self.subscribers += quantity

canal_lancode = Channel("Lan Code", "Programming Channel", 34000)
```

- This method takes the current number of subscribers and adds a given quantity (default is 1).

2. Usage Example:

```python
print(f"Subscribers: {canal_lancode.subscribers}")
canal_lancode.subscribe()
print(f"New subscribers count: {canal_lancode.subscribers}")
```

---

## Inheritance

Inheritance happens when we create a class based on another class. The new class inherits all attributes and methods from the parent class, but can also have its own features.

1. Creating an Employee class and a subclass:

```python
class Employee:
    def __init__(self, id, name, salary):
        self.id = id 
        self.name = name
        self.salary = salary
```

```python
class EmployeeDirector(Employee):
    def __init__(self, id, name, salary, team):
        super().__init__(id, name, salary)
        self.team = team
```
- Even when inheriting, we still need to define a constructor.
- super() refers to the parent class and calls its constructor.

2. Usage Example:

```python
class Employee:
    def __init__(self, id, name, salary):
        self.id = id 
        self.name = name
        self.salary = salary

class EmployeeDirector(Employee):
    def __init__(self, id, name, salary, team):
        super().__init__(id, name, salary)
        self.team = team

employee_1 = Employee(12345, "Guilherme Sobrenome", 4000)
employee_2 = Employee(52134, "Ruan Sobrenome", 4500)
employee_3 = Employee(54321, "Lanilsson Sobrenome", 2300)

director_1 = EmployeeDirector(
    11111, 
    "Fernando Sobrenome", 
    40000, 
    [employee_1.id, employee_2.id, employee_3.id]
    )

print(employee_1.salary)
print(director_1.team)
```

---

## Encapsulation

Some properties should not be modified directly. We may want validation before modifying them. This is where encapsulation comes in.
We will prevent adding the same member twice to a team.

1. Rename team to _team (convention for protected attribute):

```python
class EmployeeDirector(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)
        self._team = []

    @property
    def team(self):
        return self._team
```

- `@property` allows access without parentheses.

2. Let's create a function that adds a member if they aren't in the team already:

```python
def add_team(self, member):
    if member not in self._team:
        self._team.append(member)
    else:
        print("This member already exists")
```

- Remember that this will stay inside the class.

3. Here is a full example for better visualization.

```python
class Employee:
    def __init__(self, id, name, salary):
        self.id = id 
        self.name = name
        self.salary = salary

class EmployeeDirector(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)
        self._team = []

    @property
    def team(self):
        return self._team
    
    def add_team(self, member):
        if member not in self._team:
            self._team.append(member)
        else:
            print("This Member Alredy Exists")

employee_1 = Employee(12345, "Guilherme Sobrenome", 4000)
employee_2 = Employee(52134, "Ruan Sobrenome", 4500)
employee_3 = Employee(54321, "Lanilsson Sobrenome", 2300)

director_1 = EmployeeDirector(
    11111, 
    "Fernando Sobrenome", 
    40000
    )


print(f"Current team members: {director_1.team}")
for i in (employee_3.id, employee_2.id, employee_1.id):
    director_1.add_team(i)
print(f"Current team members: {director_1.team}")
director_1.add_team(employee_3.id)
print(f"Current team members: {director_1.team}")
```

---

## Full Composition Example

```python
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
```


---

## Note

This content was created for study purposes and is based on a reference video.
