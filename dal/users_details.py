from interface.query_execution import execute_query

def FollowUser(params):
    select_query = """SELECT * FROM FOLLOWED WHERE FOLLOWED_BY = (%s) AND FOLLOWS = (%s)"""
    res = execute_query(query = select_query, query_params = params)
    if res != -1:
        if len(res) > 0:
            return f'already follows'
        else:
            insert_query = """INSERT INTO FOLLOWED
                                (FOLLOWED_BY, FOLLOWS, ACCEPTED)
                                VALUES (%s, %s, 0)"""
            res = execute_query(query = insert_query, query_params = params)
            print(res)
            if res != -1:
                return 'Successfully Inserted'
            else:
                return 'No Such User exists to follow'
    else:
        return 'Select failed.'


def UnFollowUser(params):
    delete_query = """DELETE FROM FOLLOWED WHERE FOLLOWED_BY = (%s) AND FOLLOWS = (%s)"""
    res = execute_query(query = delete_query, query_params = params)
    return res

def GetAllFollowersMapping():
    select_query = """SELECT * FROM FOLLOWED"""
    res = execute_query(query = select_query)
    print(res)
    if res != -1:
        return res
    else:
        return 'Select failed'

def GetAllUser():
    select_query = """SELECT * FROM USERS"""
    res = execute_query(query = select_query)
    print(res)
    if res != -1:
        return res
    else:
        return 'Select failed'

def GetAllFollowersById(params):
    select_query = """SELECT * FROM FOLLOWED WHERE FOLLOWS = (%s)"""
    res = execute_query(query = select_query, query_params = params)
    filtered_data = [val['FOLLOWED_BY'] for val in res]
    return filtered_data
