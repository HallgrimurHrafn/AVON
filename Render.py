import Main
import menu
import threading

# basis fyrir forritid thitt kalli og sma documentation
# um hvad tharf ad gera til ad breyta sumum hlutum i
# main fallinu til ad fa effect.

# breyta tempo:
# 1.)   Main.taptemp=0              # af virkja tap tempo a medan
# 2.)   Main.tempo= <value>         # velja tempo
# 3.)   Main.taptemp=1              # virkja tap tempo aftur.

# stylla lengd notu, prosenta af 1. hversu lengi notan lifir yfir 1 slag.
# 1.)   Main.lengd=<value>          # 0<value<1.
#                                   # 0.1 thydir ad notan lifi 90% af timanum.

# stylla lengdina a taktmaelis flashi.
# 1.)   Main.FLASH=<value>          # 0<value<1, i hlutfalli vid tempo.


# skipta um channel/voice/whatever
# 1.)   Main.v=<value>              # value verdur rasin.
# 2.)   Main.ChannelChange()        # ser algjorlega um skiptinguna.

#  liveplay
# 1.)   Main.lGO=1 eda 0            # 0 kveikir og 1 slekkur
# 2.)   Main.multithread()          # held thetta aetti ad duga. tharf ad testa


# skali
# 1.)   Main.skali[i]=<value>       # i visar til trellis, 7 fyrir botm, 0 fyrir top
#                                   # 0<value<128,  MIDI nota.
#                                   # breytir ollum channelum...


# camera
# ekki configured eins og er. nada.


# thad vantar eitthvad render fall sem a ad sja um renderid.
# thannig i stadinn fyrir constant update latum vid menu kalla a thetta
# fall til ad uppfaera skjainn thegar eitthvad er gert
def Render():
# kannski gera eitthvad svo hann uppfaeri sig ekki hradar en refresh rate-id er a skjanum





#
