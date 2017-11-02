class MultiSet(object):
    dico = {}
    
    def __init__(self, data):
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
                print "Ignoring ", erreurs, " out of ", len(data)
                
    def __repr__ (self):
        return "Multiclass({})".format(sef.dico)
