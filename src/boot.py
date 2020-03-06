# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
import gc


#uos.dupterm(None, 1) # disable REPL on UART(0)
#import webrepl
#webrepl.start()

gc.collect()
