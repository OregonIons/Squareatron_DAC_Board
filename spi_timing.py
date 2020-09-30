# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:53:58 2019

@author: ions
"""

from artiq.experiment import *
import numpy as np

class SPI(EnvExperiment):

    def build(self):
        self.setattr_argument("Bits",StringValue())
        self.setattr_device("core")
        self.setattr_device("ttl8")
        self.setattr_device("ttl9")
        self.setattr_device("ttl11")
        

        
    def prepare(self):
        self.data = [int(x) for x in self.Bits]
    @kernel
    def run(self): 
        self.core.reset()
        data = self.data
        

        self.ttl8.off()
        self.ttl9.off()
        self.ttl11.off()
        delay(500*ns)
        j=0
        k=0
        for i in range(50):
            
            with sequential:
                if k==1:
                    with parallel:
                        self.ttl11.pulse(125*ns)          
                        with sequential:
                            delay(80*ns)
                            self.ttl9.pulse(250*ns)
                            
                else:
                    self.ttl9.pulse(250*ns)
                    
                delay(75*ns)

                if k>0:
                    if j<=15:
                        if data[j]==1:
                            
                            self.ttl8.on()
                            j+=1
                        else:
                            
                            self.ttl8.off()
                            j+=1
               
                k+=1
                if k==18:
                    self.ttl11.on()
                if k==1:
                    delay(95*ns)
                else:
                    delay(175*ns)