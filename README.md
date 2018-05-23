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

You can change the systems used in the engine by creating a module or a class that defines three functions that return an instance of each system

```python
class MyBackend:
    def get_input_handler():
        return MyInputHandler()
    def get_renderer():
        return MyRenderer()
    def get_tick_provider():
        return MyTickProvider()

from xudia import Xudia
# create the engine
engine = Engine()
scene = MyScene()
# initialize Xudia with a scene and the engine
# set backend to your module or class that provide 
#   the previously defined functions: get_input_handler, get_renderer,
#   get_tick_provider
Xudia.init(scene, engine, backend=MyBackend)

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