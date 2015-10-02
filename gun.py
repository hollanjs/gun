class Gun:
    def __init__(self, ammo=0, clips=0, capacity=6):
        self.safety = True
        self.clip_count = self.bullets//capacity
        self.bullets = ammo
        self.capacity = capacity
        self.action = None

    def pull_trigger(self):
        if self.safety:
            print("Safety is on - you need to turn it off!")
        elif:
            self.action == None:
                print("You haven't even put a clip in yet!")
        else:
            try:
                self.shoot()
            except StopIteration:
                print("Clip is empty - you need to reload")

    def check_clip_ammo(self):
        dup = self.action
        num_bullets = 0
        for _ in dup:
            num_bullets += 1
        print("{} bullets left in clip".format(num_bullets))

    def shoot(self):
        print("# ~BANG~ #")
        self.action.next()

    def reload(self):
        self.eject_clip()
        if self.bullets == 0:
            print("Out of ammo")
        else:
            self.load_clip()        

    def load_clip(self):
        if self.clip_count > 0:
            load = [x for x in range(self.capacity)][::-1]
            self.bullets -= self.capacity
        else:
            load = [x for x in range(self.bullets)][::-1]
            self.bullets = 0
        print("-- Clip loaded")
        self.action = load        

    def eject_clip(self):
        print("-- Clip ejected")

    def toggle_safety(self):
        self.safety = not self.safety
        if self.safety == True:
            print("Safety is now on")
        else:
            print("Safety off - weapon is hot")

    def safety_state(self):
        print(self.safety)

    def cock_gun(self):
        pass

    def throw_gun(self, target="the target"):
        print("You're out of ammo, so you throw your gun at " + target)
        
