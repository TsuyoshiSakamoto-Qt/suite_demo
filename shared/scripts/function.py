# encoding: UTF-8

def my_function():
    test.log("function.py!")
    
    
def getChildrenOfType(parent, typename, depth=1000, parent_count=0):
    parent_container = waitForObjectExists(parent)
    while parent_count >0:
        parent_container = parent_container.parent
        parent_count -=1
    
    children_found = []
    for child in object.children(parent_container):
        if typename in className(child):
            children_found.append(child)
        if depth:
            child = objectMap.realName(child)
            children_found.extend(getChildrenOfType(child, typename, depth-1))
    return children_found

        
        
def getChildrenWithProperty(parent, property_type, property_value, depth=1000, parent_count=0):
    parent_container = waitForObjectExists(parent)
    while parent_count >0:
        parent_container = parent_container.parent
        parent_count -=1
    
    children_found = []
    for child in object.children(parent_container):
        if hasattr(child, property_type) and getattr(child, property_type)==property_value:
            children_found.append(child)
        if depth:
            child = objectMap.realName(child)
            children_found.extend(getChildrenWithProperty(child, property_type, property_value, depth-1, parent_count))
    return children_found
