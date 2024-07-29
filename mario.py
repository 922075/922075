import pyxel

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.current = 0
        self.direction = 1
        self.ground = 16*9
        self.canJump = True
        self.y_prev = self.y
        self.F = -1
    
    def jump(self):
        if self.canJump:
            self.F = -10
            self.canJump = False
    
    def update(self):
        if pyxel.btn(pyxel.KEY_SPACE):
            self.jump()

        if pyxel.btn(pyxel.KEY_D):
            self.x = (self.x + 3) % pyxel.width
            self.current = (self.current + 1) % 4
            if self.direction == -1:
                self.direction *= -1
        elif pyxel.btn(pyxel.KEY_A):
            self.x = (self.x - 3) % pyxel.width
            self.current = (self.current + 1) % 4
            if self.direction == 1:
                self.direction *= -1
        else:
            self.current = 0
        
        if self.canJump:
            return
        
        y_tmp = self.y
        self.y += (self.y - self.y_prev) + self.F
        self.y_prev = y_tmp
        self.F = 1

        if self.y == self.ground:
            self.canJump = True
    
    def draw(self):
        if self.canJump == False:
            pyxel.blt(self.x,self.y,0,16*4,0,16*self.direction,16,6)
        else:
            pyxel.blt(self.x,self.y,0,16*self.current,0,16*self.direction,16,6)

class App:
    def __init__(self): #初期値
        pyxel.init(16*16, 16*12)
        pyxel.load("my_resource.pyxres")

        self.player = Player(0,9*16)
        
        pyxel.run(self.update, self.draw)

    def update(self): #フレームの更新処理
        self.player.update()

    def draw(self): #描画処理
        pyxel.cls(6)
        for i in range(16):
            pyxel.blt(16*i,16*11,0,0,16,16,16)
            pyxel.blt(16*i,16*10,0,0,16,16,16)
        self.player.draw()

App()