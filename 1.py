print('Hello World!')

import f2
import pyautogui as bot


f2.start()
bot.hotkey('win','r')
bot.typewrite('cmd')
bot.press('enter')
f2.finish()
