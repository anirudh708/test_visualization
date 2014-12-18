'''
Created on Dec 15, 2014

@author: Anirudh
'''

# import pysvg
# import svgwrite

# import numpy as np
from  tornado.web import *

import os

import tornado.httpserver
import tornado.ioloop

from tornado.web import Application
from io import StringIO

import tornado



# py.bar([0,1,2,3,4,5,6,7,8,9], [23,80,92,62,98,7,9,56,19,68], width=0.8, bottom=None, hold=None)
# 
# py.show()
# 
# py.savefig("E:\\signal", ext="svg", close=True, verbose=True)

# x=np.array([1,2,3])
# y=np.array([1,1,3])
# 
# z= np.square(x)*2000
# 
# py.scatter(x, y, s=z)
# py.show()

# R=np.corrcoef([[1,2,3],[2,4,6],[-1,-2,-3]])
# print R.T
# py.pcolor(R)
# py.colorbar()
# py.yticks(np.arange(0.5,2),range(1,3))
# py.xticks(np.arange(0.5,2),range(0,2))
# py.show()

class MainHandler(RequestHandler):
    def get(self):
        self.write('''
        
        <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>HTML5 snake - Canvas Snake Game</title>
<style >
article, aside, details, figcaption, figure, footer, header,
hgroup, menu, nav, section { 
  display: block; 
}
body {
  background-color: #CCC;
}
h1 {
  text-align: center;
}
p {
  text-align: center;
}
canvas {
  display: block;
  margin: 0 auto;
  background-color: #666;
}
</style>
</head>
<body>

<h1>html5-snake</h1>
<p><a href="http://en.wikipedia.org/wiki/HTML5">HTML5</a> variation of the classic <a href="http://en.wikipedia.org/wiki/Snake_(video_game)">snake game</a>.</p>

<div>
  <canvas id="the-game" width="320" height="240">
</div>

<p>Control snake with arrow keys, WASD, or HJKL (vim keys).</p>

<p>New food may appear under snake, uncoil to reveal.</p>

<p>Collect the food to grow and increase speed.</p>

 <script type="text/javascript">
var canvas = document.getElementById("the-game");
var context = canvas.getContext("2d");
var game, snake, food;

game = {
  
  score: 0,
  fps: 8,
  over: false,
  message: null,
  
  start: function() {
    game.over = false;
    game.message = null;
    game.score = 0;
    game.fps = 8;
    snake.init();
    food.set();
  },
  
  stop: function() {
    game.over = true;
    game.message = 'GAME OVER - PRESS SPACEBAR';
  },
  
  drawBox: function(x, y, size, color) {
    context.fillStyle = color;
    context.beginPath();
    context.moveTo(x - (size / 2), y - (size / 2));
    context.lineTo(x + (size / 2), y - (size / 2));
    context.lineTo(x + (size / 2), y + (size / 2));
    context.lineTo(x - (size / 2), y + (size / 2));
    context.closePath();
    context.fill();
  },
  
  drawScore: function() {
    context.fillStyle = '#999';
    context.font = (canvas.height) + 'px Impact, sans-serif';
    context.textAlign = 'center';
    context.fillText(game.score, canvas.width / 2, canvas.height * 0.9);
  },
  
  drawMessage: function() {
    if (game.message !== null) {
      context.fillStyle = '#00F';
      context.strokeStyle = '#FFF';
      context.font = (canvas.height / 10) + 'px Impact';
      context.textAlign = 'center';
      context.fillText(game.message, canvas.width / 2, canvas.height / 2);
      context.strokeText(game.message, canvas.width / 2, canvas.height / 2);
    }
  },
  
  resetCanvas: function() {
    context.clearRect(0, 0, canvas.width, canvas.height);
  }
  
};

snake = {
  
  size: canvas.width / 40,
  x: null,
  y: null,
  color: '#0F0',
  direction: 'left',
  sections: [],
  
  init: function() {
    snake.sections = [];
    snake.direction = 'left';
    snake.x = canvas.width / 2 + snake.size / 2;
    snake.y = canvas.height / 2 + snake.size / 2;
    for (var i = snake.x + (5 * snake.size); i >= snake.x; i -= snake.size) {
      snake.sections.push(i + ',' + snake.y); 
    }
  },
  
  move: function() {
    switch (snake.direction) {
      case 'up':
        snake.y -= snake.size;
        break;
      case 'down':
        snake.y += snake.size;
        break;
      case 'left':
        snake.x -= snake.size;
        break;
      case 'right':
        snake.x += snake.size;
        break;
    }
    snake.checkCollision();
    snake.checkGrowth();
    snake.sections.push(snake.x + ',' + snake.y);
  },
  
  draw: function() {
    for (var i = 0; i < snake.sections.length; i++) {
      snake.drawSection(snake.sections[i].split(','));
    }    
  },
  
  drawSection: function(section) {
    game.drawBox(parseInt(section[0]), parseInt(section[1]), snake.size, snake.color);
  },
  
  checkCollision: function() {
    if (snake.isCollision(snake.x, snake.y) === true) {
      game.stop();
    }
  },
  
  isCollision: function(x, y) {
    if (x < snake.size / 2 ||
        x > canvas.width ||
        y < snake.size / 2 ||
        y > canvas.height ||
        snake.sections.indexOf(x + ',' + y) >= 0) {
      return true;
    }
  },
  
  checkGrowth: function() {
    if (snake.x == food.x && snake.y == food.y) {
      game.score++;
      if (game.score % 5 == 0 && game.fps < 60) {
        game.fps++;
      }
      food.set();
    } else {
      snake.sections.shift();
    }
  }
  
};

food = {
  
  size: null,
  x: null,
  y: null,
  color: '#0FF',
  
  set: function() {
    food.size = snake.size;
    food.x = (Math.ceil(Math.random() * 10) * snake.size * 4) - snake.size / 2;
    food.y = (Math.ceil(Math.random() * 10) * snake.size * 3) - snake.size / 2;
  },
  
  draw: function() {
    game.drawBox(food.x, food.y, food.size, food.color);
  }
  
};

var inverseDirection = {
  'up': 'down',
  'left': 'right',
  'right': 'left',
  'down': 'up'
};

var keys = {
  up: [38, 75, 87],
  down: [40, 74, 83],
  left: [37, 65, 72],
  right: [39, 68, 76],
  start_game: [13, 32]
};

function getKey(value){
  for (var key in keys){
    if (keys[key] instanceof Array && keys[key].indexOf(value) >= 0){
      return key;
    }
  }
  return null;
}

addEventListener("keydown", function (e) {
    var lastKey = getKey(e.keyCode);
    if (['up', 'down', 'left', 'right'].indexOf(lastKey) >= 0
        && lastKey != inverseDirection[snake.direction]) {
      snake.direction = lastKey;
    } else if (['start_game'].indexOf(lastKey) >= 0 && game.over) {
      game.start();
    }
}, false);

var requestAnimationFrame = window.requestAnimationFrame ||
      window.webkitRequestAnimationFrame ||
      window.mozRequestAnimationFrame;

function loop() {
  if (game.over == false) {
    game.resetCanvas();
    game.drawScore();
    snake.move();
    food.draw();
    snake.draw();
    game.drawMessage();
  }
  setTimeout(function() {
    requestAnimationFrame(loop);
  }, 1000 / game.fps);
}

requestAnimationFrame(loop);
</script>

</body>
</html>
        
        ''')


        

app = Application([
    url(r"/", MainHandler),
  
    ])

if __name__=="__main__":
    http_server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
    





