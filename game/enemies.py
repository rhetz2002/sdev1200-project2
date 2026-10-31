class mage(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.image = pygame.image.load('sprites/enemy_mage.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

    def atk(self):
        
        bullet = orange_bullet()

        bullet.fire(self.rect.x, self.rect.y)

        return bullet

    def spawn(self, item):

        self.rect.topleft = (item, -110)

    def update(self):

        self.rect.y += 1

        if self.rect.y >= 900:

            self.kill()

class mele(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.image = pygame.image.load('sprites/enemy_mele.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

    def atk(self):
        
        bullet = orange_bullet()

        bullet.fire(self.rect.x, self.rect.y)

        return bullet

    def spawn(self, item):

        self.rect.topleft = (item, -110)

    def update(self):

        self.rect.y += 1

        if self.rect.y >= 900:

            self.kill()

