#!/usr/bin/env python


import numpy as np

def cvc_calc(ca,va,cb,vb):
    i=0
    storage=[]
    
    if ca=='':
        i+=1
        storage.append('ca')
        
    if va=='':
        i+=1
        storage.append('va')
        
    if cb=='':
        i+=1
        storage.append('cb')
        
    if vb=='':
        i+=1
        storage.append('vb')

    if i>1:
        result='You have too many open variables'
        
    elif i==0:
        result='You have no open variables'
        
    else:
        if storage[0]=='ca':
            result=float(cb)*float(vb)/float(va)
        
        if storage[0]=='va':
            result=float(cb)*float(vb)/float(ca)
            
        if storage[0]=='cb':
            result=float(ca)*float(va)/float(vb)
            
        if storage[0]=='vb':
            result=float(ca)*float(va)/float(cb)
            
        
    return result


def uc_calc(unit,mil,mic,nan):
    output=[]
        
    if unit!='':
        output.append(float(unit))
        mil=float(unit)*1e3
        output.append(mil)
        mic=float(unit)*1e6
        output.append(mic)
        nan=float(unit)*1e9
        output.append(nan)
        
    elif mil!='':
        unit=float(mil)*1e-3
        output.append(unit)
        output.append(float(mil))
        mic=float(mil)*1e3
        output.append(mic)
        nan=float(mil)*1e6
        output.append(nan)
        
    elif mic!='':
        unit=float(mic)*1e-6
        output.append(unit)
        mil=float(mic)*1e-3
        output.append(mil)
        output.append(float(mic))
        nan=float(mic)*1e3
        output.append(nan)
        
    elif nan!='':
        unit=float(nan)*1e-9
        output.append(unit)
        mil=float(nan)*1e-6
        output.append(mil)
        mic=float(nan)*1e-3
        output.append(mic)      
        output.append(float(nan))
    
    return output 
