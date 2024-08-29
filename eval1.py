d={}
def student(d):
    id_=input("Enter id")
    name=input("Enter name:")
    class_=input("enter class:")
    height=input("Enter height:")
    weight=input("Enter weight:")
    p_sport=input("Enter preferred sport:")
    
    d[id_]={"name": name,
           "class":class_,
           "height":height,
           "weight":weight,
           "p_sport":p_sport}
student(d)

def get_sport(agility,speed,strength):
    if agility>10 and speed>10 and strength>10:

        return "cricket"
    if agility>8 and speed>8 and strength>8:
        return "football"
    if agility>6 and speed>6 and strength>6:
        return "chess"
    if agility>4 and speed>4 and strength>4:
        return "javelin"
    
def get_diet(agility,speed,strength):
    if agility>10 and speed>10 and strength>10:

        return "abc"
    if agility>8 and speed>8 and strength>8:
        return "def"
    if agility>6 and speed>6 and strength>6:
        return "ghi"
    if agility>4 and speed>4 and strength>4:
        return "jkl"




def sport(i_d):
    if id_ in d:
        agility=input("Enter agility")
        speed=input("Enter speed")
        strength=input("Ener strength")
    d[sport]=get_sport(agility,speed,strength)
    d[diet]=get_diet(agility,speed,strength)
  
    
    
    
    
i_d=input("Enter id")    
sport(i_d)
    
    
