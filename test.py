import math,asyncio,os,subprocess,time
from playwright.async_api import async_playwright
async def main():
  srv=subprocess.Popen(['python3','-m','http.server','8771'],cwd=os.path.dirname(os.path.abspath(__file__)),stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);time.sleep(1)
  try:
   await run()
  finally: srv.terminate()
async def run():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--headless=new'])
    pg=await b.new_page(viewport={'width':820,'height':620});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:m.type=='error' and errs.append(m.text))
    await pg.goto('http://localhost:8771/index.html');await pg.wait_for_timeout(800);assert not await pg.evaluate('__gk.started'),'timer started before input'
    await pg.keyboard.down('ArrowUp');held=None;shift=False;seen=False
    for i in range(3000):
      s=await pg.evaluate('({x:__gk.car.x,y:__gk.car.y,a:__gk.car.a,l:__gk.laps,g:!!__gk.ghost})')
      if s['l']>=2: 
        if s['g'] and not seen: seen=True
        break
      t=math.atan2((s['y']-280)/170,(s['x']-400)/270)-0.25  # aim ahead, counterclockwise on screen
      tx,ty=400+270*math.cos(t),280+170*math.sin(t)
      d=math.atan2(ty-s['y'],tx-s['x'])-s['a'];d=(d+math.pi)%(2*math.pi)-math.pi
      want='ArrowRight' if d>0.05 else 'ArrowLeft' if d<-0.05 else None
      if want!=held:
        if held: await pg.keyboard.up(held)
        if want: await pg.keyboard.down(want)
        held=want
      if s['l']>=1 and not shift: await pg.keyboard.down('Shift');shift=True
      await pg.wait_for_timeout(30)
    await pg.wait_for_timeout(1500)
    r=await pg.evaluate('({laps:__gk.laps,ghost:__gk.ghost&&__gk.ghost.time,best:__gk.best,ls:Object.keys(localStorage)})')
    await pg.screenshot(path='shot.png');print(r,'houseGhosts:',await pg.evaluate('__gk.houseGhosts.length'),'errors:',errs);await b.close()
asyncio.run(main())
