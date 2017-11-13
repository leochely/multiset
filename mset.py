# -*- coding: cp1252 -*-
# ==============================================================================
"""MULTISET: multi-ensembles"""
# ==============================================================================
__author__  = "Gorbatoff & Banos"
__date__    = "2017-10-20"
# ------------------------------------------------------------------------------
class MultiSet(object): 
 # ----------------------------------------------------------------------------
  def __init__(self, data = None):
      self.dico = {}
      if type(data) == list:
         for value in data:
             if type(value) == tuple:
                self.dico[value[0]] = value[1] 
             else:
                if value in self.dico:
                   self.dico[value] += 1
                else:
                   self.dico[value] = 1
      elif type(data) == tuple:
           for value in data:
               if value in self.dico:
                  self.dico[value] += 1
               else:
                  self.dico[value] = 1
      elif type(data) == set:
           for value in data:
               if value in self.dico:
                  self.dico[value] += 1
               else:
                  self.dico[value] = 1
      elif type(data) == dict:
           self.dico = data
      elif data == None:
           self.dico = {}
      else:
           erreurs = 0
           for value in data:
               if(value.isalpha()):
                  if value in self.dico:
                     self.dico[value] += 1   
                  else:
                     self.dico[value] = 1
               else:
                  erreurs += 1
           if erreurs > 0:
              print ("Ignoring {} out of {}".format(erreurs,len(data))) 
 # ----------------------------------------------------------------------------
  def __repr__ (self):
      return "MultiSet(" + repr(self.dico) + ")" 
 # ----------------------------------------------------------------------------
  def __str__(self):
      aff = "{{"
      for i in self.dico:
          aff += '\n' + str(i) + ": " + repr(self.dico[i]) + "," 
      aff = aff[:len(aff)-1]
      aff += "}}"
      return aff
 # ----------------------------------------------------------------------------
  def __len__(self): 
      s = 0
      for i in self.dico:
          s += self.dico[i]
      return s
 # ----------------------------------------------------------------------------
  def __iter__(self):
      for i in self.dico:
          yield i 
 # ----------------------------------------------------------------------------
  def __contains__(self, element):
      return element in self.dico 
 # ----------------------------------------------------------------------------
  def to_Set(self):
      return set(self.dico) 
 # ----------------------------------------------------------------------------
  def to_List(self): 
      l = [(i, self.dico[i]) for i in self] 
      return l
 # ----------------------------------------------------------------------------
  def to_Dict(self):
      return self.dico
 # ----------------------------------------------------------------------------
  def __mul__(self,msetb):
      temp = {}
      for i in self:
          for j in msetb :
              if i == j :
                 temp[i] = min(self.dico[i], msetb.dico[j])
      return temp #repr ?
 # ----------------------------------------------------------------------------
  def __add__(self,msetb):
      temp = {}
      for i in self: 
          if i in msetb:
             temp[i] = max(self.dico[i],msetb.dico[i])
          else :  
             temp[i] = self.dico[i]
      for j in msetb:
          if j not in self:
             temp[j] = msetb.dico[j]
      return temp #pb d'aff : U->{  } au lieu de MultiSet({ })
 # ----------------------------------------------------------------------------
  def __sub__(self,msetb):
      temp = {}
      for i in self:
          for j in msetb:
              if i == j and (self.dico[i] - msetb.dico[j])>0:
                 temp[i] = self.dico[i] - msetb.dico[j]
      return temp #repr ?
 # ----------------------------------------------------------------------------
  def __mod__(self,msetb): 
      temp = {}
      for i in self:
          if i in msetb:
             temp.dico[i] = abs(self.dico[i]-msetb.dico[i])
          else:
             temp.dico[i] = self.dico[i]
      for j in msetb:
          if not __contains__(dico,j): 
             temp.dico[j] = msetb.dico[j]
      return __repr__(temp) #je ne comprend pas ce que ça doit faire
 # ----------------------------------------------------------------------------
  def __lt__(self,msetb):
      for i in self:
          if i not in msetb: #contains?
             return False
          if i in msetb and self.dico[i] >= msetb.dico[i]:
             return False
      return True  
 # ----------------------------------------------------------------------------
  def __eq__(self,msetb): #voir avec alexane
      for i in self:
          if i not in msetb :
             return False
      for j in msetb :
          if j not in msetb:
             return False
      return True
  # ----------------------------------------------------------------------------
  def __le__(self, msetb):
      for i in self:
          if i not in msetb: #contains?
             return False
          if  i in msetb and self.dico[i] > msetb.dico[i]:
             return False
      return True  
 # ----------------------------------------------------------------------------
  def multiplicity(self, element):
    if element in self.dico :
       return self.dico[element]
    else :
      return 0
 # ----------------------------------------------------------------------------
  def union(self, *args): #j'ai pas compris la différence entre a.union(b) et a+b
      return 0
 # ----------------------------------------------------------------------------
  def intersection(self, *args): #pareil pour a.inter(b) et a*b
      return 0
 # ----------------------------------------------------------------------------
  def ajoute(self, valeur, occ = 1):
      if valeur in self.dico:
         self.dico[valeur] += occ
      else:
         self.dico[valeur] = occ
 # ----------------------------------------------------------------------------
  def supprime(self, valeur, occ = 1):
      if valeur in self.dico:
         self.dico[valeur] -= occ
 # ----------------------------------------------------------------------------
  def sup(self,valeur):
      e = set()
      for i in self.dico:
          if self.dico[i] > valeur :
             e = e.add(i)
      return e 
 # ----------------------------------------------------------------------------
  def inf(self, valeur):
      e = set()
      for i in self.dico:
          if self.dico[i] < valeur :
             e = e.add(i)
      return e
 # ----------------------------------------------------------------------------
  def cut(self,valeur):
      e = set()
      for i in self.dico:
          if self.dico[i] == valeur :
             e = e.add(i)
      return e
 # ----------------------------------------------------------------------------
  def elements(self): #pas compris ce que c'est 
      return 0
# ==============================================================================
#def main(): #essayer de faire un testcode  
#    if __name__ == "__main__":
#    main()
# test code for class "MultiSet"

# ==============================================================================

