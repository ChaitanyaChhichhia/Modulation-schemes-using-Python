class am (AbstractClass):
    '''
    Class for Amplitude Modulation scheme
    ### Concept of polymorphism has been used by having same methods for different classes
    '''
    
    def __init__(self):
        '''
        Constructor for Amplitude Modulation scheme
        '''
        print ("To prevent overmodulation, enter Ac > Am.")
        
        ### Concept of exception handling 
        
        # Taking user input
        while True:
            try:
                self.Am = float(input("Enter the amplitude of message : "))
                break
            except:
                print ("Please enter a proper value")
        while True:
            try:
                self.fm = float(input("Enter the frequency of sinusoidal msg signal : "))
                break
            except:
                print ("Please enter a proper value")
        while True:
            try:
                self.Ac = float(input("Enter the carrier amplitude : "))
                break
            except:
                print ("Please enter a proper value")   
        while True:
            try:
                self.fc = float(input("Enter the carrier frequency : "))
                break
            except:
                print ("Please enter a proper value")
        
        
        self.car_wave = []
        self.__msg_wave = []
    
    def data_generator (self):
        '''        
        Description
        -----------
        Generates the message and carrier wave based on the inputs provided by the user.
        Also states the type of amplitude modulation ("Overmodulation/Undermodulation")

        Returns
        -------
        None

        '''
        if (self.Am > self.Ac):
                print ("Overmodulation")
        elif (self.Am < self.Ac):
                print ("Undermodulation")
        else:
                print ("Am = Ac")
        
        t = np.linspace (0, 1, 1000)     #time interval

        self.car_wave[:] = self.Ac * np.cos(2*np.pi*self.fc*t)
        self.__msg_wave[:] = self.Am * np.cos(2*np.pi*self.fm*t)
        
        
    def transmitter (self):
        '''
        Description
        -----------
        Performs the function of a transmitter in a communication system.
        Gets the generated data from the data_generator function computes the modulated signal.

        Returns
        -------
        None.
        '''
        mod_index = self.Am / self.Ac
        t = np.linspace (0, 1, 1000)
        self.data_generator()
        self.__data = self.Ac * (1 + mod_index*np.cos(2*np.pi*self.fm*t)) * self.Ac*np.cos (2*np.pi*self.fc*t)
                
        
    def plotting (self): 
        '''
        DESCRIPTION
        -----------
        Plots the message, carrier and modulated signals.
        
        Returns
        -------
        None
    
        '''
        t = np.linspace (0, 1, 1000)
        
        # plotting the message wave
        plt.plot (t,self.__msg_wave, label = "Message wave")
        plt.title ("Amplitude Modulation")
        plt.xlabel ("t")
        plt.ylabel ("Amplitude")
        plt.legend (loc = 1)
        plt.show()
        
        # plotting the carrier wave
        plt.plot (t,self.car_wave, label = "Carrier wave")
        plt.title ("Amplitude Modulation")
        plt.xlabel ("t")
        plt.ylabel ("Amplitude")
        plt.legend (loc = 1)
        plt.show()
        
        # plotting the modulated wave
        plt.plot (t,self.__data, label = "Modulated wave")
        plt.title ("Amplitude Modulation")
        plt.xlabel ("t")
        plt.ylabel ("Amplitude")
        plt.legend (loc = 1)
        plt.show()
        