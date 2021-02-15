import json

def parents_json_parser(result):
    result_list = []
    
    for element in result:
        element_dict = {
            "id": element[0],
            "name": element[1],
            "email": element[2],
            "created_at": element[3],
            "updated_at": element[4],
            "chidren_count": element[5]
        } 
        
        result_list.append(element_dict)
        
    result_json = json.dumps(result_list, default = str, indent = 4)
    
    return result_json

def children_json_parser(result):
    result_list = []
    
    for element in result:
        element_dict = {
            "id": element[0],
            "name": element[1],
            "email": element[2],
            "created_at": element[3],
            "updated_at": element[4],
            "parent_count": element[5]
        } 
        
        result_list.append(element_dict)
        
    result_json = json.dumps(result_list, default = str, indent = 4)
    
    return result_json