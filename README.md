# Xudia
Xudia is a game engine for terminal based games.
It uses curses as the backend for drawing in the screen and recieving input.

# Installing
Just download and copy the xudia folder into your game's folder and you'r done.

# Usage
Xudia is an entity-based game engine. The engine is responsible for the systems update cycle, currently there's three main systems added by default to the engine:

1. A InputHandler
2. A Renderer
3. A TickProvider

You can change default systems in `xudia.Xudia` class located in the `__init__.py` file

```python
from xudia import Xudia
# change default systems
Xudia.input = MyInputHandler()
Xudia.renderer = MyRenderer()
Xudia.tickProvider = MyTickProvider()

# create the engine
engine = Engine()
scene = MyScene()
# initialize Xudia with a scene and the engine
# set default_systems to False 
#   if you wish to use the systems we provided earlier
Xudia.init(scene, engine, default_systems=False)

# start the engine: update loop
engine.start()
```

As it's shown, starting the engine for our game is a four step procedure:

1. create the engine
2. create the starting scene
3. initialize Xudia
4. start the engine

A scene is a subclass of Scene where the entities that are updated, and rendererd are managed, it's a container for the entities of the scene.
You can check the `gameScene.py` file for more on how scenes work

An entity is a game object. To add an entity to the current scene use `addEntity` method on the current scene instance

```python
from xudia import Xudia

# create the entity
entity = MyEntity()

# add to current scene
Xudia.scene.addEntity(entity)
```

For more info check the example provided with the source code.