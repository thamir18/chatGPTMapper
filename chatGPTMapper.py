# Author: Thamir Alshammari
# License: GPL 3

import requests

# Global variables
chatgpt_url="https://api.openai.com/v1/chat/completions"
chatgpt_api_token="place_your_token_here"
chatggp_model="gpt-3.5-turbo"
mapper = {}
prompt=""
ai_request=""
ai_response=""
x = 0

# Open the text file for reading
with open("prompt.txt", "r") as file:
	# Read the contents of the file into a string
    prompt = file.read()

# Prepare the ChatGPT request
ai_request = prompt;

# Split the prompt content into lines
prompt = prompt.split()

# Loop over each line in the file
for line in prompt: 
	# Split the line into words
	words = line.split()
	# Loop over each word in the line    	
	for word in words:
		# Read only the words that are taged with suffix ($_) and prefix (_$)
		if word.startswith('$_') and '_$' in word:
			# Counter
			x = x + 1
			# Prepare the mapper key
			v="value_" + str(x)
			# Track the index where the mapped word will end
			index_suffex = word.find("_$")    	
			# Prepare the mapper value. Extract the actual word excluding the suffix and prefix	 
			w = word[2:index_suffex]
			# Check if current read value already mapped
			if w.lower() not in [elem.lower() for elem in mapper.values()]:
				# If the current value not mapped, add it to the mapper with the key (v) and the value (w)
		 		mapper[v] = w
		 		# Replace the mapped word from the prepared ai request 
		 		ai_request = ai_request.replace("$_"+w+"_$", v)	 

# Write the mapped request content to a file for validation
with open('ai_request.txt', 'w') as f:
    f.write(ai_request)    				    				
print("ChatGPT request after mapping --> ai_request.txt\n")	    				
 		  				
# Define the request headers
headers = {
    'Authorization': 'Bearer ' + chatgpt_api_token,
    'Content-Type': 'application/json'
}

# Define the request payload
payload = {
    'model': chatggp_model,
    'messages': [{"role": "user", "content": ai_request}]
}

# Send the request with the JSON body and authorization headers
response = requests.post(chatgpt_url, json=payload, headers=headers)

# Parse the response JSON 
response_json = response.json()

# Extract the ChatGPT response form the json object.
ai_response = response_json["choices"][0]['message']["content"]

# Write the unmapped response content to a file for validation
with open('ai_response_before_mapping.txt', 'w') as f:
    f.write(ai_response)   
print("ChatGPT response before mapping --> ai_response_before_mapping.txt\n")	   

# Map back the fake words to the original words
for word in mapper:
	ai_response = ai_response.replace(word, mapper[word])
	
# Write the mapped response content to a file for validation
with open('ai_response_after_mapping.txt', 'w') as f:
    f.write(ai_response)    
print("ChatGPT response after mapping --> ai_response_after_mapping.txt\n")	   
