# -*- coding: utf-8 -*-
"""
/***************************************************************************
 opeNoise

 opeNoise allows to compute the noise level generated by road traffic 
 at fixed receiver points and buildings.
 This nmpb.py is the implementation of the French national computation method 
 NMPB-Routes-96, as indicated in the DIRECTIVE 2002/49/EC OF THE EUROPEAN 
 PARLIAMENT AND OF THE COUNCIL of 25 June 2002 relating to the assessment 
 and management of environmental noise.
 
                              -------------------
        begin                : March 2014
        copyright            : (C) 2014 by Arpa Piemonte
        email                : s.masera@arpa.piemonte.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from math import log10

class nmpb():
    """ Arguments:
        - light_number: number of light vehicles per hour (number)
        - heavy_number: number of heavy vehicles per hour (number)
        - light_speed: speed of light vehicles (number)
        - heavy_speed: speed of heavy vehicles (number)
        - traffic: type of the traffic flow (string: 'continuos','pulsed accelerated', 'pulsed decelerated', 'non-differentiated pulsed')
        - surface: type of road surface (string: 'smooth','porous','stones','cement','corrugated')
        - slope: slope of the road (string: 'flat', 'down', 'up')
    """
    def __init__(self, light_number=0, heavy_number=0, light_speed=0, heavy_speed=0, traffic="continuos", surface="smooth", slope="flat"):
        self.light_number = light_number
        self.heavy_number = heavy_number
        self.light_speed = light_speed
        self.heavy_speed = heavy_speed
        self.traffic = traffic
        self.surface = surface
        self.slope = slope

    def __str__(self):
        return '(' + \
                'light_number=' + str(self.light_number) + '; ' +\
                'heavy_number=' + str(self.heavy_number) + '; ' +\
                'light_speed=' + str(self.light_speed) + '; ' +\
                'heavy_speed=' + str(self.heavy_speed) + '; ' + \
                'slope=' + str(self.slope) + '; ' +\
                'traffic=' + str(self.traffic) + '; ' +\
                'surface=' + str(self.surface) + '; ' +\
                'power=' + str(self.run()) + ')'

    def power(self):
        return self.run()
        
    def run(self):
        # light vehicles
        if self.traffic == 'continuos':
            if self.slope == 'flat' or self.slope == 'down':
                if self.light_speed < 44:
                    E_o_l = 29.4
                    a_l = 0
                else:
                    E_o_l = 22.0
                    a_l = 21.6

            if self.slope == 'up':
                if self.light_speed < 43:
                    E_o_l = 37.0
                    a_l = -10.0
                elif self.light_speed >= 43 and self.light_speed < 80: 
                    E_o_l = 32.1
                    a_l = 4.8
                else:
                    E_o_l = 22.0
                    a_l = 21.6

        if self.traffic == 'pulsed accelerated':
            if self.slope == 'flat':
                if self.light_speed < 50:
                    E_o_l = 37.2
                    a_l = -10.0
                elif self.light_speed >= 50 and self.light_speed < 64: 
                    E_o_l = 33.0
                    a_l = 0
                else:
                    E_o_l = 22.0
                    a_l = 21.6
                    
            if self.slope == 'up':
                if self.light_speed < 32:
                    E_o_l = 37.0
                    a_l = -10.0
                else:
                    E_o_l = 34.0
                    a_l = 5.2                    

            if self.slope == 'down':
                if self.light_speed < 40:
                    E_o_l = 34.0
                    a_l = -9.3
                elif self.light_speed >= 40 and self.light_speed < 53: 
                    E_o_l = 31.2
                    a_l = 0
                else:
                    E_o_l = 22.0
                    a_l = 21.6                    
                    
        if self.traffic == 'non-differentiated pulsed':
            if self.slope == 'flat' or self.slope == 'down':
                if self.light_speed < 40:
                    E_o_l = 34.0
                    a_l = -9.3
                elif self.light_speed >= 40 and self.light_speed < 53: 
                    E_o_l = 31.2
                    a_l = 0
                else:
                    E_o_l = 22.0
                    a_l = 21.6  

            if self.slope == 'up':
                if self.light_speed < 43:
                    E_o_l = 37.0
                    a_l = -10.0
                elif self.light_speed >= 43 and self.light_speed < 80: 
                    E_o_l = 32.1
                    a_l = 4.8
                else:
                    E_o_l = 22.0
                    a_l = 21.6
                    
        if self.traffic == 'pulsed decelerated':
            if self.slope == 'flat':
                if self.light_speed < 60:
                    E_o_l = 29.4
                    a_l = 0
                elif self.light_speed >= 60 and self.light_speed < 100: 
                    E_o_l = 13.0
                    a_l = 34.3
                else:
                    E_o_l = 22.0
                    a_l = 21.6 
            if self.slope == 'up':
                if self.light_speed < 40:
                    E_o_l = 34.0
                    a_l = -9.3
                elif self.light_speed >= 40 and self.light_speed < 53: 
                    E_o_l = 31.2
                    a_l = 0
                else:
                    E_o_l = 22.0
                    a_l = 21.6  
            if self.slope == 'down':
                if self.light_speed < 60:
                    E_o_l = 27.1
                    a_l = 0
                else:
                    E_o_l = 11.3
                    a_l = 33.8
                    
        # heavy vehicles
        if self.traffic == 'continuos' or self.traffic == 'pulsed accelerated' or self.traffic == 'non-differentiated pulsed':                    
            if self.slope == 'flat' or self.slope == 'down':                    
                if self.heavy_speed < 51:
                    E_o_h = 47.0
                    a_h = -10.3
                elif self.heavy_speed >= 51 and self.heavy_speed < 70: 
                    E_o_h = 42.8
                    a_h = 0  
                else:
                    E_o_h = 32.3
                    a_h = 19.4                    
            if self.slope == 'up':                           
                if self.heavy_speed < 63:
                    E_o_h = 48
                    a_h = -10.4
                elif self.heavy_speed >= 63 and self.heavy_speed < 70: 
                    E_o_h = 42.8
                    a_h = 0  
                else:
                    E_o_h = 32.3
                    a_h = 19.4            
        else:
            if self.slope == 'flat':                    
                if self.heavy_speed < 65:
                    E_o_h = 36
                    a_h = 3.9
                else:
                    E_o_h = 16.7
                    a_h = 41.7          
            if self.slope == 'up':                    
                if self.heavy_speed < 65:
                    E_o_h = 41
                    a_h = 0
                else:
                    E_o_h = 27.9
                    a_h = 25.7
            if self.slope == 'down':                    
                if self.heavy_speed < 51:
                    E_o_h = 47.0
                    a_h = -10.3
                elif self.heavy_speed >= 51 and self.heavy_speed < 70: 
                    E_o_h = 42.8
                    a_h = 0  
                else:
                    E_o_h = 32.3
                    a_h = 19.4

        # surface correction
        if self.surface == 'smooth':
            surface_correction_l = 0
            surface_correction_h = 0
        elif self.surface == 'stones':
            surface_correction_l = 3
            surface_correction_h = 3
        elif self.surface == 'cement' or self.surface == 'corrugated':
            surface_correction_l = 2
            surface_correction_h = 2
        elif self.surface == 'porous':
            if self.light_speed <= 60:
                surface_correction_l = -1                    
            elif self.light_speed > 60 or self.light_speed <= 80: 
                surface_correction_l = -2
            else:
                surface_correction_l = -3            
            if self.heavy_speed <= 60:
                surface_correction_h = -1                    
            elif self.heavy_speed > 60 or self.heavy_speed <= 80: 
                surface_correction_h = -2
            else:
                surface_correction_h = -3 
        
        v_o = 20.0
        if self.light_number > 0 and self.light_number != None and self.light_speed > 0 and self.light_speed != None:
            power_l = E_o_l + a_l*log10(self.light_speed/v_o) + 10*log10(self.light_number) + surface_correction_l
            power_l_lin = 10**(power_l/10)         
        else:
            power_l = 0
            power_l_lin = 0
        if self.heavy_number > 0 and self.heavy_number != None and self.heavy_speed > 0 and self.heavy_speed != None:       
            power_h = E_o_h + a_h*log10(self.heavy_speed/v_o) + 10*log10(self.heavy_number) + surface_correction_h
            power_h_lin = 10**(power_h/10) 
        else:
            power_h = 0
            power_h_lin = 0
        
        if (power_l_lin + power_h_lin) > 0:
            power = 10*log10(power_l_lin + power_h_lin)
        else:
            power = 0
        
        return power