import os
import openai
import json
import customtkinter
from tkinter import *




class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.something = 0
        self.root.title("Open API Chat")
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("450x500") # L x H change back to 270 or 280?
        self.root.config(background="#282828")
        
        
        # ------------ First Frame ------------ #
        self.first_frame = customtkinter.CTkFrame(self.root, fg_color='#282828', border_color=("black"))
        self.first_frame.pack(pady=(0, 20))#side=TOP, anchor="w", padx=(10, 0), pady=(15, 0))
        
        # User input label
        self.input = customtkinter.StringVar(value="Enter your input below...")
        self.input_label = customtkinter.CTkLabel(self.first_frame, textvariable=self.input)
        self.input_label.pack()
        
        
        
        
        
        
        
        # ------------ Second Frame ------------ #
        self.second_frame = customtkinter.CTkFrame(self.root, fg_color='#282828', border_color=("black"))
        self.second_frame.pack()#side=TOP, anchor="w", padx=(10, 0), pady=(15, 0))
        
        
        self.entry = customtkinter.CTkEntry(master=self.second_frame, placeholder_text="Enter Text", width=250, height=32, border_width=2, corner_radius=10)
        self.entry.grid(row=0, column=0)
        
        
        self.button = customtkinter.CTkButton(master=self.second_frame, corner_radius=8, text="Enter", width=25, height=32, command=self.enter_btn)
        self.button.grid(row=0, column=1, padx=(5, 0))
        
        
        


    
        self.root.mainloop()
        
    # all app class methods
                
    def enter_btn(self):
        # Number StrVariable that is set
        value = self.entry.get()
        
        if value == "":
            self.input.set(value="Please enter a prompt")
        else:
            self.input.set(value=value)
        
        
    
    
    def api_response(self, prompt):
        """
        Generates a text response based on a given prompt using the OpenAI API.
        
        Parameters:
            prompt (str): The text prompt that the API will use as the starting point for generating a response.
        
        Returns:
            str: The generated text response.
            
        Example:
            response = api_response("What is the weather like today?")
            print(response)
            # Output: "The weather today is sunny with a high of 75 degrees."
        """
        openai.api_key = "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"
        # openai.api_key = os.environ("OpenAI_Key")


        model_response = str(openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.9
        ))
        json_obj = json.loads(model_response)
        response = json_obj["choices"][0]["text"]
        return response


    
    

app = App()