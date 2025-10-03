import time
from random import randint
from time import sleep
import random

import pygame
pygame.init()
clock = pygame.time.Clock()
an = 0
mw = pygame.display.set_mode((1300, 700))
fon1 = pygame.image.load("fon2.jpg")
fon1 = pygame.transform.scale(fon1, (1300, 700))
fon2 = pygame.image.load("fon3.png")
fon2 = pygame.transform.scale(fon2, (1300, 700))
#if enemy.anim == enemy.right or enemy.anim == enemy.up:
#   mw.blit(v1[an], (enemy.rect.x + 30, enemy.rect.y))
#else:
#    mw.blit(v2[an], (enemy.rect.x - 60, enemy.rect.y))

i1 = pygame.image.load('2482598597.png')
i1 = pygame.transform.scale(i1, (40, 70))
i2 = pygame.image.load('24825yth.png')
i2 = pygame.transform.scale(i2, (40, 70))
i3 = pygame.image.load('2482590.png')
i3 = pygame.transform.scale(i3, (40, 70))

i4 = pygame.image.load('341.png')
i4 = pygame.transform.scale(i4, (40, 70))
i5 = pygame.image.load('452897443133333333333.png')
i5 = pygame.transform.scale(i5, (40, 70))
i6 = pygame.image.load('48584524524524529.png')
i6 = pygame.transform.scale(i6, (40, 70))

i7 = pygame.image.load('833833883.png')
i7 = pygame.transform.scale(i7, (40, 70))
i8 = pygame.image.load('erdfca.png')
i8 = pygame.transform.scale(i8, (40, 70))

i9 = pygame.image.load('413133.png')
i9 = pygame.transform.scale(i9, (40, 70))
i10 = pygame.image.load('372832787823.png')
i10 = pygame.transform.scale(i10, (40, 70))
i11 = pygame.image.load('372832787823.png')
i11 = pygame.transform.scale(i11, (40, 70))

i12 = pygame.image.load('1.png')
i12 = pygame.transform.scale(i12, (40, 70))
i13 = pygame.image.load('2.png')
i13 = pygame.transform.scale(i13, (40, 70))
i14 = pygame.image.load('3.png')
i14 = pygame.transform.scale(i14, (40, 70))

i15 = pygame.image.load('4.png')
i15 = pygame.transform.scale(i15, (40, 70))
i16 = pygame.image.load('5.png')
i16 = pygame.transform.scale(i16, (40, 70))
i17 = pygame.image.load('6.png')
i17 = pygame.transform.scale(i17, (40, 70))

i18 = pygame.image.load('7.png')
i18 = pygame.transform.scale(i18, (40, 70))
i19 = pygame.image.load('8.png')
i19 = pygame.transform.scale(i19, (40, 70))

i20 = pygame.image.load('9.png')
i20 = pygame.transform.scale(i20, (40, 70))
i21 = pygame.image.load('10.png')
i21 = pygame.transform.scale(i21, (40, 70))

i22 = pygame.image.load('4.png')
i22 = pygame.transform.scale(i22, (40, 70))

i23 = pygame.image.load('stena1.jpg')

i24 = pygame.image.load('gun1.png')
i24 = pygame.transform.scale(i24, (40, 20))
i25 = pygame.image.load('gun2.png')
i25 = pygame.transform.scale(i25, (40, 20))
i26 = pygame.image.load('gun3.png')
i26 = pygame.transform.scale(i26, (40, 20))
i27 = pygame.image.load('gun5.png')
i27 = pygame.transform.scale(i27, (40, 20))

i28 = pygame.image.load('e6.png')
i28 = pygame.transform.scale(i28, (40, 70))
i29 = pygame.image.load('e7.png')
i29 = pygame.transform.scale(i29, (40, 70))
i30 = pygame.image.load('e8.png')
i30 = pygame.transform.scale(i30, (40, 70))

i31 = pygame.image.load('e3.png')
i31 = pygame.transform.scale(i31, (40, 70))
i32 = pygame.image.load('e4.png')
i32 = pygame.transform.scale(i32, (40, 70))
i33 = pygame.image.load('e5.png')
i33 = pygame.transform.scale(i33, (40, 70))

i34 = pygame.image.load('e9.png')
i34 = pygame.transform.scale(i34, (40, 70))
i35 = pygame.image.load('e10.png')
i35 = pygame.transform.scale(i35, (40, 70))

i36 = pygame.image.load('e1.png')
i36 = pygame.transform.scale(i36, (40, 70))
i37 = pygame.image.load('e2.png')
i37 = pygame.transform.scale(i37, (40, 70))

#up
z1 = pygame.image.load('z1.png')
z1 = pygame.transform.scale(z1, (40, 50))
z2 = pygame.image.load('z2.png')
z2 = pygame.transform.scale(z2, (40, 50))
z3 = pygame.image.load('z3.png')
z3 = pygame.transform.scale(z3, (40, 50))

#l
z4 = pygame.image.load('z4.png')
z4 = pygame.transform.scale(z4, (40, 50))
z5 = pygame.image.load('z5.png')
z5 = pygame.transform.scale(z5, (40, 50))

#r
z6 = pygame.image.load('z6.png')
z6 = pygame.transform.scale(z6, (40, 50))
z7 = pygame.image.load('z7.png')
z7 = pygame.transform.scale(z7, (40, 50))

#d
z8 = pygame.image.load('z8.png')
z8 = pygame.transform.scale(z8, (40, 50))
z9 = pygame.image.load('z9.png')
z9 = pygame.transform.scale(z9, (40, 50))
z10 = pygame.image.load('z10.png')
z10 = pygame.transform.scale(z10, (40, 50))


f1 = pygame.image.load('f1.png')
f1 = pygame.transform.scale(f1, (40, 50))
f2 = pygame.image.load('f2.png')
f2 = pygame.transform.scale(f2, (40, 50))
f3 = pygame.image.load('f3.png')
f3 = pygame.transform.scale(f3, (40, 50))

f4 = pygame.image.load('f4.png')
f4 = pygame.transform.scale(f4, (40, 50))
f5 = pygame.image.load('f5.png')
f5 = pygame.transform.scale(f5, (40, 50))

f6 = pygame.image.load('f6.png')
f6 = pygame.transform.scale(f6, (40, 50))
f7 = pygame.image.load('f7.png')
f7 = pygame.transform.scale(f7, (40, 50))

f8 = pygame.image.load('f8.png')
f8 = pygame.transform.scale(f8, (40, 50))
f9 = pygame.image.load('f9.png')
f9 = pygame.transform.scale(f9, (40, 50))
f10 = pygame.image.load('f10.png')
f10 = pygame.transform.scale(f10, (40, 50))

t2 = pygame.image.load('t2.png')
t3 = pygame.image.load('t3.png')
t4 = pygame.image.load('t4.png')
t5 = pygame.image.load('t5.png')

d1 = pygame.image.load('d1.png')
d2 = pygame.image.load('d2.png')
down_hero = (
    i1,
    i2,
    i3)
up_hero = (
    i4,
    i5,
    i6,
)
left_hero = (
    i7,
    i8
)
right_hero = (
    i9,
    i10
)

game = True
anim_a = 0
speed_hero = 10
an2 = 0
x = 500
y =  500
Health_hero = 100
an3 = 0
st = 0
maks_p = 5
perezaryadka = maks_p
p2 = 0
armor = 100
emn = 0
fon_num = randint(1, 2)
if fon_num == 1:
    fon = fon1
if fon_num == 2:
    fon = fon2
class npc:
    def __init__(self, x_npc, y_npc, damage, Health, speed, distance, peresaryadka_npc, pole_vidimosti, im1 = i1, im2 = i2, im3 = i3, im4 = i4, im5 = i5, im6 = i6, im7 = i7, im8 = i8, im9=i9, im10 = i10, im11 = i11):
        self.Health = Health
        self.pole_vidimosti = pole_vidimosti
        self.peresaryadka_npc = peresaryadka_npc
        self.distance = distance
        self.speed = speed
        self.im1 = im1
        self.im2 = im2
        self.im3 = im3
        self.im4 = im4
        self.im5 = im5
        self.im6 = im6
        self.im7 = im7
        self.im8 = im8
        self.im9 = im9
        self.im10 = im10
        self.im11 = im11
        self.damage = damage
        self.st = st
        self.last_attack_time = 0
        self.pos_player = 0



        self.down = (
            self.im1,
            self.im2,
            self.im3,
        )
        self.up = (
            self.im4,
            self.im5,
            self.im6,        )
        self.left = (
            self.im7,
            self.im8,
        )
        self.right = (
            self.im9,
            self.im10,
        )
        self.stop = (
            self.im5,
            self.im5,
        )
        self.anim = self.stop
        self.rect = self.anim[0].get_rect(topleft=(x_npc, y_npc))
        self.rect.x = x_npc
        self.rect.y = y_npc



    def movee_anim(self, x, y):
        if self.rect.y < y:
            self.anim = self.down
        if self.rect.y > y :
            self.anim = self.up
        if self.rect.x < x :
            self.anim = self.right
        if self.rect.x > x :
            self.anim = self.left



    def movee(self, x, y):
        if abs(self.rect.x - x) < self.pole_vidimosti and abs(self.rect.y - y) < self.pole_vidimosti or self.pos_player == 1:
            if self.rect.x < x:
                self.rect.x += self.speed
            elif self.rect.x > x:
                self.rect.x -= self.speed

            if self.rect.y < y:
                self.rect.y += self.speed
            elif self.rect.y > y:
                self.rect.y -= self.speed


    def draw(self, mw, an):
        mw.blit(self.anim[an], self.rect)
        pygame.draw.rect(mw, (250, 0, 25), (self.rect.x - 35, self.rect.y - 10, self.Health, 10))











fire_delay = 0.2
last_fire_time = 0
class pulya():
    def __init__(self, damage, radius, speed, color, direction ):
        self.damage = damage
        self.radius = radius
        self.speed = speed
        self.color = color
        self.x_p = x_gun + 12
        self.y_p = y_gun + 12
        self.direction = direction
        self.rect = pygame.Rect(self.x_p, self.y_p, self.radius, self.radius)

    def movee(self):
        if self.direction == 'right':
            self.x_p += self.speed
            self.y_p += random.randint(-7, 7)
        if self.direction == 'left':
            self.x_p -= self.speed
            self.y_p += random.randint(-7, 7)
        if self.direction == 'down':
            self.y_p += self.speed
            self.x_p += random.randint(-7, 7)
        if self.direction == 'up':
            self.y_p -= self.speed
            self.x_p += random.randint(-7, 7)
    def draw(self):
        pygame.draw.circle(mw, self.color, (self.x_p, self.y_p), self.radius)
class pulya_enemy():
    def __init__(self, damage, radius, speed, color, x_p, y_p, ):
        self.damage = damage
        self.radius = radius
        self.speed = speed
        self.color = color
        self.x_p = x_p
        self.y_p = y_p

    def movee(self, x, y):
        if self.x_p < x:
            self.x_p += self.speed
        if self.x_p > x:
            self.x_p -= self.speed
        if self.y_p < y:
            self.y_p += self.speed
        if self.y_p > y:
            self.y_p -= self.speed

    def draw(self):
        pygame.draw.circle(mw, self.color, (self.x_p, self.y_p), self.radius)






class block():
    def __init__(self, x_block, y_block, width, height, width2, height2, image_block):
        self.x_block= x_block
        self.y_block = y_block
        self.width = width
        self.height = height
        self.width2 = width2
        self.height2 = height2
        self.image_block = image_block
        self.image_block = pygame.transform.scale(self.image_block, (self.width, self.height))
        self.rect = self.image_block.get_rect(topleft=(x_block, y_block))
        self.rect.x = x_block
        self.rect.y = y_block
    def draw(self):
        mw.blit(self.image_block, self.rect)
class dom():
    def __init__(self, x_block, y_block, width, height, width2, height2, Health, peresaryadka, image_block):
        self.x_block= x_block
        self.y_block = y_block
        self.width = width
        self.height = height
        self.width2 = width2
        self.height2 = height2
        self.image_block = image_block
        self.Health = Health
        self.peresaryadka = peresaryadka
        self.image_block = pygame.transform.scale(self.image_block, (self.width, self.height))
        self.rect = self.image_block.get_rect(topleft=(x_block, y_block))
        self.rect.x = x_block
        self.rect.y = y_block
        self.last_attack_time = 0

    def draw(self):
        mw.blit(self.image_block, self.rect)



mnozyna_enemy = 0
direction = 'right'
bulets = []
bulets_enemy = []
cats = []
enemys = []
bloks = []
x_gun = x + 10
y_gun = y
gun_anim = i25
doma = []
details = []

cats.append(
npc(
    500,500,
    5, 100, 6, 100, 20, 3000, i21, i20, i14, i15, i16, i17, i18, i19, i12, i13, i22,
                    ))
an4 = 0
raund = 0
wawe = 0
p3 = 0
while game:
    if Health_hero > 0 :
        pygame.display.update()
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        mw.blit(fon, (0, 0))




        rama = pygame.draw.rect(mw, (255,255,255), (0,600, 1300, 200))
        font = pygame.font.Font(None, 40)
        mw.blit(gun_anim, (x_gun, y_gun))

        pygame.draw.rect(mw, (255, 0, 0), (0, 600, Health_hero, 20))
        pygame.draw.rect(mw, (250, 250, 25), (0, 620, perezaryadka * 20, 30))
        text = font.render("кількість патронів", True, (250, 250, 25))
        mw.blit(text, [maks_p * 20, 620])
        text = font.render("життя", True, (250, 0, 5))
        mw.blit(text, [Health_hero , 600])
        pygame.draw.rect(mw, (60, 60, 60), (0, 640, armor, 30))
        text = font.render("захист", True, (60, 60, 60))
        mw.blit(text, [armor, 640])
        text = font.render("кількість ворогів", True, (0, 0, 0))
        mw.blit(text, [1000, 600])
        text = font.render(str(mnozyna_enemy), True, (0, 0, 0))
        mw.blit(text, [1250, 600])
        text = font.render("рівень", True, (0, 0, 0))
        mw.blit(text, [1000, 620])
        text = font.render(str(wawe), True, (0, 0, 0))
        mw.blit(text, [1100, 620])









        if not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a]:
            k1 = mw.blit(i11, (x, y))
        if keys[pygame.K_d] and keys[pygame.K_s] or keys[pygame.K_d] and keys[pygame.K_w] or keys[pygame.K_d] and keys[pygame.K_a] or keys[pygame.K_s] and keys[pygame.K_a] or keys[pygame.K_s] and keys[pygame.K_w] or keys[pygame.K_a] and keys[pygame.K_w]:
            k1 = mw.blit(i11, (x, y))
        if keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a]:
            i11 = i10
            x += speed_hero
            k2 = mw.blit(right_hero[an], (x, y))
        if keys[pygame.K_w] and not keys[pygame.K_d] and not keys[pygame.K_s] and not keys[pygame.K_a]:
            i11 = i6
            y -= speed_hero
            k2 = mw.blit(up_hero[an], (x, y))
        if keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_d] and not keys[pygame.K_a]:
            i11 = i3
            y += speed_hero
            k2 = mw.blit(down_hero[an], (x, y))
        if keys[pygame.K_a] and not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_d]:
            x -= speed_hero
            i11 = i8
            k2 = mw.blit(left_hero[an], (x, y))
        if click[0] and time.time() - last_fire_time > fire_delay and perezaryadka > 0:
            if i11 == i10:
                direction = 'right'
            elif i11 == i8:
                direction = 'left'
            elif i11 == i3:
                direction = 'down'
            elif i11 == i6:
                direction = 'up'


            bulets.append(pulya(20,4, 20, (200, 250, 25), direction))
            last_fire_time = time.time()
            perezaryadka -= 1

        if i11 == i10:
            gun_anim = i25
            x_gun = x + 20
            y_gun = y + 20
        if i11 == i8:
            gun_anim = i24
            x_gun = x - 20
            y_gun = y + 20
        if i11 == i3:
            gun_anim = i27
            x_gun = x  + 25
            y_gun = y + 45
        if i11 == i6:
            gun_anim = i26
            x_gun = x + 15
            y_gun = y + 10



        if x > 1300:
            x -= speed_hero
        elif x < 0:
            x += speed_hero
        elif y < 0:
            y += speed_hero
        elif y > 500:
            y -= speed_hero









        if an < 2:
            sleep(0.08)
            an += 1
            an2 += 1
            an3 += 1

        if an == 2:
            an = 0
        if perezaryadka < maks_p:
            p2 += 1
            if p2 == 5:
                perezaryadka += 1
                p2 = 0
        if armor < 100:
            p3 += 1
            if p3 == 10:
                armor += 3
                p3 = 0
        for B in bloks[:]:
            if B.rect.colliderect(pygame.Rect(x, y,  B.width2, B.height2)):

                overlap_x = min(B.rect.right - x, x + B.width2 - B.rect.left)
                overlap_y = min(B.rect.bottom - y, y +  B.height2 - B.rect.top)


                if overlap_x < overlap_y:

                    if x < B.rect.centerx:
                        x = B.rect.left -  B.width2
                    else:
                        x = B.rect.right
                else:

                    if y < B.rect.centery:
                        y = B.rect.top - B.height2
                    else:
                        y = B.rect.bottom
            for enemy in enemys[:]:
                if B.rect.colliderect(pygame.Rect(enemy.rect.x, enemy.rect.y,  B.width2, B.height2)):

                    overlap_x = min(B.rect.right - enemy.rect.x, enemy.rect.x +  B.width2 - B.rect.left)
                    overlap_y = min(B.rect.bottom - enemy.rect.y, enemy.rect.y + B.height2 - B.rect.top)

                    if overlap_x < overlap_y:

                        if enemy.rect.x < B.rect.centerx:
                            enemy.rect.x = B.rect.left -  B.width2
                        else:
                            enemy.rect.x = B.rect.right
                    else:

                        if enemy.rect.y < B.rect.centery:
                            enemy.rect.y = B.rect.top - B.height2
                        else:
                            enemy.rect.y = B.rect.bottom
        for D in doma[:]:
            if emn < 6:
                if D.last_attack_time == D.peresaryadka:
                    enemys.append(
                        npc(
                            D.x_block,  D.y_block ,
                            7, 100, 3.8, 100, 25, 1350,
                            f1, f2, f3, f8, f9, f10, f4, f5, f6, f7, f2,
                        )
                    )
                    D.last_attack_time = 0
                    mnozyna_enemy += 1
                    emn += 1
                else:
                    D.last_attack_time += 1
            else:
                doma.remove(D)


        for enemy in enemys[:]:
            if enemy.Health > 0:
                if abs(enemy.rect.x - x) < enemy.distance and abs(enemy.rect.y - y) < enemy.distance:
                    if enemy.last_attack_time == enemy.peresaryadka_npc:
                        if armor > 0:
                            armor -= enemy.damage
                            enemy.last_attack_time = 0
                        else:
                            Health_hero -= enemy.damage
                            enemy.last_attack_time = 0
                    else:
                        enemy.last_attack_time += 1
                        enemy.pole_vidimosti += 500





                for bulet in bulets[:]:
                    if enemy.rect.collidepoint(bulet.x_p, bulet.y_p):
                        enemy.Health -= bulet.damage
                        bulets.remove(bulet)
                        enemy.pos_player = 1


            else:
                enemys.remove(enemy)

        if len(enemys) < 15 and raund == 0:
            raund = 1
            an4 = 0


        if len(enemys) == 0 and raund == 1:
            an4 += 1
            font = pygame.font.Font(None, 250)
            text = font.render(str(wawe), True, [50, 50, 50])
            mw.blit(text, [800, 300])
            font = pygame.font.Font(None, 250)
            text = font.render("Рівень", True, [50, 50, 50])
            mw.blit(text, [250, 300])
            bloks.clear()
            details.clear()
            doma.clear()
            mnozyna_enemy = 0
            x = 500
            y =  500
            if an4 == 40:
                wawe += 1
                raund = 0
                skeletons = randint(3, 5)
                zombie = randint(3, 5)
                camin2 = randint(2, 3)
                cust = randint(3, 5)
                derevo = randint(2, 4)
                cherep = randint(2, 6)
                fon_num = randint(1, 2)
                if fon_num == 1:
                    fon = fon1
                if fon_num == 2:
                    fon = fon2
                for _ in range(skeletons):
                    enemys.append(
                        npc(
                            random.randint(50, 1000), random.randint(50, 450),
                            20, 50, 5, 100, 15, 150 ,
                            i28, i29, i30, i31, i32, i33, i34, i35, i36, i37, i32,
                        )
                    )
                    mnozyna_enemy += 1
                for _ in range(zombie):
                    enemys.append(
                        npc(
                            randint(50, 1000), randint(50, 450),
                            5, 100, 2.5, 100, 25, 350,
                            z1, z2, z3, z8, z9, z10, z4, z5, z6, z7, z2,
                        )
                    )
                    mnozyna_enemy += 1
                if fon_num == 2:
                    for _ in range(camin2):
                        bloks.append(
                            block(
                                random.randint(50, 1000), random.randint(50, 450), 50, 50, 25, 25, t2,))
                    for _ in range(cust):
                        details.append(block(
                                random.randint(50, 1000), random.randint(50, 450), 70, 70, 15, 30, t3,))
                    for _ in range(derevo):
                        bloks.append(block(
                                random.randint(50, 1000), random.randint(50, 450), 40, 100, 15, 5, t4,))
                    for _ in range(1):
                        doma.append(
                            dom(
                                random.randint(300, 800), random.randint(0, 100), 200, 200, 1, 1, 250, 100, d1))
                        bloks.append(
                            dom(
                                random.randint(300, 800), random.randint(0, 100), 200, 200, 1, 1, 250, 100, d1))
                else:
                    for _ in range(1):
                        details.append(block(
                                random.randint(50, 1000), random.randint(50, 450), 20, 40, 45, 40, t5,))
                        for _ in range(1):
                            doma.append(
                                dom(
                                    random.randint(300, 800), random.randint(0, 200), 150, 250, 1, 1, 250, 100, d2))
                            bloks.append(
                                dom(
                                    random.randint(300, 800), random.randint(0, 200), 150, 250, 1, 1, 250, 100, d2))




                an4 = 0
        for detail in details:
            detail.draw()
        for enemy in enemys:
            enemy.draw(mw, an)
            enemy.movee(x, y)
            enemy.movee_anim(x,y)

        for bulet_enemy in bulets_enemy[:]:
            bulet_enemy.movee(x, y)
            bulet_enemy.draw()
        for bulet_enemy in bulets_enemy[:]:
            if x == bulet_enemy.x_p and y == bulet_enemy.y_p:
                Health_hero +=  bulet_enemy.damage
                bulets_enemy.remove(bulet_enemy)
        for cat in cats:
            cat.draw(mw, an)
            cat.movee(x, y)
            cat.movee_anim(x, y)
        for cat in cats:
            if abs(cat.rect.x - x) < cat.distance and abs(cat.rect.y - y) < cat.distance and Health_hero < 100:
                if cat.last_attack_time == cat.peresaryadka_npc:
                        bulets_enemy.append(pulya_enemy(10, 5, 5, (100, 250, 205), cat.rect.x, cat.rect.y))
                        cat.last_attack_time = 0
                else:
                    cat.last_attack_time += 1

        for bulet in bulets[:]:
            bulet.movee()
            if bulet.x_p > 1500 or bulet.x_p < 100 or bulet.y_p < 50 or bulet.y_p > 750:
                bulets.remove(bulet)
            else:
                bulet.draw()


        for B in bloks[:]:
            B.draw()

    else:
        font = pygame.font.Font(None, 100)
        font2 = pygame.font.Font(None, 50)
        text = font.render("Гру закінчено", True, (255, 0, 0))
        text4 = font2.render("нажміть Enter щоб почати знову ", True, (255, 255, 255))
        mw.blit(text, [300, 400])
        mw.blit(text4, [300, 500])
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            enemys.clear()
            bloks.clear()
            details.clear()
            bulets_enemy.clear()
            bulets.clear()
            cats.clear()
            Health_hero = 100
            armor = 100
            perezaryadka = 5
            cats.append(
                npc(
                    500, 500,
                    5, 100, 6, 100, 20, 3000, i21, i20, i14, i15, i16, i17, i18, i19, i12, i13, i22,
                ))
            raund = 0
            wawe = 0
            x = 500
            y =  500
            doma.clear()
            mnozyna_enemy = 0




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()



clock.tick(60)