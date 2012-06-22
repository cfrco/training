#!/usr/bin/env python

"""
    create a table with prototype
"""
def create(prototype,data=None):
    out = {"prototype":prototype}

    if data != None :
        out["data"] = data
    else :
        out["data"] = []

    return out

"""
    check an entry has all element in prototype
"""
def check_entry(entry,prototype):
    for col in prototype :
        if not col in entry:
            return False
    return True

def check_where(where,prototype):
    for key in where :
        if not key in prototype :
            return False
    return True

"""
    insert a entry to a table
"""
def insert(table,entry):
    if check_entry(entry,table["prototype"]) :
        table["data"] += [entry] 
        return True
    else :
        return False


def where_equal(where,entry):
    for key in where :
        if entry[key] != where[key]:
            return False
    return True

"""
    select entries from a table with where(condition)
"""
def select(table,where=None):
    if where == None:
        return table["data"]

    elif check_where(where,table["prototype"]):
        out = []
        for entry in table["data"]:
            if where_equal(where,entry):
                out += [entry]

        return out

    else :
        None

def update(table,update,where=None):
    edited = select(table,where)
    
    if edited == None:
        return False

    for entry in edited:
        for key in update :
            entry[key] = update[key]
    return True

def delete(table,where):
    if check_where(where,table["prototype"]):
        for entry in table["data"]:
            if where_equal(where,entry):
                table["data"].remove(entry)
        return True

    else :
        return False
