import numpy as np

class TimeSeries:
    ''' Class object for earthquake time history/series data
    
    ATTRIBUTES:
    -----------
    time-series 2D array, earthquake name
    record station, date, component and sampling interval
    '''
    def __init__(self):
        pass
    
    def set_timeSeries(self,timeSeries):
        '''
        TimeSeries object initialised as 2D array
        '''
        self.timeSeries_ = timeSeries
    
    def set_eqName(self, name):
        '''
        Set earthquake name
        '''
        self.eqName = name
        
    def set_recordStation(self, station):
        '''
        Record station
        '''
        self.recordStation = station
    
    def set_eqDate(self, date):
        '''
        Set earthquake date
        '''        
        self.eqDate = date
        
    def set_component(self, component):
        '''
        Set earthquake component
        '''
        self.component = component
    
    def set_dt(self, dt):
        '''
        Set sampling interval
        '''        
        self.dt = dt
    
    def set_Yunit(self, unit):
        '''
        Units for value component
        '''
        self.yUnit = unit
        
    def set_Tunit(self, unit):
        '''
        Units for Time component
        '''
        self.tUnit = unit