import os, sys, json  # Unnecessary imports

x = 10
y=  20 # Bad spacing
def badFunction (  a,b ):# No docstring, bad spacing
  if a > 0:print("Positive") # No indentation, inline statement
  else:
      print ("Negative" )  # Extra spaces, inconsistent indentation
  return x+y # Unused variables, bad return

def anotherFunc():
        pass # Bad indentation

class testClass: # Class name should be in PascalCase
 def __init__( self,x,y ):
      self.x=x
      self.y = y
 def method_1( self ): return self.x*self.y  # Inline return, bad spacing

 def method2(self,    a,b): # Inconsistent method naming, bad spacing
  if(a>b): return a   # No indentation
  else:
       return b

def bad_
