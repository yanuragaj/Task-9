import speech_recognition as sr
import pyttsx3
import subprocess
import sys
import warnings


def status(cmd):
	rc,op=subprocess.getstatusoutput(cmd)
	if rc!= 0:
		print('Something Went Wrong.....!!!\n\n======== Getting Error ========\n',op)
	else:
		print(op,"\n")
		pyttsx3.speak("Successfully Completed")
		print("Successfully Completed...!!!")




def aryan():
	pyttsx3.speak("Hiiii....I am AARYAN... your smart virtual assistant is here!!!! ")
	pyttsx3.speak("What services would you like to get?")
	print("======== What services would you like to get? ========")
	print("1. Docker\t 2. AWS\t\t 3. Hadoop\t\t 4. Web Configuration\t\t 5. LVM\t\t 6. Ansible\t\t 7. Exit")


#Docker
def Docker():
	while True:
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nDocker-Service is running....\n")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t\t\tDocker-Service is Running")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	
			print("\n======== LISTENING (Service-type is 'Docker') ========")
			audio = r.listen(source)
			print(audio)
			print("processing your requested Docker instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				print("======== Given Docker Instruction is ======== \n",q,"\n")
				if (("install" in q) and (("docker" in q) or ("Docker" in q) or ("DOCKER" in q))):
					cmd="yum install docker-ce --nobest"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif (("start" in q) or ("Start" in q)):
					cmd="systemctl start docker"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("stop" in q) or ("Stop" in q) or ("exit" in q) or ("Exit" in q)) and (("docker" in q) or ("Docker" in q))):
					cmd="systemctl stop docker"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("search" in q) or ("Search"  in q)) and (("image" in q) or ("Image" in q) or ("Images" in q) or ("images" in q))):
					print("Enter Image name to search :")
					b=input()
					cmd="docker search {}".format(b)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("download" in q) or ("Download"  in q)) and (("image" in q) or ("Image" in q) or ("Images" in q) or ("images" in q))):
					print("Enter Image name to Download/Pull")
					c=input()
					cmd="docker pull {}".format(c)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("list" in q) or ("show"  in q)) and (("launched os" in q) or ("OS" in q) or ("Os" in q) or ("operating system" in q))):
					cmd="docker ps -a"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("Running" in q) or ("running"  in q)) and (("os" in q) or ("OS" in q) or ("Os" in q) or ("operating system" in q))):
					cmd="docker ps"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("start" in q) or ("Start"  in q)) and (("os" in q) or ("OS" in q) or ("Os" in q) or ("operating system" in q))):
					print("Enter Docker Os to start:")
					d=input()
					cmd="docker start {}".format(d)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("stop" in q) or ("Stop"  in q)) and (("os" in q) or ("OS" in q) or ("Os" in q) or ("operating system" in q))):
					print("Enter Docker OS to stop:")
					e=input()
					cmd="docker stop {}".format(e)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("Delete" in q) or ("delete"  in q)) and (("image" in q) or ("Image" in q) or ("Images" in q) or ("images" in q))):
					print("Enter Image Name to Delete:")
					f=input()
					cmd="docker rm {}".format(f)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("delete all" in q) or ("Delete All "  in q)) and (("os" in q) or ("OS" in q) or ("Os" in q) or ("operating system" in q)) ):
					cmd="docker rm `docker ps -a -q`"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("launch" in q) or ("run"  in q)) and (("os" in q) or ("OS" in q) or ("Os" in q) or ("operating system" in q)) ):
					print("Enter image name to install:")
					g=input()
					print("Give Name to Your Docker OS")
					osname=input()
					cmd="docker run -it --name {}  {}".format(osname,g)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("get" in q) or ("Get"  in q)) and (("Terminal" in q) or ("terminal" in q))):
					print("Enter Docker-OS Name to get Terminal:")
					h=input()
					cmd="docker attach {}".format(h)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("show" in q) or ("list"  in q)) and  (("image" in q) or ("Image" in q) or ("Images" in q) or ("images" in q))):
					cmd="docker images"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("show" in q) or ("list"  in q)) and  (("info" in q) or ("Information" in q) or ("Info" in q) or ("information" in q))):
					cmd="docker info" 
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
				elif (("exit" in q) or ("Exit" in q) or ("quit" in q) or ("Quit" in q) or ("stop" in q) or ("Stop" in q)):
					pyttsx3.speak("Exiting...")
					print("Exiting....")
					break
				
				else:  
					print("======== This Docker-Service Does not exist in the system ========")
			
			except:
				print("======== Cannot recog your requested docker-instruction!!!... Kindly say again... ========")



#AWS
def AWS():
	while True:
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nAWS-Service is running....\n")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t\t\tAWS-Service is Running")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	
			print("\n======== LISTENING (Service-type is 'AWS') ========")
			audio = r.listen(source)
			print(audio)
			print("processing your requested AWS instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				print("======== Given AWS Instruction is ======== \n",q,"\n")
				if (("version" in q) and (("AWS" in q) or ("aws" in q) or ("Aws" in q) or ("a w s" in q))):
					cmd="aws --version"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("key" in q) and ("create" in q)):
					print("Enter Key Name:")
					b=input()
					cmd="aws ec2 create-key-pair --key-name {}".format(b)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("sg" in q) or ("security group" in q)) and ("create" in q)):
					print("Enter Security-Group Name:")
					c=input()
					print("Give Description Here:")
					d=input()
					cmd="aws ec2 create-security-group --group-name {} --description \"{}\" ".format(c,d)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("instance" in q) or ("Instance" in q)) and ("launch" in q)):
					print("Enter Image-ID")
					e=input()
					print("Enter Instance-Type")
					f=input()
					print("Enter Key-Pair Name")
					g=input()
					print("Enter Security-Group ID:")
					h=input()
					cmd="aws ec2 run-instances --image-id {} --instance-type {} --count 1 --subnet-id subnet-601c1508 --key-name {} --security-group-ids {} ".format(e,f,g,h)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("ebs" in q) or ("e b s" in q)) and ("create" in q)):
					print("Enter the Zone Name:")
					i=input()
					cmd="aws ec2 create-volume --availability-zone {} --size 1 --volume-type gp2".format(i)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("ebs" in q) or ("e b s" in q)) and ("attach" in q)):
					print("Enter Instance-ID:")
					j=input()
					print("Enter Volume-ID:")
					k=input()
					cmd="aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/sdk".format(j,k)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("exit" in q) or ("Exit" in q) or ("quit" in q) or ("Quit" in q) or ("stop" in q) or ("Stop" in q)):
					pyttsx3.speak("Exiting...")
					print("Exiting....")
					break
				else:  
					print("======== This AWS-Service Does not exist in the system ========")
			
			except:
				print("======== Cannot recog your requested aws-instruction!!!... Kindly say again... ========")    


#WEB
def web():
	while True:
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nWeb Configuration is running....\n")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t\t\tWeb Configuration is Running")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	
			print("\n======== LISTENING (Service-type is 'Web Configuration') ========")
			audio = r.listen(source)
			print(audio)
			print("processing your requested Web Configuration instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				print("======== Given Web Configuration Instruction is ======== \n",q,"\n")
				if (("install" in q) and (("apcahe" in q) or ("Apache" in q))):
					cmd="yum install httpd -y"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("list" in q) and ("web pages" in q)):
					cmd="ls /var/www/html"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("start" in q) or ("run" in q)) and (("web service" in q) or ("web services" in q))):
					cmd="systemctl start httpd"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("stop" in q) or ("kill" in q)) and (("web service" in q) or ("web services" in q))):
					cmd="systemctl stop httpd"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("status" in q) or ("Status" in q)) and (("web service" in q) or ("web services" in q))):
					cmd="systemctl status httpd"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("exit" in q) or ("Exit" in q) or ("quit" in q) or ("Quit" in q) or ("stop" in q) or ("Stop" in q)):
					pyttsx3.speak("Exiting...")
					print("Exiting....")
					break
				else:  
					print("======== This Web Configuration Service Does not exist in the system ========")
			
			except:
				print("======== Cannot recog your requested Web Configuration-instruction!!!... Kindly say again... ========") 


# In[ ]:

#Hadoop
def hadoop():
	while True:
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nHadoop is running....\n")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t\t\tHADOOP is Running")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	
			print("\n======== LISTENING (Service-type is 'Hadoop') ========")
			audio = r.listen(source)
			print(audio)
			print("processing your requested Hadoop instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				print("======== Given Hadoop Instruction is ======== \n",q,"\n")
				if (("install" in q) and (("namenode" in q) or ("service" in q))):
					cmd="hadoop-daemon.sh start namenode"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("show" in q) and ("report" in q)):
					cmd="hadoop dfsadmin -report"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("start" in q) or ("run" in q)) and (("web service" in q) or ("web services" in q))):
					cmd="systemctl start httpd"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("stop" in q) or ("kill" in q)) and (("web service" in q) or ("web services" in q))):
					cmd="systemctl stop httpd"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("status" in q) or ("Status" in q)) and (("web service" in q) or ("web services" in q))):
					cmd="systemctl status httpd"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("exit" in q) or ("Exit" in q) or ("quit" in q) or ("Quit" in q) or ("stop" in q) or ("Stop" in q)):
					pyttsx3.speak("Exiting...")
					print("Exiting....")
					break
				else:  
					print("======== This Hadoop-Service Does not exist in the system ========")
			
			except:
				print("======== Cannot recog your requested Hadoop-instruction!!!... Kindly say again... ========") 
	

#LVM
def LVM():
	while True:
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nLVM is running....\n")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t\t\tLVM is Running")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	
			print("\n======== LISTENING (Service-type is 'LVM') ========")
			audio = r.listen(source)
			print(audio)
			print("processing your requested LVM instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				print("======== Given LVM Instruction is ======== \n",q,"\n")
				if (("list" in q) and (("show" in q) or ("disk" in q))):
					cmd="fdisk -l"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("create" in q) and ("partition" in q)):
					c=input("Enter the name of partition to create partition")
					cmd="fdisk /dev{}".format(c)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("format" in q) or ("Format" in q)) and (("partition" in q) or ("Partition" in q))):
					a=input("Enter the name of storage/partition which you want to format:")
					cmd="mkfs.ext4  /dev{}".format(a)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("mount" in q) or ("Mount" in q)) and (("partition" in q) or ("Partition" in q))):
					b=input("enter name of volume which you want to mount")
					cmd="mount /dev{} /fold".format(b)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("block" in q) or ("partition" in q)) and (("details" in q) or ("Details" in q))):
					cmd="lsblk"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")

				elif ((("create" in q) or ("make" in q)) and (("pv" in q) or ("physical volume" in q))):
					pv1=input("Enter the name of storage 1:")
					pv2=input("Enter the name of storage 2:")
					cmd="pvcreate {}".format(pv1)
					status(cmd)
					cmd="pvcreate {}".format(pv2)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("show" in q) or ("display" in q)) and (("pv" in q) or ("physical volume" in q))):
					pv=input("Enter the name of storage:")
					cmd="pvdisplay {}".format(pv)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")

				elif ((("create" in q) or ("make" in q)) and (("vg" in q) or ("volume group" in q))):
					vgn=input("Give name to the VG:")
					pvn1=input("Enter the name of physical volume 1 (pv1):")
					pvn2=input("Enter the name of physical volume 2 (pv2):")
					cmd="vgcreate {} {} {}".format(vgn,pvn1,pvn2)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("show" in q) or ("display" in q)) and (("vg" in q) or ("volume group" in q))):
					vgn1=input("Enter the name of VG:")
					cmd="vgdisplay {}".format(vgn1)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("create" in q) or ("make" in q)) and (("lv" in q) or ("logical volume" in q))):
					size=input("Enter size for your LV:")
					lvn=input("Give name to your LV:")
					vgn2=input("Enter name of the VG:")
					cmd="lvcreate --size{} --name{} {}".format(size,lvn,vgn2)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("show" in q) or ("display" in q)) and (("lv" in q) or ("logical volume" in q))):
					cmd="lvdisplay"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")

				elif ((("format" in q) or ("Format" in q)) and (("lv" in q) or ("logical volume" in q))):
					vgn4=input("Enter the name of VG:")
					lvn2=input("Enter the name of LV:")
					cmd="mkfs.ext4  /dev{}{}".format(vgn4,lvn2)
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("exit" in q) or ("Exit" in q) or ("quit" in q) or ("Quit" in q) or ("stop" in q) or ("Stop" in q)):
					pyttsx3.speak("Exiting...")
					print("Exiting....")
					break
				else:  
					print("======== This LVM-Service Does not exist in the system ========")
			
			except:
				print("======== Cannot recog your requested LVM-instruction!!!... Kindly say again... ========") 

#Ansible
def Ansible():
	while True:
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nAnsible is running....\n")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t\t\tAnsible is Running")
			print("--------------------------------------------------------------------------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	
			print("\n======== LISTENING (Service-type is 'Ansible') ========")
			audio = r.listen(source)
			print(audio)
			print("processing your requested Ansible instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				print("======== Given Ansible Instruction is ======== \n",q,"\n")
				if (("install" in q) and (("ansible" in q) or ("Ansible" in q))):
					cmd="pip3 install ansible"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("ansible" in q) and ("version" in q)):
					cmd="ansible --version"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("configuration" in q) or ("config" in q)) and (("ansible" in q) or ("Ansible" in q))):
					def cfg():
						inventory=input("Give path of inventory: ")
						file=open("etc/ansible/ansible.cfg","w")
						file.write("[defualts]\n")
						file.write("inventory={}\n/".format(inventory))
						file.write("host_key_checking=false")
						file.close()
						return "Successfully Created!!!"
					cmd=cfg()
					print(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("configure" in q) or ("setup" in q)) and (("yum repo" in q) or ("docker repo" in q))):
					cmd="ansible-playbook -vv yum-repo.yml"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("install" in q) or ("setup" in q)) and (("docker" in q) or ("docker engine" in q))):
					cmd="ansible-playbook -vv docker-install.yml"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")

				elif ((("configure" in q) or ("set up" in q)) and (("apache web server" in q) or ("web server" in q))):
					cmd="ansible-playbook -vv docker-httpd.yml"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")

				elif ((("configure" in q) or ("set up" in q)) and (("Hadoop" in q) or ("hadoop" in q))):
					cmd="ansible-playbook -vv namenode.yml"
					status(cmd)
					cmd="ansible-playbook -vv datanode.yml"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")

				elif ((("configure" in q) or ("set up" in q)) and (("haproxy" in q) or ("Haproxy" in q))):
					cmd="ansible-playbook -vv haproxy.yml"
					status(cmd)
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("exit" in q) or ("Exit" in q) or ("quit" in q) or ("Quit" in q) or ("stop" in q) or ("Stop" in q)):
					pyttsx3.speak("Exiting...")
					print("Exiting....")
					break
				else:  
					print("======== This Ansible-Service Does not exist in the system ========")
			
			except:
				print("======== Cannot recog your requested Ansible-instruction!!!... Kindly say again... ========") 



def service():
	try:
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			print("\n======== LISTENING (Services) ========")
			audio = r.listen(source)
			print(audio)
			print("processing your requested services....please wait!!!\n")
			global q
			q = r.recognize_google(audio)
			print(q)   
		return q
				
	except:
		print("======== Failed to detect requested services...Kindly, say again!!! ========")


aryan()
while True:    
	service_type=service()
	if service_type is None:
		service_type=[]
	if( ("docker" in service_type) or ("Docker" in service_type ) ):
		Docker()
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\t\tTerminated Docker-Service")
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		break
	elif( ("AWS" in service_type) or ("aws" in service_type )  or ("Aws" in service_type) or ("a w s" in service_type)):
		AWS()
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\t\tTerminated AWS-Service")
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		break
	elif( (("web" in service_type) or ("Web" in service_type ) ) and (("configuration" in service_type) or ("Configuration" in service_type))):
		web()
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\t\tTerminated Web Configuration")
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		break
	elif( ("hadoop" in service_type) or ("Hadoop" in service_type ) ):
		hadoop()
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\t\tTerminated Hadoop-Service")
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		break
	elif( ("Ansible" in service_type) or ("ansible" in service_type ) ):
		Ansible()
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\t\tTerminated Ansible-Service")
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		break
	elif service_type == []:
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\t\tDidn't hear any voice , Kindly say!!!!")
		print("--------------------------------------------------------------------------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

	elif (("Exit" in service_type) or ("exit" in service_type) or ("quit" in service_type) or ("stop" in service_type) or ("Stop" in service_type)):
		warnings.filterwarnings("ignore")
		pyttsx3.speak("Exiting From Services ")
		print("======== Exiting From Services ========")
		cmd=sys.exit()
		status(cmd)
	else: 
		print("======== This Service Does not exist in the system ========")

	