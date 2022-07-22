#  settings.py

import sarg
Debug   = 0             # Debug level

CmdScale          = sarg.Int("scale", 2)  # 2 generally just right
CmdEncapsuleLayer = sarg.Int("layer", 2)  # 2 shows detail of outermost circuit

BGCOLOR = (250,250,250)
RED     = (255,  0,  0)
GREEN   = (  0,255,  0)
BLUE    = (  0,  0,255)
YELLOW  = (255,255,  0)

COLD = BLUE    # wire colors
HOT  = RED

TICKS_PER_SECOND = 200

SCREEN_WIDTH  = sarg.Int("width", 1200)
SCREEN_HEIGHT = sarg.Int("height", 600)

PULS_INTERVAL       = 50   # ticks
MULT_PULS_HALFCYCLE = 50   # ticks each half

