import pygame
import platform
import asyncio
import random

w = 800
h = 700
cs = 15
ui = 1.0
wt = (255, 255, 255)
bk = (0, 0, 0)

def init():
    global s, g, gen
    pygame.init()
    s = pygame.display.set_mode((w, h))
    g = set()
    gen = 0
    for _ in range(500):
        x = random.randint(-15, 15)
        y = random.randint(-15, 15)
        g.add((x, y))

def nbs(c):
    x, y = c
    return [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]

def nextgen():
    global g
    tc = set(g)
    for c in g:
        tc.update(nbs(c))
    ng = set()
    for c in tc:
        ns = nbs(c)
        ln = sum(1 for n in ns if n in g)
        if c in g and ln in [2, 3]:
            ng.add(c)
        elif c not in g and ln == 3:
            ng.add(c)
    g = ng

def draw():
    s.fill(bk)
    ox = w // 2
    oy = h // 2
    for x, y in g:
        sx = x * cs + ox
        sy = y * cs + oy
        if 0 <= sx < w and 0 <= sy < h:
            pygame.draw.rect(s, wt, (sx, sy, cs - 1, cs - 1))
    f = pygame.font.Font(None, 36)
    t = f.render(f"gen: {gen}", True, wt)
    s.blit(t, (10, 10))
    pygame.display.flip()

async def main():
    global gen
    init()
    r = True
    while r:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                r = False
        nextgen()
        gen += 1
        draw()
        await asyncio.sleep(ui)
    pygame.quit()

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())
