from getnames import *

   #  you can pass any number of the following tokens to getnames() in any order. 
   #
   #          xand: use "xand" and "nxand" for the "false" and "true" gates, or "x&" and "nx&" if using symbols.
   #      implies: use "implies" instead of "nxleft", "nimplied-by" instead of "xright", etc.
   #          xleft: use "xleft" and "xright" instead of "nimplies" and "nimplied-by" (default unless implies is specified).
   #    symbols: use symbolic names for logic gates, e.g. "&" instead of "and".
   #    pointers: use "◄" and "►" instead of "<" and ">" when using symbols.  (symbols can still be typed in using < and >)
   #     nocaret: don't use "^" for "xor" when using symbols.  use "x|" for "xor" and "nx|" for "xnor".
   #             "!": use "!" instead of "n" in names when using symbols.
   #    true and false are keyword-only parameters. they set the names for the "true" and "false" gates when using symbols.
   #      possible false values:     f, n,         "n*", x,     "x&"
   #      possible true values:      t, nn, y,    "*", nx,    "nx&", "xn&", "!x&", "x!&"
   #      not every possible combination of "true" vs. "false" values can be used..
   #
   #  example: 
   #    names = getnames(symbols, nocaret, pointers, "!", true="x&")

#names, lookup = getnames(), getlookup()

names = "xand nor xleft nleft xright nright xor nand and nxor right nxright left nxleft or nxand".split()
lookup = dict(map(reversed, enumerate(names)))

prompt = "<logic gate> <operator> <logic gate>: "

print
while 1:
  try:
    tables = table1, table2, table3 = raw_input(prompt).lower().split()
    t1, t2, t3 = map(lookup.get, tables)
  except:
    raise SystemExit
  
  r = sum((
     x * 
       (
         (
         t2 >> 
           (
             ( (  (t3 & x) > 0) *2 )
             | 
             ((t1 & x) > 0)
           )
         ) 
       > 0
       ) 
     for x in (1, 2, 4, 8)
             
))

   # study order of ops to get rid of parenthesis
  print names[r]


#  print '%s %s %s == %s' % (names[rtable1


# kup[table1].capitalize(), lookup[table2], lookup[table3].capitalize(), names[r].capitalize())

# should we look up all the names instead of using the input?




"""
1 1 0 0  b
1 0 1 0  a
---------             
0 0 0 0        xand
0 0 0 1        nor
0 0 1 0        xleft
0 0 1 1        nleft
0 1 0 0        xright
0 1 0 1        nright
0 1 1 0        xor
0 1 1 1        nand
1 0 0 0        and
1 0 0 1        nxor
1 0 1 0        right
1 0 1 1        nxright
1 1 0 0        left
1 1 0 1        nxleft
1 1 1 0        or
1 1 1 1        nxand
"""









