#-*- encoding: utf-8 -*-

#todo: rearrange the order so that bit-index = left*2+right
#noimplies, nxleft/nx</etc.
#look for implies/noimplies before nxleft/xleft
#"<-", "->"  ~ ! n 

words, symbols, t, f, xand, x, n, nx, nn, nt, implies, noimplies, xleft, nxleft, angles, pointers, nocaret  = xrange(1, 18) 
nxand = xnand = xand;     true, false = t, f;        xright = xleft;       xnleft = xnright = nxright = nxleft

def getnames(*args, **kwargs):
  mode = (words, symbols)[symbols in args]

  if mode==words:
    names = "false  and  xleft  left  xright  right  xor  or  nor  xnor  nright  nxright  nleft  nxleft  nand  true".split()
  else:
    names = "f  &  x◄  ◄  x►  ►  ^  |  ~|  ~^  ←  ~► →  ~◄  ~&  t".split()      

  if implies in args:
    names[13] == ("->", "implies")[mode==words]
    names[11] == ("<-", "implied-by")[mode==words]
    names[3] = ("n->", "nimplies")[mode==words]
    names[5] = ("n<-", "nimplied-by")[mode==words]
  if (xand in args 
      or kwargs.get(false, None) in ("x&", xand) 
      or kwargs.get(true, None) in ("nx&", "!x&", "x!&", "xn&", nxand) ):
     names[0] = ("x&", "xand")[mode==words]
     names[15] = ("nx&", "nxand")[mode==words]
           #  technically we could pass true=xand and it would work, but oh well. 

  if mode==symbols:
    sl, sr = "<>"
    if pointers in argse:
      sl, sr = "◄►"

    af = kwargs.get(false, None)
    at = kwargs.get(true, None)
    if af == "n*":
      sf, st = "n*", "*"
    elif af == x or at == "*":
      sf = "x"
      st = {"*": "*", y: "y", t: "t", nx: "nx"}.get(at, "*")
    elif af == n:
      sf = "n"
      st = {y: "y", t: "t", nn: "nn"}.get(at, "t")
    elif af == f:
      sf, st = "ft"
    elif af == "x&" or at in ("nx&", "xn&"):
      sf = af
      st = at if at else "nx&"
    if af == nt and at in (t, None):
      sf, st = "nt", "t"
    if sf and st:
      names[0] = sf
      names[15] = st
    if nocaret in args:
      names[6] = "x|"
      names[9] = "nx|"

  if xleft in args:
    names[3] = ("x"+sl, "xleft")[mode==words]
    names[5] = ("x"+sr, "xright")[mode==words]

  if mode==symbols and "!" in args:
    names = [(x.replace("n", "!"), x[0].replace("n", "!")+x[1:])[mode==words] for x in names] 

  return names

lookupl = ["f n ! false xand x& x no none never off 0 n1 !1 nyes nalways nall ntrue ny nt !y !t non !ever !yes !always !all !true"
                 "    n. !. !o -o -. -true -all -always -yes -ever -on -t -y -true  -1 n* !* -* ~* ~true ~y ~t ~on ~ever ~yes ~always ~all"             
                 "    ~true ~o",   
                 "and &",     "nimplies   -implies ~implies    !implies    ~-> -->   n-> xleft x< x◄ !->",      "left  < ◄", 
                                    "nimplied-by !implied-by n<- !<- xright x> x►",    "right ► >",        "xor x| ^",   "or |",
                 "nor n| !| !or",                    "xnor nxor nx| xn| n^ !x| x!| !^ !xor",                                   "n► !► n> !> nright !right",   
                 "implied-by <- nx◄ !x◄ x!◄  !x< x!< xn◄ nx< xn< nxleft   xnleft   !xleft",                            "n◄ !◄ n< !< nleft !left",   
                 "implies      -> nx► !x► x!►  !x> x!> xn► nx> xn> nxright xnright !xright",     
                 "nand !and n& !&",      
                 "t * nn !! y t nx& !x& x!& xn& true xnand nxand yes always all 1 on nnever noff nno nnone nfalse nf !f !1 ever n0 !0 o ."
                 "    !xand !never !off !no !none !false nx !x -x -none -false -no -off -never -xand -0 -1 -f -xand -x& -- ~x& ~xand ~f ~1"
                 "    ~0 ~xand ~never ~off ~no ~false ~none ~x"]

def getlookup():
  return dict(((k, c) for c, s in enumerate(lookupl) for k in s.split()))


