#!/usr/bin/env fontforge -script

font0 = fontforge.font()
font0.ascent = 55
font0.descent = 0
char0 = font0.createChar(257)
char0.importOutlines(filename="symbols/CH_CloudHigh/WeatherSymbol_WMO_CloudHigh_CH_1.svg",scale=False)
font0.save("font0_5.sfd")
quit()
