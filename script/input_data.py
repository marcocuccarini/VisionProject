import sys
sys.path.append('/home/nbuser/library/')
import pandas as pd



class input_data():


	#Function that get the file with all the classes sorted using the main age ((StartYear,EndYear)\2)
	def getCronology(self):

		with open('/content/drive/MyDrive/dataset2/arcNames25.txt') as f:
			lines = f.readlines()
		dfCron = pd.DataFrame(columns=((lines[0].replace("\n",""))).split(','))
		lines.pop(0)
		for i in lines:
			line=i.split(',')
			line[3]=line[3].replace("\n","")
			dfCron.loc[len(dfCron.index)] = line

		#We made the main between the start year and end year
		listMain=[]
		for i in range(len(dfCron['Name'])):

			listMain.append((int(dfCron['StartYear'][i])+int(dfCron['EndYear'][i]))/2)

		dfCron['MainYear']=listMain
		dfCron.drop('StartYear', inplace=True, axis=1)
		dfCron.drop('EndYear', inplace=True, axis=1)
		dfCron.sort_values(['MainYear'], axis=0, ascending=True, inplace=True)

		return dfCron

	#Function that get the file of reletion between classes
	def getRelation(self,gdict=None):
		with open('/content/drive/MyDrive/dataset2/arcRelationship25.txt') as f:
			lines = f.readlines()
		dfRel = pd.DataFrame(columns=['Ver1','Ver2','Rel'])
		for i in lines:
			line=i.split(',')
			line[2]=line[2].replace("\n","")
			dfRel.loc[len(dfRel.index)] = line

		return dfRel
	

	




	 