class qpsk (AbstractClass):
    
    '''
    Class for QPSK modulation scheme
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
        self.s_trans_odd_ref = self.__data[1::2]
        self.s_trans_even_ref = self.__data[0::2]
        x = 2*self.__data - 1
        self.s_trans_odd = x[1::2]
        self.s_trans_even = x[0::2]
   
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
        noise_o = np.random.randn(int(len(self.__data)/2))
        noise_e = np.random.randn(int(len(self.__data)/2))
                                  
        self.trans_e = p*self.s_trans_even + noise_e
        self.trans_o = p*self.s_trans_odd + noise_o
    
    def receiver (self):
        '''
        Description
        -----------
        Performs the task of a receiver in a communication system.
        Detects the noisy data.
        Also calculates the BER for given data and snr.
    
        Returns
        -------
        None.
    
        '''
        self.data_detect_o = (np.sign(self.trans_o)+1)/2
        self.data_detect_e = (np.sign(self.trans_e)+1)/2
        self.data_detect_o = (self.data_detect_o).astype('int')
        self.data_detect_e = (self.data_detect_e).astype('int')
        e1 = sum(self.s_trans_odd_ref^self.data_detect_o)
        e2 = sum(self.s_trans_even_ref^self.data_detect_e)
        ber = (e1+e2)/(self.n)
        print (f"Ber : {ber}\tsnr : {self.snrdb}")
                                                     
    def plotting (self):
        '''
        DESCRIPTION
        -----------
        Plots the transmitted and received signals.
        
        Returns
        -------
        None
    
        '''
        t = np.linspace(0,1,100)  # Time
        tb = 1;
        fc = 1/tb;    # carrier frequency

        phi1 = np.sqrt(2/tb)*np.sin(2*np.pi*fc*t + np.pi/4)  # carrier frequency cosine wave
        phi2 = np.sqrt(2/tb)*np.sin(2*np.pi*fc*t + 3*np.pi/4)  # carrier frequency sine wave
        phi3 = np.sqrt(2/tb)*np.sin(2*np.pi*fc*t + 5*np.pi/4)
        phi4 = np.sqrt(2/tb)*np.sin(2*np.pi*fc*t + 7*np.pi/4)
        
        # plotting the transmitted data
        
        trans_wave = np.empty([0, len(self.s_trans_odd)])
        for i in range (len(self.s_trans_odd)):
            if (self.s_trans_odd_ref[i] == 1 and self.s_trans_even_ref[i] == 0 ):
                trans_wave = np.append(trans_wave, phi1 )
            if (self.s_trans_odd_ref[i] == 0 and self.s_trans_even_ref[i] == 0 ):
                trans_wave = np.append(trans_wave, phi2 )
            if (self.s_trans_odd_ref[i] == 0 and self.s_trans_even_ref[i] == 1 ):
                trans_wave = np.append(trans_wave, phi3 )
            if (self.s_trans_odd_ref[i] == 1 and self.s_trans_even_ref[i] == 1 ):
                trans_wave = np.append(trans_wave, phi4 )

        plt.plot (range(len(t)*len(self.s_trans_odd)), trans_wave, label = "Transmitted signal")
        plt.title ("QPSK")
        plt.xlabel ("t")
        plt.ylabel ("Amplitude")
        plt.legend (loc = 1)
        plt.show()
        
        # plotting the detected wave
        
        detect_wave = np.empty([0, len(self.s_trans_odd)])
        for i in range (len(self.s_trans_odd)):
            if (self.data_detect_o[i] == 1 and self.data_detect_o[i] == 0 ):
                detect_wave = np.append(detect_wave, phi1 )
            if (self.data_detect_o[i] == 0 and self.data_detect_o[i] == 0 ):
                detect_wave = np.append(detect_wave, phi2 )
            if (self.data_detect_o[i] == 0 and self.data_detect_o[i] == 1 ):
                detect_wave = np.append(detect_wave, phi3 )
            if (self.data_detect_o[i] == 1 and self.data_detect_o[i] == 1 ):
                detect_wave = np.append(detect_wave, phi4 )

        plt.plot (range(len(t)*len(self.s_trans_odd)), detect_wave, label = "Recieved signal")
        plt.title ("QPSK")
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

        plt.semilogy(np.arange(20),ber,color='r',marker='+',linestyle='-', label = "QPSK")
        plt.title ("QPSK")
        plt.ylabel ("BER")
        plt.xlabel ("SNR db")
        plt.legend (loc = 1)
        plt.show()
