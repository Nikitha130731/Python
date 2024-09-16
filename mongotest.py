# mongodb is used for document based data like json files


import pymongo
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://008160497:Chinnoda1331@cluster0.2sxiq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


data={
    "name": "nikitha",
    "email": "nikitha@gmail.com",
    "surname":"kondreddy",
    "subject" : ["data science","big data", "data analytics"]
}


list_of_records = [
    {'company_name' : 'ineuron',
     'product': 'Affordable ai',
     'course_offered': 'ML with deployment'},

     {'company_name' : 'ineuron',
     'product': 'Affordable ai',
     'course_offered': 'ML with projects'},

     {'company_name' : 'ineuron',
     'product': 'Affordable ai',
     'course_offered': 'Data SCience'}
]

data2=  {
    "medications":[{
            "aceInhibitors":[{
                "name":"lisinopril",
                "strength":"10 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "antianginal":[{
                "name":"nitroglycerin",
                "strength":"0.4 mg Sublingual Tab",
                "dose":"1 tab",
                "route":"SL",
                "sig":"q15min PRN",
                "pillCount":"#30",
                "refills":"Refill 1"
            }],
            "anticoagulants":[{
                "name":"warfarin sodium",
                "strength":"3 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "betaBlocker":[{
                "name":"metoprolol tartrate",
                "strength":"25 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "diuretic":[{
                "name":"furosemide",
                "strength":"40 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "mineral":[{
                "name":"potassium chloride ER",
                "strength":"10 mEq Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }]
        }
    ]
    
}



database = client['mongotest'] # dattabase creation  'mongotest' 
collection=database['test'] # creating table called test(collection is table creation)
#collection.insert_one(data) # inserting data into table called 'test'
# collection.insert_many(list_of_records)
collection1= database['dpkt']
# collection1.insert_one(data2)


# To check what are databes and colections available in my cluster
# to get all from database 
records= collection.find()
for i in records:
    print(i)


# to query in  mongodb
# collection.find({'company_name': 'ineuron'})
# or
# data3= collection.find({'company_name': 'ineuron'})
# for i in data3:
#     print(i)


# applying fliter conditions 
# return grater than "L"
data3= collection.find({'course_offered':{'$gt':'L'}})
for i in data3:
    print(i)

# make sure to insert '$' if there is any conditions

#Examples for filter from other source of data
collection.find({'status':'A'}) # stataus =='A'
collection.find({'status':{'$in':['A','P']}}) # where status=='A' or "p"
collection.find({'status':{'$gt':"C"}}) # where status is grater than C
collection.find({'quantity':{'$gte':100}})  # where quantity is garter than equal to 100
collection.find({'quantity':95},{'item':'sketch pad'}) # returns data where item and quantity has
collection.find({'item':'sketch pad','quantity':{'$gte': 75}}) # represents 'AND condition
collection.find({'$or':[{'item':'sketch pad','quantity':{'$gte': 75}}]}) #represents 'OR' conditions

##update operations  
collection.update_one({'Item':'canvas'}, {'$set':{'item':'peacock'}})
collection.delete_one({'item':'peacock'}) # deletes one record









