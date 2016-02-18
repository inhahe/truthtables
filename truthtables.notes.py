
# a implies b                 ->
# a is implied by b        <-
# a implies not-b         ->!
# not-a is implied by b  !<-  (???)

## a isn't implied by b          !<- (???)
# a is implied by not-b         <-!  
# not-a is implied by not-b  !<-!
## a isn't implied by not-b          !<-!
# not-a implies b                 !->
## a doesn't imply b                !->  
# not-a implies not-b          !->!
## a doesn't imply not-b           !->! 

# not-a doesn't imply b         !!->
# not-a isn't implied by b      !!<-
# not-a doesn't imply not-b   !!->!
# not-a isn't implied by not-b   !!->!


# or:
## a isn't implied by b          /<-  or <!-   or </-


# what is implied-by-not if False is default?


 is-and-perhaps
                  !<-
                  could-be-but
                  xor
                  or 
                  nor 
                  xnor 
                  could-be-and-not
                  <-
                  isn't-but-perhaps
                  ->

all names:

false          or xand
and 
xleft   "exclusive left"
left                                
xright
right                 
xor                   
or 
nor 
xnor 
nright               
xnleft
nleft                 
xnright
nand 
true             or xnand


names = "false and  x◄  ◄ x►  ►  xor  or  nor  xnor n►  xn◄ n◄ xn► nand  true").split()


or-not left 

xnor is actually nxor!
because xnor itself is the same as nor.  not_both(invert(or))).
 alternatively it could be considered not_neither(invert(or)) which results in false.

false is actually nxand, not xnand.

all symbols: "^^ &  ->!   ◄  !<-    ►  ^      |  !|  !^  ►!  <-  !◄  ->  !&  !^^").split()

all symbols: "^^ &  &!   ◄ 

but then we change 'is implied by' to n!&  except that !& looks like nand 
we change 'implies' to n&!         

a==1 ◄ b==2                 a==1 !◄ b==2                 a==1 ►! b==2                 a==1 ►! b==2                 

a==1 left b==3           a==1 !left b==3         a==1 right b==3           a==1 !right b==3         

 x==1  <*   b==3             x==1  *>   b==3                 x==1  !<*   b==3             x==1  *>!   b==3

a==1 <~ b==3               a==1 !<~ b==3           a==1 ~> b==3                 a==1 ~>! b==3

x==1  p  b==3	     x==1  q  b==3                x==1  !p  b==3	     x==1  !q  b==3

tables.update({"-/>":  3, "</-": 5, "</-!": 10, "!</-": 12})                             # e.g. 'not-a is true' as if that were 'not-a is not implied by b' as if that were '!</-'


                                                                                                                    # or just use a/!a/b/!b, or !left, or !t[0], or !first, or "first-only" but that's just like could-be-and-not


"!   &   !->    ◄  !<-  ►  ^  |  !|  !^    !►   <-    !◄  ->  !&  !!").split()

names = "xand  and  n->  ◄ n<-  ►  xor  or  nor  xnor n►  <- n◄  ->  nand  xnand").split()




# names = "false  and  n->  ◄  n<-  ►  xor  or  nor  xnor  n►  <-  n◄  ->  nand  true").split()
# names = "n  &  n->  ◄  n<-  ►  ^  |  n|  n^  n►  <-  n◄  ->  n&  nn").split()
# names = "n  &  x◄  ◄  x►  ►  ^  |  n|  n^  n►  xn►  n◄  xn◄  n&  nn").split()
# names = "n  &  x◄  ◄  x►  ►  x|  |  n|  nx|  n►  xn►  n◄  xn◄  n&  nn").split()
# names = "x&  &  x◄  ◄  x►  ►  x|  |  n|  nx|  n►  xn►  n◄  xn◄  n&  nx&").split()

# names = "f  &  x◄  ◄  x►  ►  x|  |  n|  nx|  n►  xn►  n◄  xn◄  n&  t").split()
# names = "n*  &  x◄  ◄  x►  ►  x|  |  n|  nx|  n►  xn►  n◄  xn◄  n&  *").split()
# names = "0  &  x◄  ◄  x►  ►  x|  |  n|  nx|  n►  xn►  n◄  xn◄  n&  1").split()

/[ny, y]    [n*, *]    /[nt, t]
[n, y]      /[n, *]      [n, t]    /[n, 1]                n, * illogical
[f, t]     /[0, 1]   
[x, xn]  /[n, nn]
[x&, nx&]  < logical

[n*, *]
[n, y]
       [n, t]
       [f, t]
       [n, nn]
[x, *]
[x, y]
       [x, t]
       [x, nx]

[n&, xn&]

/[no, yes]     [false, true]   [xand, xnand]  /[never, always]   /[n, nn]   /[x, nx]   < latter two probably illogical


 ^ or x|      # x| fewer symbols but ^ readily understood
n-> or x◄    # x◄ fewer symbols, easier to understand, hard to type, -> is already standandized
◄ or <   

  # names = "nt  &  x◄  ◄  x►  ►  x|  |  n|  nx|  n►  xn►  n◄  xn◄  n&  t").split()-
# names = "n  &  x◄  ◄  x►  ►  x|  |  n|  nx|  n►  xn►  n◄  xn◄  n&  y").split()
# names = "n  &  x<  <  x>  >  x|  |  n|  nx|  n>  xn<  n<  xn<  n&  y").split()-

# names = "n  &  x<  <  x>  >  ^  |  n|  x^  n>  nx<  n<  nx<  n&  y").split()-

# names = "ny  &  x◄  ◄  x►  ►  x|  |  n|  nx|  n►  xn►  n◄  xn◄  n&  y").split()-


# names = "false  and  n->  ◄  n<-  ►  xor  or  nor  xnor  n►  <-  n◄  ->  nand  true").split()
# names = "x  &  n->  ◄  n<-  ►  ^  |  n|  n^  n►  <-  n◄  ->  n&  nx").split()
# names = "x  &  x◄  ◄  x►  ►  ^  |  n|  n^  n►  xn►  n◄  xn◄  n&  nx").split()
# names = "x  &  x◄  ◄  x►  ►  x|  |  n|  nx|  n►  xn►  n◄  xn◄  n&  nx").split()
# names = "x  &  x◄  ◄  x►  ►  x|  |  n|  nx|  n►  xn►  n◄  xn◄  n&  nx").split()

# names = "xand  and  xleft  left  xright  right  xor  or  nor  xnor  nright  xnleft  nleft  xnright  nand  xnand".split()
# names = "no  and  xleft  left  xright  right  xor  or  nor  xnor  nright  xnleft  nleft  xnright  nand  yes".split()
# names = "false  and  xleft  left  xright  right  xor  or  nor  xnor  nright  xnleft  nleft  xnright  nand  true".split()
# names = "never  and  xleft  left  xright  right  xor  or  nor  xnor  nright  xnleft  nleft  xnright  nand  always".split()
# names = "n  and  xleft  left  xright  right  xor  or  nor  xnor  nright  xnleft  nleft  xnright  nand  nn".split()
# names = "x  and  xleft  left  xright  right  xor  or  nor  xnor  nright  xnleft  nleft  xnright  nand  nx".split()

names = "false and  x◄  ◄ x►  ►  xor  or  nor  xnor n►  xn◄ n◄ xn► nand  true").split()