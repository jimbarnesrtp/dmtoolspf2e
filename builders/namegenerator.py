from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os
import json

class NameGenerator():
    
    def generate_new_name_by_ancestry(self, ancestry: str) -> list:
        
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        model = GPT2LMHeadModel.from_pretrained('gpt2')
        blank_string = " "
        
        sequence =  blank_string.join(self.get_sequence_by_ancestry(ancestry))
            
        inputs = tokenizer.encode(sequence, return_tensors='pt')
        
        outputs = model.generate(inputs, max_length=100, do_sample=True, pad_token_id=tokenizer.eos_token_id)

        text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        output_list = text.split(" ")
        
        return_list = []
        
        for output in output_list:
            skipped_output = 0
            if output in sequence:
                skipped_output += 1
            elif output == "" or output == " ":
                return return_list
            else:
                return_list.append(output)
        
        return return_list
    
    def get_sequence_by_ancestry(self, ancestry: str) -> str:
        languages = self.get_available_languages()
        for key in languages.keys():
            if key == ancestry.lower():
                return languages[key]['seed']
        
    
    def get_available_languages(self) -> dict:
        languages = {}
        directory_path = os.getcwd()
        files = os.listdir(directory_path+"/json/")
        for entry in files:
            with open(directory_path+"/json/"+entry) as file:
                lang = json.load(file)
                languages[lang['ancestry']] = lang
        return languages
                