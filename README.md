# chatGPTMapper

The ChatGPT Mapper is a Python script designed to map sensitive words before sending requests to the ChatGPT server. This script proves useful in various scenarios where the presence of tagged sensitive words does not impact the processing of ChatGPT. These scenarios may include tasks such as drafting executive reports, fine-tuning model responses, rewriting emails, and rephrasing contextual information.

# Script Prerequisites

- Python Installed
- ChatGPT API Token

# Script Preparation
Edit the scrip file and update with your ChatGPT API token:

```

...

 chatgpt_api_token="place_your_API_token_here"
 
... 

```


# How to use chatGPTMapper?

1- Place your original content in the file prompt.txt

```

Act as a cyber security analyst. Write an executive summary for a cyber incident using the following root cause:
Our main online server server_1 was hacked by the threat actor threat_actor_1 using the malware name malware_1 targeting 
our prodution system system_1. We also identified a use of backdoor named backdoor_1. The attacker used the technique_1 
technique as well as the exploit exploit_1. The dropped file is called file_1.exe and it has infected 000 of machines. 
The same backdoor backdoor_1 was found in other machines.

```

2- Wrap the senstive words with suffix ($_) and prefix (_$): 

```

Act as a cyber security analyst. Write an executive summary for a cyber incident using the following root cause:
Our main online server $_server_1_$ was hacked by the threat actor $_threat_actor_1_$ using the malware name $_malware_1_$ targeting 
our prodution system $_system_1_$. We also identified a use of backdoor named $_backdoor_1_$. The attacker used the $_technique_1_$ 
technique as well as the exploit $_exploit_1_$. The dropped file is called $_file_1.exe_$ and it has infected $_000_$ of machines. 
The same backdoor $_backdoor_1_$ was found in other machines.

```

3- Run the script: 

```
$ python3 ai_word_mapper.py

```

4- Analyz the response file: 

```
ChatGPT request after mapping --> ai_request.txt

ChatGPT response before mapping --> ai_response_before_mapping.txt

ChatGPT response after mapping --> ai_response_after_mapping.txt

```
