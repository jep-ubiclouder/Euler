# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

__author__  = "Jean-Eric PREIS"
__contact__ = "jep@ubiclouder.com"
__license__ = 'GPL v3'


import boto3
import xlsxwriter
import tweepy
from tweepy import OAuthHandler
import getopt
import json
import time
import os
import sys
import pprint
# Vecteurs d'accreditation a renseigner
# apres creation dans le gestionnaire d'applications Twitter 
# cf : https://apps.twitter.com/
consumer_key = "sZ8bvMYauqwmRipNX8bLLF7hb"
consumer_secret = "0NlYKlLWyrn5TSBF8IgY2rjhkOWbVT0IszDJksLaTmt8orstnn"
access_token = "212698993-hY1EdCRRPVU2pGgsIB7pAK1NJAJQDG5EcTG82Wyx"
access_token_secret = "Iu8IVTmgQ12eFCUuXuVSwlzG8juRwHeoPvqwgB7kdBbXJ"

# Constantes
## petites valeurs pour tester

maxTweets = 10   # Nombre de tweet max a recuperer
tw_block_size = 10    # Nombre de Tweet par requete
sinceId = None         # Recuperation des tweets du plus recent au plus ancien

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def sendToS3(output_file,workbook):
    s3 = boto3.resource('s3')
    s3.Bucket('ubicloudermm').put_object(Key='Resultats Twitter Marketing/'+output_file, Body=workbook)
def usage():
    """
    Display usage
    """
    sys.stderr.write( "Usage: collect.py -s <hashtag> | --search=<hashtag>\n"+
                      "                 [-f <output_file.xslx> | --output_file=<output_file.xslx>]\n"+
                      "                 [-m <max-id> | --maxid=<max-id>]\n")

def main(argv):
    """
    Collecte des tweets associe a un hashtag.
    """
    tweetCount = 0
    search_query = None
    max_id = -1
    output_dir = "."

    try:
        opts, args = getopt.getopt(argv, "ho:s:m:", ["help","output_file=","search=","maxid="])
    except getopt.GetoptError:
        usage()
        sys.exit(1)
    output_file =None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        if o in ("-s", "--search" ):
            search_query = a
        if o in ("-f", "--output_file" ):
            output_file = a
        if o in ("-m", "--maxid" ):
            max_id = long(a)
        
    if output_file is None:
        output_file = 'results-'+search_query+'.xlsx' 
    if output_file[:-5] !='.xlsx':
        output_file = output_file+'.xlsx'
        
           
    if not search_query:
        usage()
        sys.exit(2)

    print("Parametres de la collecte :")
    print(" - Hashtag    : {0}".format(search_query))
    print(" - Fichier : {0}".format(output_file))
    print(" - Max ID     : {0}".format(max_id))
    print("")

    workbook = xlsxwriter.Workbook(output_file)
    line = 0
    col = 0
    currentSheet = workbook.add_worksheet(search_query)
    labels= ('screen_name' ,'name','followers_count','day','text','hashtag')
    for label in labels :
        currentSheet.write_string(line,col,label)
        col += 1
    currentLine = 1
    pp = pprint.PrettyPrinter(indent=4)

    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                   new_tweets = api.search(q=search_query, count=tw_block_size)
                else:
                    new_tweets = api.search(q=search_query, count=tw_block_size, since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=search_query, count=tw_block_size, max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=search_query, count=tw_block_size, max_id=str(max_id - 1), since_id=sinceId)
            if not new_tweets:
                print("Collecte terminee.")
                break
            for tweet in new_tweets:
                ## labels= ('screen_name' ,'name','followers_count','day','text')
                record = {'screen_name': tweet.user.screen_name,
                          'name': tweet.user.name,
                          'followers_count' : tweet.user.followers_count,
                          'day': tweet.created_at.strftime('%Y-%m-%d'),
                          'text' : tweet.text,
                          'hashtag':search_query
                           }
                col = 0
                for k in record.keys():
                    currentSheet.write(currentLine,col,record[k])
                    col += 1
                currentLine += 1
            tweetCount += len(new_tweets)
            print("{0} tweets téléchargés".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            print("Une erreur est intervenue. Pour poursuivre le processus de collecte, relancer la commande suivante :")
            print("python collect.py -s \"{0}\" -o \"{1}\" -m \"{2}\"".format(search_query, output_dir, max_id))
            print("")
            print("Error : " + str(e))
            workbook.close()
            sendtoS3(workbook)
            break
    workbook.close()
    sendtoS3(workbook)

if __name__ == "__main__":
    main(sys.argv[1:]
