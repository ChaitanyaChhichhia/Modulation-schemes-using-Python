import bpsk
import qpsk
import am
#import fm

print ("Press\n'b' for BPSK modulation scheme")
print ("'q' for QPSK modulation scheme")
print ("'a' for Amplitude modulation scheme")
print ("'f' for Frequency modulation scheme\n")
choice = input ("Enter your choice : ").lower()
print()
l = ['b', 'q', 'a', 'f']
while True:
    if (choice.isalpha() and choice in l):
        break
    else:
        if (choice.isalpha() and choice not in l):
            print ("No such modulation scheme available")
        else:
            print ("Please enter a character")
        choice = input ("Enter your choice : ").lower()

        

if (choice == 'b'):
    while True:
        try:
            n = int (input(("Enter the number of bits to be transmitted")))
            break
        except:
            print ("Please enter a valid input")
    while True:
        try:
            snrdb = int (input(("Enter the value of snr in db")))
            break
        except:
            print ("Please enter a valid input")
    b = bpsk(n)
    b.transmitter()
    b.channel(snrdb)
    b.receiver()
    b.plotting()
    b.ber_vs_snr()

elif (choice == 'q'):
    while True:
        try:
            n = int (input(("Enter the number of bits to be transmitted")))
            break
        except:
            print ("Please enter a valid input")
    while True:
        try:
            snrdb = int (input(("Enter the value of snr in db")))
            break
        except:
            print ("Please enter a valid input")
    q = qpsk(n)
    q.transmitter()
    q.channel(snrdb)
    q.receiver()
    q.plotting()
    q.ber_vs_snr()

elif (choice == 'a'):
    a = am()
    a.transmitter()
    a.plotting()

elif (choice == 'f'):
    f = fm()
    f.transmitter()
    f.plotting()

else:
    print ("Please enter a valid choice")
