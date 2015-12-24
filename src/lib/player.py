from character import Character
from util import gamedir
import json

class Player(Character):

    @property
    def character_type(self):
        return 'player'

    def savetoslot(self,slot):
        savedir = gamedir[-1]
        filename = os.path.join(savedir,str(slot), 'player','player.yaml')
        os.makedirs(os.dirname(filename
            ))
        open(filename, 'w').write(json.dump(self(),indent=4))

    def moveto(self, map, x, y):
        if not mapname:
            return
        if not isinstance(x, int) or not isinstance(y, int):
            try:
                x = int(x)
                y = int(y)
            except:
                return
        if not map.tile(x,y).canenter():
            return
        current = self.location()
        if current.get('map') and x and y:
            gamemap = GameMap(load_yaml('maps', current['map']))
            gamemap.removefromtile(current['x'], current['y'],self,'player')
        self.put('location/x', x)
        self.put('location/y', y)
        self.put('location/map', mapname)
        map.addtotile(x, y, 'npc', self)
        messages.warning('%s moves to %sx%s' %(self.displayname(),x, y))
