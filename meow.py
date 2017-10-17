import arcade
from models import *

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class MEOWWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        # set world bg
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT,"images/background-living.jpg")
        self.coin_sprite = ModelSprite('images/coin.png', model=self.world.coin)
        self.block_food_sprite = ModelSprite('images/Block.png', model=self.world.block_food)
        self.food_sprite = ModelSprite('images/food.jpg', model=self.world.food)

        self.choose = Choose(self.world,"images/background-working.jpg")
        self.choose_status = False

    def update(self, delta):
        self.world.update(delta)
        
    def on_draw(self):
        arcade.start_render()
        
        if self.choose_status == False:

            # draw bg
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                                SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture(self.world.background)) 
            # draw cat
            self.world.meow_sprite_list.draw()
            # draw block food
            self.block_food_sprite.draw()
            self.food_sprite.draw()
            # draw coin
            self.coin_sprite.draw()
            arcade.draw_text(str(self.world.coin.coin),
                                    self.width - 30, self.height - 30,
                                    arcade.color.CITRINE, 20)    
            #############################################################################################
            arcade.draw_text(str(self.world.meow_list[0].hungry),
                                    self.width - 50, self.height - 50,
                                    arcade.color.YELLOW, 20)
            arcade.draw_text(str(self.world.meow_list[0].time),
                                    self.width - 110, self.height - 110,
                                    arcade.color.YELLOW, 20)   
            arcade.draw_text(str(self.world.food.food),
                                    self.width - 150, self.height - 150,
                                    arcade.color.YELLOW, 20)  
            if len(self.world.meow_list) > 1:
                arcade.draw_text(str(self.world.meow_list[1].hungry),
                                        self.width - 50, self.height - 70,
                                        arcade.color.GREEN, 20)
                arcade.draw_text(str(self.world.meow_list[1].time),
                                        self.width - 110, self.height - 130,
                                        arcade.color.GREEN, 20)   
            #############################################################################################
            for i in range(0,len(self.world.meow_list)):
                arcade.draw_text('Lv:{0}  Dmg:{1}'.format(str(self.world.meow_list[i].level),str(self.world.meow_list[i].damage)),
                                        self.world.meow_sprite_list[i].center_x - 60, self.world.meow_sprite_list[i].center_y + 50,
                                        arcade.color.BLUE_YONDER, 20)
            #  draw food 
            self.food_sprite.draw()

        elif self.choose_status == True:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                              SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture(self.choose.background))
            

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        self.world.on_mouse_press(x, y, button, modifiers)
        # center block 650,30
        if button == arcade.MOUSE_BUTTON_LEFT and (x > 625 and x < 675 ) and (y > 5 and y < 55) and (self.choose_status == False):
            self.choose_status = True
        elif button == arcade.MOUSE_BUTTON_LEFT and (x > 625 and x < 675 ) and (y > 5 and y < 55) and (self.choose_status == True):
            self.choose_status = False

def main():
    window = MEOWWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()