import numpy as np
import re
from earthquakepy import timeseriesobject


def readPEER(pathToFile):
    '''
    Parameters
    ----------
    pathToFile : Relative or absolute Path to PEER Acceleration/Velocity/Displacement file.

    Returns
    -------
    Time series array.

    '''
    with open(pathToFile, 'r') as f:
        lines = f.readlines()
        Yunit = lines[2]
        eqName, eqDate, recordStation, component = lines[1].split(", ") 
        for line in lines:
            if "NPTS" and "DT" in line:
                print (line)
                dt = float(re.search('DT=   (.*?) SEC', line).group(1)) #Searches and picks DT value from the line
                npts = int(re.search('NPTS=   (.*?),', line).group(1)) #Searches and picks NPTS value from the line
                break
        
        time = np.arange(0,npts*dt, dt) #time series array with dt interval
        values=np.loadtxt(pathToFile, skiprows=4) #Array of values from file
        values=np.reshape(values, np.size(values)) #Reshapes 2D value array into 1D array of same size
        timeSeries = np.stack((time,values), axis=1) #Stacks time array and values array columnwise (axis=1)
        arraySize = timeSeries.size
    th = timeseriesobject.TimeSeries()
    th.set_timeSeries(timeSeries)
    th.set_eqName(eqName)
    th.set_eqDate(eqDate)
    th.set_recordStation(recordStation)
    th.set_component(component)
    th.set_dt = (dt)
    th.set_Yunit(Yunit)
    th.set_Tunit('seconds')
    return th


        