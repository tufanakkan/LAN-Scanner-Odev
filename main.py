from scapy.all import *
import sys
import configparser
config=configparser.ConfigParser()
config.read('config.conf')

def listofKeys():
    keys = []
    for key in config['IP-MAC']:
        keys.append(key)
    return keys

def listofValues():
    values = []
    for item in config['IP-MAC']:
        values.append(config['IP-MAC'][item])
    return values

def newOnes(ans):
    ips = []
    macs = []
    for s,r in ans:
        ips.append(r.sprintf("%ARP.psrc%"))
        macs.append(r.sprintf("%Ether.src%"))
    return (ips,macs)

def sameornot(conf_keys,conf_values,new_ips,new_macs):
    for i in range(len(new_ips)):
	for j in range(len(conf_keys)):
	    if( (new_ips[i]==conf_keys[j]) and (new_macs[i]==conf_values[j]) ):
		deger=0
	    elif( (new_ips[i]!=conf_keys[j]) and (new_macs[i]!=conf_values[j]) ):
		deger=1
	    elif( (new_ips[i]!=conf_keys[j]) and (new_macs[i]==conf_values[j]) ):
		deger=2
	    if(deger==0):
	        break
            elif(deger==2):
                print "UYARI! Aginizdaki " +new_macs[i]+ " mac adresine sahip cihaz yeni bir ip adresi ("+new_ips[i]+") aldi."
		conf_remove(conf_keys[j])
		conf_ekle(new_ips[i],new_macs[j])
		break
	    elif((deger==1) and (j == len(conf_keys)-1)):
                new_mac=new_macs[i]
		choise = "a"
		while (not(choise=="y" or choise=="Y" or choise=="n" or choise=="N") ):
                    choise = raw_input("Aginizda yeni bir mac adresi bulundu ( "+new_mac+" ) listeye eklemek ister misiniz?(y/n):")
                    if(choise=="y" or choise=="Y"):
                        conf_ekle(new_ips[i],new_macs[i])
                        break
                    elif(choise=="n" or choise=="N"):
                        break
                    else:
                        continue
                
    
    
    
def conf_yazdir(ans):
    for s,r in ans:
        config['IP-MAC'][r.sprintf("%ARP.psrc%")] = r.sprintf("%Ether.src%")  
    with open('config.conf','w') as configfile:
    	config.write(configfile)
        
def conf_ekle(str1,str2):
    config['IP-MAC'][str1] = str2
    with open('config.conf','w') as configfile:
    	config.write(configfile)
        
def conf_remove(key):
	with open('config.conf','w') as configfile:
		s = config.remove_option('IP-MAC',key)
		config.write(configfile)

sbx=config['SETTINGS']['subnet']
if(config['FIRST']['firsttime']=='0'):
    config['FIRST']['firsttime']='1'
    ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sbx),timeout=2)
    conf_yazdir(ans)
    ip_list = listofKeys()
    mac_list = listofValues()
    

    for i in ip_list:
        print "%s\n" %i
    for j in mac_list:
        print "%s\n" %j
        
else:
    ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sbx),timeout=2)
    new_ips,new_macs = newOnes(ans)
    
    for i in new_ips:
        print "%s\n" %i
    for j in new_macs:
        print "%s\n" %j
        
    conf_keys = listofKeys()
    conf_values = listofValues()
    #new_ips[0] = "192.168.42.1"
    sameornot(conf_keys,conf_values,new_ips,new_macs)
    



    
    

    






