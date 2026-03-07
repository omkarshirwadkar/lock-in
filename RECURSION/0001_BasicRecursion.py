def withParams(param):
    if param > 10:
        return param
    param += 2
    return withParams(param)
print(withParams(1))

outParam = 0
def withoutParam():
    global outParam
    if outParam >= 10:
        return outParam
    outParam += 2
    return withoutParam()
print(withoutParam())