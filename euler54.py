#/usr/bin/python


class card:
    def __init__(self, suit=1, rank=2):
        self.suit = suit
        self.rank = rank

    def value(self):
        """ we want things order primarily by rank then suit """
        return self.suit + (self.rank-1)*14

    def __cmp__(self, other):
        return cmp(self.value(), other.value())
    
    def __str__(self):
        return `self.rank`+':'+`self.suit`
        
        
def tri_par_v(tab):
    ## decorate, sort,undecorate
    tmp=[]
    for c in tab:
        tmp.append(card(['C','D','H','S'].index(c[1])+1,valeurs.index(c[0])+1))

    tmp.sort()

    return tmp

def evalue(hand):
    
    found = False

    # check for the different hands...

    # straight flush

    # the hand is sorted by rank then suit, make sure
    # that they all have the same suit and that they are
    # sequential
    if (not found and
        (hand[0].suit == \
         hand[1].suit == \
         hand[2].suit == \
         hand[3].suit == \
         hand[4].suit) and
        (hand[0].rank == \
         hand[1].rank - 1 == \
         hand[2].rank - 2 == \
         hand[3].rank - 3 == \
         hand[4].rank - 4)):
        #nStraightFlush += 1
        #print "<<< Straight Flush >>>"
        val=1000
        found = True


    # four of a kind

    # they are sorted so either cards 0,1,2,3 have the same rank
    # or 1,2,3,4 have the same rank.
    if (not found and
        ((hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank) or
         (hand[1].rank == hand[2].rank == hand[3].rank == hand[4].rank))):
        #nFourOfAKind += 1
        #print "<<< Four of a kind >>> "
        found = True
        val=500+ hand[2].rank

    # full house

    # we are sorted again, so make sure that the first two are equal
    # and then the last three are equal or reverse
    if (not found and
        (((hand[0].rank == hand[1].rank) and
          (hand[2].rank == hand[3].rank == hand[4].rank)) or
         ((hand[0].rank == hand[1].rank == hand[2].rank) and
          (hand[3].rank == hand[4].rank)))):
        #nFullHouse += 1
        #print "<<< Full house >>> "
        found = True
        val=400+hand[2].rank

    # flush

    # look for all the same suit
    if (not found and
        (hand[0].suit == \
         hand[1].suit == \
         hand[2].suit == \
         hand[3].suit == \
         hand[4].suit)):
        #nFlush += 1
        #print "<<< Flush >>> "
        found = True
        val=300+hand[4].rank

    # straight

    # we are already sorted, so just look at the rank
    if (not found and
        (hand[0].rank == \
         hand[1].rank - 1 == \
         hand[2].rank - 2 == \
         hand[3].rank - 3 == \
         hand[4].rank - 4)):
        #nStraight += 1
        #print "<<< Straight >>> "
        found = True
        val=200+hand[4].rank

    # three of a kind

    # since we are sorted, only 0,1,2 or 1,2,3, or 2,3,4 can be
    # equal
    if (not found and
        ((hand[0].rank == hand[1].rank == hand[2].rank) or
         (hand[1].rank == hand[2].rank == hand[3].rank) or
         (hand[2].rank == hand[3].rank == hand[4].rank))):
        #nThreeOfAKind += 1
        #print "<<< Three of a kind >>> "
        found = True
        val=100+hand[2].rank

    # two pair and one pair
    if (not found):

        numPairs=0
        val=0
        if (hand[0].rank == hand[1].rank):
            numPairs += 1
            val+=hand[1].rank+15*numPairs
        if (hand[1].rank == hand[2].rank):
            numPairs += 1
            val+=hand[1].rank+15*numPairs
        if (hand[2].rank == hand[3].rank):
            numPairs += 1
            val+=hand[2].rank+15*numPairs
        if (hand[3].rank == hand[4].rank):
            numPairs += 1
            val+=hand[3].rank+15*numPairs
            
        if numPairs == 2:
            #nTwoPair += 1
            #print "<<< Two Pair >>> "
            found = True
            
        elif numPairs == 1:
            #nOnePair += 1
            #print "<<< One Pair >>> "
            found = True
            
            
    if (not found):
        #print "<<<", hand[4],"High>>>"
        val=hand[4].rank
    return val
if __name__=='__main__':
    global valeurs
    valeurs=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    f=open('/media/ipod/Download/poker.txt')
    rep=0
    for l in f.readlines():
        prems=l[:-1].split(' ')[:5]
        deuz=l[:-1].split(' ')[5:]
    
        p= evalue(tri_par_v(prems))
        d=evalue(tri_par_v(deuz))

        if p >d:
            rep+=1
        elif p==d: print 'oops',prems,deuz
        
    print rep
