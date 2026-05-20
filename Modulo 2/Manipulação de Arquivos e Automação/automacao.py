import pyautogui as pg



#pg.mouseInfo()

pg.press("win")

pg.write("chrome")
pg.sleep(1)
pg.press("enter")
pg.sleep(1)

pg.write("www.youtube.com")
pg.press("enter")

pg.moveTo(816,113, duration=0.5)
pg.sleep(2)

pg.click()
pg.write("fifa")
pg.press("enter")
pg.sleep(2)

pg.moveTo(749,824, duration=0.5)
pg.sleep(2)
pg.click()









