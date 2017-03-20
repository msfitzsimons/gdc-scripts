import requests
import json
import sys
	
def GetProjects():
	response = requests.get('https://gdc-api.nci.nih.gov/projects?fields=project_id&size=1000')
	Projects_Json = json.loads(response.text)
	Total_Projects = len(Projects_Json['data']['hits']) # Total number of projects
	print('Total number of GDC Projects = ' + str(Total_Projects))
	for i in range(Total_Projects):
		String = Projects_Json['data']['hits'][i]['project_id']
		print(String)

def GetMetaData(EndPoint, Project, Fields):

	# List of API Endpoints
	if EndPoint == "Cases":
		EP =   'https://gdc-api.nci.nih.gov/cases'
	if EndPoint == "Files":
		EP =  'https://gdc-api.nci.nih.gov/files'
	if EndPoint == "Projects":
		EP = 'https://gdc-api.nci.nih.gov/projects'

	# Create Initial Payload Structure
	Payload = {
	   "filters":{
	   "op": "and",
	   "content": [
	      {  
	         "op":"in",
	         "content":{  
	            "field":"cases.project.project_id",
  	          "value":[  
  	             Project
  	          ]
 	        }
 	     }
 	   ]
	},
	    "format":"tsv",
	    "fields":Fields,
	    "size":"10000"
	}
	
	# Perform POST request
	response = requests.post(EP, json=Payload)
	
	#Write results to file in same directory
	text_file = open("MetaData.txt", "w")
	text_file.write(response.text)
	text_file.close()
