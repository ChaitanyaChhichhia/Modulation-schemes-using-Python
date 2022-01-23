#importing the required libraries, modules, packages
import random
import numpy as np
import math
from abc import ABC, abstractmethod
from matplotlib import pyplot as plt
import abstractclass

###Concept of abstraction


class bpsk (AbstractClass):
    '''
    Class for BPSK modulation scheme
    ### Concept of polymorphism has been used by having same methods for different classes
    '''
    
    def __init__(self, n):
        '''
        Constructor for BPSK Modulation scheme
        '''
        self. n = n # no. of bits in the data
        self.trans_data = 0 # transmitted data
        self.snrdb = 0
    
    def data_generator (self, n):
        '''
        Parameters
        ----------
        n : number of bits
        
        Description
        -----------
        Generates random data bits

        Returns
        -------
        list
            list of data stream

        '''
        return [random.randint(0, 1) for i in range (n)]
        
    def transmitter (self):
        '''
        Description
        -----------
        Performs the function of a transmitter in a communication system.
        Gets the generated data from the data_generator function and does bit mapping.

        Returns
        -------
        None.

        '''
        self.__data = np.array(self.data_generator(self.n)) 
        self.__data_bit_map = 2*self.__data-1 # bit mapping
                
    def channel (self, snrdb):
        '''
        Parameters
        ----------
        snrdb : float
    
        DESCRIPTION
        -----------
        Performs the function of a channel in a communication system
        Gets the bit mapped data and adds noise to it.
    
        Returns
        -------
        None.
    
        '''
        self.snrdb = snrdb
        snr_norm = 10**(self.snrdb/10)
        p = snr_norm**0.5
        self.noise = np.random.randn(len(self.__data)) 
        self.__trans_data = p*self.__data_bit_map + self.noise
    
    def receiver (self):
        '''
        Description
        -----------
        Performs the task of a receiver in a communication system.
        Detects the noisy data.
        Also calculates the BER for given data and snr
    
        Returns
        -------
        None.
    
        '''
        self.__detected_data = np.zeros (len(self.__data))
        for i in range (len(self.__trans_data)):
            if (self.__trans_data[i] > 0):
                self.__detected_data[i] = 1
            else:
                self.__detected_data[i] = 0
        
        for i in range (self.n):
            if (self.__data[i] > 0):
                self.__data[i] = 1
            else:
                self.__data[i] = 0
        
        for i in range (self.n):
            if (self.__detected_data[i] > 0):
                self.__detected_data[i] = 1
            else:
                self.__detected_data[i] = 0
            
        self.__detected_data = (self.__detected_data).astype('int')
        error_bits = self.__data^self.__detected_data
        ber = sum(error_bits)/(self.n)
        print (f"Ber : {ber}\tsnr : {self.snrdb}")
        
        
    def plotting (self):
        '''
        DESCRIPTION
        -----------
        Plots the transmitted, received signals.
        
        Returns
        -------
        None
    
        '''
        Tb = 1 # T
        Eb = 1
        fc = 1/Tb
        t = np.linspace (0, 1, 1000)
        
        # plotting the transmitted data
        phi = np.sqrt(2*Eb/Tb)*np.sin(2*np.pi*fc*t)
        trans_wave = np.empty([0, len(self.__trans_data)])
        for i in range (len(self.__trans_data)):
            trans_wave = np.append(trans_wave, self.__data_bit_map[i]*phi )
            
        plt.plot (range(len(t)*len(self.__trans_data)), trans_wave, label = "Transmitted signal")
        plt.title ("BPSK")
        plt.xlabel ("t")
        plt.ylabel ("Amplitude")
        plt.legend (loc = 1)
        plt.show()
        
        # plotting the detected wave
        phi = np.sqrt(2*Eb/Tb)*np.sin(2*np.pi*fc*t)
        detected_wave = np.empty([0, len(self.__trans_data)])
        self.__detected_data = 2*self.__detected_data-1
        for i in range (len(self.__detected_data)):
            detected_wave = np.append(detected_wave, self.__detected_data[i]*phi )
     
        plt.plot (range(len(t)*len(self.__detected_data)), detected_wave, label = "Detected signal")
        plt.title ("BPSK")
        plt.xlabel ("t")
        plt.ylabel ("Amplitude")
        plt.legend (loc = 1)
        plt.show()
        
        
        
    def ber_vs_snr(self):
        '''
        Description
        -----------
        Plots the BER vs SNR curve for the modulation scheme.
    
        Returns
        -------
        None.
    
        '''
        ber = np.zeros(20)
        for i in range (20):
            snr = 10**(i/10)
            ber[i] = 0.5*math.erfc(np.sqrt(snr/2))

        plt.semilogy(np.arange(20),ber,color='r',marker='o',linestyle='-', label = "BPSK")
        plt.title ("BPSK")
        plt.ylabel ("BER")
        plt.xlabel ("SNR db")
        plt.legend (loc = 1)
        plt.show()