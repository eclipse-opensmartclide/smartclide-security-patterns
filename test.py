import pymongo
from bson.objectid import ObjectId
f=open('password.cfg','r')
password = f.read()
client = pymongo.MongoClient("mongodb+srv://maria:"+password+"@cluster0.gecb7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

def find_patterns(requirement,pattern):
    for x in db["SecurityRequirements"].find({"requirement name": requirement}):
        id_=x["_id"]
        patterns=x["related_security_patterns"]
        description=x["description"]
        standard=x["standard"]
    #print(patterns)
    cur_list=[]
    for item in patterns:
        if pattern is not None:
            cur=db["SecurityPatterns"].find({"_id": ObjectId(item),"pattern name":pattern})
            # print(cur)
            cur_list.append(cur)
        else:
            cur=db["SecurityPatterns"].find({"_id": ObjectId(item)})
            cur_list.append(cur)

    patterns_list=[]
    for item in cur_list:
        for doc in item:
            patterns_list.append(doc)

    json={"requirement name":requirement,"_id":id_,"description":description,"standard":standard, "patterns":patterns_list}
    return(json,patterns_list)


def find_technologies3(boolean, pattern, technology):
    if boolean is False:
        all_lists = []
        for thing in pattern:
            local = thing["pattern name"]
            for x in db["SecurityPatterns"].find({"pattern name": local}):
                id_ = x["_id"]
                technologies = x["related_security_control_technologies"]
                description = x["description"]
                pattern_type = x["pattern type"]
            # print(technologies)

            # print(technologies)
            cur_list2 = []
            for item in technologies:
                if technology is not None:
                    cur = db["SecurityControlTechnology"].find({"_id": ObjectId(item)  # ,"technology name":technology
                                                                })
                    # print(cur)
                    cur_list2.append(cur)
                else:
                    cur = db["SecurityControlTechnology"].find({"_id": ObjectId(item)})
                    cur_list2.append(cur)

            # print(cur_list2)
            technologies_list = []
            for item in cur_list2:
                for doc in item:
                    technologies_list.append(doc)

            # boolean2=False
            json2 = {"pattern name": local, "_id": id_, "description": description, "pattern type": pattern_type,
                     "technologies": technologies_list}
            all_lists.append(json2)
    else:
        for x in db["SecurityPatterns"].find({"pattern name": pattern}):
            id_ = x["_id"]
            technologies = x["related_security_control_technologies"]
            description = x["description"]
            pattern_type = x["pattern type"]

        # print(technologies)
        cur_list2 = []
        for item in technologies:
            if technology is not None:
                cur = db["SecurityControlTechnology"].find({"_id": ObjectId(item), "technology name": technology})
                # print(cur)
                cur_list2.append(cur)
            else:
                cur = db["SecurityControlTechnology"].find({"_id": ObjectId(item)})
                cur_list2.append(cur)

        technologies_list = []
        for item in cur_list2:
            # print(item)
            for doc in item:
                # print(doc)
                technologies_list.append(doc)

        # boolean2=True
        all_lists = {"pattern name": pattern, "_id": id_, "description": description, "pattern type": pattern_type,
                     "technologies": technologies_list}

    return (all_lists)


def find_libraries(technology, language):
    for x in db["SecurityControlTechnology"].find({"technology name": technology}):
        id_ = x["_id"]
        libraries = x["related_security_libraries"]

    if language == None:
        cur_list = []
        for item in libraries:
            cur = db["SecurityLibraries"].find({"_id": ObjectId(item)})
            # print(cur)
            cur_list.append(cur)
    else:
        cur_list = []
        for item in libraries:
            cur = db["SecurityLibraries"].find({"_id": ObjectId(item), "language": language})
            # print(cur)
            cur_list.append(cur)

    libraries_list = []
    for item in cur_list:
        for doc in item:
            libraries_list.append(doc)

    return (libraries_list)

def all_together(requirement, pattern, technology, language):
    json, l = find_patterns(requirement, pattern)
    # print(l)
    if pattern is None:
        json2 = find_technologies3(False, l, technology)
    else:
        json2 = find_technologies3(True, pattern, technology)

    # json["patterns"]=json2
    # print(json2)
    if technology is None and pattern is None:
        # print(json3,json)
        # json3=find_libraries2(technology,language)
        for item in json2:
            # print(item)
            for item2 in item:
                if item2 == "technologies":
                    for item4 in item[item2]:
                        for item5 in item4:
                            if item5 == 'technology name':
                                local = item4[item5]
                                # print(local)
                                json3 = find_libraries(local, language)
                                # print(json3)
                                item4["related_security_libraries"] = json3
        json["patterns"] = json2
    elif technology is None and pattern is not None:
        json["patterns"] = json2
        dict1 = json["patterns"]
        for key in dict1:
            if key == "technologies":
                for item in dict1[key]:
                    for item2 in item:
                        if item2 == "technology name":
                            local = item[item2]
                        if item2 == "related_security_libraries":
                            json3 = find_libraries(local, language)
                            item[item2] = json3



    # here we still have a problem
    elif technology is not None and pattern is None:
        json["patterns"] = json2
        dict1 = json["patterns"]
        # print(dict1)
        for key in dict1:
            # print(key)
            for item1 in key:
                if item1 == "technologies":
                    # print(key[item1])
                    # my_list=key[item1]
                    for item2 in key[item1]:
                        # print(item2)
                        for item3 in item2:
                            # print(item3)
                            if item3 == "related_security_libraries":
                                json3 = find_libraries(technology, language)
                                item2[item3] = json3
                                # print(my_list)
        for key in dict1:
            # print(key)
            for item in key:
                if item == "technologies":
                    # print(key[item])
                    item2 = key[item]
                    for i in range(0, 50):
                        for index in range(len(item2)):
                            if item2[index]['technology name'] != technology:
                                del item2[index]
                                break
                    # print(item2)


    elif technology is not None and pattern is not None:
        json["patterns"] = json2
        dict1 = json["patterns"]
        for key in dict1:
            if key == "technologies":
                for item in dict1[key]:
                    for item2 in item:
                        if item2 == "related_security_libraries":
                            # print(" ")
                            json3 = find_libraries(technology, language)
                            item[item2] = json3
                            # json["patterns"]=json2
    return (json)
#requirement="Authentication"
#pattern="Authenticator"
#technology="OAuth2.0"
#language=None
#print(all_together(requirement,pattern,technology,language))