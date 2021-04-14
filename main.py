import pymongo
from sqlite3.dbapi2 import Date

if __name__ == '__main__':
  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["TpMongo"]
mycol = mydb["Produit"]
mycol1 = mydb["Commande"]
mycol2 = mydb["InventaireProduit"]
mycol3 = mydb["Caisse"]

inventaireProduit1 = {'_id': 1,
                      "quantite": 10}
inventaireProduit2 = {'_id': 2,
                      "quantite": 9}
inventaireProduit3 = {'_id': 3,
                      "quantite": 8}
inventaireProduit4 = {'_id': 4,
                      "quantite": 7}

produit1 = {'_id': 1,
            "nomP": "Fromage",
            "desc": "origine france",
            "quantite":[inventaireProduit1]}
produit2 = {'_id': 2,
            "nomP": "Poires",
            "desc": "origine espagne",
            "quantite": [inventaireProduit2]}
produit3 = {'_id': 3,
            "nomP": "Pommes",
            "desc": "origine portugal",
            "quantite": [inventaireProduit3]}
produit4 = {'_id': 4,
            "nomP": "Citron",
            "desc": "origine france ",
            "quantite": [inventaireProduit4]}

commande1={"_id": "1",
           "contenu": [produit1,produit2],
           "date": "13/04/2021"}
commande2={"_id": "2",
           "contenu": [produit3,produit4],
           "date": "13/04/2021"}
commande3={"_id": "3",
           "contenu": [produit2,produit4],
           "date": "14/04/2021"}

caisse1={"_id": "1",
         "commande": [commande1,commande2]}
caisse2={"_id": "2",
         "commande": [commande2,commande1]}


# insertion inventaire produit

'''x1 = mycol2.insert_one(inventaireProduit1)
x2 = mycol2.insert_one(inventaireProduit2)
x3 = mycol2.insert_one(inventaireProduit3)
x4 = mycol2.insert_one(inventaireProduit4)
print(x1)
print(x2)
print(x3)
print(x4)'''

# insertion des produits
'''x1=mycol.insert_one(produit1)
x2=mycol.insert_one(produit2)
x3=mycol.insert_one(produit3)
x4=mycol.insert_one(produit4)

print(x1)
print(x2)
print(x3)
print(x4)'''

# insertion des commandes

'''x1=mycol1.insert_one(commande1)
x2=mycol1.insert_one(commande2)
x3=mycol1.insert_one(commande3)

print(x1)
print(x2)
print(x3)'''


# insertion des Caisses

'''x1=mycol3.insert_one(caisse1)
x2=mycol3.insert_one(caisse2)

print(x1)
print(x2)'''


# Questions 1 : Nombre de commande effectué hier pour la caisse Numéro 1

'''db.Commande.find({"date":"13/04/2021"}).count()'''

# Elements de recherche pour les autres questions ....

pipe = [{'addFields': {'_id': None, 'totalReactions': {'$sum': '$contenu'}}}]
mycol1.aggregate(pipeline=pipe)

collection_with_new_field = mycol1.aggregate(
    [
        {
            "$addFields":
                {
                "_id": None,
                "totalReactions": {"$sum": "$contenu"}
                }
        }
    ]
)
for agg in collection_with_new_field:
    print(agg)
