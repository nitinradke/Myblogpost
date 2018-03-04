from django import template

register = template.Library()

def cut(v,args):
    return v.replace(args,'')



def table(v,args):
    l=[]
    for i in range(args):
        l.append(v)
    return ' '.join(l)

register.filter('cut',cut)
register.filter('table',table)
