
#!/usr/bin/python
# -*- coding: utf-8 -*-
def cheeseshop(kind,*arguments,**keywords):
  print "-- Do you hava any",kind,"?"
  print "-- I'm sorry,we're all out of",kind
  for arg in arguments:
    print arg
  print "-"*40
  keys = sorted(keywords.keys())
  for kw in keys:
    print kw,":",keywords[kw]

cheeseshop("Limurger","It's very runny,sir.",
          "It's really very,VERY runny,sir.",
          shopkeeper="Michael Palin",
          client="John Cleese",
          sketch="Cheese Shop Sketch")   

